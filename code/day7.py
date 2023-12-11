from collections import Counter
from typing import Literal

from common import read_input


def process_input(input: list[str]) -> tuple[list, list]:
    hands = []
    values = []
    for single_hand in input:
        hand, value = single_hand.split(" ")
        hands.append(hand)
        values.append(int(value))

    return hands, values


def classify_hand(
    counts: Counter,
) -> (
    Literal[
        "five_of_a_kind",
        "four_of_a_kind",
        "full_house",
        "two_pairs",
        "three_of_a_kind",
        "one_pair",
        "high_card",
    ]
    | None
):
    """Classify a given hand into a poker hand type."""
    hand_length = len(counts)

    if hand_length == 1:
        return "five_of_a_kind"
    elif hand_length == 2:
        return "four_of_a_kind" if counts.most_common(1)[0][1] == 4 else "full_house"
    elif hand_length == 3:
        return "two_pairs" if counts.most_common(2)[0][1] == 2 else "three_of_a_kind"
    elif hand_length == 4:
        return "one_pair"
    elif hand_length == 5:
        return "high_card"


def get_hand_types(hands: list, values: list) -> dict[str, list]:
    global part_2
    hand_types = {
        type_: []
        for type_ in [
            "five_of_a_kind",
            "four_of_a_kind",
            "full_house",
            "three_of_a_kind",
            "two_pairs",
            "one_pair",
            "high_card",
        ]
    }

    for hand, value in zip(hands, values):
        counts = Counter(hand)
        if part_2 and "J" in hand and len(counts) > 1:
            first_key = (
                counts.most_common(1)[0][0]
                if counts.most_common(1)[0][0] != "J"
                else counts.most_common(2)[1][0]
            )
            counts[first_key] += counts["J"]
            del counts["J"]

        hand_type = classify_hand(counts)
        hand_types[hand_type].append((hand, value))
    return hand_types


def custom_sort_key(hand: list) -> tuple[int, ...]:
    global part_2
    if part_2:
        custom_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        custom_order = [
            "A",
            "K",
            "Q",
            "J",
            "T",
            "9",
            "8",
            "7",
            "6",
            "5",
            "4",
            "3",
            "2",
        ]
    hand_str_value = hand[0]
    return tuple(
        custom_order.index(c) if c in custom_order else len(custom_order)
        for c in hand_str_value
    )


def solution(hand_types: dict[str, list], len_hands: int) -> int:
    product = 0
    for hands in hand_types.values():
        sorted_hands = sorted(hands, key=custom_sort_key)
        for hand in sorted_hands:
            product += len_hands * hand[1]
            len_hands -= 1

    return product


if __name__ == "__main__":
    part_2 = True
    input = read_input("inputs/day7.txt")
    hands, values = process_input(input)
    len_hands = len(hands)
    hand_types = get_hand_types(hands, values)
    print(solution(hand_types, len_hands))
