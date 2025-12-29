"""
Top K Frequent Elements

Find k most frequent elements using heap.

Problem Statement:
-------------------
Given an array and integer k, find the k most frequent elements.

Example:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Why Heap?
---------
- Need to find k largest frequencies
- Min heap of size k: O(n log k)
- More efficient than sorting: O(n log n)

Useful in:
- Finding top elements
- Common interview problems
"""

from typing import List
from collections import Counter
import heapq


# ----------------------------------------------------------------------
# Top K Frequent Elements (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using min heap.

    Algorithm:
    1. Count frequencies using hash map
    2. Maintain min heap of size k (frequency, element)
    3. Return elements from heap

    Args:
        nums (List[int]): Input array
        k (int): Number of elements to return

    Returns:
        List[int]: K most frequent elements

    Complexity:
        Time: O(n log k)  - Count O(n) + heap operations O(n log k).
        Space: O(n)      - Frequency map and heap.
    """
    # Count frequencies
    freq_map = Counter(nums)
    
    # Min heap of size k
    heap = []
    
    for num, freq in freq_map.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))
    
    # Extract elements
    result = [num for freq, num in heap]
    return result


# ----------------------------------------------------------------------
# Top K Frequent (Alternative: Using Counter)
# ----------------------------------------------------------------------
def top_k_frequent_counter(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent using Counter's most_common.

    Args:
        nums (List[int]): Input array
        k (int): Number of elements

    Returns:
        List[int]: K most frequent elements

    Complexity:
        Time: O(n log n)  - Counter + sorting.
        Space: O(n)      - Frequency map.
    """
    counter = Counter(nums)
    return [num for num, freq in counter.most_common(k)]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Top K Frequent Elements Demonstration")
    
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Array: {nums}, k = {k}")
    
    result = top_k_frequent(nums, k)
    print(f"Top {k} frequent elements: {result}")
    
    # Using Counter
    result2 = top_k_frequent_counter(nums, k)
    print(f"Using Counter: {result2}")

