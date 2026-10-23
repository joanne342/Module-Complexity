
def count_letters(s: str) -> int:
    """
    Return the number of distinct letters that occur in uppercase
    but never occur in lowercase in the input string.
    """
    # Precompute the distinct uppercase and lowercase letters.
    uppercase_letters = {char for char in s if char.isupper()}
    lowercase_letters = {char for char in s if char.islower()}

    # Convert lowercase letters to uppercase so that corresponding
    # letters can be compared consistently.
    lowercase_as_uppercase = {
        char.upper() for char in lowercase_letters
    }

    # Keep only uppercase letters with no lowercase equivalent.
    only_uppercase = uppercase_letters - lowercase_as_uppercase

    return len(only_uppercase)
