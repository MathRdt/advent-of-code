from pathlib import Path
from commons import utils
import re


def main(input_lines: list[str]):
    numbers_list = []
    seed_inputs = input_lines.pop(0).split(":")[1].split()
    seed_ranges = zip(seed_inputs[::2], seed_inputs[1::2])
    seeds_environments = []
    for seed_range in seed_ranges:
        local_seed_envs = [
            {"seed": int(seed)} for seed in range(int(seed_range[0]), int(seed_range[0]) + int(seed_range[1]))
        ]
        seeds_environments += local_seed_envs
    print(seeds_environments)
    # current_element = None
    # next_element = None
    # for input_line in input_lines:
    #     if input_line == "\n":
    #         continue
    #     elements = re.search(r"([a-zA-Z0]*)-to-([a-zA-Z0]*) map:$", input_line)
    #     if elements is not None:
    #         current_element, next_element = elements.groups()
    #         for seed_env in seeds_environments:
    #             seed_env[next_element] = seed_env[current_element]
    #         continue

    #     target_start, source_start, range = input_line.split()
    #     for seed_env in seeds_environments:
    #         if seed_env[current_element] >= int(source_start) and seed_env[current_element] < (
    #             int(source_start) + int(range)
    #         ):
    #             seed_env[next_element] = int(target_start) + seed_env[current_element] - int(source_start)
    # seeds_environments = sorted(seeds_environments, key=lambda x: x["location"])
    # return seeds_environments[0]["location"]


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
