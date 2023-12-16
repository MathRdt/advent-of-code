from pathlib import Path

match_points = {
    "X": {"value": 0, "A": 3, "B": 1, "C": 2},
    "Y": {"value": 3, "A": 1, "B": 2, "C": 3},
    "Z": {"value": 6, "A": 2, "B": 3, "C": 1},
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
