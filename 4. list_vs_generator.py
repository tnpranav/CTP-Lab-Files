import time
import tracemalloc

N = 1_000_000  # size of the large dataset

# ---------------------------
# List-based processing
# ---------------------------
def list_based(n):
    data = [x * x for x in range(n)]   # stores all values in memory
    total = sum(data)
    return total

# ---------------------------
# Generator-based processing
# ---------------------------
def generator_based(n):
    data = (x * x for x in range(n))   # produces values one at a time
    total = sum(data)
    return total

# ---------------------------
# Measurement function
# ---------------------------
def measure(func, n, label):
    tracemalloc.start()
    start = time.time()

    result = func(n)

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"{label}:")
    print(f"  Result        = {result}")
    print(f"  Time taken    = {end - start:.4f} seconds")
    print(f"  Memory used   = {current / 1024:.2f} KB")
    print(f"  Peak memory   = {peak / 1024:.2f} KB")
    print()

# ---------------------------
# Run comparison
# ---------------------------
measure(list_based, N, "List-based Processing")
measure(generator_based, N, "Generator-based Processing")