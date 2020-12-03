import re


def read_file(path):
    with open(file=path, mode="r", encoding="utf-8") as f:
        data = f.readlines()
    return data


def check_policy(string: str):
    pattern = r"^(\d+)-(\d+)\s+(.):\s(.+)$"

    lower_limit, upper_limit, character, password = re.match(pattern, string).groups()

    character_count = password.count(character)

    if character_count >= int(lower_limit) and character_count <= int(upper_limit):
        return True
    else:
        return False


def check_policy_position(string: str):
    pattern = r"^(\d+)-(\d+)\s+(.):\s(.+)$"

    position_a, position_b, character, password = re.match(pattern, string).groups()

    if (password[int(position_a) - 1] == character) + (
        password[int(position_b) - 1] == character
    ) == 1:
        return True
    else:
        return False


inputs = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
assert sum([check_policy(i) for i in inputs]) == 2

data = read_file("data/day_02.txt")
good_passwords = sum([check_policy(i) for i in data])
print(good_passwords)

assert sum([check_policy_position(i) for i in inputs]) == 1
good_passwords = sum([check_policy_position(i) for i in data])
print(good_passwords)