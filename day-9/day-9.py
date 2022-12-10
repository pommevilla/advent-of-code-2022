from typing import List


class knot_position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> "knot_position":
        return knot_position(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "knot_position":
        return knot_position(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"x={self.x}, y={self.y}"

    def move(self, x, y) -> None:
        self.x += x
        self.y += y

    def distance(self, other: "knot_position"):
        return (self.x - other.x, self.y - other.y)

    def get_position(self):
        return (self.x, self.y)

    def __contains__(self, key):
        return key in (self.x, self.y)

    def __iter__(self):
        for pos in (self.x, self.y):
            yield pos


direction_steps = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def part_one(input_file: str) -> int:
    tail = knot_position(0, 0)
    head = knot_position(0, 0)

    positions_traveled = set([tail.get_position()])

    with open(input_file) as fin:
        counter = 0
        for line in fin:
            counter += 1
            direction, steps = line.split()
            print("-----------------------")
            print(f"{direction=}, {steps=}")
            print(f"\tMove: {direction_steps[direction]}")

            print(f"\tHead position before move: {head}")
            for _ in range(int(steps)):

                print(f"{head=}\t{tail=}")
                this_move = direction_steps[direction]
                head.move(*this_move)
                if any(abs(coord) == 2 for coord in head.distance(tail)):
                    if any(abs(coord) == 1 for coord in head.distance(tail)):
                        # print(f"\tMoving tail with last move: {last_move=}")
                        tail.move(*last_move)
                    print(f"\t{head=}\t{tail=}\t{head.distance(tail)}")
                    tail.move(*this_move)  # This works for one move away
                    print(f"\tMoving tail with {this_move=}")

                    positions_traveled.add(tail.get_position())
                # print(f"Distance={head.distance(tail)}")
            print(f"\tTail position after move: {tail}")
            print(f"\tHead position after move: {head}")
            last_move = this_move

    print(f"{positions_traveled=}")
    print(f"Num positions visited: {len(positions_traveled)}")


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
            part_one(input_file)
        elif args.mode == "p2":
            part_two(input_file)

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
