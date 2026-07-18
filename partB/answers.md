|## B1

### KV Cache Size

Formula:

28 layers × 8 KV heads × 128 head dimension × 2 (K+V) × 2 bytes (FP16)

= **114,688 bytes/token**

### Maximum Concurrent Sequences

Available KV memory:

24 GB × 0.92 − 1.6 GB ≈ 20.48 GB

Memory per 4096-token sequence:

114,688 × 4096 = 469,762,048 bytes ≈ 448 MB

Maximum concurrent sequences:

≈46 sequences

This matches the benchmark where throughput begins degrading as KV utilization approaches saturation.

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

The report assumes `reported_tok_s` represents useful generated-token throughput. However, it counts total processed tokens (prompt + generated), making comparisons across different prompt lengths misleading.

### Evidence

Batch 24:

Generated tokens:
24 × 512 = 12288

Wall clock:
61.16 s

Generated-token goodput:
12288 / 61.16 = **200.9 tok/s**

Observed:

- Reported throughput = 1607.4 tok/s
- Goodput = 200.9 tok/s

Ratio:
1607.4 / 200.9 ≈ 8×

This matches:

(3584 + 512) / 512 = 8

indicating the reported metric counts prompt and generated tokens together.

### Conclusion

Longer prompts do not inherently improve useful serving throughput. Capacity planning should rely on generated-token goodput rather than the reported throughput counter.

## B4

I would monitor the scheduler's **preempted sequence count** together with **KV-cache utilization**.

Evidence from the benchmark shows:

- Batch 24: KV utilization = 93%, Preempted = 0, Throughput = 1607.4 tok/s
- Batch 32: KV utilization = 97%, Preempted = 7, Throughput = 1384.0 tok/s
- Batch 48: KV utilization = 97%, Preempted = 23, Throughput = 1298.5 tok/s

The increasing number of preempted sequences as KV-cache utilization approaches saturation supports the conclusion that the throughput drop is caused by KV-cache pressure rather than insufficient compute capacity.

In production, I would expect preempted sequences to remain close to zero during healthy operation and increase rapidly once KV-cache utilization exceeds approximately 95%.