import re
from dataclasses import dataclass


@dataclass
class Password:
    number_a: int
    number_b: int
    character: str
    password: str


def read_file(path):
    with open(file=path, mode="r", encoding="utf-8") as f:
        data = f.readlines()
    return data


def decompose_string(string: str) -> Password:
    """
    No teksta izgriež visus nepieciešamos laukus un agtriež tos kā Password klasi.
    Piemērs:
      '1-3 a: abcde' -> Password(number_a=1, number_b=3, character='a', password='abcde')
    """
    pattern = r"^(\d+)-(\d+)\s+(.):\s(.+)$"
    number_a, number_b, character, password = re.match(pattern, string).groups()

    return Password(
        number_a=int(number_a),
        number_b=int(number_b),
        character=character,
        password=password,
    )


def check_policy_count(string: str) -> bool:
    p = decompose_string(string=string)
    character_count = p.password.count(p.character)
    if character_count >= p.number_a and character_count <= p.number_b:
        return True
    else:
        return False


def check_policy_position(string: str):
    p = decompose_string(string=string)

    if (p.password[p.number_a - 1] == p.character) + (
        p.password[p.number_b - 1] == p.character
    ) == 1:
        return True
    else:
        return False


inputs_test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
assert sum([check_policy_count(i) for i in inputs_test]) == 2

inputs_real = read_file("data/day_02.txt")
good_passwords = sum([check_policy_count(i) for i in inputs_real])
print(f"Atbilde pirmajam jautājumam: {good_passwords}")

assert sum([check_policy_position(i) for i in inputs_test]) == 1
good_passwords = sum([check_policy_position(i) for i in inputs_real])
print(f"Atbilde otrajam jautājumam: {good_passwords}")
