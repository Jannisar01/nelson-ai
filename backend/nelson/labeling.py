"""Blind human-labeling set for Nelson's review decisions.

Why: the 2,582 reviewer decisions in `customer_review_logs` are synthetic, and each one is a
fixed function of its `scenario` (escalation_retention_case -> Escalate, late_delivery_frustration
-> Monitor; there is no Stabilize label). Agreement with them measures how well a model recovers
the generator's scenario, not whether its recommendation is sound. This module builds a set of
cases for people to label without seeing any label, so Nelson can be scored against human
judgment instead.

What a labeler sees: the same raw evidence bundle the eval gives the model, frozen to JSON, minus
anything that reveals a label: prior review decisions and notes, and the generator's scenario and
topic tags (as fields and inside note and email text) are removed. No model call is made here.

    python -m nelson.cli label-sheet [n] [seed]      build eval/human_labels/ (default 80 cases, seed 7)
    python -m nelson.cli label-predict               model predictions on the frozen cases (API calls)
    python -m nelson.cli label-score SHEET.csv ...   score labels and predictions (see label_score.py)
"""
from __future__ import annotations

import csv
import json
import random
import re
from pathlib import Path
from typing import Any

from nelson.config.settings import ROOT

LABEL_DIR = ROOT / "eval" / "human_labels"
DECISIONS = ("Monitor", "Stabilize", "Escalate")
SHEET_COLUMNS = ("case_id", "decision", "confidence", "labeler", "notes")

# Tags the synthetic-data generator attached to each case; each maps straight to a label.
GENERATOR_TAGS = (
    "escalation_retention_case",
    "executive_escalation",
    "late_delivery_frustration",
    "late_delivery_recovery",
)
# Fields removed from every record in a blind bundle.
BLIND_DROP_FIELDS = {
    "scenario",
    "topic",
    "tenant_id",
    "customer_email",
    "customer_full_name",
    "source_signal_ids",
    "synthetic_flag",
    "decision_boundary",
}
_TAG_RE = re.compile("|".join(re.escape(tag) for tag in GENERATOR_TAGS), re.IGNORECASE)


def redact_text(text: str, names: list[str] | None = None) -> str:
    """Replace generator tags (and the customer's name) in free text."""
    out = _TAG_RE.sub("[redacted]", text)
    for name in names or []:
        if name:
            out = re.sub(re.escape(name), "the customer", out, flags=re.IGNORECASE)
    return out


def _redact_record(record: dict[str, Any], names: list[str]) -> dict[str, Any]:
    clean: dict[str, Any] = {}
    for key, value in record.items():
        if key in BLIND_DROP_FIELDS:
            continue
        clean[key] = redact_text(value, names) if isinstance(value, str) else value
    return clean


def blind_bundle(bundle: dict[str, Any]) -> dict[str, Any]:
    """The evidence bundle with every label-revealing field removed.

    prior_reviews are reduced to their dates: their decisions are labels of the same synthetic
    generator, and their notes and topics name the scenario.
    """
    customer = dict(bundle.get("customer") or {})
    names = [customer.get("customer_full_name") or ""]
    out: dict[str, Any] = {"customer": _redact_record(customer, names)}
    out["prior_review_dates"] = [
        review.get("reviewed_at") for review in bundle.get("prior_reviews", []) if review.get("reviewed_at")
    ]
    for key in ("recent_orders", "recent_tickets", "recent_notes", "recent_emails", "fulfillment_events"):
        out[key] = [_redact_record(record, names) for record in bundle.get(key, [])]
    return out


def leaks_label(blind: dict[str, Any]) -> list[str]:
    """Generator tags or decision words still present anywhere in a blind bundle (should be [])."""
    text = json.dumps(blind, default=str)
    found = [tag for tag in GENERATOR_TAGS if tag.lower() in text.lower()]
    if '"human_decision"' in text or '"review_notes"' in text:
        found.append("prior review decision or notes")
    return found


def stratified_sample(rows: list[dict[str, Any]], n: int, seed: int) -> list[dict[str, Any]]:
    """n rows split evenly across human_decision classes (deterministic for a seed)."""
    by_class: dict[str, list[dict[str, Any]]] = {}
    for row in sorted(rows, key=lambda r: r["review_id"]):
        by_class.setdefault(row["human_decision"], []).append(row)
    rng = random.Random(seed)
    per_class = n // max(len(by_class), 1)
    picked: list[dict[str, Any]] = []
    for label in sorted(by_class):
        items = by_class[label]
        picked.extend(rng.sample(items, min(per_class, len(items))))
    rng.shuffle(picked)
    return picked


def _review_rows(tenant_id: str) -> list[dict[str, Any]]:
    from nelson.data.db import get_connection

    rows = get_connection().execute(
        """
        SELECT review_id, customer_id, human_decision, reviewed_at
        FROM customer_review_logs
        WHERE tenant_id = ? AND human_decision IS NOT NULL
        """,
        (tenant_id,),
    ).fetchall()
    # one case per customer, so a labeler never sees the same customer twice
    seen: set[str] = set()
    out = []
    for review_id, customer_id, decision, reviewed_at in sorted(rows):
        if customer_id in seen:
            continue
        seen.add(customer_id)
        out.append(
            {"review_id": review_id, "customer_id": customer_id, "human_decision": decision,
             "reviewed_at": str(reviewed_at) if reviewed_at else None}
        )
    return out


