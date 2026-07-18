from datasets import load_dataset
from pathlib import Path

N = 500

pairs = [
    ("en-hi", "hi", "hin"),
    ("en-kn", "kn", "kan"),
    ("en-ta", "ta", "tam"),
]

Path("partA/corpus").mkdir(parents=True, exist_ok=True)

english = []

for config, target_lang, short in pairs:
    print(f"Downloading {config}...")

    ds = load_dataset("Helsinki-NLP/opus-100", config, split=f"train[:{N}]")

    target_lines = []

    for row in ds:
        english.append(row["translation"]["en"])
        target_lines.append(row["translation"][target_lang])

    with open(f"partA/corpus/{short}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(target_lines))

# Save English only once
with open("partA/corpus/eng.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(english[:N]))

print("Corpus prepared successfully!")