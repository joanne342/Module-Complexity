from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n + m) where n and m are the lengths of the first and second sequences.
    Space Complexity: O(m + k) where k is the number of unique common items.
    Optimal time complexity: O(n + m)
    """
    second_items = set(second_sequence)
    seen_items = set()
    common_items: List[ItemType] = []

    for item in first_sequence:
        if item in second_items and item not in seen_items:
            common_items.append(item)
            seen_items.add(item)

    return common_items
