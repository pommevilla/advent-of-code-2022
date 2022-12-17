from typing import List
from collections import deque
from termcolor import colored, cprint
from time import sleep


def print_out_cave(grid) -> None:
    for i, row in grid:
        for j, x in row:
            print(x, end="")


def create_border_and_abyss(input_file: str) -> List[List[int]]:
    abyss = 0
    border = set()
    with open(input_file) as fin:
        for line in fin:
            line = line.rstrip().split("->")
            points = [list(map(int, point.split(","))) for point in line]
            for (x1, y1), (x2, y2) in zip(points, points[1:]):
                x1, x2 = sorted([x1, x2])
                y1, y2 = sorted([y1, y2])
                abyss = max(abyss, y2 + 1)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        border.add(x + y * 1j)

    return border, abyss


def part_one(input_file: str) -> int:
    blocked, abyss = create_border_and_abyss(input_file)
    print(blocked)

    total_sand_particles = 0

    while 500 not in blocked:
        sand_position = 500
        while True:
            if sand_position.imag >= abyss:
                break
            # Tries to fall straight down
            if sand_position + 1j not in blocked:
                sand_position += 1j
                continue
            # If it can't, it goes diagonally left
            if sand_position + 1j - 1 not in blocked:
                sand_position += 1j - 1
                continue
            # If it can't, it goes diagonally right
            if sand_position + 1j + 1 not in blocked:
                sand_position += 1j + 1
                continue
            break
            # If it can't do any of these, it's not moving.
        blocked.add(sand_position)
        total_sand_particles += 1

    return total_sand_particles


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
