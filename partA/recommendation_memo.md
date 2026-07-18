# Recommendation Memo

## Summary

The original REPORT_v0 recommends routing all Indic traffic to a separate tokenizer/model and budgeting approximately 6× higher serving cost for Hindi.

After reproducing the benchmark and auditing both the tokenizer analysis and the serving benchmarks, I do not believe this recommendation is sufficiently supported by the available evidence.

---

## Corrected Findings

### 1. Small implementation issues exist

I evaluated two implementation issues in `fertility.py`.

- Using `split(" ")` instead of `split()`
- Averaging per-line fertility instead of computing corpus-level fertility

Both produced only minor numerical changes and did not materially affect the report's conclusions.

---

### 2. Tokenizer choice dominates the results

The original report evaluated only GPT-2.

Repeating the experiment using XLM-RoBERTa produced dramatically different fertility values for Indic languages.

| Language | GPT-2 | XLM-R |
|----------|-------:|-------:|
| English | 1.31 | 1.46 |
| Hindi | 7.17 | 1.63 |
| Kannada | 17.93 | 2.79 |
| Tamil | 24.08 | 2.68 |

This demonstrates that tokenizer selection has a much larger impact than the implementation issues identified in the script.

Therefore the statement

> "Any tokenizer will struggle."

is not supported by the evidence.

---

### 3. Serving analysis

The report interprets `reported_tok_s` as useful serving throughput.

Recomputing generated-token goodput shows that long-context workloads actually deliver lower useful generation throughput than suggested by the benchmark counter.

The benchmark also shows throughput peaking at batch size 24 before decreasing because KV-cache utilization approaches saturation and scheduler preemption begins.

---

## Recommendation

I do **not** recommend immediately routing all Indic traffic to a separate model based solely on the original benchmark.

Instead I recommend:

1. Benchmark multiple multilingual tokenizers.
2. Evaluate using a larger multilingual parallel corpus.
3. Measure generated-token goodput instead of relying only on `reported_tok_s`.
4. Monitor KV-cache utilization and scheduler preemptions during production deployment.

---

## Biggest Caveat

The evaluation corpus contains only 500 sampled parallel sentences and represents general-domain text.

Additional domains such as chat conversations, code, legal text and customer-support conversations should be evaluated before making production routing decisions.

---

## Production Metric

If I could monitor only one production metric, I would monitor **generated-token goodput together with KV-cache utilization**.

A sustained increase in KV-cache utilization above approximately 95% accompanied by scheduler preemption would indicate that serving efficiency is degrading and routing assumptions should be re-evaluated.