from collections import defaultdict
from math import prod
from typing import List

inputs_test_01 = """16
10
15
5
1
11
7
19
6
12
4"""

inputs_test_02 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def read_data(path: str) -> str:
    with open(file=path, mode="r") as f:
        return f.read().strip()


def parse_input(inputs: str) -> list[int]:
    return [int(line) for line in inputs.strip().split("\n")]


def jolt_differences_1_3(inputs: str):

    inputs = parse_input(inputs)
    inputs.append(0)
    inputs.sort()

    jolt_differences = defaultdict(int)

    for i, value in enumerate(inputs[:-1]):
        difference = inputs[i + 1] - value
        jolt_differences[difference] += 1

    return jolt_differences[1] * (jolt_differences[3] + 1)


def make_adapter_groups(bags: List[int]) -> List[List[int]]:
    target = max(bags)
    groups = [[target]]

    while True:

        group = [i for i in bags if target - 3 <= i < target]
        groups.append(group)

        target = min(group)

        if target == min(bags):
            break

    groups.append([0])

    return groups


def convert_groups_to_combinations(groups: List[List[int]]) -> List[int]:
    combinations = []
    for i, group in enumerate(groups[:-1]):
        group_size = len(group)
        if group_size < 3:
            combinations.append(group_size)
        else:
            next_group_max = max(groups[i + 1])
            group_numbers_can_be_first = len(
                [i for i in group if next_group_max + 3 >= i]
            )
            if group_numbers_can_be_first == 3:
                combinations.append(7)
            elif group_numbers_can_be_first == 1:
                combinations.append(4)
    return combinations


def calculate_adapter_paths(inputs: str) -> int:
    bags = parse_input(inputs=inputs)
    groups = make_adapter_groups(bags=bags)
    combinations = convert_groups_to_combinations(groups=groups)

    return prod(combinations)


assert jolt_differences_1_3(inputs=inputs_test_01) == 35
assert jolt_differences_1_3(inputs=inputs_test_02) == 22 * 10

inputs = read_data("data/day_10.txt")
answer_1 = jolt_differences_1_3(inputs=inputs)
print(f"Jolt differences 1 * 3 = {answer_1}")

assert calculate_adapter_paths(inputs=inputs_test_01) == 8
assert calculate_adapter_paths(inputs=inputs_test_02) == 19208


answer_2 = calculate_adapter_paths(inputs=inputs)
print(f"Number of distinct ways you can arrange the adapters: {answer_2}")
