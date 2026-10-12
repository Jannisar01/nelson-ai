"""Score human labels (and optionally model predictions) on the blind labeling set.

    python -m nelson.cli label-score eval/human_labels/sheet_alice.csv eval/human_labels/sheet_bob.csv \
        [--predictions eval/human_labels/predictions_<stamp>.json] [--out report.md]

Reports, with no model calls:
- each labeler's agreement with the synthetic label, and Cohen's kappa
- agreement between labelers (pairwise percent agreement and Cohen's kappa)
- the human reference label per case: the majority decision (ties are left out)
- if predictions are given: the model against the human reference (accuracy with a 95% Wilson
  interval, macro F1, per-class precision and recall, confusion matrix), and the model against the
  synthetic label on the same cases for comparison
"""
from __future__ import annotations

import csv
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Iterable

from nelson.config.settings import ROOT
from nelson.labeling import DECISIONS, LABEL_DIR, load_cases

REVIEW_LOGS = ROOT / "data" / "customer_2000" / "customer_review_logs.csv"


def normalise_decision(value: str | None) -> str | None:
    text = (value or "").strip().lower()
    for decision in DECISIONS:
        if text == decision.lower():
            return decision
    return None


def read_sheet(path: Path) -> tuple[str, dict[str, str]]:
    """(labeler, {case_id: decision}) from a filled label sheet; blank or invalid rows are skipped."""
    labels: dict[str, str] = {}
    labeler = Path(path).stem
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            decision = normalise_decision(row.get("decision"))
            if decision and row.get("case_id"):
                labels[row["case_id"].strip()] = decision
            if (row.get("labeler") or "").strip():
                labeler = row["labeler"].strip()
    return labeler, labels


def read_predictions(path: Path) -> dict[str, str]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    out = {}
    for item in payload.get("predictions", []):
        decision = normalise_decision(item.get("predicted_decision"))
        if decision:
            out[item["case_id"]] = decision
    return out


def synthetic_labels(cases: list[dict], review_logs: Path = REVIEW_LOGS) -> dict[str, str]:
    by_review = {}
    with Path(review_logs).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            by_review[row["review_id"]] = row["human_decision"]
    return {case["case_id"]: by_review[case["review_id"]] for case in cases if case["review_id"] in by_review}


def majority(labels_by_labeler: Iterable[dict[str, str]]) -> dict[str, str]:
    """Most common decision per case; a tie for first place gives no reference label."""
    votes: dict[str, Counter] = {}
    for labels in labels_by_labeler:
        for case_id, decision in labels.items():
            votes.setdefault(case_id, Counter())[decision] += 1
    out = {}
    for case_id, counter in votes.items():
        top = counter.most_common()
        if len(top) == 1 or top[0][1] > top[1][1]:
            out[case_id] = top[0][0]
    return out


def agreement(a: dict[str, str], b: dict[str, str]) -> tuple[int, int]:
    shared = [case for case in a if case in b]
    return sum(1 for case in shared if a[case] == b[case]), len(shared)


def cohen_kappa(a: dict[str, str], b: dict[str, str]) -> float | None:
    shared = [case for case in a if case in b]
    n = len(shared)
    if n == 0:
        return None
    observed = sum(1 for case in shared if a[case] == b[case]) / n
    count_a = Counter(a[case] for case in shared)
    count_b = Counter(b[case] for case in shared)
    expected = sum(count_a[label] * count_b[label] for label in DECISIONS) / (n * n)
    if expected == 1:
        return 1.0 if observed == 1 else 0.0
    return (observed - expected) / (1 - expected)


