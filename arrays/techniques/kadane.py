"""
Kadane's Algorithm for Maximum Subarray Sum

Kadane's algorithm finds the maximum sum of a contiguous subarray in O(n) time.

The key insight: At each position, we decide whether to:
1. Extend the previous subarray (if it contributes positively)
2. Start a new subarray from the current position

Why Kadane's Algorithm?
------------------------
Without Kadane's algorithm (naive approach):
    Check all subarrays = O(n²) or O(n³)
With Kadane's algorithm:
    Single pass through array = O(n)

The algorithm maintains:
- `max_ending_here`: Maximum sum ending at current position
- `max_so_far`: Maximum sum seen so far

Useful in:
- Maximum subarray sum problems
- Stock trading problems (best time to buy/sell)
- Maximum product subarray (with modifications)
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Brute-force / Naive Approach
# ----------------------------------------------------------------------
def max_subarray_sum_naive(arr: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray using naive approach.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Maximum sum of any contiguous subarray

    Complexity:
        Time: O(n²)   - Nested loops check all possible subarray starting positions.
        Space: O(1)   - Only uses variables for tracking current and max sums.
    """
    max_sum = float('-inf')
    
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum


# ----------------------------------------------------------------------
# Kadane's Algorithm (Optimized)
# ----------------------------------------------------------------------
def max_subarray_sum_kadane(arr: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray using Kadane's algorithm.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Maximum sum of any contiguous subarray

    Complexity:
        Time: O(n)    - Single pass through array, constant work per element.
        Space: O(1)   - Only uses two variables (max_ending_here, max_so_far).
    """
    if not arr:
        return 0
    
    max_ending_here = arr[0]
    max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend previous subarray or start new one
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def max_subarray_sum_with_indices(arr: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum sum of contiguous subarray and return the subarray indices.

    Args:
        arr (List[int]): Input array

    Returns:
        Tuple[int, int, int]: (max_sum, start_index, end_index)

    Complexity:
        Time: O(n)    - Single pass through array, tracks indices while computing max.
        Space: O(1)   - Only uses variables for sums and indices.
    """
    if not arr:
        return (0, 0, 0)
    
    max_ending_here = arr[0]
    max_so_far = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if max_ending_here < 0:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    return (max_so_far, start, end)


def max_subarray_sum_handle_negative(arr: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray, returns 0 if all elements are negative.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Maximum sum (0 if all elements are negative)

    Complexity:
        Time: O(n)    - Single pass through array, resets sum to 0 when negative.
        Space: O(1)   - Only uses two variables for tracking sums.
    """
    max_ending_here = 0
    max_so_far = 0
    
    for num in arr:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Kadane's Algorithm Demonstration")
    
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Example 1: Maximum Subarray Sum")
    print("Array:", arr1)
    
    # Naive approach
    print("\nNaive Approach:")
    print("Max subarray sum ->", max_subarray_sum_naive(arr1))
    
    # Kadane's algorithm
    print("\nKadane's Algorithm:")
    max_sum = max_subarray_sum_kadane(arr1)
    print("Max subarray sum ->", max_sum)
    
    # With indices
    max_sum, start, end = max_subarray_sum_with_indices(arr1)
    print(f"Max subarray: indices [{start}:{end}] = {arr1[start:end+1]}, sum = {max_sum}")
    print("Explanation: Subarray [4, -1, 2, 1] has sum = 6 (maximum)")
    
    # Example 2: All negative numbers
    print("\n" + "="*50)
    arr2 = [-2, -3, -1, -5]
    print("Example 2: Array with all negative numbers")
    print("Array:", arr2)
    print("Max subarray sum (standard) ->", max_subarray_sum_kadane(arr2))
    print("Max subarray sum (handle negative) ->", max_subarray_sum_handle_negative(arr2))
    
    # Example 3: Mixed positive and negative
    print("\n" + "="*50)
    arr3 = [1, -3, 2, 1, -1]
    print("Example 3: Mixed positive and negative")
    print("Array:", arr3)
    max_sum = max_subarray_sum_kadane(arr3)
    max_sum_with_idx, start, end = max_subarray_sum_with_indices(arr3)
    print("Max subarray sum ->", max_sum)
    print(f"Max subarray: indices [{start}:{end}] = {arr3[start:end+1]}")

