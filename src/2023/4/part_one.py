from pathlib import Path
from commons import utils
import math


def main(input_lines: list[str]):
    numbers_list = []
    for input_line in input_lines:
        winning_numbers_string, current_numbers_string = input_line.split(":")[1].split("|")
        winning_numbers = [int(win) for win in winning_numbers_string.split()]
        my_winning_numbers = [int(cur) for cur in current_numbers_string.split() if int(cur) in winning_numbers]
        if len(my_winning_numbers) > 0:
            numbers_list.append(int(math.pow(2, len(my_winning_numbers) - 1)))
    return sum(numbers_list)


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
