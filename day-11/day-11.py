from typing import Dict, List
import re
from collections import defaultdict


def get_starting_items(starting_items_info: str) -> List[int]:
    """
    >>> get_starting_items("Starting items: 79, 98")
    [79, 98]
    >>> get_starting_items("Starting items: 54, 65, 75, 74")
    [54, 65, 75, 74]
    >>> get_starting_items("Starting items: 79, 60, 97")
    [79, 60, 97]
    >>> get_starting_items("Starting items: 74")
    [74]
    """
    starting_items = [int(x) for x in starting_items_info.split(":")[1].split(",")]

    return starting_items


def get_operation(operation_info: str) -> str:
    """
    >>> get_operation("Operation: new = old * 19")
    'old * 19'
    >>> get_operation("Operation: new = old + 6")
    'old + 6'
    >>> get_operation("Operation: new = old * old")
    'old * old'
    >>> get_operation("Operation: new = old + 3")
    'old + 3'
    """
    operation = operation_info.split("=")[1].strip()
    return operation


def get_test(test_info: str) -> str:
    """
    >>> get_test("Test: divisible by 23")
    23
    >>> get_test("Test: divisible by 19")
    19
    >>> get_test("Test: divisible by 13")
    13
    >>> get_test("Test: divisible by 17")
    17
    """
    test = int(re.search(r"divisible\sby\s(\d+)", test_info).group(1))

    return test


def get_next_monkey(throw_info: str) -> str:
    """
    >>> get_next_monkey("If true: throw to monkey 2")
    2
    >>> get_next_monkey("If true: throw to monkey 1")
    1
    >>> get_next_monkey("If true: throw to monkey 0")
    0
    >>> get_next_monkey("If true: throw to monkey 2")
    2
    """
    throw_to = int(throw_info.split()[-1])

    return throw_to


def parse_monkey(monkey_info: str) -> Dict[str, str]:
    monkey_info = monkey_info.splitlines()
    starting_items = get_starting_items(monkey_info[1])
    operation = lambda old: eval(get_operation(monkey_info[2]))
    test = get_test(monkey_info[3])
    if_true = get_next_monkey(monkey_info[4])
    if_false = get_next_monkey(monkey_info[5])

    new_monkey = {
        "starting_items": starting_items,
        "operation": operation,
        "test": test,
        "if_true": if_true,
        "if_false": if_false,
    }

    return new_monkey


def parse_input(input_file: str) -> List[Dict[str, str]]:
    with open(input_file) as fin:
        monkeys = []
        raw_text = fin.read().split("\n\n")
        for monkey_info in raw_text:
            monkeys.append(parse_monkey(monkey_info))

    return monkeys


def get_monkey_lcm(monkeys: List[Dict[str, str]]):
    from math import lcm

    # See day-11/README.md

    monkey_lcm = lcm(*(monkey["test"] for monkey in monkeys))

    return monkey_lcm


def part_one(monkeys: List[Dict[str, str]], worry_mod=3, rounds=20) -> int:
    inspections = defaultdict(int)
    for round in range(rounds):
        for i, monkey in enumerate(monkeys):
            for item in monkey["starting_items"]:
                inspections[i] += 1

                # Get new value, divide by worry_mod.
                # Uncomment this line for part 1
                # I know the operations aren't the same, but I don't feel like
                # refactoring :)
                # new_value = monkey["operation"](item) // worry_mod

                # Get new value, divide by monkey_lcm
                new_value = monkey["operation"](item) % worry_mod

                # Giving monkeys an inner 'throw_to' dictionary with keys 'True'
                # and 'False' simplifies this part a lot.
                pass_test = "true" if new_value % monkey["test"] == 0 else "false"
                next_monkey = monkey[f"if_{pass_test}"]
                monkeys[next_monkey]["starting_items"].append(new_value)

            # Monkey will always throw away all their items
            monkey["starting_items"] = []

    print(f"== After round {round + 1} ==")
    for monkey in inspections:
        print(f"Monkey {monkey} inspected items {inspections[monkey]} times.")

    inspections = sorted(inspections.values())

    return inspections[-1] * inspections[-2]


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
        input_file = "test_input.txt"
        input_file = "input.txt"
        monkeys = parse_input(input_file)
        if args.mode == "p1":
            answer = part_one(monkeys)
            print(f"Monkey business: {answer}")
        elif args.mode == "p2":
            worry_mod = get_monkey_lcm(monkeys)
            answer = part_one(monkeys, worry_mod=worry_mod, rounds=10000)
            print(f"Monkey business: {answer}")

    else:
        print("unknown argument")


if __name__ == "__main__":
    main()
