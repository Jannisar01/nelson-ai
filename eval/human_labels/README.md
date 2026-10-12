# Blind human labels

The reviewer decisions in `customer_review_logs` are synthetic, and each one follows from its scenario: every `escalation_retention_case` review is labeled Escalate and every `late_delivery_frustration` review is labeled Monitor (1,599 and 983 of 2,582). No review is labeled Stabilize. Agreement with those labels shows how well a model recovers the generator's scenario, not whether its recommendation is sound. This folder holds a set of cases for people to label without seeing any label, so Nelson can be scored against human judgment.

## Files

| File | What it is |
|---|---|
| `packet.md` | 80 cases (H001 to H080) to read: account fields, recent orders, tickets, notes, emails and fulfillment events |
| `label_sheet_TEMPLATE.csv` | the answer sheet: `case_id, decision, confidence, labeler, notes` |
| `cases.json` | the frozen evidence for each case and the review it came from. Labelers should not open it: the review ID leads to the synthetic label |

Built with `python -m nelson.cli label-sheet 80 7`: one review per customer, 40 drawn from each synthetic label, seed 7. Each case shows the same evidence bundle the eval gives the model, with these removed: the customer's name and email, prior review decisions and notes (only their dates remain), and the generator's scenario and topic tags, as fields and inside note and email text. The synthetic notes and emails were written from the scenario, so their wording can still hint at it (for example an email subject "Executive Escalation").

## Labeling

1. Copy `label_sheet_TEMPLATE.csv` to `sheet_<name>.csv`.
2. For each case in `packet.md`, fill in `decision` (Monitor, Stabilize or Escalate), `confidence` (1 unsure to 3 sure), and your name in `labeler`. Label alone; do not discuss cases.
3. Two or more labelers are needed for an agreement figure.

## Scoring

```bash
python -m nelson.cli label-predict                                   # model predictions on the same 80 cases; one Gemini call each
python -m nelson.cli label-score eval/human_labels/sheet_a.csv eval/human_labels/sheet_b.csv \
    --predictions eval/human_labels/predictions_<stamp>.json --out eval/human_labels/report.md
```

`label-score` makes no model calls. It reports each labeler's agreement with the synthetic label, agreement between labelers (Cohen's kappa), the majority human label per case (ties left out), and the model against that human label: accuracy with a 95% interval, macro F1, per-class precision and recall, and a confusion matrix, next to the model's score against the synthetic label on the same cases.

No human labels exist yet. Model predictions are in `predictions_20261012_150618.json` (`gemini-3-flash-preview`, 12 Oct 2026, Gemini API free tier): 78 of the 80 cases have a decision (41 Stabilize, 30 Escalate, 7 Monitor); H034 and H035 came back as parse errors and have none. They have not been scored, since there are no human labels to score them against.
