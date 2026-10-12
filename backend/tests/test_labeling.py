"""Blind labeling set and label scoring. No API calls and no database needed."""
from __future__ import annotations

import csv
import json
from types import SimpleNamespace

import pytest

from nelson import label_score, labeling

BUNDLE = {
    "customer": {
        "customer_id": "C1",
        "customer_full_name": "Pat Example",
        "customer_email": "XXXX",
        "late_delivery_rate": 0.6,
        "tenant_id": "demo-tenant",
    },
    "prior_reviews": [
        {
            "reviewed_at": "2026-04-01",
            "scenario": "late_delivery_frustration",
            "topic": "late_delivery_recovery",
            "human_decision": "Monitor",
            "review_notes": "Review Pat Example for late_delivery_recovery before next outreach.",
        }
    ],
    "recent_orders": [{"order_id": "O1", "customer_id": "C1", "delivery_status": "Late delivery"}],
    "recent_tickets": [],
    "recent_notes": [
        {
            "note_id": "N1",
            "customer_id": "C1",
            "customer_full_name": "Pat Example",
            "scenario": "escalation_retention_case",
            "topic": "executive_escalation",
            "note_text": "Pat Example has a Escalation_Retention_Case pattern; topic is executive_escalation.",
            "source_signal_ids": "T1",
            "tenant_id": "demo-tenant",
        }
    ],
    "recent_emails": [{"email_id": "E1", "subject": "late_delivery_frustration follow-up for Pat Example"}],
    "fulfillment_events": [],
}


def test_blind_bundle_removes_every_label_signal():
    blind = labeling.blind_bundle(BUNDLE)
    text = json.dumps(blind).lower()
    for tag in labeling.GENERATOR_TAGS:
        assert tag not in text
    for word in ('"human_decision"', '"review_notes"', "pat example", "demo-tenant", '"scenario"', '"topic"'):
        assert word not in text
    assert blind["prior_review_dates"] == ["2026-04-01"]
    assert "prior_reviews" not in blind
    assert blind["recent_notes"][0]["note_text"] == "the customer has a [redacted] pattern; topic is [redacted]."
    assert blind["recent_orders"][0]["delivery_status"] == "Late delivery"  # evidence is kept
    assert labeling.leaks_label(blind) == []


def test_leaks_label_detects_a_tag():
    assert labeling.leaks_label({"recent_notes": [{"note_text": "late_delivery_recovery"}]}) == [
        "late_delivery_recovery"
    ]


def test_stratified_sample_is_balanced_and_deterministic():
    rows = [{"review_id": f"R{i:04d}", "human_decision": "Escalate" if i % 3 else "Monitor"} for i in range(300)]
    first = labeling.stratified_sample(rows, 80, seed=7)
    again = labeling.stratified_sample(list(reversed(rows)), 80, seed=7)
    assert [r["review_id"] for r in first] == [r["review_id"] for r in again]
    assert sum(1 for r in first if r["human_decision"] == "Monitor") == 40
    assert sum(1 for r in first if r["human_decision"] == "Escalate") == 40


