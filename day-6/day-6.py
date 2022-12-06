from collections import deque


def part_one(input_file: str, n: int = 4) -> int:
    with open(input_file) as fin:
        # line = fin.read().rstrip()
        for line in fin:
            line = line.rstrip()
            last_n = deque(line[: n - 1])
            for i, x in enumerate(line[n - 1 :]):
                last_n.append(x)
                item_counts = [last_n.count(x) for x in last_n]

                # This works because if there is a duplicate in the counts,
                # then there will be 2 2s, which will make the sum != n
                if sum(item_counts) == n:
                    return i + n
                last_n.popleft()


def part_one_improved(input_file: str, n: int = 4) -> int:
    from collections import Counter

    with open(input_file) as fin:
        for line in fin:
            line = line.rstrip()
            counts = Counter(line[: n - 1])
            for i, x in enumerate(line[n - 1 :]):
                counts[x] += 1

                last_letter = line[i]
                counts[last_letter] -= 1

                if len(counts) == n:
                    return i + n

                if counts[last_letter] == 0:
                    del counts[last_letter]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="mode")

    args = parser.parse_args()

    if args.mode is None:
        print("Nothing")
    elif args.mode == "test":
        import doctest

        doctest.testmod()
    elif args.mode.startswith("p"):
        input_file = "input.txt"
        if args.mode == "p1":
            # process_start = part_one(input_file)
            process_start = part_one_improved(input_file)
        elif args.mode == "p2":
            # process_start = part_one(input_file, n=14)
            process_start = part_one_improved(input_file, n=14)

        print(f"Transmission start: {process_start}")
    elif args.mode == "timing":
        import timeit

        print("------Timing Part One------")
        avg_time_elapsed = (
            timeit.timeit("part_one('input.txt')", number=10000, globals=globals())
            / 10000
        )
        print(f"Average time for part_one over 10000 trials: {avg_time_elapsed:.8f}")
        avg_time_elapsed = (
            timeit.timeit(
                "part_one_improved('input.txt')", number=10000, globals=globals()
            )
            / 10000
        )
        print(
            f"Average time for part_one_improved over 10000 trials: {avg_time_elapsed:.8f}"
        )

        print("------Timing Part Two------")
        avg_time_elapsed = (
            timeit.timeit(
                "part_one('input.txt', n=14)", number=10000, globals=globals()
            )
            / 10000
        )
        print(f"Average time for part_two over 10000 trials: {avg_time_elapsed:.8f}")
        avg_time_elapsed = (
            timeit.timeit(
                "part_one_improved('input.txt', n=14)", number=10000, globals=globals()
            )
            / 10000
        )
        print(
            f"Average time for part_two_improved over 10000 trials: {avg_time_elapsed:.8f}"
        )

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
