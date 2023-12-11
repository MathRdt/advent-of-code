from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    expanded_universe_coordinates, expanded_universe_values = expand_universe(input_lines)
    galaxies = []
    for line_index, line in enumerate(expanded_universe_coordinates):
        for column_index, column in enumerate(line):
            if column == "#":
                galaxies.append([line_index, column_index])
    distances = 0
    while len(galaxies) > 1:
        galaxy = galaxies.pop()
        for other_galaxy in galaxies:
            for line_index in range(min(galaxy[0] + 1, other_galaxy[0] + 1), max(galaxy[0] + 1, other_galaxy[0] + 1)):
                distances += expanded_universe_values[line_index][galaxy[1]]
            for column_index in range(min(galaxy[1] + 1, other_galaxy[1] + 1), max(galaxy[1] + 1, other_galaxy[1] + 1)):
                distances += expanded_universe_values[other_galaxy[0]][column_index]
    return distances


def expand_universe(input_lines: list[str]) -> list[list[int]]:
    height = len(input_lines)
    length = len(input_lines[0].strip())
    starting_coordinates = []
    starting_universe = [[1] * length] * height
    for line_index, input_line in enumerate(input_lines):
        stripped_line = list(input_line.strip())
        starting_coordinates.append(stripped_line)
        if not "#" in stripped_line:
            starting_universe[line_index] = [1000000] * length
    transposed_starting_coordinates = [list(x) for x in zip(*starting_coordinates)]
    transposed_starting_universe = [list(x) for x in zip(*starting_universe)]

    for column_index, input_column in enumerate(transposed_starting_coordinates):
        if not "#" in input_column:
            transposed_starting_universe[column_index] = [1000000] * height
    return starting_coordinates, [list(x) for x in zip(*transposed_starting_universe)]


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
