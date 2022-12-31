from typing import List
from collections import deque

blizzard_directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),  # directions reversed since we're starting from the top
    "v": (1, 0)
}


def read_map(input_file: str) -> List[List[str]]:
    blizzards = {}
    with open(input_file) as fin:
        for r, line in enumerate(fin):
            line = line.rstrip()
            for c, x in enumerate(line):
                print(x, end="")
                if x in blizzard_directions:
                    # blizzards.append((x, (r, c)))
                    blizzards[(r, c)] = [x]

            print()
    print(blizzards)

    return r, c, blizzards


def move_blizzard(blizzard, dims):
    next_loc = tuple(
        (a + b) % c for a, b, c in zip(blizzard[1], blizzard_directions[blizzard[0]], dims))
    # a + b for a, b in zip(blizzard[1], blizzard_directions[blizzard[0]]))
    return (blizzard[0], next_loc)


def minute(blizzards, map_height, map_width):
    return [move_blizzard(blizzard, (map_height, map_width)) for blizzard in blizzards]


def print_map(blizzards, map_height, map_width) -> None:
    for r in range(map_height):
        for c in range(map_width):
            if r == 0 or c == 0 or r == map_height - 1 or c == map_width - 1:
                print("#", end="")
            elif (r, c):
                print("X")
            else:
                print(".", end="")
        print()


def part_one(input_file: str) -> int:

    HEIGHT, WIDTH, blizzards = read_map(input_file)

    for i in range(8):
        blizzards = minute(blizzards, HEIGHT, WIDTH)
        print(f"\n=====Minute {i}=====\n")
        print_map(blizzards, HEIGHT, WIDTH)
        # print(blizzards)

    # print_map(blizzard_map)

    return "Not yet implemented."


def part_two(input_file: str) -> int:
    return "Not yet implemented."


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
        # input_file = "input.txt"
        if args.mode == "p1":
            answer = part_one(input_file)

        elif args.mode == "p2":
            answer = part_two(input_file)

        print(f"{answer=}")

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
