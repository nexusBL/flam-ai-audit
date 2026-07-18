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