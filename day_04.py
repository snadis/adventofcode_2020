import re

inputs_test = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split(
    "\n\n"
)

validators = {
    "byr": {"low": 1920, "hi": 2002},
    "iyr": {"low": 2010, "hi": 2020},
    "eyr": {"low": 2020, "hi": 2030},
    "hgt": {
        "cm": {"low": 150, "hi": 193},
        "in": {"low": 59, "hi": 76},
        "pattern": r"^(\d+)(\w+)",
    },
    "hcl": r"^#[0-9a-f]{6}$",
    "ecl": "amb blu brn gry grn hzl oth".split(),
    "pid": r"^\d{9}$",
}


def read_file(path: str) -> list[str]:
    with open(file=path, mode="r", encoding="utf-8") as f:
        data = f.read()
    return data.split("\n\n")


def parse_passport(passport_data: str) -> dict:
    passport = passport_data.split()
    items = [val.split(":") for val in passport]

    return {k: v for k, v in items}


def check_passport_keys(passport_data: str, keys: list[str]) -> bool:
    passport = parse_passport(passport_data=passport_data)
    try:
        _ = [passport[key] for key in keys]
        return True
    except KeyError:
        return False


def check_key_constrains(passport: str, keys: list[str]) -> bool:
    all_keys = check_passport_keys(passport_data=passport, keys=keys)
    passport = parse_passport(passport)
    key_validation = []
    if all_keys:
        valid_keys = [check_key(passport=passport, key=key) for key in keys]
        return all(valid_keys)
    return False


def check_key(passport, key):
    p = passport
    if key in ("byr", "iyr", "eyr"):
        try:
            return validators[key]["low"] <= int(p[key]) <= validators[key]["hi"]
        except (ValueError, KeyError):
            return False

    elif key == "hgt":
        try:
            pattern = validators[key]["pattern"]
            value, units = re.match(pattern, p[key]).groups()
            return (
                validators[key][units]["low"]
                <= int(value)
                <= validators[key][units]["hi"]
            )
        except (ValueError, KeyError):
            return False

    elif key == "hcl":
        pattern = validators[key]
        if re.search(pattern, p[key]):
            return True
        else:
            return False

    elif key == "ecl":
        return p[key] in validators[key]

    elif key == "pid":
        pattern = validators[key]
        if re.search(pattern, p[key]):
            return True
        else:
            return False


def answer1(inputs: list[str], keys: list[str]) -> int:
    return sum(
        [
            check_passport_keys(passport_data=passport, keys=passport_keys_mandatory)
            for passport in inputs
        ]
    )


def answer2(inputs: list[str], keys: list[str]) -> int:
    return sum(
        [
            check_key_constrains(passport=passport, keys=passport_keys_mandatory)
            for passport in inputs
        ]
    )


# Visas atslēgas kas var būt pasē
passport_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

# Obligātās atslēgas pasē
passport_keys_mandatory = passport_keys.copy()
passport_keys_mandatory.remove("cid")

inputs_real = read_file("data/day_04.txt")

# Pārbauda pirmo uzdevumu ar testa datiem
assert answer1(inputs=inputs_test, keys=passport_keys_mandatory) == 2
# Īstie dati
a1 = answer1(inputs=inputs_real, keys=passport_keys_mandatory)
print(f"Drīgas passes pēc atslēgām: {a1}")

a2 = answer2(inputs=inputs_real, keys=passport_keys_mandatory)
print(f"Drīgas passes pēc atslēgām un to vērtībām: {a2}")
