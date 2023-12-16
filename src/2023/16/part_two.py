from pathlib import Path

input = open(Path(__file__).parent / "input.txt").read()
matrix = [[column for column in input_line] for input_line in input.splitlines()]


def next_beams(position, direction):
    next_beams = []
    if (position, direction) in total_cache_set:
        return []
    total_cache_set.add((position, direction))
    position_cache.add((position[0], position[1]))
    match direction:
        case "N":
            if matrix[position[0]][position[1]] in ".|":
                if position[0] > 0:
                    return [{"position": (position[0] - 1, position[1]), "direction": "N"}]
            elif matrix[position[0]][position[1]] == "/":
                if position[1] + 1 < len(matrix[0]):
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0], position[1] + 1), "direction": "E"}]
            elif matrix[position[0]][position[1]] == "\\":
                if position[1] > 0:
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0], position[1] - 1), "direction": "W"}]
            elif matrix[position[0]][position[1]] == "-":
                if position[1] > 0:
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0], position[1] - 1), "direction": "W"})
                if position[1] + 1 < len(matrix[0]):
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0], position[1] + 1), "direction": "E"})
            else:
                raise Exception(
                    f"should not be possible for {position[0]},{position[1]} to have this sign {matrix[position[0]][position[1]]}"
                )
        case "E":
            if matrix[position[0]][position[1]] in ".-":
                if position[1] + 1 < len(matrix[0]):
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0], position[1] + 1), "direction": "E"}]
            elif matrix[position[0]][position[1]] == "/":
                if position[0] > 0:
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0] - 1, position[1]), "direction": "N"}]
            elif matrix[position[0]][position[1]] == "\\":
                if position[0] + 1 < len(matrix):
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0] + 1, position[1]), "direction": "S"}]
            elif matrix[position[0]][position[1]] == "|":
                if position[0] > 0:
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0] - 1, position[1]), "direction": "N"})
                if position[0] + 1 < len(matrix):
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0] + 1, position[1]), "direction": "S"})
            else:
                raise Exception(
                    f"should not be possible for {position[0]},{position[1]} to have this sign {matrix[position[0]][position[1]]}"
                )
        case "S":
            if matrix[position[0]][position[1]] in ".|":
                if position[0] + 1 < len(matrix):
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0] + 1, position[1]), "direction": "S"}]
            elif matrix[position[0]][position[1]] == "/":
                if position[1] > 0:
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0], position[1] - 1), "direction": "W"}]
            elif matrix[position[0]][position[1]] == "\\":
                if position[1] + 1 < len(matrix[0]):
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0], position[1] + 1), "direction": "E"}]
            elif matrix[position[0]][position[1]] == "-":
                if position[1] > 0:
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0], position[1] - 1), "direction": "W"})
                if position[1] + 1 < len(matrix[0]):
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0], position[1] + 1), "direction": "E"})
            else:
                raise Exception(
                    f"should not be possible for {position[0]},{position[1]} to have this sign {matrix[position[0]][position[1]]}"
                )
        case "W":
            if matrix[position[0]][position[1]] in ".-":
                if position[1] > 0:
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0], position[1] - 1), "direction": "W"}]
            elif matrix[position[0]][position[1]] == "/":
                if position[0] + 1 < len(matrix):
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0] + 1, position[1]), "direction": "S"}]
            elif matrix[position[0]][position[1]] == "\\":
                if position[0] > 0:
                    position_cache.add((position[0], position[1]))
                    return [{"position": (position[0] - 1, position[1]), "direction": "N"}]
            elif matrix[position[0]][position[1]] == "|":
                if position[0] > 0:
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0] - 1, position[1]), "direction": "N"})
                if position[0] + 1 < len(matrix):
                    position_cache.add((position[0], position[1]))
                    next_beams.append({"position": (position[0] + 1, position[1]), "direction": "S"})
            else:
                raise Exception(
                    f"should not be possible for {position[0]},{position[1]} to have this sign {matrix[position[0]][position[1]]}"
                )
    return next_beams


starts_positions = []
starts_positions += [[0, i, "S"] for i in range(len(matrix[0]))]
starts_positions += [[len(matrix) - 1, i, "N"] for i in range(len(matrix[0]))]
starts_positions += [[i, 0, "E"] for i in range(len(matrix))]
starts_positions += [[i, len(matrix[0]) - 1, "W"] for i in range(len(matrix))]

current_counts = []
for start_position in starts_positions:
    total_cache_set = set()
    position_cache = set()
    # total_cache_list = []
    current_count = 0
    current_beam_list = [{"position": (start_position[0], start_position[1]), "direction": start_position[2]}]

    while len(current_beam_list) > 0:
        new_beam_list = []
        for current_beam in current_beam_list:
            new_beam_list += next_beams(current_beam["position"], current_beam["direction"])
        current_beam_list = new_beam_list
    current_counts.append(len(position_cache))
print(max(current_counts))
