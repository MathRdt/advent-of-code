from pathlib import Path


def main(input: str):
    meals = [sum([int(meal) for meal in meals.strip().split("\n")]) for meals in input.split("\n\n")]
    meals.sort(reverse=True)
    return sum(meals[:3])


if __name__ == "__main__":
    print(main(open(Path(__file__).parent / "input.txt").read()))
