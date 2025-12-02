"""
Two Sum Problem

Given an array of integers and a target sum, find two numbers that add up to the target.
Return the indices of these two numbers.

Problem Statement:
------------------
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Useful in:
- Hash table practice
- Array manipulation
- Common interview problem
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def two_sum_naive(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that sum to target using brute-force approach.

    This approach works in all programming languages without special features.

    Args:
        nums (List[int]): Input array of integers
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int]]: Indices of the two numbers, or None if not found

    Complexity:
        Time: O(n²)    - Nested loops check all pairs of elements.
        Space: O(1)    - Only uses variables for indices.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


# ----------------------------------------------------------------------
# Hash Table Approach (Python-optimized)
# ----------------------------------------------------------------------
def two_sum_hashmap(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that sum to target using hash map (dictionary).

    This uses Python's dictionary for O(1) lookups.

    Args:
        nums (List[int]): Input array of integers
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int]]: Indices of the two numbers, or None if not found

    Complexity:
        Time: O(n)     - Single pass through array, hash lookup is O(1).
        Space: O(n)    - Stores up to n elements in hash map.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None


# ----------------------------------------------------------------------
# Two Pointers Approach (For sorted array, language-agnostic)
# ----------------------------------------------------------------------
def two_sum_two_pointers(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that sum to target using two pointers (requires sorted array).

    This approach works in all languages and is efficient for sorted arrays.
    Note: This returns indices in the sorted array, not original indices.

    Args:
        nums (List[int]): Input array (must be sorted in ascending order)
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int]]: Indices of the two numbers, or None if not found

    Complexity (on sorted array):
        Time: O(n)     - Each pointer moves at most n steps total.
        Space: O(1)   - Only uses a couple of indices.
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Two Sum Problem Demonstration")
    
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Array:", nums1)
    print("Target:", target1)
    
    # Brute-force approach
    result_naive = two_sum_naive(nums1, target1)
    if result_naive:
        i, j = result_naive
        print(f"\nBrute-force: Indices [{i}, {j}] -> {nums1[i]} + {nums1[j]} = {target1}")
    
    # Hash map approach
    result_hash = two_sum_hashmap(nums1, target1)
    if result_hash:
        i, j = result_hash
        print(f"Hash map: Indices [{i}, {j}] -> {nums1[i]} + {nums1[j]} = {target1}")
    
    # Two pointers (sorted array)
    print("\n" + "="*50)
    nums2 = sorted(nums1)  # [2, 7, 11, 15]
    target2 = 9
    print("Sorted array:", nums2)
    print("Target:", target2)
    result_two_ptr = two_sum_two_pointers(nums2, target2)
    if result_two_ptr:
        i, j = result_two_ptr
        print(f"Two pointers: Indices [{i}, {j}] -> {nums2[i]} + {nums2[j]} = {target2}")
    
    # Test with no solution
    print("\n" + "="*50)
    nums3 = [1, 2, 3, 4]
    target3 = 10
    print("Array:", nums3)
    print("Target:", target3)
    result = two_sum_hashmap(nums3, target3)
    print(f"Result: {'Found' if result else 'Not found'}")

