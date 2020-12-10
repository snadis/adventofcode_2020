from collections import defaultdict
from dataclasses import dataclass
import re

inputs_test_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

inputs_test_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


@dataclass
class Bag:
    color: str
    children: dict[str, int]


def read_data(path: str) -> str:
    with open(file=path, mode="r") as f:
        return f.read()


def parse_line(line: str) -> Bag:

    bag, subbags = line.split(" bags contain ")

    contains = {}
    for b in subbags.split(","):
        if b.strip() == "no other bags.":
            continue
        regex = r"(\d+)\s(.*)\sbag"
        count, color = re.match(regex, b.strip()).groups()
        contains[color] = count

    return Bag(color=bag, children=contains)


def make_bags(input: str) -> list[Bag]:
    return [parse_line(line) for line in input.split("\n")]


def make_parent_dict(bags: list[Bag]):
    contains = defaultdict(list)
    for bag in bags:
        for subbag in bag.children:
            contains[subbag].append(bag.color)
    return dict(contains)


def outermost_bag_colors(bags: list[Bag], color: str) -> list[str]:

    parents = make_parent_dict(bags)

    valid_colors = set()

    stack = [color]
    while stack:
        check = stack.pop()
        for child in parents.get(check, []):
            valid_colors.add(child)
            stack.append(child)

    return list(valid_colors)


def number_of_bags_inside_bag(bags: list[Bag], color: str) -> int:

    ludge = {bag.color: bag.children for bag in bags}

    number_of_bags = 0

    stack = [(color, 1)]
    while stack:
        color, count = stack.pop()

        for child_color, child_count in ludge[color].items():

            child_count = int(child_count) * count
            number_of_bags = number_of_bags + child_count

            stack.append((child_color, child_count))

    return number_of_bags


bags_test_1 = make_bags(input=inputs_test_1)
assert len(outermost_bag_colors(bags=bags_test_1, color="shiny gold")) == 4
assert number_of_bags_inside_bag(bags=bags_test_1, color="shiny gold") == 32

bags_test_2 = make_bags(inputs_test_2)
assert number_of_bags_inside_bag(bags=bags_test_2, color="shiny gold") == 126

bags = make_bags(read_data("data/day_07.txt"))
a1 = len(outermost_bag_colors(bags=bags, color="shiny gold"))
print("Soma var būt {count} krāsu somās.".format(count=a1))

a2 = number_of_bags_inside_bag(bags=bags, color="shiny gold")
print(f"Somā jāatrodas vismaz {a2} citām somām")