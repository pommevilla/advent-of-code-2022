from typing import List
from collections import deque


DIGITS = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

# For translating decimal back to SNAFU
SNAFU_DIGITS = {v: k for k, v in DIGITS.items()}


def snafu_number(number: int) -> str:
    snafu = ""
    while number > 0:
        number, digit = divmod(number, 5)
        if digit > 2:
            digit -= 5
            number += 1
        snafu += SNAFU_DIGITS[digit]

    return snafu[::-1]


def part_one(input_file: str) -> int:

    total = 0
    with open(input_file) as fin:
        for line in fin:
            line = line.rstrip()
            for i, x in enumerate(line[::-1]):
                total += DIGITS[x] * (5 ** i)

    snafu_total = snafu_number(total)
    print(f'{total=}\t{snafu_total=}')

    return snafu_total


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

    elif args.mode == "p1":
        # input_file = "test_input.txt"
        input_file = "input.txt"
        answer = part_one(input_file)

        print(f"{answer=}")

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
