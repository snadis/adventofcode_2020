from os import name, read
from pathlib import Path


def read_file(filepath: Path) -> list[int]:
    with open(file=filepath, mode="r", encoding="utf-8") as f:
        data = f.readlines()

    return [int(i) for i in data]


def brute_force_sum(data: list[int]):
    result = [i * j for i in data for j in data if j + i == 2020 and i != j][0]

    return result


def brute_force_sum3(data: list[int]):
    result = [
        i * j * x
        for i in data
        for j in data
        for x in data
        if j + i + x == 2020 and i != j
    ][0]

    return result


def main():
    assert brute_force_sum([1721, 979, 366, 299, 675, 1456]) == 514579

    data = read_file(filepath="data/day_01.txt")
    answer1 = brute_force_sum(data=data)

    print(f"Answer 1: {answer1}")

    assert brute_force_sum3([1721, 979, 366, 299, 675, 1456]) == 241861950
    answer2 = brute_force_sum3(data=data)
    print(f"Answer 2: {answer2}")


if __name__ == "__main__":
    main()
