from collections import defaultdict
from functools import lru_cache

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


def make_adapter_paths(
    bag, current_adapter: int, path: list[int], paths=list[list[int]]
) -> list[list[int]]:

    # print(f"ca:{current_adapter}, path={path}")
    global adapter_paths
    target_adapter = max(bag)
    # bag.sort()

    if not path:
        path = []

    if current_adapter == target_adapter:
        adapter_paths.append(path)

    if not current_adapter:
        current_adapter = 0
        path.append(current_adapter)

    for adapter in bag:
        if current_adapter < adapter <= current_adapter + 3:
            make_adapter_paths(bag, adapter, path + [adapter])

    return adapter_paths


assert jolt_differences_1_3(inputs=inputs_test_01) == 35
assert jolt_differences_1_3(inputs=inputs_test_02) == 22 * 10

inputs = read_data("data/day_10.txt")
answer_1 = jolt_differences_1_3(inputs=inputs)
print(f"Jolt differences 1 * 3 = {answer_1}")

adapter_paths = []
assert (
    len(
        make_adapter_paths(
            bag=parse_input(inputs_test_01), current_adapter=None, path=None, paths=None
        )
    )
    == 8
)

adapter_paths = []
assert (
    len(
        make_adapter_paths(
            bag=parse_input(inputs_test_02), current_adapter=None, path=None, paths=None
        )
    )
    == 19208
)


adapter_paths = []
make_adapter_paths(bag=parse_input(inputs), current_adapter=None, path=None, paths=None)
answer_2 = len(adapter_paths)
print(f"Number of distinct ways you can arrange the adapters: {answer_2}")