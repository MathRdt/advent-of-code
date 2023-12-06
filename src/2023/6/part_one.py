from pathlib import Path
from commons import utils
from functools import reduce


def main(input_lines: list[str]):
    numbers_list = []
    times = [int(time) for time in input_lines[0].split(":")[1].split()]
    distances = [int(dist) for dist in input_lines[1].split(":")[1].split()]
    races = zip(times, distances)

    for race in races:
        numbers_list.append(ways_of_winning(race))
    return reduce((lambda x, y: x * y), numbers_list)


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
