from typing import List
from collections import deque
from termcolor import colored, cprint
from time import sleep

COLORS_DICT = {
    "CURRENT": "\33[43m",
    "VISITED": "\33[33m",
    "NOT_VISITED": "\033[90m",
    "CEND": "\033[0m",
    "START_OR_END": "\33[41m",
}


def read_elevation_map(input_file: str) -> List[List[str]]:
    elevation_map = []
    with open(input_file) as fin:
        for line in fin:
            line = list(line.strip())
            elevation_map.append(line)

    return elevation_map


def color_text(text: str, color_style: str) -> str:
    return f"{COLORS_DICT[color_style]}{text}{COLORS_DICT['CEND']}"


def print_pretty_map(
    elevation_map: List[List[str]],
    next_location: tuple[int],
    visited: set[tuple[int]],
    start: tuple[int],
    end: tuple[int],
    current_paths: set[tuple[int]] = None,
) -> None:
    output = []
    output.append("=" * len(elevation_map[0]))
    for i, row in enumerate(elevation_map):
        this_row = []
        for j, loc in enumerate(row):
            this_loc = (i, j)
            height = ord(loc)
            if this_loc == next_location:
                # loc = colored(f"{loc}", "yellow")
                loc = color_text(loc, "CURRENT")
            elif this_loc in [start, end]:
                loc = color_text(loc, "START_OR_END")
            elif this_loc in visited:
                loc = color_text(loc, "VISITED")
            else:
                loc = color_text(loc, "NOT_VISITED")
            this_row.append(f"{loc}")
        output.append("".join(this_row))
    print("\n".join(output), end="")
    import sys


def neighborhood(row: int, column: int) -> List[tuple[int]]:
    return [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]


def out_of_bounds(elevation_map: List[List[str]], row: int, column: int) -> bool:
    return (
        row < 0
        or column < 0
        or row >= len(elevation_map)
        or column >= len(elevation_map[0])
    )


def part_one(input_file: str) -> int:
    elevation_map = read_elevation_map(input_file)

    start_positions = []
    bfs = deque()
    visited = {()}

    for i, row in enumerate(elevation_map):
        for j, x in enumerate(row):
            if x in ["S", "a"]:
                start_row = i
                start_column = j
                start_position = (start_row, start_column)
                bfs.append((0, i, j))
                visited.add((0, i, j))
                start_positions.append(start_position)
                elevation_map[i][j] = "a"
            if x == "E":
                end_row = i
                end_column = j
                goal = (end_row, end_column)
                elevation_map[i][j] = "z"

    shortest_distance = None

    while bfs:
        distance, row, column = bfs.popleft()
        for next_row, next_column in neighborhood(row, column):
            next_location = (next_row, next_column)
            # print_pretty_map(
            #     elevation_map, next_location, visited, start_position, goal
            # )
            sleep(0.01)
            if out_of_bounds(elevation_map, next_row, next_column):
                continue
            if next_location in visited:
                continue

            if (
                ord(elevation_map[next_row][next_column])
                - ord(elevation_map[row][column])
                > 1
            ):
                continue
            if next_location == goal:
                print(f"\tDistance traveled: {distance + 1}")
                if shortest_distance is None:
                    shortest_distance = distance + 1
                if distance + 1 < shortest_distance:
                    shortest_distance = distance + 1
                break
            visited.add(next_location)
            bfs.append((distance + 1, next_row, next_column))

    return shortest_distance


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
            answer = part_one()

        print(f"{answer=}")

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
