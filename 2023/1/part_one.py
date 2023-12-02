from pathlib import Path
import re


def main(file_path: Path):
    with file_path.open(mode="r") as input_file:
        input_content = input_file.readlines()
        numbers_list = []
        for line in input_content:
            numbers_line = [n for n in line if n.isdigit()]
            numbers_list.append(int(numbers_line[0] + numbers_line[-1]))

    return sum(numbers_list)


if __name__ == "__main__":
    print(main(Path("input.txt")))
