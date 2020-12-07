from collections import Counter

inputs_test = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def read_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        data = f.read()

    return data


assert sum([len(set(g.replace("\n", ""))) for g in inputs_test.split("\n\n")]) == 11
inputs_real = read_file("data/day_06.txt")
answer1 = sum([len(set(g.replace("\n", ""))) for g in inputs_real.split("\n\n")])
print(f"Atbilžu summa: {answer1}")

assert (
    sum(
        [
            (list(Counter(g.replace("\n", "")).values()).count(len(g.split())))
            for g in inputs_test.split("\n\n")
        ]
    )
    == 6
)

answer2 = sum(
    [
        (list(Counter(g.replace("\n", "")).values()).count(len(g.split())))
        for g in inputs_real.split("\n\n")
    ]
)
print(f"Visu atbilžu summa: {answer2}")