
from typing import TextIO, Iterator, List

def read_assignment_file(input_io: TextIO) -> Iterator[List[str]]:
    for line in input_io:
        yield line.rstrip().split(sep=',')

def parse_assignments(assignments: List[str]):
    """
    >>> parse_assignments(['1-8', '2-2'])
    [[1, 8], [2, 2]]
    >>> parse_assignments(['59-77', '59-81'])
    [[59, 77], [59, 81]]
    >>> parse_assignments(['13-72', '50-100'])
    [[13, 72], [50, 100]]
    """
    parsed_assignments = []
    for assignment in assignments:
        parsed_assignments.append([int(x) for x in assignment.split(sep="-")])
    return parsed_assignments


def containment_exists(assignments: List[int]) -> bool:
    # first, second = convert_assignments_to_ranges(assignments)     
    """
    >>> containment_exists(['1-8', '2-2'])
    True
    >>> containment_exists(['59-77', '59-81'])
    True
    >>> containment_exists(['13-72', '14-55'])
    True
    >>> containment_exists(['13-72', '50-100'])
    False
    """
    first, second = parse_assignments(assignments)
    if first[0] >= second[0] and first[1] <= second[1]:
        return True
    elif second[0] >= first[0] and second[1] <= first[1]:
        return True
    else:
        return False

def overlap_exists(assignments: List[int]) -> bool:
    # first, second = convert_assignments_to_ranges(assignments)     
    """
    >>> overlap_exists(['1-8', '2-2'])
    True
    >>> overlap_exists(['40-59', '59-81'])
    True
    >>> overlap_exists(['13-13', '20-55'])
    False
    >>> overlap_exists(['10-13', '20-55'])
    False
    >>> overlap_exists(['13-72', '50-100'])
    True
    """
    first, second = parse_assignments(assignments)

    """
    Can look like this:
            -----xxxxxxx----
            ----------xxx---
    Or like this
            --------xxx-----
            ---xxxxxx-------
    """
    
    # case one
    if first[0] <= second[0] <= first[1]:
        return True
    elif second[0] <= first[0] <= second[1]:
        return True
    else:
        return False

def main():
    input_file = "input.txt"
    contained_assignments = 0
    overlapping_assignments = 0
    with open(input_file) as fin:
        for assignments in read_assignment_file(fin):
            if containment_exists(assignments):
                contained_assignments += 1
            if overlap_exists(assignments):
                overlapping_assignments += 1
    print(f'{contained_assignments=}')
    print(f'{overlapping_assignments=}')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="mode")

    args = parser.parse_args()

    if args.mode == "test":
        import doctest
        doctest.testmod()
    else:
        main()