"""
Sort Colors (Dutch National Flag Problem)

Sort array of 0s, 1s, and 2s in-place using three-way partitioning.

Problem Statement:
-------------------
Given an array containing only 0s, 1s, and 2s, sort it in-place.

Example:
    Input: [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Why Three-Way Partitioning?
---------------------------
- Single pass O(n) solution
- In-place sorting
- Optimal for this specific problem
- Dutch National Flag algorithm

Useful in:
- Three-way partitioning problems
- Medium difficulty interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Sort Colors (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def sort_colors(nums: List[int]) -> None:
    """
    Sort array of 0s, 1s, and 2s using Dutch National Flag algorithm.

    Algorithm:
    1. Use three pointers: low, mid, high
    2. low: boundary of 0s
    3. mid: current element
    4. high: boundary of 2s
    5. Swap elements to correct region

    Args:
        nums (List[int]): Array containing only 0, 1, 2 (modified in-place)

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(1)   - Only uses three pointers.
    """
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid, need to check swapped element


# ----------------------------------------------------------------------
# Sort Colors (Counting Sort)
# ----------------------------------------------------------------------
def sort_colors_counting(nums: List[int]) -> None:
    """
    Sort colors using counting sort approach.

    Args:
        nums (List[int]): Array (modified in-place)

    Complexity:
        Time: O(n)     - Two passes through array.
        Space: O(1)   - Only uses count variables.
    """
    count = [0, 0, 0]
    
    # Count occurrences
    for num in nums:
        count[num] += 1
    
    # Fill array
    idx = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[idx] = color
            idx += 1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sort Colors Demonstration")
    
    nums = [2, 0, 2, 1, 1, 0]
    print(f"Original: {nums}")
    
    sort_colors(nums)
    print(f"Sorted (Dutch Flag): {nums}")
    
    # Counting sort
    print("\n" + "="*50)
    nums2 = [2, 0, 1, 2, 1, 0]
    print(f"Original: {nums2}")
    sort_colors_counting(nums2)
    print(f"Sorted (Counting): {nums2}")

