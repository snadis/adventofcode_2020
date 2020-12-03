import re
from dataclasses import dataclass
from operator import xor


@dataclass
class Password:
    number_a: int
    number_b: int
    character: str
    password: str


def read_file(path) -> list[str]:
    """Atver failu un nolasa visas rindas."""
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
    # Saskaita prasītā simola skaitu parolē.
    character_count = p.password.count(p.character)
    # Pārbauda vai skaits iekļaujas norādītajās robežās, ja ir tad True, ja nē tad False.
    if character_count >= p.number_a and character_count <= p.number_b:
        return True
    else:
        return False


def check_policy_position(string: str) -> bool:
    p = decompose_string(string=string)

    # Pārbauda vai prasītais simbolas atroadas vienā vai otrā pozīcijā un neatrodas abās.
    # Ja izpildas tikai 1 no nosacījumiem tad atgriež True, ja nē tad False.
    if xor(
        p.password[p.number_a - 1] == p.character,
        p.password[p.number_b - 1] == p.character,
    ):
        return True
    else:
        return False


# Testa dati no piemēra.
inputs_test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

# Pārbauda testa datus.
assert sum([check_policy_count(i) for i in inputs_test]) == 2

# Pārbauda un izdrukā pirmā uzdevuma datus.
inputs_real = read_file("data/day_02.txt")
good_passwords = sum([check_policy_count(i) for i in inputs_real])
print(f"Atbilde pirmajam jautājumam: {good_passwords}")

# Pārbauda testa datus.
assert sum([check_policy_position(i) for i in inputs_test]) == 1

# Pārbauda un izdrukā otrā uzdevuma datus.
good_passwords = sum([check_policy_position(i) for i in inputs_real])
print(f"Atbilde otrajam jautājumam: {good_passwords}")
