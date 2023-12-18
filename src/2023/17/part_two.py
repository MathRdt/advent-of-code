from pathlib import Path
from heapq import heappush, heappop


# HeapQueue solution found thanks to HyperNeutrino
# https://www.youtube.com/watch?v=2pDSooPLLkI

input = open(Path(__file__).parent / "input.txt").read()
matrix = [[int(column) for column in input_line] for input_line in input.splitlines()]
hq = [
    (
        0 - matrix[0][0],
        0,
        0,
        "S",
        0,
    ),
    (
        0 - matrix[0][0],
        0,
        0,
        "E",
        0,
    ),
]
ancestors = set()
possible_moves = {"N": ["N", "E", "W"], "S": ["S", "E", "W"], "E": ["E", "S", "N"], "W": ["W", "S", "N"]}


def find_best_path(
    current_heat_loss,
    current_line,
    current_column,
    current_direction,
    current_direction_repeat,
):
    done = False
    impossible_moves = []
    current_heat_loss += matrix[current_line][current_column]

    # Thanks to Heap, we are sure that the first time we arrive to the end is the minimum
    # because we will order our heap by minimum heat loss
    if current_line == len(matrix) - 1 and current_column == len(matrix[0]) - 1:
        if 4 <= current_direction_repeat <= 10:
            print(current_heat_loss)
            return True
        return False

    key = (current_line, current_column, current_direction, current_direction_repeat)
    if key in ancestors:
        return False
    ancestors.add(key)

    if current_line == 0:
        impossible_moves.append("N")
    if current_line == len(matrix) - 1:
        impossible_moves.append("S")
    if current_column == 0:
        impossible_moves.append("W")
    if current_column == len(matrix[0]) - 1:
        impossible_moves.append("E")

    if current_direction_repeat < 4:
        impossible_moves += [x for x in possible_moves[current_direction] if x != current_direction]
    elif current_direction_repeat == 10:
        impossible_moves.append(current_direction)

    current_possible_moves = [x for x in possible_moves[current_direction] if x not in impossible_moves]

    for current_move in current_possible_moves:
        next_direction_repeat = 1
        if current_move == current_direction:
            next_direction_repeat = current_direction_repeat + 1
        if current_move == "N":
            heappush(hq, (current_heat_loss, current_line - 1, current_column, current_move, next_direction_repeat))
        if current_move == "S":
            heappush(hq, (current_heat_loss, current_line + 1, current_column, current_move, next_direction_repeat))
        if current_move == "W":
            heappush(hq, (current_heat_loss, current_line, current_column - 1, current_move, next_direction_repeat))
        if current_move == "E":
            heappush(hq, (current_heat_loss, current_line, current_column + 1, current_move, next_direction_repeat))
    return done


done = False

while done is False:
    current_heat_loss, current_line, current_column, current_direction, current_direction_repeat = heappop(hq)
    done = find_best_path(current_heat_loss, current_line, current_column, current_direction, current_direction_repeat)
# print(position_cache[(len(matrix) - 1, len(matrix[0]) - 1)])
