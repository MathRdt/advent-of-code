from pathlib import Path
import re
from commons import utils


def main(input_lines: list[str]):
    input_matrix = [list(input_line.strip()) for input_line in input_lines]
    inverted_tilted_matrix = tilt_matrix(input_matrix)
    return calculate_weight(inverted_tilted_matrix)


def tilt_matrix(input_matrix: list[list[str]]) -> list[list[str]]:
    inversed_transposed_matrix = [list(line)[::-1] for line in zip(*input_matrix)]

    for line in inversed_transposed_matrix:
        mobile_rocks = [i for i, x in enumerate(line) if x == "O"][::-1]
        for mobile_rock in mobile_rocks:
            new_index = mobile_rock
            while new_index + 1 < len(line):
                if line[new_index + 1] != ".":
                    break
                new_index += 1
            if new_index != mobile_rock:
                line[new_index] = "O"
                line[mobile_rock] = "."
    return [list(line) for line in zip(*inversed_transposed_matrix)]


def calculate_weight(input_matrix: list[list[str]]) -> int:
    sum = 0
    weight = 1
    for line in input_matrix:
        sum += len([i for i, x in enumerate(line) if x == "O"]) * weight
        weight += 1
    return sum


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
