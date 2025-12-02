"""
Maximum Subarray Sum Problem

Find the contiguous subarray within a one-dimensional array that has the largest sum.

Problem Statement:
------------------
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: [4, -1, 2, 1] has the largest sum = 6

This is a classic dynamic programming problem, also known as Kadane's Algorithm.

Useful in:
- Dynamic programming practice
- Array manipulation
- Stock trading problems
- Common interview problem
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Kadane's Algorithm (Language-agnostic)
# ----------------------------------------------------------------------
def max_subarray_sum(nums: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray using Kadane's algorithm.

    This implementation works in all programming languages.

    Args:
        nums (List[int]): Input array of integers

    Returns:
        int: Maximum sum of any contiguous subarray

    Complexity:
        Time: O(n)     - Single pass through array, constant work per element.
        Space: O(1)   - Only uses two variables (max_ending_here, max_so_far).
    """
    if not nums:
        return 0
    
    max_ending_here = nums[0]
    max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend previous subarray or start new one
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def max_subarray_sum_with_indices(nums: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum sum of contiguous subarray and return the subarray indices.

    Args:
        nums (List[int]): Input array of integers

    Returns:
        Tuple[int, int, int]: (max_sum, start_index, end_index)

    Complexity:
        Time: O(n)     - Single pass through array, tracks indices while computing max.
        Space: O(1)   - Only uses variables for sums and indices.
    """
    if not nums:
        return (0, 0, 0)
    
    max_ending_here = nums[0]
    max_so_far = nums[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if max_ending_here < 0:
            max_ending_here = nums[i]
            temp_start = i
        else:
            max_ending_here += nums[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    return (max_so_far, start, end)


# ----------------------------------------------------------------------
# Handle All Negative Case (Language-agnostic)
# ----------------------------------------------------------------------
def max_subarray_sum_handle_negative(nums: List[int]) -> int:
    """
    Find maximum sum, returns 0 if all elements are negative.

    Useful for problems where empty subarray (sum = 0) is allowed.

    Args:
        nums (List[int]): Input array of integers

    Returns:
        int: Maximum sum (0 if all elements are negative)

    Complexity:
        Time: O(n)     - Single pass through array, resets sum to 0 when negative.
        Space: O(1)   - Only uses two variables for tracking sums.
    """
    max_ending_here = 0
    max_so_far = 0
    
    for num in nums:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Maximum Subarray Sum Problem Demonstration")
    
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Array:", nums1)
    
    max_sum = max_subarray_sum(nums1)
    print(f"Maximum subarray sum: {max_sum}")
    
    # With indices
    max_sum, start, end = max_subarray_sum_with_indices(nums1)
    print(f"Maximum subarray: indices [{start}:{end}] = {nums1[start:end+1]}, sum = {max_sum}")
    print("Explanation: Subarray [4, -1, 2, 1] has sum = 6 (maximum)")
    
    # Test with all negative numbers
    print("\n" + "="*50)
    nums2 = [-2, -3, -1, -5]
    print("Array with all negative numbers:", nums2)
    max_sum = max_subarray_sum(nums2)
    print(f"Maximum subarray sum: {max_sum}")
    print("Maximum subarray sum (handle negative):", max_subarray_sum_handle_negative(nums2))
    
    # Test with mixed positive and negative
    print("\n" + "="*50)
    nums3 = [1, -3, 2, 1, -1]
    print("Array:", nums3)
    max_sum, start, end = max_subarray_sum_with_indices(nums3)
    print(f"Maximum subarray: indices [{start}:{end}] = {nums3[start:end+1]}, sum = {max_sum}")

