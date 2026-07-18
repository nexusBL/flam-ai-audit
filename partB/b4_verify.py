import pandas as pd

df = pd.read_csv("bench/bench_log.csv")

print("=" * 90)
print("Rows where KV cache is above 90%\n")

high_kv = df[df["kv_cache_util"] >= 0.90]

print(
    high_kv[
        [
            "batch_size",
            "kv_cache_util",
            "preempted_seqs",
            "reported_tok_s",
        ]
    ]
)