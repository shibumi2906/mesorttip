import time
import psutil
import os
import tracemalloc

def measure_time_memory(func, *args, **kwargs):
    # Measure time
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    time_taken = end_time - start_time

    # Measure memory
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    memory_usage = memory_info.rss  # in bytes

    return time_taken, memory_usage

def example_algorithm(n):
    result = 0
    for i in range(n):
        result += i
    return result

if __name__ == "__main__":
    tracemalloc.start()
    n = 1000000  # Input size
    time_taken, memory_usage = measure_time_memory(example_algorithm, n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time taken: {time_taken} seconds")
    print(f"Memory usage: {memory_usage / (1024 * 1024)} MB")
    print(f"Peak memory usage: {peak / (1024 * 1024)} MB")
