from typing import List


def check_cycle(cycle: int, mod=20):
    return (cycle + mod) % 40 == 0


def add_to_sum(cycle: int, signal_strength, x):
    if check_cycle(cycle):
        signal_strength += cycle * x
        print(f"{cycle=}\t{x=}\t{cycle * x=}")

    return signal_strength


def get_signal_strength(input_file: str) -> int:
    with open(input_file) as fin:
        cycle = 0
        x = 1
        signal_strength = 0
        for line in fin:
            match line.split():
                case ["noop"]:
                    cycle += 1
                    add_to_sum(cycle, signal_strength, x)
                case ["addx", num]:
                    cycle += 1
                    signal_strength = add_to_sum(cycle, signal_strength, x)
                    cycle += 1
                    signal_strength = add_to_sum(cycle, signal_strength, x)
                    x += int(num)

    return signal_strength


def part_one(input_file: str) -> int:
    return get_signal_strength(input_file)


def handle_pixels(cycle: int, x: int) -> int:
    if cycle % 40 in (x - 1, x, x + 1):
        print("#", end="")
    else:
        print(".", end="")
    cycle += 1
    if check_cycle(cycle, mod=0):
        print()

    return cycle


def part_two(input_file: str) -> int:
    with open(input_file) as fin:
        cycle = 0
        x = 1
        for line in fin:
            match line.split():
                case ["noop"]:
                    cycle = handle_pixels(cycle, x)
                case ["addx", num]:
                    cycle = handle_pixels(cycle, x)
                    cycle = handle_pixels(cycle, x)
                    x += int(num)


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
        # input_file = "test_2.txt"
        # input_file = "test_input.txt"
        input_file = "input.txt"
        if args.mode == "p1":
            target_sum = part_one(input_file)
            print(f"Sum of interest: {target_sum}")
        elif args.mode == "p2":
            part_two(input_file)

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
