from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    numbers_list = [1] * len(input_lines)
    for index, input_line in enumerate(input_lines):
        winning_numbers_string, current_numbers_string = input_line.split(":")[1].split("|")
        winning_numbers = [int(win) for win in winning_numbers_string.split()]
        my_winning_numbers = [int(cur) for cur in current_numbers_string.split() if int(cur) in winning_numbers]
        next_index = index + 1
        for winning_number in my_winning_numbers:
            if next_index >= len(input_lines):
                break
            numbers_list[next_index] += numbers_list[index]
            next_index += 1
    return sum(numbers_list)


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
