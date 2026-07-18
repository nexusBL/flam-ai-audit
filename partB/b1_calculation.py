layers = 28
kv_heads = 8
head_dim = 128
bytes_per_fp16 = 2

kv_bytes_per_token = (
    layers
    * 2
    * kv_heads
    * head_dim
    * bytes_per_fp16
)

print("KV bytes/token:", kv_bytes_per_token)

gpu_memory = 24 * 1024**3
usable = gpu_memory * 0.92 - (1.6 * 1024**3)

sequence_memory = kv_bytes_per_token * 4096

print("Memory per 4096-token sequence:", sequence_memory)

print("Approx concurrent sequences:", usable // sequence_memory)