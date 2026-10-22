
from typing import Dict, Tuple

COINS = (200, 100, 50, 20, 10, 5, 2, 1)


def ways_to_make_change(total: int) -> int:

    if total < 0:
        raise ValueError("total must be non-negative")

    cache: Dict[Tuple[int, int], int] = {}

    def helper(remaining: int, coin_index: int) -> int:
        # There is one way to make zero: choose no more coins.
        if remaining == 0:
            return 1

        # No coins remain, but the target has not been reached.
        if coin_index >= len(COINS):
            return 0

        # The result depends on both the amount and available coins.
        key = (remaining, coin_index)

        if key in cache:
            return cache[key]

        coin = COINS[coin_index]
        ways = 0

        # Try every possible quantity of the current denomination.
        for count in range(remaining // coin + 1):
            new_remaining = remaining - count * coin

            ways += helper(new_remaining, coin_index + 1)

        # Save the result so this subproblem is not recalculated.
        cache[key] = ways

        return ways

    return helper(total, 0)
