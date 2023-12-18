from pathlib import Path
import re

input = open(Path(__file__).parent / "input.txt").read()

direction_mapping = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}

max_line_size = 1
max_column_size = 1
current_line = 0
current_column = 0
trenches = []
perimeter = 0
shoelace = 0
for line in input.splitlines():
    next_line = current_line
    next_column = current_column
    _, _, color = line.split()
    hexa_numbers = color.replace("(", "").replace(")", "").replace("#", "").strip()
    count = int(hexa_numbers[:5].upper(), 16)
    direction = direction_mapping[hexa_numbers[5]]
    if direction == "D":
        next_line += int(count)
    if direction == "U":
        next_line -= int(count)
    if direction == "R":
        next_column += int(count)
    if direction == "L":
        next_column -= int(count)

    perimeter += int(count)
    trenches.append((next_line, next_column))

    # Shoelace Formula
    shoelace += current_line * next_column - next_line * current_column

    current_line = next_line
    current_column = next_column

pool_area = abs(shoelace) // 2
# Pick's theorem
points_inside = pool_area + 1 - perimeter // 2
print(points_inside + perimeter)
