from typing import List
from math import prod


def read_forest(input_file: str) -> List[str]:
    with open(input_file) as fin:
        forest = fin.read().splitlines()
    return forest


def part_one(forest: List[str]) -> int:
    visible_inner_trees = 0
    num_rows = len(forest)
    num_cols = len(forest[0])
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            tree = forest[i][j]
            # A boolean statement evalutes to one if True
            visible_inner_trees += (
                # Check row to left for visibility
                all(forest[k][j] < tree for k in range(i))
                or
                # Check row to right for visibility
                all(forest[k][j] < tree for k in range(i + 1, num_rows))
                or
                # check column above...
                all(forest[i][l] < tree for l in range(j))
                or
                # check column below
                all(forest[i][l] < tree for l in range(j + 1, num_cols))
            )

    border_trees = (2 * num_cols) + (2 * num_rows) - 4
    return visible_inner_trees + border_trees


def part_two(forest: List[str]) -> int:
    highest_scenic_score = 0
    num_rows = len(forest)
    num_cols = len(forest[0])
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            tree = forest[i][j]
            visibility_scores = []

            visibility = 0
            # Looking right
            for k in range(j + 1, num_cols):
                visibility += 1
                if tree <= forest[i][k]:
                    break
            visibility_scores.append(visibility)

            # Looking left
            visibility = 0
            for k in range(j - 1, -1, -1):
                visibility += 1
                if tree <= forest[i][k]:
                    break
            visibility_scores.append(visibility)

            # Looking down
            visibility = 0
            for l in range(i + 1, num_rows):
                visibility += 1
                if tree <= forest[l][j]:
                    break
            visibility_scores.append(visibility)

            # Looking up
            visibility = 0
            for l in range(i - 1, -1, -1):
                visibility += 1
                if tree <= forest[l][j]:
                    break
            visibility_scores.append(visibility)

            scenic_score = prod(visibility_scores)

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score


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
        forest = read_forest(input_file)
        if args.mode == "p1":
            answer = part_one(forest)
            print(f"Number of visible trees: {answer}")
        elif args.mode == "p2":
            answer = part_two(forest)
            print(f"Number of visible trees: {answer}")

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
