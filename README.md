# FLAM AI Team Internship Assignment – The Audit

This repository contains my submission for the **FLAM AI Team Internship – The Audit** assignment.

## Assignment Objectives

The assignment required auditing a previous intern's work in three areas:

- **Part A:** Tokenizer audit
- **Part B:** Serving capacity reconciliation
- **Part C:** Product decision memo

The goal was to reproduce results, identify implementation and conceptual issues, support every claim with measurable evidence, and document the complete investigation process.

---

## Repository Structure

```
.
├── partA/
│   ├── corpus/                     # Multilingual evaluation corpus
│   ├── prepare_corpus.py           # Corpus preparation
│   ├── experiments.py              # Tokenizer comparison experiments
│   ├── fertility_split_fix.py      # Whitespace experiment
│   ├── fertility_ratio_fix.py      # Aggregation experiment
│   ├── corpus_selection.md
│   ├── results.md
│   └── recommendation_memo.md
│
├── partB/
│   ├── b1_calculation.py
│   ├── b3_verify.py
│   ├── b4_verify.py
│   └── answers.md
│
├── partC/
│   ├── estimate.py
│   └── memo.md
│
├── bench/
├── corpus_sample/
├── fertility.py
├── REPORT_v0.md
├── NOTEBOOK.md
├── AI_USAGE.md
└── README.md
```

---

## Deliverables

### Part A – Tokenizer Audit

- Built a multilingual evaluation corpus (English, Hindi, Kannada, Tamil)
- Audited the provided tokenizer benchmark
- Investigated implementation issues
- Compared GPT-2 and XLM-RoBERTa tokenizers
- Produced an evidence-backed recommendation memo

### Part B – Capacity Reconciliation

- Computed KV-cache memory requirements
- Estimated maximum concurrent sequences
- Investigated throughput anomalies
- Verified benchmark metrics using reproducible calculations

### Part C – Decision Memo

- Evaluated three deployment strategies
- Performed engineering trade-off analysis
- Included back-of-the-envelope calculations
- Recommended an inference-time rewriter approach

---

## Reproducibility

All reported conclusions are supported by executable scripts and documented experiments.

Example:

```bash
python fertility.py ...
python partA/experiments.py
python partB/b1_calculation.py
python partB/b3_verify.py
python partB/b4_verify.py
python partC/estimate.py
```

---

## Documentation

- **NOTEBOOK.md** – Chronological research log (hypothesis → experiment → result → conclusion)
- **AI_USAGE.md** – Summary of AI assistance during the assignment

---

## Technologies

- Python
- Hugging Face Transformers
- Hugging Face Datasets
- tiktoken
- pandas

---

## Summary

This submission focuses on **reproducible experiments** rather than assumptions. Every major conclusion in the audit is supported by measured evidence, consistent with the assignment requirements.

## Development Workflow

The repository was developed incrementally with multiple Git commits to reflect the chronological investigation process. The commit history mirrors the progression from reproducing the baseline to experimentation, analysis, and final recommendations.