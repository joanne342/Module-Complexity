from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n)
    Space Complexity: O(n)
    Optimal time complexity: O(n)
    """
    seen = set()

    for number in numbers:
        complement = target_sum - number

        if complement in seen:
            return True

        seen.add(number)

    return False
