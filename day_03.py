from collections import deque
from math import prod

inputs_test = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split()


def read_file(path) -> list[str]:
    """Atver failu un nolasa visas rindas."""
    with open(file=path, mode="r", encoding="utf-8") as f:
        data = f.readlines()
    return [l.strip() for l in data]


def shift_row(tree_row: deque[str], step: int, right: int) -> deque[str]:
    """Pagriež rindu par x"""
    shift = step * -right
    tree_row.rotate(shift)
    return tree_row


def slope_trees(inputs: list[str], right: int) -> int:
    """
    Izstaigā mežu pārvieotjoties vienu rindu uz leju un trīs pa labi
    Atgriež ceļā sastapto koku skatu
    """
    path = [
        shift_row(tree_row=deque(row), step=i, right=right)[0]
        for i, row in enumerate(inputs, start=0)
    ]

    return path.count("#")


def multiple_slopes(slopes: str, inputs: list[str]):
    trees = []
    for right, down in slopes:
        inputs = inputs[::down]
        trees.append(slope_trees(inputs=inputs, right=right))

    return prod(trees)


inputs_real = read_file("data/day_03.txt")
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# Pārbauda pirmo uzdevumu ar piemēru.
assert slope_trees(inputs=inputs_test, right=3) == 7
# Pirmais uzdevums.
trees_1 = slope_trees(inputs=inputs_real, right=3)
print(f"Pirmajā gadījumā satiekam: {trees_1}")

# Pārbauda otro uzdevumu ar piemēru.
assert multiple_slopes(slopes=slopes, inputs=inputs_test) == 336

# Pirmais uzdevums.
trees_2 = multiple_slopes(slopes=slopes, inputs=inputs_real)
print(f"Otrajā gadījumā reizinājums ir: {trees_2}")