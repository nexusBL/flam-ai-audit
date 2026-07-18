## B2

### Throughput anomaly

Throughput increases from batch 4 to batch 24, peaking at **1607 tok/s**.

However, increasing the batch further causes throughput to decrease:

- Batch 32 → 1384 tok/s
- Batch 48 → 1298 tok/s

### Mechanism

The drop coincides with KV-cache utilization reaching 97% and scheduler preemption increasing from 0 to 7 and then 23 sequences.

The system becomes KV-cache limited rather than compute limited, so scheduler overhead reduces effective throughput.

### Recommendation

Limit the batch size to approximately 24 for this workload.

Expected improvement:

1298 tok/s → 1607 tok/s

≈24% higher throughput while avoiding scheduler preemption.

## B2

### Throughput anomaly

Throughput increases with batch size up to batch 24 (1607.4 tok/s), but then decreases despite larger batches:

- Batch 24 → 1607.4 tok/s
- Batch 32 → 1384.0 tok/s
- Batch 48 → 1298.5 tok/s

### Mechanism

The throughput drop coincides with KV-cache utilization increasing from 93% to 97% and scheduler preemptions increasing from 0 to 7 and then 23 sequences.

This indicates the workload becomes KV-cache limited rather than compute limited. Once the KV cache is nearly saturated, the scheduler begins preempting sequences, introducing additional overhead and reducing effective throughput.

### Recommendation

Limit the batch size to approximately 24 for this workload.

Using the measured results:

- Batch 24: 1607.4 tok/s
- Batch 48: 1298.5 tok/s

Running at batch 24 provides approximately **24% higher throughput** while avoiding scheduler preemption.

## B3

### Misread column

The report interprets `reported_tok_s` as useful generated-token throughput.

However, the benchmark compares workloads with different prompt lengths and generation lengths, so `reported_tok_s` cannot be directly compared across rows.

### Honest goodput

Batch 24

Generated tokens:

24 × 512 = 12288

Wall clock:

61.16 s

Goodput:

12288 / 61.16 = **200.9 generated tokens/s**

A second estimate using ITL produces a similar order of magnitude, confirming that useful decode throughput is much lower than the reported throughput counter.

### Correct conclusion

Longer prompts do **not** inherently improve serving throughput.

The reported throughput metric mixes prompt prefill and decoding work and should not be extrapolated linearly for capacity planning.

The report incorrectly interprets `reported_tok_s` as useful generated-token throughput and compares workloads with different prompt lengths directly.

Using the benchmark log, actual generated-token goodput is:

- Batch 24 (3584 prompt): 12288 generated tokens / 61.16 s = 200.9 tok/s

This is substantially lower than the reported throughput of 1607.4 tok/s.

Repeating the calculation across all long-context rows shows that generated-token goodput decreases beyond batch 24 (200.9 → 173.0 → 162.3 tok/s), contradicting the report's claim that throughput scales linearly with batch size or improves with longer prompts.

The `reported_tok_s` counter appears to measure total processed tokens
(prompt + generated), not only generated output.

Evidence:

Short workload:
- Prompt = 512
- Generation = 256
- (512 + 256) / 256 = 3
- Reported/Goodput = 3.00×

Long workload:
- Prompt = 3584
- Generation = 512
- (3584 + 512) / 512 = 8
- Reported/Goodput = 8.00×

Therefore, REPORT_v0 incorrectly compares `reported_tok_s` across workloads
with different prompt lengths. This leads to the false conclusion that
longer prompts improve throughput and that throughput scales linearly with
batch size.