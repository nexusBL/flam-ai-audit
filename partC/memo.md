# Part C – Decision Memo

## Recommendation

I recommend **Option (B): Deploy a small (≤1B) inference-time conversational rewriter model after the main model.**

---

## Assumptions

- One NVIDIA A100 80GB GPU is available for two weeks.
- One native reviewer is available for Hindi and Kannada only.
- Reviewer availability: **10 hours/week × 2 weeks = 20 hours**.
- Reviewer throughput: **~50 samples/hour**.
- Synthetic training data can be generated locally without external APIs.
- Launch review is scheduled in three weeks.

---

## Back-of-the-envelope calculations

Reviewer capacity:

20 hours × 50 samples/hour = **1000 reviewed samples**

Synthetic dataset:

**50,000** casualization pairs

Human review coverage:

1000 / 50,000 = **2%**

This level of review is sufficient for quality auditing through sampling rather than reviewing the entire dataset.

---

## Why Option B

### Option A (SFT)

Pros

- Permanent improvement
- Single-model deployment

Cons

- Requires larger verified datasets
- Limited reviewer availability
- Higher training risk within the available timeline

---

### Option C (Prompt Engineering)

Pros

- Fastest implementation
- No additional model

Cons

- Inconsistent conversational tone
- Difficult to guarantee behavior across six languages
- Prompt drift over time

---

### Option B (Chosen)

Pros

- Faster than full SFT
- More consistent than prompt engineering
- Easy rollback
- Main model remains unchanged
- Small inference overhead
- Can be iterated independently

This approach provides the best balance between quality, engineering effort, and launch risk.

---

## Success Metric

At least **90%** of reviewed outputs should:

- preserve the original meaning
- improve conversational tone
- introduce no factual errors

---

## Kill Criterion

After the first week, if fewer than **80%** of reviewed samples preserve meaning while improving conversational style, abandon the rewriter approach and fall back to prompt engineering for launch.

---

## Day 1 Experiment

1. Generate 500 Hindi and Kannada responses using the current assistant.
2. Rewrite them using the 1B conversational rewriter.
3. Review a random sample with the native reviewer.
4. Record:
   - Meaning preservation
   - Conversational tone
   - Fluency
   - Hallucinations

The experiment will determine whether the rewriter consistently improves style without affecting correctness.