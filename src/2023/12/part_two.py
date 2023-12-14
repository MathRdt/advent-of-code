from pathlib import Path
from commons import utils

cache = {}

# Reimplementation of HyperNeutrino solution
# https://www.youtube.com/watch?v=WCVOBKUNc38


def main(input_lines: list[str]):
    total_count = 0
    for input_line in input_lines:
        springs_map, broken_springs_string = input_line.strip().split(" ")
        expanded_springs_map = "?".join([springs_map] * 5)
        expanded_broken_springs = tuple([int(broken_spring) for broken_spring in broken_springs_string.split(",")]) * 5
        local_count = get_possible_combinations(expanded_springs_map, expanded_broken_springs)
        total_count += local_count
    return total_count


def get_possible_combinations(springs_map, broken_springs):
    if len(broken_springs) == 0:
        if "#" in springs_map:
            return 0
        return 1

    if springs_map == "":
        if len(broken_springs) > 0:
            return 0
        return 1

    if broken_springs[0] > len(springs_map):
        return 0

    key = (springs_map, broken_springs)
    if key in cache:
        return cache[key]
    local_count = 0
    if springs_map[0] in ".?":
        local_count += get_possible_combinations(springs_map[1:], broken_springs)
    if springs_map[0] in "#?":
        if "." in springs_map[: broken_springs[0]]:
            local_count += 0

        # check that springs map continue after this broken spring serie
        # if the next spring is broken as well, it means the serie is greater than expected
        elif broken_springs[0] < len(springs_map) and springs_map[broken_springs[0]] == "#":
            local_count += 0
        else:
            # If slice is greater than springs_map range, it will return empty string, that will be treated in the next occurence
            local_count += get_possible_combinations(springs_map[broken_springs[0] + 1 :], broken_springs[1:])
    cache[key] = local_count
    return local_count


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
