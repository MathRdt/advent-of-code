from pathlib import Path


def read_file(file_path: Path):
    with file_path.open(mode="r") as input_file:
        return input_file.readlines()
