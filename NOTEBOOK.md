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

## Experiment 2 – Whitespace Tokenization

### Hypothesis
Using `split(" ")` instead of `split()` incorrectly counts empty strings created by multiple spaces as words.

### Method
Created a copy of `fertility.py` and replaced:

```python
line.split(" ")
```

with

```python
line.split()
```

All other logic remained unchanged.

### Results

| Metric | Original | Modified |
|---------|---------:|---------:|
| English fertility | 1.27 | 1.28 |
| Hindi fertility | 7.45 | 7.60 |
| Hindi/English ratio | 5.89× | 5.92× |

### Conclusion

The implementation is less robust because repeated spaces create empty tokens.
However, the effect on the reported fertility values is very small and does not explain the report's main conclusions.

## Experiment 3 – Aggregation Strategy

### Hypothesis

The script computes the average of per-line fertility values rather than the ratio of total tokens to total words.

### Method

Modified only the aggregation logic while leaving tokenization unchanged.

### Results

| Metric | Original | Modified |
|---------|---------:|---------:|
| English fertility | 1.27 | 1.25 |
| Hindi fertility | 7.45 | 7.40 |
| Hindi/English ratio | 5.89× | 5.91× |

### Conclusion

Changing the aggregation method produces only a small change.
This implementation choice is not sufficient to explain the report's recommendation.

## Experiment 4 – Tokenizer Comparison

### Goal

Determine whether the report's conclusions hold across different tokenizers.

### Corpus

500 aligned sentences in:

- English
- Hindi
- Kannada
- Tamil

Prepared from the OPUS-100 multilingual parallel corpus.

### Tokenizers

1. GPT-2
2. XLM-RoBERTa Base

### Results

| Language | GPT-2 tok/word | XLM-R tok/word |
|----------|---------------:|---------------:|
| English | 1.31 | 1.46 |
| Hindi | 7.17 | 1.63 |
| Kannada | 17.93 | 2.79 |
| Tamil | 24.08 | 2.68 |

### Observation

GPT-2 produces dramatically more tokens for Indic languages than XLM-RoBERTa.

### Conclusion

The report's statement that "any tokenizer will struggle" is not supported.

The observed fertility depends strongly on tokenizer choice.

## Experiment 8 – Validate KV Cache Saturation Hypothesis

### Hypothesis

The throughput drop observed after batch size 24 is caused by KV-cache saturation leading to scheduler preemption.

### Method

Filtered the benchmark log to inspect runs with KV cache utilization above 90%.

Command:

```bash
python partB/b4_verify.py
```

### Results

| Batch | KV Util | Preempted | Reported tok/s |
|------:|---------:|----------:|---------------:|
|24|0.93|0|1607.4|
|32|0.97|7|1384.0|
|48|0.97|23|1298.5|

### Conclusion

As KV cache utilization approaches saturation, scheduler preemption increases and throughput decreases. This supports the hypothesis that the workload becomes KV-cache limited rather than compute limited.

## Experiment 9 – Deployment Strategy Evaluation

### Goal

Evaluate the feasibility of the three proposed deployment strategies under the provided engineering constraints.

### Method

Estimated reviewer capacity using:

- 20 review hours
- 50 samples/hour

Implemented:

```bash
python partC/estimate.py
```

### Results

Reviewer capacity: 1000 samples

Synthetic dataset: 50,000 samples

Review coverage: 2%

### Conclusion

A sampled review process is feasible within the available reviewer budget.

Given the timeline and hardware constraints, an inference-time rewriter provides the best trade-off between deployment risk and conversational quality.