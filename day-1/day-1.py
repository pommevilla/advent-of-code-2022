# Part 1
# Iterate over each one
# Compare to current highest
# If higher than current highest, keep track of which elf it was
# and how many calories they have

current_calories = 0
current_elf_position = 1

highest_calories = 0
highest_elf_position = 0

# with open('day-1/input.txt') as fin:
#     for line in fin:
#         if line.strip():
#             current_calories += int(line)
#         else:
#             if current_calories >= highest_calories:
#                 highest_calories = current_calories
#                 highest_elf_position = current_elf_position
#             current_calories = 0
#             current_elf_position += 1

# print(f'The elf with the most calories had {highest_calories} at position {highest_elf_position}.')

# Part 2
# Approaches:
# 1. Just record every elves' calories, sort the list, take the top 3
#       Running time: O(n) for going through the list +
#                    + O(k * log k) for sorting 
#                    + m for taking the top 3,
#           where n is the number of lines in the file, k is the number of elves, and
#           m is the highest calories you're interested in
#       Space: O(k) for the number of elves
# 2. Every time you see a new elf, compare it to the three highest calories recorded so far
#       Running time: O(n) for going through the list
#                   * O(m) for going through the list of 3 
#       Space: O(m) for the number of records you're interested in

n = 3
input_file = 'day-1/input.txt'

# Approach 1
print("----Approach 1----")
print("Record all calories, sort list, sum top 3\n")

from typing import List
import timeit

def approach_1(elves_file: str, n: int) -> List[int]:
    calories_array = []
    current_calories = 0
    with open(elves_file) as fin:
        for line in fin:
            if line.strip():
                current_calories += int(line)
            else:
                calories_array.append(current_calories)
                current_calories = 0

    calories_array.sort(reverse=True)
    return calories_array[:n]

# time_elapsed = timeit.timeit('approach_1(input_file, n)', number = 10000, globals=globals())
# print(f'Average time for approach 1 over 10000 trials: {time_elapsed:.4f}')

highest_n = approach_1(input_file, n)
print(f'Highest three calories from approach 1: {highest_n}')
print(f'Sum of highest three calories from approach 1: {sum(highest_n)}')


# Approach 2
print("----Approach 2----")
print("Keep list of top 3")

def approach_2(elves_file: str, n: int) -> List[int]:
    current_calories = 0
    highest_n_calories = [0 for _ in range(n)]
    with open(elves_file) as fin:
        for line in fin:
            if line.strip():
                current_calories += int(line)
            else:
                for i in range(n):
                    array_position = i + 1
                    if current_calories > highest_n_calories[-array_position]:
                        highest_n_calories.insert(n - i, current_calories)
                        highest_n_calories = highest_n_calories[1:]
                        break
                current_calories = 0
    return highest_n_calories

approach_2_highest = approach_2(input_file, n)
print(f'Highest three calories from approach 2: {approach_2_highest}')
print(f'Sum of {n} highest calories: {sum(approach_2_highest)}')


# Timing 
time_elapsed = timeit.timeit('approach_1(input_file, n)', number = 10000, globals=globals())
print(f'Average time for approach 1 over 10000 trials: {time_elapsed:.4f}')
time_elapsed = timeit.timeit('approach_2(input_file, n)', number = 10000, globals=globals())
print(f'Average time for approach 2 over 10000 trials: {time_elapsed:.4f}')