def test_write_label_set_has_no_labels_in_the_labeler_files(tmp_path):
    cases = [
        {"case_id": "H001", "review_id": "R1", "customer_id": "C1", "review_date": "2026-05-06",
         "bundle": labeling.blind_bundle(BUNDLE)},
    ]
    labeling.write_label_set(cases, out_dir=tmp_path, seed=7)
    packet = (tmp_path / "packet.md").read_text(encoding="utf-8")
    assert "## H001" in packet
    assert "Late delivery" in packet
    for leak in ("Monitor |", "human_decision", "R1", "late_delivery_frustration"):
        assert leak not in packet
    with (tmp_path / "label_sheet_TEMPLATE.csv").open(encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    assert rows == [list(labeling.SHEET_COLUMNS), ["H001", "", "", "", ""]]


def test_predict_cases_uses_the_frozen_bundle_and_records_failures():
    seen = []

    class FakeModels:
        def generate_content(self, model, contents, config):
            seen.append(contents[0])
            if len(seen) == 2:
                raise RuntimeError("quota")
            return SimpleNamespace(text=json.dumps({"predicted_decision": "Stabilize", "rationale": "x"}))

    client = SimpleNamespace(models=FakeModels())
    cases = [{"case_id": "H001", "bundle": {"customer": {"late_delivery_rate": 0.6}}},
             {"case_id": "H002", "bundle": {"customer": {}}}]
    out = labeling.predict_cases(client, cases)
    assert out[0]["predicted_decision"] == "Stabilize" and not out[0]["parse_error"]
    assert out[1]["parse_error"] and out[1]["predicted_decision"] == ""
    assert "late_delivery_rate" in seen[0]


# --- scoring -------------------------------------------------------------------------------


def test_kappa_and_agreement():
    a = {"1": "Monitor", "2": "Escalate", "3": "Monitor", "4": "Stabilize"}
    assert label_score.agreement(a, a) == (4, 4)
    assert label_score.cohen_kappa(a, a) == pytest.approx(1.0)
    b = {"1": "Monitor", "2": "Monitor", "3": "Escalate", "4": "Stabilize"}
    assert label_score.agreement(a, b) == (2, 4)
    assert label_score.cohen_kappa(a, b) < 0.5
    assert label_score.cohen_kappa({}, b) is None


def test_majority_drops_ties():
    ref = label_score.majority(
        [{"1": "Monitor", "2": "Escalate"}, {"1": "Monitor", "2": "Stabilize"}, {"1": "Escalate"}]
    )
    assert ref == {"1": "Monitor"}  # case 2 is a tie between Escalate and Stabilize


def test_wilson_interval_bounds():
    low, high = label_score.wilson_interval(15, 30)
    assert 0.3 < low < 0.5 < high < 0.7
    assert label_score.wilson_interval(0, 0) == (0.0, 0.0)


def test_macro_f1_and_confusion():
    ref = {"1": "Monitor", "2": "Monitor", "3": "Escalate", "4": "Escalate"}
    pred = {"1": "Escalate", "2": "Escalate", "3": "Escalate", "4": "Escalate"}  # always escalates
    stats = label_score.per_class(ref, pred)
    assert stats["Monitor"]["recall"] == 0.0
    assert stats["Escalate"]["recall"] == 1.0
    assert label_score.macro_f1(ref, pred) == pytest.approx((0 + 2 / 3) / 2)
    assert label_score.confusion(ref, pred)["Monitor"]["Escalate"] == 2


def test_read_sheet_skips_blank_and_invalid_rows(tmp_path):
    path = tmp_path / "sheet_a.csv"
    path.write_text(
        "case_id,decision,confidence,labeler,notes\nH001,monitor,3,alex,\nH002,,,alex,\nH003,maybe,1,alex,\n",
        encoding="utf-8",
    )
    assert label_score.read_sheet(path) == ("alex", {"H001": "Monitor"})


def test_build_report_end_to_end():
    cases = [{"case_id": f"H{i}", "review_id": f"R{i}"} for i in range(1, 5)]
    synthetic = {"H1": "Monitor", "H2": "Monitor", "H3": "Escalate", "H4": "Escalate"}
    sheets = {
        "alex": {"H1": "Monitor", "H2": "Stabilize", "H3": "Escalate", "H4": "Stabilize"},
        "sam": {"H1": "Monitor", "H2": "Stabilize", "H3": "Escalate", "H4": "Escalate"},
    }
    predictions = {"H1": "Escalate", "H2": "Stabilize", "H3": "Escalate", "H4": "Escalate"}
    report = label_score.build_report(cases, sheets, synthetic, predictions)
    assert "| alex / sam | 3/4 |" in report
    assert "Cases with a majority label: 3 of 4" in report  # H4 is a 1-1 tie
    assert "## Model against the human reference" in report
    assert "Accuracy: 2/3" in report
    assert "## Model against the synthetic label (same cases)" in report
    assert "Accuracy: 2/4" in report
