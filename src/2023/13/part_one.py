from pathlib import Path


def main(input: str):
    models = [model.strip().split("\n") for model in input.split("\n\n")]
    count = 0
    for model in models:
        if (mirror_index := get_mirroring_index(model)) is not None:
            print(mirror_index)
            count += mirror_index * 100
        else:
            transposed_model = ["".join(list(x)) for x in zip(*model)]
            transposed_mirror_index = get_mirroring_index(transposed_model)
            print(transposed_mirror_index)
            count += transposed_mirror_index
    return count


def get_mirroring_index(model):
    model_len = len(model)
    starting_index = 0
    is_mirroring = False
    while starting_index < model_len and is_mirroring == False:
        diff_index = 1
        while starting_index - diff_index >= 0 and starting_index + diff_index - 1 < model_len:
            if model[starting_index + diff_index - 1] != model[starting_index - diff_index]:
                is_mirroring = False
                break
            diff_index += 1
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
