from typing import Iterator, List
from collections import deque


def parse_steps(steps: str) -> Iterator[int]:
    import re

    digit_matcher = re.compile('\\d+')

    for step in steps.splitlines():
        boxes, start, end = map(int, re.findall(digit_matcher, step))
        yield boxes, start, end


def parse_input_file(input_file: str) -> List[List[str]]:
    with open(input_file) as fin:
        crate_layout, steps = fin.read().split('\n\n')

    crate_layout = parse_beginning_arrangement(crate_layout)

    return (crate_layout, steps)


def parse_beginning_arrangement(crate_layout: str) -> List[deque[str]]:
    crates = []
    for stack_number, value in read_crate_layout(crate_layout):
        while stack_number >= len(crates):
            crates.append(deque())
        if value != " ":
            crates[stack_number].append(value)

    return crates


def read_crate_layout(crate_layout: str) -> Iterator[str]:
    crate_layout = crate_layout.splitlines()
    for line in crate_layout:
        for i, x in enumerate(range(1, len(line), 4)):
            yield i, line[x]


def get_message(crates: List[deque[str]]) -> str:
    return ''.join(stack[0] for stack in crates)


def part_one(crates, steps) -> List[deque]:
    for boxes, start, end in parse_steps(steps):
        for _ in range(boxes):
            crates[end - 1].appendleft(crates[start - 1].popleft())

    return crates


def part_two(crates: List[deque], steps) -> List[deque]:
    for boxes, start, end in parse_steps(steps):
        temp_stack = deque()
        for _ in range(boxes):
            temp_stack.appendleft(crates[start - 1].popleft())
        crates[end - 1].extendleft(temp_stack)

    return crates


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="mode")

    args = parser.parse_args()

    if args.mode == "test":
        import doctest
        doctest.testmod()
    elif args.mode.startswith('p'):
        input_file = "input.txt"
        beginning_arrangement, steps = parse_input_file(input_file)
        if args.mode == "p1":
            ending_arrangement = part_one(
                crates=beginning_arrangement, steps=steps)
        elif args.mode == "p2":
            ending_arrangement = part_two(
                crates=beginning_arrangement, steps=steps)

        print(get_message(ending_arrangement))
    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
