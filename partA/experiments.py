samples = [
    "Please keep the books  in the cupboard.",
    "books in cupboard",
    "books  in  cupboard",
]

for s in samples:
    print("=" * 50)
    print(s)

    print("split(' '):", s.split(" "))
    print("count:", len(s.split(" ")))

    print("split():", s.split())
    print("count:", len(s.split()))