def wilson_interval(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def per_class(reference: dict[str, str], predicted: dict[str, str]) -> dict[str, dict[str, float | int]]:
    shared = [case for case in reference if case in predicted]
    out = {}
    for label in DECISIONS:
        tp = sum(1 for c in shared if predicted[c] == label and reference[c] == label)
        fp = sum(1 for c in shared if predicted[c] == label and reference[c] != label)
        fn = sum(1 for c in shared if predicted[c] != label and reference[c] == label)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        out[label] = {"support": tp + fn, "precision": precision, "recall": recall, "f1": f1}
    return out


def macro_f1(reference: dict[str, str], predicted: dict[str, str]) -> float:
    """Mean F1 over the classes that occur in the reference labels."""
    stats = per_class(reference, predicted)
    present = [label for label in DECISIONS if stats[label]["support"]]
    return sum(stats[label]["f1"] for label in present) / len(present) if present else 0.0


def confusion(reference: dict[str, str], predicted: dict[str, str]) -> dict[str, dict[str, int]]:
    matrix = {a: {p: 0 for p in DECISIONS} for a in DECISIONS}
    for case, actual in reference.items():
        if case in predicted:
            matrix[actual][predicted[case]] += 1
    return matrix


def _pct(x: float) -> str:
    return f"{x:.0%}"


def _compare_block(title: str, reference: dict[str, str], predicted: dict[str, str]) -> list[str]:
    hits, n = agreement(reference, predicted)
    if n == 0:
        return [f"## {title}", "", "No cases in common.", ""]
    low, high = wilson_interval(hits, n)
    kappa = cohen_kappa(reference, predicted)
    lines = [
        f"## {title}",
        "",
        f"- Accuracy: {hits}/{n} = {_pct(hits / n)} (95% interval {_pct(low)} to {_pct(high)})",
        f"- Macro F1: {macro_f1(reference, predicted):.2f}",
        f"- Cohen's kappa: {kappa:.2f}" if kappa is not None else "- Cohen's kappa: n/a",
        "",
        "| Class | Support | Precision | Recall | F1 |",
        "|---|---:|---:|---:|---:|",
    ]
    for label, stats in per_class(reference, predicted).items():
        lines.append(
            f"| {label} | {stats['support']} | {stats['precision']:.2f} | {stats['recall']:.2f} | {stats['f1']:.2f} |"
        )
    lines += ["", "Rows are the reference, columns the prediction.", ""]
    lines.append("| | " + " | ".join(DECISIONS) + " |")
    lines.append("|---|" + "|".join("---:" for _ in DECISIONS) + "|")
    for actual, row in confusion(reference, predicted).items():
        lines.append(f"| **{actual}** | " + " | ".join(str(row[p]) for p in DECISIONS) + " |")
    return lines + [""]


def build_report(
    cases: list[dict],
    sheets: dict[str, dict[str, str]],
    synthetic: dict[str, str],
    predictions: dict[str, str] | None = None,
) -> str:
    lines = [
        "# Nelson human-label report",
        "",
        f"- Cases in the set: {len(cases)}",
        f"- Labelers: {len(sheets)} ({', '.join(sheets) or 'none'})",
        "",
        "## Labelers against the synthetic label",
        "",
        "| Labeler | Labeled | Agrees with synthetic | Kappa |",
        "|---|---:|---:|---:|",
    ]
    for name, labels in sheets.items():
        hits, n = agreement(labels, synthetic)
        kappa = cohen_kappa(labels, synthetic)
        lines.append(
            f"| {name} | {len(labels)} | {hits}/{n} ({_pct(hits / n) if n else 'n/a'}) | "
            f"{f'{kappa:.2f}' if kappa is not None else 'n/a'} |"
        )
    lines.append("")
    if len(sheets) > 1:
        lines += ["## Agreement between labelers", "", "| Pair | Agree | Kappa |", "|---|---:|---:|"]
        for (name_a, a), (name_b, b) in combinations(sheets.items(), 2):
            hits, n = agreement(a, b)
            kappa = cohen_kappa(a, b)
            lines.append(
                f"| {name_a} / {name_b} | {hits}/{n} | {f'{kappa:.2f}' if kappa is not None else 'n/a'} |"
            )
        lines.append("")
    reference = majority(sheets.values())
    label_counts = Counter(reference.values())
    lines += [
        "## Human reference label",
        "",
        f"- Cases with a majority label: {len(reference)} of {len(cases)} (ties and unlabeled cases are left out)",
        "- Distribution: " + ", ".join(f"{label} {label_counts.get(label, 0)}" for label in DECISIONS),
        "",
    ]
    if predictions is not None:
        lines += _compare_block("Model against the human reference", reference, predictions)
        lines += _compare_block("Model against the synthetic label (same cases)", synthetic, predictions)
    return "\n".join(lines)


def run_score(argv: list[str]) -> int:
    predictions_path = None
    out_path = None
    sheet_paths: list[Path] = []
    args = iter(argv)
    for arg in args:
        if arg == "--predictions":
            predictions_path = Path(next(args))
        elif arg == "--out":
            out_path = Path(next(args))
        else:
            sheet_paths.append(Path(arg))
    cases = load_cases(LABEL_DIR / "cases.json")
    sheets = dict(read_sheet(path) for path in sheet_paths)
    report = build_report(
        cases,
        sheets,
        synthetic_labels(cases),
        read_predictions(predictions_path) if predictions_path else None,
    )
    if out_path:
        out_path.write_text(report, encoding="utf-8")
        print(f"  [labels] report -> {out_path}")
    else:
        print(report)
    return 0
