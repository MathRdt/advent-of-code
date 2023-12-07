from pathlib import Path
from commons import utils
from collections import Counter
from dataclasses import dataclass


@dataclass
class Hand:
    """Class for keeping track of an item in inventory."""

    value: str
    bid: int
    type: int = 0


values_mapping = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}


def main(input_lines: list[str]):
    hands_list = []
    for input_line in input_lines:
        hand_value, hand_bid = input_line.split()
        hands_list.append(Hand(value=hand_value, bid=int(hand_bid), type=get_type(hand_value)))
    sorted_hands_list = sorted(hands_list, key=lambda x: (x.type, get_real_value(x.value)))
    bids_values = []
    for index, hand in enumerate(sorted_hands_list):
        bids_values.append(hand.bid * (index + 1))
    return sum(bids_values)


def get_type(hand_value: str):
    counter = Counter(list(hand_value))
    hand_strength = list(counter.values())
    hand_strength.sort(reverse=True)
    hand_strength = [str(i) for i in hand_strength]
    return int("".join(fill_list_values(hand_strength)))


def get_real_value(hand_value: str):
    real_value_list = [values_mapping[char] for char in hand_value]
    return int("".join(real_value_list))


def fill_list_values(hand_strength):
    return hand_strength + ["0"] * (5 - len(hand_strength))


if __name__ == "__main__":
    print(main(utils.read_file(Path(__file__).parent / "input.txt")))
