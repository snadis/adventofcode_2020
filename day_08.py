from dataclasses import dataclass

INSTRUCTION_SET = ("acc", "jmp", "nop")

inputs_test_01 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


@dataclass
class Instuction:
    code: str
    argument: int


def read_data(path: str) -> str:
    with open(file=path, mode="r") as f:
        return f.read()


def parse_line(line: str) -> Instuction:
    code = line[:3]
    argument = int(line[4:])

    return Instuction(code=code, argument=argument)


def make_program(input: str) -> list[Instuction]:
    return [parse_line(line=l) for l in input.strip().split("\n")]


def parse_instruction(i: Instuction) -> tuple[int, int]:
    if i.code not in INSTRUCTION_SET:
        raise KeyError(f"{i.code} nav korekta instruckija")

    if i.code == "acc":
        return (1, i.argument)

    elif i.code == "nop":
        return (1, 0)

    elif i.code == "jmp":
        return (i.argument, 0)


def run_program_till_loop(input: str) -> int:
    program = make_program(input=input)

    current_position = 0
    accumulator = 0
    seen = set()
    while True:
        if current_position in seen:
            break

        instruction = program[current_position]

        seen.add(current_position)

        offset, accumulator_add = parse_instruction(i=instruction)

        current_position += offset
        accumulator += accumulator_add

    return accumulator


def run_program_with_changes(input: str) -> int:

    program = make_program(input=input)

    codes = [i.code for i in program]
    for n, code in enumerate(codes):

        current_position = 0
        accumulator = 0
        seen = set()

        sub_program = program.copy()
        instruction = sub_program[n]

        if code == "nop":
            sub_program[n] = Instuction(code="jmp", argument=instruction.argument)
        elif code == "jmp":
            sub_program[n] = Instuction(code="nop", argument=instruction.argument)
        else:
            continue

        while True:
            if current_position in seen:
                break

            try:
                instruction = sub_program[current_position]
            except IndexError:
                return accumulator

            seen.add(current_position)

            offset, accumulator_add = parse_instruction(i=instruction)

            current_position += offset
            accumulator += accumulator_add


assert run_program_till_loop(input=inputs_test_01) == 5

input = read_data("data/day_08.txt")

answer_01 = run_program_till_loop(input=input)
print(f"Loop starts with accumulator having value: {answer_01}.")

assert run_program_with_changes(input=inputs_test_01) == 8

answer_02 = run_program_with_changes(input=input)
print(f"Program terminates with accumulator having value: {answer_02}.")
