from pathlib import Path
from commons import utils

# Cycles solution found thanks to Hyperneutrino solution
# https://www.youtube.com/watch?v=WCVOBKUNc38

seen_grids = set()
seen_grids_ancestors = []


def main(input_lines: list[str]):
    input_matrix = tuple([tuple(input_line.strip()) for input_line in input_lines])
    current_cycle = 0
    seen_grids.add(input_matrix)
    seen_grids_ancestors.append(input_matrix)
    while True:
        for _ in range(4):
            input_matrix = rotate_and_tilt_counter_clockwise(input_matrix)
        current_cycle += 1
        if input_matrix in seen_grids:
            break
        seen_grids.add(input_matrix)
        seen_grids_ancestors.append(input_matrix)
    first_seen_cycle = seen_grids_ancestors.index(input_matrix)
    return calculate_weight(
        seen_grids_ancestors[first_seen_cycle + ((1000000000 - first_seen_cycle) % (current_cycle - first_seen_cycle))]
    )


def rotate_and_tilt_counter_clockwise(input_matrix: list[list[str]]) -> tuple[tuple[str]]:
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
    return tuple(tuple(line) for line in inversed_transposed_matrix)


def calculate_weight(input_matrix: list[list[str]]) -> int:
    sum = 0
    weight = len(input_matrix)
    for line in input_matrix:
        sum += len([x for x in line if x == "O"]) * weight
        weight -= 1
    return sum


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
