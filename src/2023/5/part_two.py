from pathlib import Path
from commons import utils
import re
from functools import reduce


def main(input_lines: list[str]):
    seed_inputs = [int(seed) for seed in input_lines.pop(0).split(":")[1].split()]
    seed_ranges_zip = zip(seed_inputs[::2], seed_inputs[1::2])
    seed_ranges = [[seed_start, seed_start + seed_range] for seed_start, seed_range in seed_ranges_zip]

    input_lines.pop(0)
    next_element = ""
    current_next_mapping_list = []
    local_minimum_list = []
    while next_element != "location":
        next_element, current_next_mapping = get_next_mapping(input_lines)
        current_next_mapping_list.append(current_next_mapping)
    for seed_range in seed_ranges:
        local_minimum_list.append(
            min([x[0] for x in get_seed_range_minimum_location(seed_range, current_next_mapping_list)])
        )
    return min(local_minimum_list)


def get_seed_range_minimum_location(seed_range: list[int], current_next_mapping_list: list[list[list[int]]]):
    current_ranges = [seed_range]
    for current_next_mapping in current_next_mapping_list:
        current_ranges = get_next_ranges(current_ranges, current_next_mapping)
    return current_ranges


def get_next_ranges(current_ranges: list[list[int]], current_next_mapping: list[list[int]]):
    next_ranges = []
    unchanged_ranges = current_ranges
    for current_next_mapping_line in current_next_mapping:
        fresh_unchanged_ranges = []
        next_mapping_start, current_mapping_start, mapping_range = current_next_mapping_line
        current_mapping_end = current_mapping_start + mapping_range
        for unchanged_range in unchanged_ranges:
            range_start, range_end = unchanged_range
            if range_start < current_mapping_start:
                before_range = [range_start, min(range_end, current_mapping_start)]
                fresh_unchanged_ranges.append(before_range)
            if (
                current_mapping_start <= range_start < current_mapping_end
                or current_mapping_start < range_end <= current_mapping_end
            ):
                interval_range = [
                    next_mapping_start - current_mapping_start + max(range_start, current_mapping_start),
                    next_mapping_start - current_mapping_start + min(range_end, current_mapping_end),
                ]
                next_ranges.append(interval_range)
            if range_end > current_mapping_end:
                after_range = [max(range_start, current_mapping_end), range_end]
                fresh_unchanged_ranges.append(after_range)
        unchanged_ranges = fresh_unchanged_ranges
    return next_ranges + unchanged_ranges


def get_next_mapping(input_lines: list[str]):
    current_next_list = []
    input_line = input_lines.pop(0)
    elements = re.search(r"([a-zA-Z0]*)-to-([a-zA-Z0]*) map:$", input_line)
    if elements is None:
        return
    _, next_element = elements.groups()
    while len(input_lines) > 0:
        input_line = input_lines.pop(0)
        if input_line == "\n":
            break
        current_next_list.append([int(obj) for obj in input_line.split()])
    return next_element, current_next_list


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
