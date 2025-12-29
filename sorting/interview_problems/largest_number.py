"""
Largest Number from Array

Form the largest number by arranging array elements.

Problem Statement:
-------------------
Given a list of non-negative integers, arrange them such that they form
the largest number.

Example:
    Input: [10, 2]
    Output: "210"

    Input: [3, 30, 34, 5, 9]
    Output: "9534330"

Why Custom Sorting?
-------------------
- Standard sorting doesn't work
- Need custom comparator: compare "ab" vs "ba"
- Sort in descending order of concatenated strings

Useful in:
- Custom sorting problems
- Medium difficulty interview problems
"""

from typing import List
from functools import cmp_to_key


# ----------------------------------------------------------------------
# Largest Number (Language-agnostic)
# ----------------------------------------------------------------------
def largest_number(nums: List[int]) -> str:
    """
    Form largest number from array using custom sorting.

    Algorithm:
    1. Convert numbers to strings
    2. Sort using custom comparator: compare "a+b" vs "b+a"
    3. Concatenate sorted strings

    Args:
        nums (List[int]): Array of non-negative integers

    Returns:
        str: Largest number as string

    Complexity:
        Time: O(n log n * k)  - n numbers, k is average string length.
        Space: O(n)          - String storage.
    """
    # Convert to strings
    str_nums = [str(num) for num in nums]
    
    # Custom comparator
    def compare(a: str, b: str) -> int:
        if a + b > b + a:
            return -1  # a should come before b
        elif a + b < b + a:
            return 1   # b should come before a
        else:
            return 0
    
    # Sort in descending order
    str_nums.sort(key=cmp_to_key(compare))
    
    # Handle leading zeros
    result = ''.join(str_nums)
    return result if result[0] != '0' else '0'


# ----------------------------------------------------------------------
# Largest Number (Alternative)
# ----------------------------------------------------------------------
def largest_number_alt(nums: List[int]) -> str:
    """
    Form largest number using alternative approach.

    Args:
        nums (List[int]): Array of non-negative integers

    Returns:
        str: Largest number as string

    Complexity:
        Time: O(n log n * k)  - Sorting with custom key.
        Space: O(n)          - String storage.
    """
    # Convert to strings and sort
    str_nums = sorted([str(num) for num in nums], 
                     key=lambda x: x * 10,  # Multiply to handle different lengths
                     reverse=True)
    
    result = ''.join(str_nums)
    return result if result[0] != '0' else '0'


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Largest Number Demonstration")
    
    nums1 = [10, 2]
    print(f"Array: {nums1}")
    result1 = largest_number(nums1)
    print(f"Largest number: {result1}")
    print("Explanation: '210' > '102'")
    
    # Another example
    print("\n" + "="*50)
    nums2 = [3, 30, 34, 5, 9]
    print(f"Array: {nums2}")
    result2 = largest_number(nums2)
    print(f"Largest number: {result2}")
    print("Explanation: '9534330' is the largest arrangement")

