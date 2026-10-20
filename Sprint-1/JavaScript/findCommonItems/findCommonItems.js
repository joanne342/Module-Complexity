/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n + m) where n is the length of firstArray and m is the length of secondArray.
 * Space Complexity: O(m + k) auxiliary space where k is the number of unique common items
 * Optimal Time Complexity: O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */

export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  const commonSet = new Set();

  for (const item of firstArray) {
    if (secondSet.has(item)) {
      commonSet.add(item);
    }
  }

  return [...commonSet];
};
