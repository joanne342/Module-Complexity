/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const number of numbers) {
    const needed = target - number;

    // Check before adding: the same element cannot be used twice.
    if (seen.has(needed)) {
      return true;
    }

    // Remember this number for subsequent iterations.
    seen.add(number);
  }

  return false;
}
