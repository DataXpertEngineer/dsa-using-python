"""
Contains Duplicate Problem

Determine if an array contains any duplicates.

Problem Statement:
------------------
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Example:
    Input: nums = [1, 2, 3, 1]
    Output: true

Example:
    Input: nums = [1, 2, 3, 4]
    Output: false

Variations:
- Contains duplicate (this problem)
- Contains duplicate within k distance
- Contains duplicate within value difference

Useful in:
- Hash tables
- Set operations
- Array manipulation
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def contains_duplicate_naive(nums: List[int]) -> bool:
    """
    Check for duplicates using brute-force approach (nested loops).

    This approach works in all programming languages.

    Args:
        nums (List[int]): Input array

    Returns:
        bool: True if duplicates exist, False otherwise

    Complexity:
        Time: O(n²)    - Nested loops check all pairs of elements.
        Space: O(1)   - Only uses variables for indices.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ----------------------------------------------------------------------
# Sorting Approach (Language-agnostic)
# ----------------------------------------------------------------------
def contains_duplicate_sorting(nums: List[int]) -> bool:
    """
    Check for duplicates by sorting and comparing adjacent elements.

    This approach works in all programming languages.

    Args:
        nums (List[int]): Input array (will be sorted)

    Returns:
        bool: True if duplicates exist, False otherwise

    Complexity:
        Time: O(n log n)  - Sorting takes O(n log n) time.
        Space: O(1)     - If sorting is in-place, otherwise O(n).
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# ----------------------------------------------------------------------
# Hash Set Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def contains_duplicate_hashset(nums: List[int]) -> bool:
    """
    Check for duplicates using hash set (optimal solution).

    This approach works in all programming languages and is the most efficient.

    Args:
        nums (List[int]): Input array

    Returns:
        bool: True if duplicates exist, False otherwise

    Complexity:
        Time: O(n)     - Single pass through array, hash set operations are O(1).
        Space: O(n)   - Stores up to n elements in hash set.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ----------------------------------------------------------------------
# Python-specific Approach (Using set length)
# ----------------------------------------------------------------------
def contains_duplicate_pythonic(nums: List[int]) -> bool:
    """
    Check for duplicates using Python set (Python-specific).

    Args:
        nums (List[int]): Input array

    Returns:
        bool: True if duplicates exist, False otherwise

    Complexity:
        Time: O(n)     - Creating set from list takes O(n) time.
        Space: O(n)   - Set stores all unique elements.
    """
    return len(nums) != len(set(nums))


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Contains Duplicate Problem Demonstration")
    
    nums1 = [1, 2, 3, 1]
    print("Array:", nums1)
    
    result1 = contains_duplicate_hashset(nums1)
    print(f"Contains duplicate: {result1}")
    
    # Test with no duplicates
    print("\n" + "="*50)
    nums2 = [1, 2, 3, 4]
    print("Array:", nums2)
    result2 = contains_duplicate_hashset(nums2)
    print(f"Contains duplicate: {result2}")
    
    # Test with multiple duplicates
    print("\n" + "="*50)
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print("Array:", nums3)
    result3 = contains_duplicate_pythonic(nums3)
    print(f"Contains duplicate: {result3}")

