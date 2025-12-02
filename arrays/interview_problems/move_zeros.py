"""
Move Zeros Problem

Move all zeros to the end while maintaining relative order of non-zero elements.

Problem Statement:
------------------
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example:
    Input: nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Useful in:
- Two pointers technique
- In-place array manipulation
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def move_zeros_naive(nums: List[int]) -> None:
    """
    Move zeros using brute-force approach (bubble-like).

    This approach works in all programming languages but is inefficient.

    Args:
        nums (List[int]): Input array (modified in-place)

    Returns:
        None: Array is modified in-place

    Complexity:
        Time: O(n²)    - For each zero, shift all following elements.
        Space: O(1)   - Only uses variables for indices.
    """
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            # Find next non-zero and swap
            for j in range(i + 1, n):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break


# ----------------------------------------------------------------------
# Two Pointers Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def move_zeros(nums: List[int]) -> None:
    """
    Move zeros using two pointers technique (optimal solution).

    Algorithm:
    1. Use slow pointer for position to place next non-zero
    2. Use fast pointer to traverse array
    3. When fast pointer finds non-zero, swap with slow pointer

    This approach works in all programming languages and is optimal.

    Args:
        nums (List[int]): Input array (modified in-place)

    Returns:
        None: Array is modified in-place

    Complexity:
        Time: O(n)     - Single pass through array, each element visited once.
        Space: O(1)   - Only uses variables for pointers.
    """
    slow = 0
    
    # Move all non-zero elements to the front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# ----------------------------------------------------------------------
# Alternative Two Pointers (Language-agnostic)
# ----------------------------------------------------------------------
def move_zeros_alternative(nums: List[int]) -> None:
    """
    Move zeros using alternative two pointers approach.

    First pass: move non-zeros to front
    Second pass: fill remaining with zeros

    Args:
        nums (List[int]): Input array (modified in-place)

    Returns:
        None: Array is modified in-place

    Complexity:
        Time: O(n)     - Two passes through array.
        Space: O(1)   - Only uses variables for indices.
    """
    write_pos = 0
    
    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_pos] = nums[i]
            write_pos += 1
    
    # Fill remaining positions with zeros
    for i in range(write_pos, len(nums)):
        nums[i] = 0


# ----------------------------------------------------------------------
# Python-specific Approach (Using list comprehension)
# ----------------------------------------------------------------------
def move_zeros_pythonic(nums: List[int]) -> None:
    """
    Move zeros using Python list operations (Python-specific).

    Args:
        nums (List[int]): Input array (modified in-place)

    Returns:
        None: Array is modified in-place

    Complexity:
        Time: O(n)     - Filtering and extending operations.
        Space: O(n)   - Creates temporary lists during filtering.
    """
    non_zeros = [x for x in nums if x != 0]
    zeros_count = len(nums) - len(non_zeros)
    nums[:] = non_zeros + [0] * zeros_count


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Move Zeros Problem Demonstration")
    
    nums1 = [0, 1, 0, 3, 12]
    print("Original array:", nums1)
    
    arr1 = nums1.copy()
    move_zeros(arr1)
    print(f"After moving zeros (two pointers): {arr1}")
    print("Expected: [1, 3, 12, 0, 0]")
    
    # Test alternative approach
    print("\n" + "="*50)
    nums2 = [0, 0, 1]
    print("Original array:", nums2)
    arr2 = nums2.copy()
    move_zeros_alternative(arr2)
    print(f"After moving zeros (alternative): {arr2}")
    
    # Test with all zeros
    print("\n" + "="*50)
    nums3 = [0, 0, 0]
    print("Original array:", nums3)
    arr3 = nums3.copy()
    move_zeros(arr3)
    print(f"After moving zeros: {arr3}")
    
    # Test with no zeros
    print("\n" + "="*50)
    nums4 = [1, 2, 3, 4]
    print("Original array:", nums4)
    arr4 = nums4.copy()
    move_zeros(arr4)
    print(f"After moving zeros: {arr4}")

