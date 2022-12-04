from typing import List, Iterator, TextIO
import timeit

def get_item_priority(rucksack_item: str) -> int:
    """
    >>> get_item_priority('a')
    1
    >>> get_item_priority('A')
    27
    >>> get_item_priority('Z')
    52
    >>> get_item_priority('D')
    30
    >>> get_item_priority('p')
    16
    >>> get_item_priority('v')
    22
    """
    from string import ascii_lowercase

    score = ascii_lowercase.find(rucksack_item.lower()) + 1

    return score + 26 if rucksack_item.isupper() else score

def split_string(input_str: str) -> List[str]:
    half_length = int(len(input_str) / 2)
    return [input_str[:half_length], input_str[half_length:]]

def approach_one(input_str: str) -> int:
    """
    Split the string in half. For each letter in the first half,
    search for that letter in the second half. If you find it,
    return it's priority.

        Running time: O(n^2) since we're searching the string for everyone 
            of it's characters
        Space: O(n) for storing the string

    >>> approach_one("vJrwpWtwJgWrhcsFMMfFFhFp")
    16
    >>> approach_one("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    38
    >>> approach_one("PmmdzqPrVvPwwTWBwg")
    42
    >>> approach_one("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    22
    >>> approach_one("ttgJtRGJQctTZtZT")
    20
    >>> approach_one("CrZsJsPPZsGzwwsLwLmpwMDw")
    19
    """
    split_strings = split_string(input_str=input_str)

    for rucksack_item in split_strings[0]:
        if split_strings[1].find(rucksack_item) != -1:
            return get_item_priority(rucksack_item=rucksack_item)

def approach_two(input: str) -> int:
    """
    Use Python counter collection to count the characters in the strings.
    Find the one that's greater than one, return it's value.

        Running time: O(n^2) since we're searching the string for everyone 
            of it's characters
        Space: O(n) for storing the string

    >>> approach_one("vJrwpWtwJgWrhcsFMMfFFhFp")
    16
    >>> approach_one("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    38
    >>> approach_one("PmmdzqPrVvPwwTWBwg")
    42
    >>> approach_one("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    22
    >>> approach_one("ttgJtRGJQctTZtZT")
    20
    >>> approach_one("CrZsJsPPZsGzwwsLwLmpwMDw")
    19
    """
    pass

def read_n_lines_from_file(input_io: TextIO, n: int=3) -> Iterator[List[str]]:
    line_counter = 0
    lines = []
    for line in input_io:
        line_counter += 1
        line = line.rstrip()
        lines.append(line)
        if line_counter == 3:
            yield lines
            line_counter = 0
            lines = []

    if lines:
        yield lines

def part_one(input_file: str) -> int:
    running_total = 0
    with open(input_file) as fin:
        for line in fin:
            running_total += approach_one(line)
    return running_total

def part_two(input_file: str) -> int:
    with open(input_file) as fin:
        running_total = 0
        for group in read_n_lines_from_file(fin):
            running_total += find_common_items(group)
            
    return running_total

def find_common_items(elf_group: List[str]) -> str:
    """
    Approach: For each string in string1, look for a duplicate in string 2. 
    If you find a duplicate in string 2, look in string 3. This sucks.

        Running time: O(mno) since we're searching the three strings for the characters,
            where m, n, and o are the length of the strings
        Space: O(m + n + o) for storing the string

    >>> group_one = [ "vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
    >>> find_common_items(group_one)
    18
    >>> group_two = [ "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw" ]
    >>> find_common_items(group_two)
    52
    """
    first, second, third = elf_group
    for letter in first:
        if second.find(letter) != -1:
            if third.find(letter) != -1:
                return get_item_priority(letter)

def main():
    input_file = "input.txt"

    part_one_answer = part_one(input_file=input_file)
    print(f'Answer for part one: {part_one_answer}')

    part_two_answer = part_two(input_file)
    print(f'Answer for part two: {part_two_answer}')






if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()