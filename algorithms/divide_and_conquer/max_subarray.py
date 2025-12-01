"""
Maximum Subarray Problem (Divide and Conquer)

The maximum subarray problem finds the contiguous subarray within a one-dimensional
array of numbers that has the largest sum.

This implementation uses the divide-and-conquer approach, which is different from
Kadane's algorithm (dynamic programming approach).

Divide and Conquer Strategy:
1. Divide: Split array into two halves
2. Conquer: Recursively find max subarray in left and right halves
3. Combine: Find max subarray crossing the midpoint
4. Return: Maximum of the three results

Why Divide and Conquer?
------------------------
Advantages:
    - Demonstrates divide-and-conquer technique
    - Guaranteed O(n log n) time complexity
    - Educational value for understanding recursion

Disadvantages:
    - Slower than Kadane's algorithm (O(n) vs O(n log n))
    - More complex implementation
    - Uses O(log n) space for recursion stack

Note: For practical purposes, Kadane's algorithm (O(n)) is preferred.
This implementation is shown for educational purposes to demonstrate
divide-and-conquer technique.

Useful in:
- Understanding divide-and-conquer paradigm
- Educational purposes
- When you need to solve similar problems using divide-and-conquer
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Divide and Conquer Approach
# ----------------------------------------------------------------------
def max_subarray_sum_dc(arr: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray using divide-and-conquer approach.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Maximum sum of any contiguous subarray

    Complexity:
        Time: O(n log n)    - Divides array log n times, processes n elements each level.
        Space: O(log n)     - Recursion stack depth is log n.
    """
    if not arr:
        return 0
    
    return _max_subarray_recursive(arr, 0, len(arr) - 1)


def _max_subarray_recursive(arr: List[int], low: int, high: int) -> int:
    """
    Recursively find maximum subarray sum in arr[low:high+1].

    Args:
        arr (List[int]): Input array
        low (int): Starting index
        high (int): Ending index

    Returns:
        int: Maximum sum of contiguous subarray
    """
    # Base case: single element
    if low == high:
        return arr[low]
    
    # Divide
    mid = low + (high - low) // 2
    
    # Conquer: find max in left and right halves
    left_max = _max_subarray_recursive(arr, low, mid)
    right_max = _max_subarray_recursive(arr, mid + 1, high)
    
    # Combine: find max crossing the midpoint
    cross_max = _max_crossing_subarray(arr, low, mid, high)
    
    # Return maximum of the three
    return max(left_max, right_max, cross_max)


def _max_crossing_subarray(arr: List[int], low: int, mid: int, high: int) -> int:
    """
    Find maximum sum of subarray crossing the midpoint.

    Args:
        arr (List[int]): Input array
        low (int): Starting index
        mid (int): Midpoint index
        high (int): Ending index

    Returns:
        int: Maximum sum of subarray crossing midpoint
    """
    # Find max sum in left half (ending at mid)
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)
    
    # Find max sum in right half (starting from mid+1)
    right_sum = float('-inf')
    total = 0
    for j in range(mid + 1, high + 1):
        total += arr[j]
        right_sum = max(right_sum, total)
    
    # Return sum of both halves
    return left_sum + right_sum


# ----------------------------------------------------------------------
# Divide and Conquer with Indices
# ----------------------------------------------------------------------
def max_subarray_sum_with_indices_dc(arr: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum sum of contiguous subarray and return indices using divide-and-conquer.

    Args:
        arr (List[int]): Input array

    Returns:
        Tuple[int, int, int]: (max_sum, start_index, end_index)

    Complexity:
        Time: O(n log n)    - Same as basic divide-and-conquer approach.
        Space: O(log n)     - Recursion stack depth is log n.
    """
    if not arr:
        return (0, 0, 0)
    
    return _max_subarray_recursive_with_indices(arr, 0, len(arr) - 1)


def _max_subarray_recursive_with_indices(arr: List[int], low: int, high: int) -> Tuple[int, int, int]:
    """
    Recursively find maximum subarray with indices.

    Returns:
        Tuple[int, int, int]: (max_sum, start_index, end_index)
    """
    if low == high:
        return (arr[low], low, high)
    
    mid = low + (high - low) // 2
    
    left_sum, left_low, left_high = _max_subarray_recursive_with_indices(arr, low, mid)
    right_sum, right_low, right_high = _max_subarray_recursive_with_indices(arr, mid + 1, high)
    cross_sum, cross_low, cross_high = _max_crossing_subarray_with_indices(arr, low, mid, high)
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_sum, left_low, left_high)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_sum, right_low, right_high)
    else:
        return (cross_sum, cross_low, cross_high)


def _max_crossing_subarray_with_indices(arr: List[int], low: int, mid: int, high: int) -> Tuple[int, int, int]:
    """
    Find maximum crossing subarray with indices.

    Returns:
        Tuple[int, int, int]: (max_sum, start_index, end_index)
    """
    left_sum = float('-inf')
    total = 0
    max_left = mid
    
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i
    
    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    
    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j
    
    return (left_sum + right_sum, max_left, max_right)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Maximum Subarray (Divide and Conquer) Demonstration")
    
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Array:", arr1)
    
    max_sum = max_subarray_sum_dc(arr1)
    print(f"Maximum subarray sum: {max_sum}")
    
    # With indices
    max_sum, start, end = max_subarray_sum_with_indices_dc(arr1)
    print(f"Maximum subarray: indices [{start}:{end}] = {arr1[start:end+1]}, sum = {max_sum}")
    print("Explanation: Subarray [4, -1, 2, 1] has sum = 6 (maximum)")
    
    # Test with all negative numbers
    print("\n" + "="*50)
    arr2 = [-2, -3, -1, -5]
    print("Array with all negative numbers:", arr2)
    max_sum = max_subarray_sum_dc(arr2)
    print(f"Maximum subarray sum: {max_sum}")
    print("Explanation: Single element [-1] has the maximum sum")
    
    # Test with mixed positive and negative
    print("\n" + "="*50)
    arr3 = [1, -3, 2, 1, -1]
    print("Array:", arr3)
    max_sum, start, end = max_subarray_sum_with_indices_dc(arr3)
    print(f"Maximum subarray: indices [{start}:{end}] = {arr3[start:end+1]}, sum = {max_sum}")

