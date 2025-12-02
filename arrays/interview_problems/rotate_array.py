"""
Rotate Array Problem

Rotate an array to the right by k steps.

Problem Statement:
------------------
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example:
    Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]
    Explanation:
        rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
        rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
        rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

Useful in:
- Array manipulation
- In-place operations
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def rotate_array_naive(nums: List[int], k: int) -> None:
    """
    Rotate array to the right by k steps using brute-force approach.

    This approach works in all programming languages.

    Args:
        nums (List[int]): Input array (modified in-place)
        k (int): Number of steps to rotate right

    Returns:
        None: Array is rotated in-place

    Complexity:
        Time: O(n * k)    - For each of k rotations, shift all n elements.
        Space: O(1)      - Only uses a temporary variable for swapping.
    """
    n = len(nums)
    if n == 0 or k == 0:
        return
    
    k = k % n  # Handle k > n
    
    for _ in range(k):
        # Store last element
        last = nums[n - 1]
        # Shift all elements to the right
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        # Place last element at the beginning
        nums[0] = last


# ----------------------------------------------------------------------
# Extra Array Approach (Language-agnostic)
# ----------------------------------------------------------------------
def rotate_array_extra_space(nums: List[int], k: int) -> None:
    """
    Rotate array using extra space (more intuitive approach).

    This approach works in all programming languages.

    Args:
        nums (List[int]): Input array (modified in-place)
        k (int): Number of steps to rotate right

    Returns:
        None: Array is rotated in-place

    Complexity:
        Time: O(n)     - Single pass to copy elements to new positions.
        Space: O(n)    - Creates a copy of the array.
    """
    n = len(nums)
    if n == 0 or k == 0:
        return
    
    k = k % n
    result = [0] * n
    
    for i in range(n):
        result[(i + k) % n] = nums[i]
    
    # Copy back to original array
    for i in range(n):
        nums[i] = result[i]


# ----------------------------------------------------------------------
# Reverse Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def rotate_array_reverse(nums: List[int], k: int) -> None:
    """
    Rotate array using reverse operations (optimal in-place solution).

    Algorithm:
    1. Reverse the entire array
    2. Reverse the first k elements
    3. Reverse the remaining n-k elements

    This approach works in all programming languages and is space-efficient.

    Args:
        nums (List[int]): Input array (modified in-place)
        k (int): Number of steps to rotate right

    Returns:
        None: Array is rotated in-place

    Complexity:
        Time: O(n)     - Three reverse operations, each takes O(n).
        Space: O(1)   - Only uses variables for indices, no extra array.
    """
    n = len(nums)
    if n == 0 or k == 0:
        return
    
    k = k % n
    
    # Reverse entire array
    _reverse(nums, 0, n - 1)
    # Reverse first k elements
    _reverse(nums, 0, k - 1)
    # Reverse remaining elements
    _reverse(nums, k, n - 1)


def _reverse(nums: List[int], start: int, end: int) -> None:
    """
    Reverse elements in array from start to end (inclusive).

    Args:
        nums (List[int]): Array to reverse
        start (int): Start index
        end (int): End index
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# ----------------------------------------------------------------------
# Python-specific Approach (Using slicing)
# ----------------------------------------------------------------------
def rotate_array_pythonic(nums: List[int], k: int) -> None:
    """
    Rotate array using Python slicing (Python-specific).

    This is concise but creates a new list temporarily.

    Args:
        nums (List[int]): Input array (modified in-place)
        k (int): Number of steps to rotate right

    Returns:
        None: Array is rotated in-place

    Complexity:
        Time: O(n)     - Slicing and concatenation operations.
        Space: O(n)   - Creates temporary lists during slicing.
    """
    n = len(nums)
    if n == 0 or k == 0:
        return
    
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Rotate Array Problem Demonstration")
    
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print("Original array:", nums1)
    print("Rotate right by", k1, "steps")
    
    # Test reverse approach (optimal)
    arr1 = nums1.copy()
    rotate_array_reverse(arr1, k1)
    print(f"After rotation (reverse method): {arr1}")
    print("Expected: [5, 6, 7, 1, 2, 3, 4]")
    
    # Test extra space approach
    arr2 = nums1.copy()
    rotate_array_extra_space(arr2, k1)
    print(f"After rotation (extra space): {arr2}")
    
    # Test Pythonic approach
    arr3 = nums1.copy()
    rotate_array_pythonic(arr3, k1)
    print(f"After rotation (Pythonic): {arr3}")
    
    # Test with k > array length
    print("\n" + "="*50)
    nums2 = [1, 2, 3]
    k2 = 4
    print("Array:", nums2)
    print("Rotate right by", k2, "steps (equivalent to", k2 % len(nums2), "steps)")
    rotate_array_reverse(nums2, k2)
    print(f"After rotation: {nums2}")

