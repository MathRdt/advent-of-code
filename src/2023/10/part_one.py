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


def main(input_lines: list[str]):
    i = 0
    j = 0
    for input_line in input_lines:
        i += 1
        if (j := input_line.find("S")) > -1:
            break
    distance = 1
    first_pipe_location = find_first_pipe_location(input_lines, i, j)
    print(first_pipe_location)
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
    return (distance + 1) // 2


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


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
