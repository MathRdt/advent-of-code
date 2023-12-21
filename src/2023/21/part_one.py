from pathlib import Path

input = open(Path(__file__).parent / "input.txt").read()
matrix = [[col for col in line] for line in input.splitlines()]

starting_pos = (-1, -1)
position_next_steps = {}
already_stepped_on = set()
is_possible_end = set()


def possible_next_steps(line, col):
    next_steps = []
    if line > 0:
        if matrix[line - 1][col] in ".S":
            next_steps.append((line - 1, col))
    if col > 0:
        if matrix[line][col - 1] in ".S":
            next_steps.append((line, col - 1))
    if line < len(matrix) - 1:
        if matrix[line + 1][col] in ".S":
            next_steps.append((line + 1, col))
    if col < len(matrix[0]) - 1:
        if matrix[line][col + 1] in ".S":
            next_steps.append((line, col + 1))
    return next_steps


for line in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[line][col] in ".S":
            if matrix[line][col] == "S":
                starting_pos = (line, col)
            position_next_steps[(line, col)] = possible_next_steps(line, col)

remaining_steps = 64
current_positions = [starting_pos]
already_stepped_on.add(starting_pos)
is_possible_end.add(starting_pos)
while remaining_steps > 0:
    new_positions = []
    for positition in current_positions:
        next_positions = [pos for pos in position_next_steps[positition] if pos not in already_stepped_on]
        already_stepped_on.update(next_positions)
        new_positions += next_positions
        if remaining_steps % 2 == 1:
            is_possible_end.update(next_positions)

    current_positions = new_positions
    remaining_steps -= 1
print(len(is_possible_end))
