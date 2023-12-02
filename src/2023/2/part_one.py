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
    game_id = int(game_attributes[0].strip()[5:])
    game_result = {
        "id": game_id,
        "max_blue": 0,
        "max_red": 0,
        "max_green": 0,
    }
    game_sets = game_attributes[1].split(";")
    for game_set in game_sets:
        cube_color_and_number = game_set.split(",")
        for cube in cube_color_and_number:
            stripped_cude = cube.strip()
            cube_amount = int(stripped_cude.split(" ")[0])
            if "blue" in stripped_cude:
                if cube_amount > 14:
                    return 0
                if cube_amount > game_result["max_blue"]:
                    game_result["max_blue"] = cube_amount
            if "red" in stripped_cude:
                if cube_amount > 12:
                    return 0
                if cube_amount > game_result["max_green"]:
                    game_result["max_green"] = cube_amount
            if "green" in stripped_cude:
                if cube_amount > 13:
                    return 0
                if cube_amount > game_result["max_red"]:
                    game_result["max_red"] = cube_amount
    return game_id


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
