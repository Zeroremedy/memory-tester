import time
import argparse

def memory_test(chunk_size: int, delay: float):
    big_list = []
    print(f"Starting memory test: allocating chunks of {chunk_size} bytes with {delay}s delay.")
    try:
        while True:
            big_list.append('a' * chunk_size)
            if delay > 0:
                time.sleep(delay)
    except MemoryError:
        print("MemoryError: Ran out of memory!")
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")

def main():
    parser = argparse.ArgumentParser(description="RAM Stress Test - Allocate large strings to fill memory.")
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=10**9,
        help="Chunk size in bytes to allocate each iteration (default: 1,000,000,000)"
    )
    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=0,
        help="Delay in seconds between allocations (default: 0)"
    )

    args = parser.parse_args()
    memory_test(args.size, args.delay)

if __name__ == "__main__":
    main()
