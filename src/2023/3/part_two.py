from pathlib import Path
from commons import utils
import re


def main(input_lines: list[str]):
    numbers_list = []
    row_size = len(input_lines)
    column_size = len(input_lines[0].strip())
    for row_index, line in enumerate(input_lines):
        column_index = 0
        while column_index < column_size:
            if line[column_index] == "*":
                numbers_list.append(get_gear_power(row_index, column_index, row_size, column_size, input_lines))
            column_index += 1
    return sum(numbers_list)


def get_gear_power(
    gear_row_index: int,
    gear_column_index: int,
    row_size: int,
    column_size: int,
    input_lines: list[str],
):
    start_row = max(gear_row_index - 1, 0)
    end_row = min(gear_row_index + 1, row_size - 1)
    start_column = max(gear_column_index - 1, 0)
    end_column = min(gear_column_index + 1, column_size - 1)

    row = start_row
    pieces = []
    while row <= end_row:
        column = start_column
        while column <= end_column:
            if input_lines[row][column].isdigit():
                while column < column_size and input_lines[row][column].isdigit():
                    column += 1
                m = re.search(r"\d+$", input_lines[row][:column])
                pieces.append(int(m.group()))
            column += 1
        row += 1
    if len(pieces) == 2:
        return pieces[0] * pieces[1]
    return 0


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
