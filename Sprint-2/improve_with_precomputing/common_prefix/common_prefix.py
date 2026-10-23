
from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    Return the longest prefix shared by any two strings.

    Return an empty string if fewer than two strings are supplied
    or if no two strings share a non-empty prefix.
    """
    if len(strings) < 2:
        return ""

    # Sort a copy so the caller's original list is not modified.
    sorted_strings = sorted(strings)

    longest = ""

    # The maximum common prefix must occur between adjacent
    # strings in lexicographically sorted order.
    for i in range(len(sorted_strings) - 1):
        common = find_common_prefix(
            sorted_strings[i],
            sorted_strings[i + 1],
        )

        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    """Return the longest prefix shared by two strings."""
    min_length = min(len(left), len(right))

    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]

    # One string may be a prefix of the other.
    return left[:min_length]
