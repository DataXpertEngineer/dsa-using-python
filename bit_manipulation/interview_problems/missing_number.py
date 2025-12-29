"""
Missing Number Using XOR

Find the missing number in an array using XOR properties.

Problem Statement:
-------------------
Given an array containing n distinct numbers taken from [0, n],
find the one missing number.

Example:
    Input: nums = [3, 0, 1], n = 3
    Output: 2

Useful in:
- Finding unique elements
- XOR properties
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Missing Number - XOR (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def missing_number_xor(nums: List[int], n: int) -> int:
    """
    Find missing number using XOR.

    Algorithm:
    XOR all numbers in array and all numbers from 0 to n.
    The missing number will be the result.

    Args:
        nums (List[int]): Array with n numbers (missing one from 0 to n)
        n (int): Maximum number (array should have 0 to n, one missing)

    Returns:
        int: Missing number

    Complexity:
        Time: O(n)     - XOR all numbers and all indices.
        Space: O(1)   - Only uses variables.
    """
    result = 0
    # XOR all numbers in array
    for num in nums:
        result ^= num
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        result ^= i
    return result


# ----------------------------------------------------------------------
# Missing Number - Sum Formula
# ----------------------------------------------------------------------
def missing_number_sum(nums: List[int], n: int) -> int:
    """
    Find missing number using sum formula.

    Expected sum = n * (n + 1) / 2
    Missing = Expected sum - Actual sum

    Args:
        nums (List[int]): Array with n numbers
        n (int): Maximum number

    Returns:
        int: Missing number

    Complexity:
        Time: O(n)     - Sums all numbers.
        Space: O(1)   - Only uses variables.
    """
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# ----------------------------------------------------------------------
# Missing Number - Array Modification
# ----------------------------------------------------------------------
def missing_number_array(nums: List[int], n: int) -> int:
    """
    Find missing number by marking present numbers.

    Args:
        nums (List[int]): Array with n numbers
        n (int): Maximum number

    Returns:
        int: Missing number

    Complexity:
        Time: O(n)     - Two passes through array.
        Space: O(1)   - Modifies input array.
    """
    # Mark present numbers as negative
    for num in nums:
        if 0 <= num <= n:
            nums[abs(num)] = -abs(nums[abs(num)])
    
    # Find unmarked number
    for i in range(n + 1):
        if i < len(nums) and nums[i] > 0:
            return i
        elif i >= len(nums):
            return i
    
    return n


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Missing Number Using XOR Demonstration")
    
    nums1 = [3, 0, 1]
    n1 = 3
    print(f"Array: {nums1}, n={n1}")
    print(f"Missing number (XOR): {missing_number_xor(nums1, n1)}")
    print(f"Missing number (Sum): {missing_number_sum(nums1, n1)}")
    print("Expected: 2")
    
    nums2 = [0, 1]
    n2 = 2
    print(f"\nArray: {nums2}, n={n2}")
    print(f"Missing number (XOR): {missing_number_xor(nums2, n2)}")
    print("Expected: 2")

