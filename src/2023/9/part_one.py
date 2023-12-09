from pathlib import Path
from commons import utils


def main(input_lines: list[str]):
    extrapolated_values = []
    while len(input_lines) > 0:
        input_line = [int(measure) for measure in input_lines.pop().strip().split()]
        sensor_history = [input_line]
        while sensor_history[-1].count(sensor_history[-1][0]) < len(sensor_history[-1]):
            sensor_history.append(compute_next_sequence(sensor_history[-1]))
        current_sequence = sensor_history.pop()
        while len(sensor_history) > 0:
            next_sequence = sensor_history.pop()
            next_sequence = next_sequence + [next_sequence[-1] + current_sequence[-1]]
            current_sequence = next_sequence
        extrapolated_values.append(current_sequence[-1])
    return sum(extrapolated_values)


def compute_next_sequence(current_sequence: list[int]):
    next_sequence = []
    i = 1
    while i < len(current_sequence):
        next_sequence.append(current_sequence[i] - current_sequence[i - 1])
        i += 1
    return next_sequence


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
