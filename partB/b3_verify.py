import pandas as pd

df = pd.read_csv("bench/bench_log.csv")

print("=" * 90)

for _, row in df.iterrows():
    generated_tokens = row["batch_size"] * row["gen_len"]

    goodput = generated_tokens / row["wall_clock_s"]
    ratio = row["reported_tok_s"] / goodput

    print(
    f"Batch={int(row['batch_size'])} "
    f"Prompt={int(row['prompt_len'])} "
    f"Reported={row['reported_tok_s']:.1f} "
    f"Goodput={goodput:.1f} "
    f"Inflation={ratio:.2f}x"
)