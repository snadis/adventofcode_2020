from typing import Set, List, Tuple, Dict

inputs_test_01 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


vectors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

Floor = Dict[Tuple[int, int], int]


def read_data(path: str) -> str:
    with open(file=path, mode="r") as f:
        return f.read().strip()


def parse_input(inputs: str) -> Floor:
    rows = [line for line in inputs.strip().split("\n")]
    max_cols = len(rows[0]) - 1
    max_rows = len(rows) - 1

    seats = {}
    for r, row in enumerate(rows):
        for c, col in enumerate(row):
            if col != ".":
                is_taken = 1 if col == "#" else 0
                seats[(c, r)] = is_taken

    return seats, max_cols, max_rows


def find_adjacent_seats(key: Tuple[int, int], rows: int, cols: int, seats: Floor):
    return [
        (c, r)
        for c in range(cols + 1)
        if max(c - 1, 0) <= key[0] <= min(c + 1, cols)
        for r in range(rows + 1)
        if max(r - 1, 0) <= key[1] <= min(r + 1, rows)
        if (c, r) != key and (c, r) in seats
    ]


def get_next_seats(current_seats: Floor, cols: int, rows: int) -> Floor:

    next_seats = dict()

    for seat in current_seats:
        seat_status = current_seats[seat]
        adjecant_seats = find_adjacent_seats(
            key=seat, cols=cols, rows=rows, seats=current_seats
        )
        adjecant_seats_taken = sum([current_seats[seat] for seat in adjecant_seats])

        if seat_status == 0 and adjecant_seats_taken == 0:
            next_seats[seat] = 1
        elif seat_status == 1 and adjecant_seats_taken >= 4:
            next_seats[seat] = 0
        else:
            next_seats[seat] = seat_status

    return next_seats


def stabilize_seating(inputs: str) -> Floor:
    current_seats, cols, rows = parse_input(inputs=inputs)
    next_seats = get_next_seats(current_seats=current_seats, cols=cols, rows=rows)
    print(sum(next_seats.values()))

    while current_seats != next_seats:
        current_seats = next_seats
        next_seats = get_next_seats(current_seats=current_seats, cols=cols, rows=rows)
        print(sum(next_seats.values()))

    return current_seats


assert sum(stabilize_seating(inputs=inputs_test_01).values()) == 37

inputs = read_data("data/day_11.txt")
seats_taken = sum(stabilize_seating(inputs=inputs).values())
print(f"Seats taken after stabilization is: {seats_taken}")
