from pathlib import Path
import re


def main(file_path: Path):
    with file_path.open(mode="r") as input_file:
        input_content = input_file.readlines()
        numbers_list = []
        for line in input_content:
            numbers_list.append(parse_numbers(line))

    return sum(numbers_list)


def parse_numbers(line: str):
    numbers_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    numbers = []
    for index, char in enumerate(line):
        if char.isdigit():
            numbers.append(char)
        else:
            for number_key in numbers_map:
                if line[index:].startswith(number_key):
                    numbers.append(numbers_map[number_key])
    if len(numbers) == 0:
        return 0
    return int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    print(main(Path("input.txt")))
