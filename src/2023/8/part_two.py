from pathlib import Path
from commons import utils
import math
import re


def main(input_lines: list[str]):
    instructions = input_lines.pop(0).strip()
    input_lines.pop(0)
    start_locations = []
    locations_map = {}
    while len(input_lines) > 0:
        input_line = input_lines.pop(0).strip()
        start, left, right = re.findall("[a-zA-Z]+", input_line)
        next_locations = {"L": left, "R": right}
        locations_map[start] = next_locations
        if start[2] == "A":
            start_locations.append(start)
    success = 0
    local_success_steps = []
    for start_location in start_locations:
        success = False
        steps = 0
        while success is False:
            for instruction in list(instructions):
                start_location = locations_map[start_location][instruction]
                steps += 1
                if start_location[2] == "Z":
                    success = True
                    local_success_steps.append(steps)
                    break
    return math.lcm(*local_success_steps)


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
