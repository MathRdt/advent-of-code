from pathlib import Path


def main(input: str):
    values = input.strip().split(",")
    count = 0
    for value in values:
        current_count = 0
        for char in value:
            current_count += ord(char)
            current_count *= 17
            current_count = current_count % 256
        count += current_count
    return count


if __name__ == "__main__":
    print(main(open(Path(__file__).parent / "input.txt").read()))
