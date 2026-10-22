
def fibonacci(n: int) -> int:
    
    if n < 0:
        raise ValueError("n must be non-negative")

    cache = {0: 0, 1: 1}

    def helper(n: int) -> int:
        # Return the answer immediately if it is already cached.
        if n in cache:
            return cache[n]

        # Calculate the answer and store it for future calls.
        cache[n] = helper(n - 1) + helper(n - 2)

        return cache[n]

    return helper(n)
