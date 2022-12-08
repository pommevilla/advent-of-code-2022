from collections import defaultdict
from pathlib import Path
from typing import Dict


def get_dir_sizes(input_file: str) -> Dict[Path, int]:

    current_dir = Path("/")
    directory_sizes = defaultdict(int)

    with open(input_file) as fin:
        for line in fin:
            line = line.rstrip().split()
            match line:
                case ["$", "cd", newdir]:
                    # print(f"cd to {newdir}")
                    current_dir = (current_dir / newdir).resolve()
                    # print(f"changing to {current_dir=}")
                case ["dir", dir_name]:
                    pass
                case [size, file_name] if size.isdigit():
                    size = int(size)
                    for parent in [current_dir, *current_dir.parents]:
                        directory_sizes[parent] += size

    return directory_sizes


def part_one(directory_sizes: Dict[Path, int]) -> int:
    return sum([x for x in directory_sizes.values() if x <= 100000])


def part_two(directory_sizes: Dict[Path, int]) -> int:
    return min(
        [
            x
            for x in directory_sizes.values()
            if directory_sizes[Path("/")] - x <= 40000000
        ]
    )


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
        directory_sizes = get_dir_sizes(input_file=input_file)
        if args.mode == "p1":
            small_directory_sum = part_one(directory_sizes)
            print(f"Sum of directories of size < 100,000: {small_directory_sum}")
        elif args.mode == "p2":
            directory_size_deleted = part_two(directory_sizes)
            print(f"Size of deleted directory: {directory_size_deleted}")
    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
