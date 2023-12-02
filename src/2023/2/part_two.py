from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    numbers_list = []
    for line in input_lines:
        numbers_list.append(parse_line(line))
    print(numbers_list)
    return sum(numbers_list)


def parse_line(input_line: str):
    game_attributes = input_line.split(":")
    game_result = {
        "min_blue": 0,
        "min_red": 0,
        "min_green": 0,
    }
    game_sets = game_attributes[1].split(";")
    for game_set in game_sets:
        cube_color_and_number = game_set.split(",")
        for cube in cube_color_and_number:
            stripped_cude = cube.strip()
            cube_amount = int(stripped_cude.split(" ")[0])
            if "blue" in stripped_cude:
                if cube_amount > game_result["min_blue"]:
                    game_result["min_blue"] = cube_amount
            if "red" in stripped_cude:
                if cube_amount > game_result["min_green"]:
                    game_result["min_green"] = cube_amount
            if "green" in stripped_cude:
                if cube_amount > game_result["min_red"]:
                    game_result["min_red"] = cube_amount
    return game_result["min_red"] * game_result["min_green"] * game_result["min_blue"]


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
