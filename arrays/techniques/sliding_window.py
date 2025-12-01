"""
Sliding Window Technique for Arrays

The sliding window technique maintains a "window" of elements and slides it
across the array to solve problems efficiently.

Instead of recalculating values for overlapping subarrays, we:
1. Expand the window by adding new elements
2. Shrink the window by removing elements from the start
3. Update the result based on the current window state

Why Sliding Window?
-------------------
Without sliding window (naive approach):
    Check all subarrays of size k = O(n * k) or O(n²)
With sliding window:
    Single pass through array = O(n)

Useful in:
- Fixed-size window problems (e.g., maximum sum of subarray of size k)
- Variable-size window problems (e.g., longest subarray with sum ≤ target)
- Substring problems
- Problems involving consecutive elements
"""

from typing import List


# ----------------------------------------------------------------------
# Brute-force / Naive Approach
# ----------------------------------------------------------------------
def max_sum_subarray_naive(arr: List[int], k: int) -> int:
    """
    Find maximum sum of any subarray of size k using naive approach.

    Args:
        arr (List[int]): Input array
        k (int): Size of the subarray

    Returns:
        int: Maximum sum of any subarray of size k

    Complexity:
        Time: O(n * k)  - For each of n-k+1 positions, sum k elements.
        Space: O(1)     - Only uses a few variables for tracking.
    """
    if k > len(arr):
        return 0
    
    max_sum = float('-inf')
    for i in range(len(arr) - k + 1):
        window_sum = sum(arr[i:i + k])
        max_sum = max(max_sum, window_sum)
    return max_sum


# ----------------------------------------------------------------------
# Sliding Window Approach (Optimized)
# ----------------------------------------------------------------------
def max_sum_subarray_sliding_window(arr: List[int], k: int) -> int:
    """
    Find maximum sum of any subarray of size k using sliding window technique.

    Args:
        arr (List[int]): Input array
        k (int): Size of the subarray

    Returns:
        int: Maximum sum of any subarray of size k

    Complexity:
        Time: O(n)    - Single pass through array, each element processed once.
        Space: O(1)   - Only uses a few variables for window sum and max.
    """
    if k > len(arr):
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def longest_subarray_with_sum_at_most(arr: List[int], target: int) -> int:
    """
    Find the length of the longest subarray with sum <= target using variable-size window.

    Args:
        arr (List[int]): Input array (non-negative integers)
        target (int): Maximum allowed sum

    Returns:
        int: Length of longest subarray with sum <= target

    Complexity:
        Time: O(n)    - Each element added once, removed at most once (amortized).
        Space: O(1)   - Only uses pointers and sum variables.
    """
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink window if sum exceeds target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sliding Window Demonstration")
    
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print("Original array:", arr)
    print("Window size k:", k)
    
    # Naive approach
    print("\nNaive Approach:")
    print("Max sum of subarray of size", k, "->", max_sum_subarray_naive(arr, k))
    
    # Sliding window approach
    print("\nSliding Window Approach:")
    print("Max sum of subarray of size", k, "->", max_sum_subarray_sliding_window(arr, k))
    print("Explanation: Subarray [5, 1, 3] has sum = 9 (maximum)")
    
    # Variable-size window example
    print("\n" + "="*50)
    arr2 = [1, 2, 3, 4, 5]
    target = 7
    print("Variable-size Window Example:")
    print("Array:", arr2)
    print("Target sum (at most):", target)
    print("Longest subarray with sum <=", target, "->", longest_subarray_with_sum_at_most(arr2, target))
    print("Explanation: Subarray [1, 2, 3] has length 3 and sum = 6 <= 7")

