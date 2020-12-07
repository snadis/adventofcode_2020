from dataclasses import dataclass


@dataclass
class Position:
    row: int
    column: int

    @property
    def seat_id(self):
        return self.row * 8 + self.column


Plane = list[Position]


def read_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        data = f.read()
    return [l.strip() for l in data.split()]


def calculate_binary_space_position(binary_string: str, group_size: int) -> int:
    values = list(range(group_size))
    for binary_possition in binary_string:
        middle_position = len(values) // 2
        if binary_possition.lower() in ["f", "l"]:
            values = values[:middle_position]
        elif binary_possition.lower() in ["b", "r"]:
            values = values[middle_position:]
        else:
            raise KeyError(f"{binary_possition} nav iespējama, lūdzu pārbaudīt datus")

    return values[0]


def get_position(binary_string: str) -> Position:
    binary_row = binary_string[:7]
    binary_column = binary_string[7:]

    row_nr = calculate_binary_space_position(binary_string=binary_row, group_size=128)
    column_nr = calculate_binary_space_position(
        binary_string=binary_column, group_size=8
    )

    return Position(row=row_nr, column=column_nr)


def get_plane(binary_positions: list[str]):
    return Plane([get_position(binary_string=bsring) for bsring in binary_positions])


def find_empty_seats(plane: Plane):
    seats_all = {(row, col) for row in range(128) for col in range(8)}
    seats_taken = {(p.row, p.column) for p in plane}

    seats_empty = seats_all - seats_taken

    return seats_empty


assert get_position(binary_string="FBFBBFFRLR").seat_id == 357
assert get_position(binary_string="BFFFBBFRRR").seat_id == 567
assert get_position(binary_string="FFFBBBFRRR").seat_id == 119
assert get_position(binary_string="BBFFBBFRLL").seat_id == 820

binary_positions = read_file("data/day_05.txt")
plane = get_plane(binary_positions=binary_positions)
answer1 = max([p.seat_id for p in plane])
print(f"Maksimālā seat_id: {answer1}")

empty_seats = find_empty_seats(plane=plane)
open_seats = [
    Position(row=row, column=col) for row, col in empty_seats if row > 20 and row < 100
]
answer2 = open_seats[0].seat_id
print(f"Tava vieta ir: {answer2}")