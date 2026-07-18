from pathlib import Path
import unicodedata

import tiktoken
from transformers import AutoTokenizer


LANGS = ["eng", "hin", "kan", "tam"]


def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [
            unicodedata.normalize("NFC", line.strip())
            for line in f
            if line.strip()
        ]


def get_encoder(name):
    if name == "gpt2":
        enc = tiktoken.get_encoding("gpt2")
        return enc.encode

    tok = AutoTokenizer.from_pretrained(name)
    return lambda x: tok.encode(x, add_special_tokens=False)


def evaluate(lines, encode):
    total_tokens = 0
    total_words = 0
    total_chars = 0
    total_bytes = 0

    for line in lines:
        tokens = encode(line)

        total_tokens += len(tokens)
        total_words += len(line.split())
        total_chars += len(line)
        total_bytes += len(line.encode("utf-8"))

    return {
        "tok/word": total_tokens / total_words,
        "tok/char": total_tokens / total_chars,
        "tok/byte": total_tokens / total_bytes,
        "tokens": total_tokens,
        "sentences": len(lines),
    }


def run(tokenizer_name):
    print("=" * 70)
    print(tokenizer_name)
    print("=" * 70)

    encode = get_encoder(tokenizer_name)

    for lang in LANGS:
        path = Path("partA/corpus") / f"{lang}.txt"

        result = evaluate(load_lines(path), encode)

        print(f"{lang}:")
        print(result)
        print()


if __name__ == "__main__":
    run("gpt2")
    run("xlm-roberta-base")