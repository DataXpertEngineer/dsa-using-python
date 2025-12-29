"""
Sliding Window Maximum Problem

Find maximum element in each sliding window of size k using deque.

Problem Statement:
-------------------
Given an array and window size k, find the maximum element in each
window of size k as it slides from left to right.

Example:
    Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]
    Explanation:
        Window 1: [1, 3, -1] -> max = 3
        Window 2: [3, -1, -3] -> max = 3
        Window 3: [-1, -3, 5] -> max = 5
        Window 4: [-3, 5, 3] -> max = 5
        Window 5: [5, 3, 6] -> max = 6
        Window 6: [3, 6, 7] -> max = 7

Why Deque?
----------
- Need to maintain decreasing sequence
- Remove elements outside window efficiently
- O(n) solution instead of O(n*k)

Useful in:
- Sliding window problems
- Array processing
- Common interview problems
"""

from typing import List
from collections import deque


# ----------------------------------------------------------------------
# Sliding Window Maximum (Language-agnostic)
# ----------------------------------------------------------------------
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window using deque.

    Algorithm:
    1. Use deque to store indices of decreasing sequence
    2. Remove indices outside current window
    3. Remove indices with smaller values (won't be max)
    4. Add current index to deque
    5. Add max to result when window size reached

    Args:
        nums (List[int]): Input array
        k (int): Window size

    Returns:
        List[int]: Maximum values for each window

    Complexity:
        Time: O(n)     - Each element added and removed at most once.
        Space: O(k)   - Deque stores at most k indices.
    """
    if not nums or k == 0:
        return []
    
    result: List[int] = []
    dq = deque()  # Store indices
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove indices with smaller values (won't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # Add current index
        dq.append(i)
        
        # Add max to result when window size reached
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# ----------------------------------------------------------------------
# Sliding Window Maximum (Brute Force)
# ----------------------------------------------------------------------
def max_sliding_window_bruteforce(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window using brute force.

    Args:
        nums (List[int]): Input array
        k (int): Window size

    Returns:
        List[int]: Maximum values for each window

    Complexity:
        Time: O(n * k)  - For each window, find max in O(k).
        Space: O(1)    - Only stores result (not counting output).
    """
    if not nums or k == 0:
        return []
    
    result: List[int] = []
    
    for i in range(len(nums) - k + 1):
        window_max = max(nums[i:i + k])
        result.append(window_max)
    
    return result


# ----------------------------------------------------------------------
# Sliding Window Minimum
# ----------------------------------------------------------------------
def min_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Find minimum in each sliding window using deque.

    Args:
        nums (List[int]): Input array
        k (int): Window size

    Returns:
        List[int]: Minimum values for each window

    Complexity:
        Time: O(n)     - Each element processed once.
        Space: O(k)   - Deque storage.
    """
    if not nums or k == 0:
        return []
    
    result: List[int] = []
    dq = deque()  # Store indices
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove indices with larger values (won't be min)
        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()
        
        # Add current index
        dq.append(i)
        
        # Add min to result when window size reached
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sliding Window Maximum Demonstration")
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Array: {nums}")
    print(f"Window size: {k}")
    
    result = max_sliding_window(nums, k)
    print(f"Maximum in each window: {result}")
    
    print("\nDetailed explanation:")
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        print(f"  Window {i}: {window} -> max = {result[i]}")
    
    # Compare with brute force
    print("\n" + "="*50)
    result_bf = max_sliding_window_bruteforce(nums, k)
    print(f"Brute force result: {result_bf}")
    print(f"Results match: {result == result_bf}")
    
    # Minimum sliding window
    print("\n" + "="*50)
    min_result = min_sliding_window(nums, k)
    print(f"Minimum in each window: {min_result}")

