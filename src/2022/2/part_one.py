from pathlib import Path

match_points = {
    "X": {"value": 1, "A": 3, "B": 0, "C": 6},
    "Y": {"value": 2, "A": 6, "B": 3, "C": 0},
    "Z": {"value": 3, "A": 0, "B": 6, "C": 3},
}


def main(input: str):
    matches = input.splitlines()
    value = 0
    for match in matches:
        opponent_action, my_action = match.strip().split()
        value += match_points[my_action]["value"] + match_points[my_action][opponent_action]
    return value


if __name__ == "__main__":
    print(main(open(Path(__file__).parent / "input.txt").read()))
