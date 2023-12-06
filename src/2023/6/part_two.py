from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    time = int(input_lines[0].split(":")[1].replace(" ", ""))
    distance = int(input_lines[1].split(":")[1].replace(" ", ""))

    first_winning_way = 0
    for way in range(time + 1):
        if way * (time - way) > distance:
            first_winning_way = way
            break

    winning_ways = time - 2 * first_winning_way + (time + 1) % 2
    return winning_ways


def ways_of_winning(race: list[int]):
    record = race[1]
    allowed_time = race[0]
    winning_ways = 0

    for way in range(allowed_time + 1):
        if way * (allowed_time - way) > record:
            winning_ways += 1
    return winning_ways


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
