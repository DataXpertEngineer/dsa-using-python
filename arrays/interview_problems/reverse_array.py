"""
Reverse Array Problem

Reverse an array in-place or return a reversed copy.

Problem Statement:
------------------
Given an array, reverse it in-place or create a reversed copy.

Example:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

This is a fundamental array manipulation problem.

Useful in:
- Array manipulation basics
- Two pointers technique
- In-place operations
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Two Pointers Approach (Language-agnostic, in-place)
# ----------------------------------------------------------------------
def reverse_array_inplace(nums: List[int]) -> None:
    """
    Reverse array in-place using two pointers technique.

    This approach works in all programming languages and is space-efficient.

    Args:
        nums (List[int]): Input array (modified in-place)

    Returns:
        None: Array is reversed in-place

    Complexity:
        Time: O(n)     - Swaps elements from both ends toward center, n/2 swaps.
        Space: O(1)   - Only uses variables for indices and temporary swap.
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def reverse_array_inplace_range(nums: List[int], start: int, end: int) -> None:
    """
    Reverse a portion of array from start to end (inclusive) in-place.

    Args:
        nums (List[int]): Input array (modified in-place)
        start (int): Start index
        end (int): End index

    Returns:
        None: Specified range is reversed in-place

    Complexity:
        Time: O(n)     - Swaps elements in the specified range.
        Space: O(1)   - Only uses variables for indices.
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# ----------------------------------------------------------------------
# Create Reversed Copy (Language-agnostic)
# ----------------------------------------------------------------------
def reverse_array_copy(nums: List[int]) -> List[int]:
    """
    Create a reversed copy of the array (original unchanged).

    This approach works in all programming languages.

    Args:
        nums (List[int]): Input array (not modified)

    Returns:
        List[int]: New reversed array

    Complexity:
        Time: O(n)     - Iterates through array once to create reversed copy.
        Space: O(n)   - Creates a new array of size n.
    """
    n = len(nums)
    reversed_arr = [0] * n
    
    for i in range(n):
        reversed_arr[i] = nums[n - 1 - i]
    
    return reversed_arr


def reverse_array_prepend(nums: List[int]) -> List[int]:
    """
    Create a reversed copy by prepending elements (building from front).

    This approach builds the reversed list by prepending each element.
    Works in all languages, though less efficient due to list prepending.

    Args:
        nums (List[int]): Input array (not modified)

    Returns:
        List[int]: New reversed array

    Complexity:
        Time: O(n²)    - Prepending to list requires shifting all elements, n operations of O(n).
        Space: O(n)   - Creates a new array of size n.
    """
    reversed_arr = []
    for num in nums:
        reversed_arr = [num] + reversed_arr  # Prepend element
    return reversed_arr


# ----------------------------------------------------------------------
# Python-specific Approaches
# ----------------------------------------------------------------------
def reverse_array_slicing(nums: List[int]) -> List[int]:
    """
    Reverse array using Python slicing (Python-specific).

    Args:
        nums (List[int]): Input array (not modified)

    Returns:
        List[int]: New reversed array

    Complexity:
        Time: O(n)     - Slicing creates a new reversed list.
        Space: O(n)   - Creates a new array of size n.
    """
    return nums[::-1]


def reverse_array_builtin(nums: List[int]) -> None:
    """
    Reverse array in-place using Python's built-in reverse() method.

    Args:
        nums (List[int]): Input array (modified in-place)

    Returns:
        None: Array is reversed in-place

    Complexity:
        Time: O(n)     - Built-in method uses efficient in-place reversal.
        Space: O(1)   - In-place operation.
    """
    nums.reverse()


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Reverse Array Problem Demonstration")
    
    nums1 = [1, 2, 3, 4, 5]
    print("Original array:", nums1)
    
    # In-place reversal (two pointers)
    arr1 = nums1.copy()
    reverse_array_inplace(arr1)
    print(f"Reversed (in-place): {arr1}")
    
    # Create reversed copy
    reversed_copy = reverse_array_copy(nums1)
    print(f"Reversed copy: {reversed_copy}")
    
    # Prepend approach
    reversed_prepend = reverse_array_prepend(nums1)
    print(f"Reversed (prepend): {reversed_prepend}")
    print(f"Original unchanged: {nums1}")
    
    # Reverse a range
    print("\n" + "="*50)
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    print("Original array:", nums2)
    arr2 = nums2.copy()
    reverse_array_inplace_range(arr2, 2, 5)
    print(f"Reversed range [2:5]: {arr2}")
    print("Expected: [1, 2, 6, 5, 4, 3, 7]")
    
    # Python-specific methods
    print("\n" + "="*50)
    nums3 = [10, 20, 30, 40]
    print("Original array:", nums3)
    
    # Using slicing
    reversed_slice = reverse_array_slicing(nums3)
    print(f"Reversed (slicing): {reversed_slice}")
    
    # Using built-in
    arr3 = nums3.copy()
    reverse_array_builtin(arr3)
    print(f"Reversed (built-in): {arr3}")

