from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    numbers_list = []
    for line in input_lines:
        numbers_line = [n for n in line if n.isdigit()]
        numbers_list.append(int(numbers_line[0] + numbers_line[-1]))

    return sum(numbers_list)


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
