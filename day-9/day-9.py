from typing import List
from math import copysign
from time import sleep


class knot_position(tuple):
    def __add__(self, other) -> "knot_position":
        return knot_position(x + y for x, y in zip(self, other))

    def __sub__(self, other) -> "knot_position":
        return knot_position(x - y for x, y in zip(self, other))

    def distance(self, other) -> "knot_position":
        return self - other


direction_steps = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def next_move(head: knot_position, tail: knot_position) -> knot_position:
    distance = head - tail
    if 2 not in distance and -2 not in distance:
        return knot_position((0, 0))
    else:
        move = (0 if x == 0 else (int(copysign(1, x))) for x in distance)

        return knot_position(move)


def part_one(input_file: str) -> int:
    tail = knot_position((0, 0))
    head = knot_position((0, 0))

    places_visited = set()

    with open(input_file) as fin:
        for line in fin:
            direction, steps = line.split()
            direction = knot_position(direction_steps[direction])

            for _ in range(int(steps)):
                head = head + direction

                tail_next_move = next_move(head, tail)

                tail = tail + tail_next_move

                places_visited.add(tail)

    print(f"Visited {len(places_visited)} places.")


def show_knots(knots: List[knot_position]) -> None:
    num_cols = 40
    num_rows = 28
    dims = (num_rows, num_cols)

    # manual positioning for test_input_2.txt
    shift_position = lambda knot: (knot[0] + 14, knot[1] + 10)

    # shift_position = lambda knot: tuple(
    #     a + int(b / 3) for a, b in zip(knot, dims[::-1])
    # )
    shifted_knots = [shift_position(knot) for knot in knots]
    print("# " * dims[1])
    for i in range(dims[0]):
        for j in range(dims[1]):
            if (j, i) in shifted_knots:
                print(f"{shifted_knots.index((j, i))} ", end="")
            else:
                print("- ", end="")
        print()
    print("# " * dims[1])


def part_two(input_file: str, num_knots=10) -> int:
    knots = [knot_position((0, 0)) for _ in range(num_knots)]

    places_visited = set()

    with open(input_file) as fin:
        for line in fin:
            direction, steps = line.split()
            direction = knot_position(direction_steps[direction])

            for _ in range(int(steps)):
                knots[0] = knots[0] + direction
                for i in range(len(knots) - 1):

                    next_knot_move = next_move(knots[i], knots[i + 1])

                    knots[i + 1] = knots[i + 1] + next_knot_move

                places_visited.add(knots[-1])

                show_knots(knots)
                sleep(0.1)

    print(f"Visited {len(places_visited)} places.")


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
        input_file = "test_input_2.txt"
        # input_file = "input.txt"
        if args.mode == "p1":
            part_two(input_file, num_knots=2)
        elif args.mode == "p2":
            part_two(input_file)

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
