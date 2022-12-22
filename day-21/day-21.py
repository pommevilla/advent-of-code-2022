from typing import List
from collections import deque


def part_one(input_file: str) -> int:
    monkeys = {}

    unparsed = [x.strip() for x in open(input_file)]

    for line in unparsed:
        name, expression = line.split(': ')
        print(f'{name=}\t{expression=}')
        if expression.isdigit():
            monkeys[name] = expression
        else:
            print(expression)
            left, operation, right = expression.split()
            # If all of the monkeys already exist, then do the operation
            if left in monkeys and right in monkeys:
                monkeys[name] = eval(
                    f"{monkeys[left]} {operation} {monkeys[right]}")

            # If they don't, add it to the originl array - you'll come back around and do it again
            else:
                unparsed.append(line)

    return monkeys["root"]


def part_two(input_file: str) -> int:
    pass


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
        input_file = "test_input.txt"
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