def build_cases(n: int = 80, seed: int = 7, tenant_id: str | None = None) -> list[dict[str, Any]]:
    """Sample n reviews (one per customer, balanced by synthetic label) and freeze blind bundles."""
    from nelson.config.settings import settings
    from nelson.eval import _bundle

    tenant_id = tenant_id or settings.default_tenant_id
    cases = []
    for index, row in enumerate(stratified_sample(_review_rows(tenant_id), n, seed), start=1):
        bundle = _bundle(tenant_id, row["customer_id"], exclude_review_id=row["review_id"])
        if not bundle:
            continue
        blind = blind_bundle(bundle)
        leaks = leaks_label(blind)
        if leaks:
            raise RuntimeError(f"case for review {row['review_id']} still reveals a label: {leaks}")
        cases.append(
            {
                "case_id": f"H{index:03d}",
                "review_id": row["review_id"],
                "customer_id": row["customer_id"],
                "review_date": row["reviewed_at"],
                "bundle": blind,
            }
        )
    return cases


def _cell(value: Any, limit: int = 160) -> str:
    text = "" if value is None else str(value)
    text = text.replace("|", "/").replace("\n", " ").strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _table(records: list[dict[str, Any]], skip: set[str] = frozenset({"customer_id"})) -> list[str]:
    if not records:
        return ["(none)", ""]
    columns = [key for key in records[0] if key not in skip]
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join("---" for _ in columns) + "|"]
    for record in records:
        lines.append("| " + " | ".join(_cell(record.get(col)) for col in columns) + " |")
    return lines + [""]


def render_packet(cases: list[dict[str, Any]]) -> str:
    lines = [
        "# Nelson blind labeling packet",
        "",
        "For each case, read the evidence and record in your copy of `label_sheet_TEMPLATE.csv`",
        "what a customer success lead should do next:",
        "",
        "- **Monitor**: keep watching; no specific recent issue needs action now.",
        "- **Stabilize**: a specific recent issue needs a concrete fix or outreach.",
        "- **Escalate**: executive attention is needed (compounding critical issues, a failed",
        "  recovery, an explicit request, or large revenue at risk that is getting worse).",
        "",
        "Add a confidence of 1 (unsure) to 3 (sure). Label on your own, without discussing cases,",
        "and do not open `data/` or `cases.json`; they can reveal the synthetic labels. Dates are as",
        "of each case's review date. Generator tags in notes and emails are shown as [redacted].",
        "",
    ]
    for case in cases:
        bundle = case["bundle"]
        lines += [f"## {case['case_id']} (review date {case.get('review_date') or 'unknown'})", ""]
        lines += ["**Account**", ""]
        lines += [f"- {key}: {_cell(value)}" for key, value in bundle["customer"].items() if key != "customer_id"]
        if bundle.get("prior_review_dates"):
            lines.append(f"- earlier reviews on: {', '.join(map(str, bundle['prior_review_dates']))}")
        lines.append("")
        for title, key in (
            ("Recent orders", "recent_orders"),
            ("Support tickets", "recent_tickets"),
            ("Account notes", "recent_notes"),
            ("Emails", "recent_emails"),
            ("Fulfillment events", "fulfillment_events"),
        ):
            lines += [f"**{title}**", ""] + _table(bundle.get(key, []))
    return "\n".join(lines)


def write_label_set(cases: list[dict[str, Any]], out_dir: Path = LABEL_DIR, seed: int | None = None) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "cases.json").write_text(
        json.dumps({"seed": seed, "count": len(cases), "cases": cases}, indent=2, default=str),
        encoding="utf-8",
    )
    (out_dir / "packet.md").write_text(render_packet(cases), encoding="utf-8")
    with (out_dir / "label_sheet_TEMPLATE.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(SHEET_COLUMNS)
        for case in cases:
            writer.writerow([case["case_id"], "", "", "", ""])
    return out_dir


def load_cases(path: Path = LABEL_DIR / "cases.json") -> list[dict[str, Any]]:
    return json.loads(Path(path).read_text(encoding="utf-8"))["cases"]


def predict_cases(client: Any, cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Model predictions on the frozen blind bundles (one API call per case)."""
    from nelson.eval import _predict

    out = []
    for case in cases:
        try:
            pred = _predict(client, case["bundle"])
        except Exception as exc:  # recorded, not raised, so one failure does not stop the run
            pred = {"_parse_error": True, "_error": f"{type(exc).__name__}: {exc}"}
        out.append(
            {
                "case_id": case["case_id"],
                "predicted_decision": (pred.get("predicted_decision") or "").strip(),
                "rationale": pred.get("rationale", ""),
                "parse_error": bool(pred.get("_parse_error")),
            }
        )
    return out


def run_build(n: int = 80, seed: int = 7) -> int:
    cases = build_cases(n=n, seed=seed)
    out = write_label_set(cases, seed=seed)
    print(f"  [labels] {len(cases)} blind cases -> {out.relative_to(ROOT)}")
    return 0


def run_predict(cases_path: Path = LABEL_DIR / "cases.json") -> int:
    import sys
    from datetime import datetime

    from google import genai

    from nelson.config.settings import settings

    if not settings.gemini_api_key:
        print("  [labels] GEMINI_API_KEY not set in .env", file=sys.stderr)
        return 1
    cases = load_cases(cases_path)
    print(f"  [labels] predicting {len(cases)} cases with {settings.gemini_model} (one API call each)")
    predictions = predict_cases(genai.Client(api_key=settings.gemini_api_key), cases)
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = LABEL_DIR / f"predictions_{stamp}.json"
    path.write_text(
        json.dumps({"model": settings.gemini_model, "predictions": predictions}, indent=2), encoding="utf-8"
    )
    print(f"  [labels] predictions -> {path.relative_to(ROOT)}")
    return 0
