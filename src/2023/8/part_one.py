from pathlib import Path
from commons import utils

import re


def main(input_lines: list[str]):
    steps = 0
    current_location = "AAA"
    instructions = input_lines.pop(0)
    input_lines.pop(0)
    locations_map = {}
    while len(input_lines) > 0:
        input_line = input_lines.pop(0).strip()
        start, left, right = re.findall("[a-zA-Z]+", input_line)
        next_locations = {"L": left, "R": right}
        locations_map[start] = next_locations
    while current_location != "ZZZ":
        for instruction in list(instructions.strip()):
            current_location = locations_map[current_location][instruction]
            steps += 1
            if current_location == "ZZZ":
                break
    return steps


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
