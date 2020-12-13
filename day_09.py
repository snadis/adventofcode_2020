from collections import deque

inputs_test_01 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def read_data(path: str) -> str:
    with open(file=path, mode="r") as f:
        return f.read().strip()


def parse_input(inputs: str) -> list[int]:
    return [int(i) for i in inputs.strip().split("\n")]


def valid_next_numbers(numbers: deque[int]) -> set[int]:
    return {
        i + ii
        for n, i in enumerate(numbers)
        for nn, ii in enumerate(numbers)
        if n != nn
    }


def find_fist_incorect_number(inputs: str, preamble_size: int) -> int:

    inputs = parse_input(inputs=inputs)
    preamble = deque()

    for number in inputs:
        # building up preamble
        if len(preamble) < preamble_size:
            preamble.append(number)
            continue

        valid_next = valid_next_numbers(numbers=preamble)

        if number not in valid_next:
            return number

        preamble.popleft()
        preamble.append(number)


def make_contiguous_set_dictionary(
    inputs: list[int], numbers: int
) -> dict[int, list[int]]:

    contiguous_numbers = {
        sum(set(inputs[i : i + numbers])): inputs[i : i + numbers]
        for i in range(len(inputs) - numbers)
    }
    return contiguous_numbers


def find_contiguous_set(inputs: str, preamble_size: int):

    find_number = find_fist_incorect_number(inputs=inputs, preamble_size=preamble_size)
    inputs = parse_input(inputs=inputs)

    for i in range(2, len(inputs)):
        contiguous_sums = make_contiguous_set_dictionary(inputs=inputs, numbers=i)

        if find_number in contiguous_sums.keys():

            return min(contiguous_sums[find_number]) + max(contiguous_sums[find_number])


assert find_fist_incorect_number(inputs=inputs_test_01, preamble_size=5) == 127

inputs = read_data(path="data/day_09.txt")

answer_01 = find_fist_incorect_number(inputs=inputs, preamble_size=25)
print(f"First number breaking rule is: {answer_01}")

assert find_contiguous_set(inputs=inputs_test_01, preamble_size=5) == 62

answer_02 = find_contiguous_set(inputs=inputs, preamble_size=25)
print(f"Encryption weakness in your XMAS-encrypted list of numbers is {answer_02}")