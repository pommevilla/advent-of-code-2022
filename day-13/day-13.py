from typing import List
from collections import deque
from termcolor import colored, cprint
from time import sleep


def read_input(input_file: str):
    with open(input_file) as fin:
        lists = fin.read().strip().split("\n\n")
        x = list(map(str.splitlines, lists))

    return x


def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    # If they're both lists...
    for a, b in zip(x, y):
        diff = compare(a, b)
        # If there is a difference...
        if diff:
            return diff

    return len(x) - len(y)


def part_one(input_file: str) -> int:
    lists = read_input(input_file)

    in_order_count = 0

    for i, (a, b) in enumerate(lists):
        if compare(eval(a), eval(b)) < 0:
            in_order_count += i + 1

    return in_order_count


def part_two(input_file: str) -> int:
    with open(input_file) as fin:
        lists = fin.read().split()
        lists = map(eval, lists)

    packet_2 = [[2]]
    packet_6 = [[6]]
    index_2 = 1
    index_6 = 2

    for x in lists:
        if compare(x, packet_2) < 0:
            index_2 += 1
            index_6 += 1
        elif compare(x, packet_6) < 0:
            index_6 += 1

    return index_2 * index_6


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
        # input_file = "test_input.txt"
        input_file = "input.txt"
        if args.mode == "p1":
            answer = part_one(input_file)

        elif args.mode == "p2":
            answer = part_two(input_file)

        print(f"{answer=}")

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
