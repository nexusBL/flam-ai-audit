# Lab Notebook

## 2026-07-18

### Repository setup
- Initialized Git repository.
- Added provided starter kit.
- Reviewed assignment requirements and deliverables.

### Initial observations
- Read REPORT_v0.md.
- Read fertility.py.
- Read model_spec.md.
- Read bench_log.csv.

### Initial hypotheses
- Need to verify whether tokens-per-word is the correct metric for routing decisions.
- Need to verify whether the reported serving throughput reflects actual goodput.
- Do not assume suspicious-looking code is incorrect without experimental evidence.

## Experiment 1 – Baseline Reproduction

Goal:
Reproduce the benchmark reported in REPORT_v0.md using the original script without modification.

Command:
python fertility.py --corpus eng=corpus_sample/eng_sample.txt --corpus hin=corpus_sample/hin_sample.txt --tokenizer gpt2

Result:
Successfully reproduced the published values.

English: 1.27 tok/word
Hindi: 7.45 tok/word
Ratio: 5.89×

Conclusion:
The original report is reproducible. Further investigation will focus on whether the methodology and metrics are correct rather than whether the implementation executes successfully.