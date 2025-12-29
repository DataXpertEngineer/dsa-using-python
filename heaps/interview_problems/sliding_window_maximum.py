"""
Sliding Window Maximum Using Heap

Find maximum in each sliding window using heap (alternative to deque).

Problem Statement:
-------------------
Given an array and window size k, find maximum in each sliding window.

Example:
    Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]

Why Heap?
---------
- Max heap maintains maximum efficiently
- O(n log n) solution
- Simpler than deque but less efficient

Note: Deque solution is O(n), heap is O(n log n)

Useful in:
- Sliding window problems
- Medium difficulty interview problems
"""

from typing import List
import heapq


# ----------------------------------------------------------------------
# Sliding Window Maximum (Using Heap)
# ----------------------------------------------------------------------
def max_sliding_window_heap(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window using max heap.

    Algorithm:
    1. Use max heap (negate values for min-heap)
    2. For each window, add elements to heap
    3. Remove elements outside window
    4. Extract maximum

    Args:
        nums (List[int]): Input array
        k (int): Window size

    Returns:
        List[int]: Maximum values for each window

    Complexity:
        Time: O(n log n)  - n windows, heap operations.
        Space: O(k)      - Heap storage.
    """
    if not nums or k == 0:
        return []
    
    result: List[int] = []
    heap: List[tuple[int, int]] = []  # (-value, index)
    
    for i in range(len(nums)):
        # Add current element
        heapq.heappush(heap, (-nums[i], i))
        
        # Remove elements outside window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        
        # Add maximum to result when window size reached
        if i >= k - 1:
            result.append(-heap[0][0])
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sliding Window Maximum Using Heap Demonstration")
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Array: {nums}, Window size: {k}")
    
    result = max_sliding_window_heap(nums, k)
    print(f"Maximum in each window: {result}")
    
    print("\nDetailed explanation:")
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        print(f"  Window {i}: {window} -> max = {result[i]}")

