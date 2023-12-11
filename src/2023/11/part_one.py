from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    expanded_universe = expand_universe(input_lines)
    galaxies = []
    for line_index, line in enumerate(expanded_universe):
        for column_index, column in enumerate(line):
            if column == "#":
                galaxies.append([line_index, column_index])
    distances = 0
    while len(galaxies) > 1:
        galaxy = galaxies.pop()
        for other_galaxy in galaxies:
            distances += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])
    return distances


def expand_universe(input_lines: list[str]) -> list[list[str]]:
    expanded_universe_lines = []
    for input_line in input_lines:
        stripped_line = input_line.strip()
        if (stripped_line.find("#")) == -1:
            expanded_universe_lines.append(list(stripped_line))
        expanded_universe_lines.append(list(stripped_line))
    transposed_expanded_universe_lines = [list(x) for x in zip(*expanded_universe_lines)]
    transposed_expanded_universe = []
    for transposed_expanded_universe_line in transposed_expanded_universe_lines:
        if not "#" in transposed_expanded_universe_line:
            transposed_expanded_universe.append(transposed_expanded_universe_line)
        transposed_expanded_universe.append(transposed_expanded_universe_line)
    return [list(x) for x in zip(*transposed_expanded_universe)]


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
