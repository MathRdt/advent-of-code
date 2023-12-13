from pathlib import Path
import difflib


def main(input: str):
    models = [model.strip().split("\n") for model in input.split("\n\n")]
    count = 0
    for model in models:
        transposed_model = ["".join(list(x)) for x in zip(*model)]
        if (mirror_index := get_mirroring_index(model)) is not None:
            count += mirror_index * 100
        else:
            transposed_mirror_index = get_mirroring_index(transposed_model)
            count += transposed_mirror_index
    return count


def get_mirroring_index(model):
    model_len = len(model)
    starting_index = 1
    is_mirroring = False
    while starting_index < model_len and is_mirroring == False:
        diff_index = 1
        smudge = 0
        while starting_index - diff_index >= 0 and starting_index + diff_index - 1 < model_len:
            errors = [
                char
                for index, char in enumerate(model[starting_index + diff_index - 1])
                if char != model[starting_index - diff_index][index]
            ]
            if len(errors) == 1:
                smudge += 1
                if smudge > 1:
                    is_mirroring = False
                    break
            elif len(errors) > 1:
                is_mirroring = False
                break
            diff_index += 1
            if smudge == 1:
                is_mirroring = True
        starting_index += 1
    if is_mirroring == False:
        return None
    return starting_index - 1


def read_input():
    with open(Path(__file__).parent / "input.txt", "r") as f:
        return f.read()


if __name__ == "__main__":
    print(main(read_input()))
