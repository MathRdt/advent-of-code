from collections import OrderedDict
from pathlib import Path


def main(input: str):
    values = input.strip().split(",")
    hashmap = {}
    for value in values:
        label_hash = 0
        i = 0
        while value[i] not in ["-", "="]:
            label_hash += ord(value[i])
            label_hash *= 17
            label_hash = label_hash % 256
            i += 1
        label_hash += 1
        label = value[:i]
        if hashmap.get(label_hash) is None:
            hashmap[label_hash] = OrderedDict()
        if value[i] == "=":
            lens = value[i + 1]
            hashmap[label_hash][label] = lens
        elif value[i] == "-":
            if hashmap[label_hash].get(label) is not None:
                del hashmap[label_hash][label]
    count = 0
    for box_index, box in hashmap.items():
        for lens_index, lens_value in enumerate(box.values()):
            count += int(box_index) * (lens_index + 1) * int(lens_value)
    return count


if __name__ == "__main__":
    print(main(open(Path(__file__).parent / "input.txt").read()))
