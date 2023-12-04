from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    numbers_list = []
    row_size = len(input_lines)
    column_size = len(input_lines[0].strip())
    for row_index, line in enumerate(input_lines):
        column_index = 0
        while column_index < column_size:
            if line[column_index].isdigit():
                int_start_column_index = column_index
                while column_index < column_size and line[column_index].isdigit():
                    column_index += 1

                piece_number_string = line[int_start_column_index:column_index]
                numbers_list.append(
                    validate_piece_number(
                        int(piece_number_string),
                        row_index,
                        int_start_column_index,
                        column_index - int_start_column_index,
                        row_size,
                        column_size,
                        input_lines,
                    )
                )
            column_index += 1
    return sum(numbers_list)


def validate_piece_number(
    piece_number: int,
    piece_row_index: int,
    piece_column_index: int,
    piece_length: int,
    row_size: int,
    column_size: int,
    input_lines: list[str],
):
    start_row = max(piece_row_index - 1, 0)
    end_row = min(piece_row_index + 1, row_size - 1)
    start_column = max(piece_column_index - 1, 0)
    end_column = min(piece_column_index + piece_length, column_size - 1)
    # print(f"will look for range [{start_row},{end_row}][{start_column},{end_column}]")
    for row in range(start_row, end_row + 1):
        for column in range(start_column, end_column + 1):
            current_char = input_lines[row][column]
            if not (current_char.isdigit() or current_char == "."):
                print(f"[{piece_row_index},{piece_column_index}]: {piece_number}, current char {current_char}")
                return piece_number
    return 0


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
