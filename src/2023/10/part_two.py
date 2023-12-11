import copy
from pathlib import Path
from commons import utils
from dataclasses import dataclass


@dataclass
class Pipe:
    """Class for keeping track of an item in inventory."""

    type: str
    direction: str
    position: list[int]
    distance_from_source: int

    def get_next_position(self):
        match self.type:
            case "|":
                if self.direction == "N":
                    return {"direction": "N", "position": [self.position[0] - 1, self.position[1]]}
                elif self.direction == "S":
                    return {"direction": "S", "position": [self.position[0] + 1, self.position[1]]}
                else:
                    raise Exception(f"not known next position from {self}")
            case "-":
                if self.direction == "E":
                    return {"direction": "E", "position": [self.position[0], self.position[1] + 1]}
                elif self.direction == "W":
                    return {"direction": "W", "position": [self.position[0], self.position[1] - 1]}
                else:
                    raise Exception(f"not known next position from {self}")
            case "L":
                if self.direction == "W":
                    return {"direction": "N", "position": [self.position[0] - 1, self.position[1]]}
                elif self.direction == "S":
                    return {"direction": "E", "position": [self.position[0], self.position[1] + 1]}
                else:
                    raise Exception(f"not known next position from {self}")
            case "J":
                if self.direction == "E":
                    return {"direction": "N", "position": [self.position[0] - 1, self.position[1]]}
                elif self.direction == "S":
                    return {"direction": "W", "position": [self.position[0], self.position[1] - 1]}
                else:
                    raise Exception(f"not known next position from {self}")
            case "7":
                if self.direction == "E":
                    return {"direction": "S", "position": [self.position[0] + 1, self.position[1]]}
                elif self.direction == "N":
                    return {"direction": "W", "position": [self.position[0], self.position[1] - 1]}
                else:
                    raise Exception(f"not known next position from {self}")
            case "F":
                if self.direction == "N":
                    return {"direction": "E", "position": [self.position[0], self.position[1] + 1]}
                elif self.direction == "W":
                    return {"direction": "S", "position": [self.position[0] + 1, self.position[1]]}
                else:
                    raise Exception(f"not known next position from {self}")
            case ".":
                raise Exception(f"not known next position from {self}")
            case "S":
                return {"start": True}


def get_pipes(input_lines: list[str]) -> list[list[int]]:
    distance = 0
    i = 0
    j = 0
    pipes = []
    for input_line in input_lines:
        i += 1
        if (j := input_line.find("S")) > -1:
            break
    pipes.append([i, j])
    first_pipe_location = find_first_pipe_location(input_lines, i, j)
    pipes.append(first_pipe_location)
    distance = 1
    current_pipe = Pipe(
        type=input_lines[first_pipe_location[0]][first_pipe_location[1]],
        position=first_pipe_location,
        distance_from_source=distance,
        direction=get_direction(i, j, first_pipe_location[0], first_pipe_location[1]),
    )
    loop_complete = False
    while loop_complete is False:
        next_pipe_infos = current_pipe.get_next_position()
        if next_pipe_infos.get("start"):
            loop_complete = True
            break
        distance += 1
        current_pipe = Pipe(
            type=input_lines[next_pipe_infos["position"][0]][next_pipe_infos["position"][1]],
            direction=next_pipe_infos["direction"],
            position=next_pipe_infos["position"],
            distance_from_source=distance,
        )
        pipes.append(next_pipe_infos["position"])

    return pipes


def find_first_pipe_location(input_lines: list[str], line: int, column: int) -> list[int]:
    if input_lines[line][column + 1] in ("-", "J", "7"):
        return [line, column + 1]
    if input_lines[line][column - 1] in ("-", "L", "F"):
        return [line, column - 1]
    if input_lines[line - 1][column] in ("|", "7", "F"):
        return [line - 1, column]
    if input_lines[line + 1][column] in ("|", "L", "J"):
        return [line + 1, column]


def get_direction(init_line, init_column, next_line, next_column):
    if next_line - init_line == -1:
        return "N"
    if next_line - init_line == 1:
        return "S"
    if next_column - init_column == -1:
        return "W"
    if next_column - init_column == 1:
        return "E"


# Shoelace formula
# https://en.wikipedia.org/wiki/Shoelace_formula
def get_pipes_area(pipes: list[list[int]]):
    pipes_area = 0
    for index in range(len(pipes)):
        if index < len(pipes) - 1:
            pipes_area += pipes[index][0] * pipes[index + 1][1] - pipes[index][1] * pipes[index + 1][0]
        elif index == len(pipes) - 1:
            pipes_area += pipes[index][0] * pipes[0][1] - pipes[index][1] * pipes[0][0]
        else:
            raise Exception("index out of range")
    return int(abs(pipes_area) / 2)


# Major tip found on reddit
# https://www.reddit.com/r/adventofcode/comments/18f1sgh/2023_day_10_part_2_advise_on_part_2/
def main(input_lines: list[str]):
    # The goal is to use the Pick's theorem to compute the number of points inside a simple polygon
    # https://en.wikipedia.org/wiki/Pick%27s_theorem

    # First we need to get the polygon coordinates
    pipes = get_pipes(input_lines)

    # Then calculate its area
    pipes_area = get_pipes_area(pipes)

    # Apply the Pick's theorem
    points_inside = pipes_area + 1 - int(len(pipes) / 2)
    return points_inside


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
