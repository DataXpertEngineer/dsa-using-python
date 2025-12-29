"""
Kth Largest/Smallest Element Using Heaps

Find kth largest or smallest element efficiently using heaps.

Problem Statement:
-------------------
Given an array and integer k, find the kth largest or smallest element.

Example:
    Input: [3, 1, 4, 1, 5, 9, 2, 6], k = 3
    Kth largest: 5
    Kth smallest: 2

Why Heaps?
----------
- Min heap of size k for kth largest: O(n log k)
- Max heap of size k for kth smallest: O(n log k)
- More efficient than sorting: O(n log n)

Useful in:
- Finding top/bottom k elements
- Common interview problems
"""

from typing import List
import heapq


# ----------------------------------------------------------------------
# Kth Largest Element (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element using min heap of size k.

    Algorithm:
    1. Maintain min heap of size k
    2. For each element, if larger than heap root, replace
    3. Root of heap is kth largest

    Args:
        nums (List[int]): Input array
        k (int): Position (1-indexed)

    Returns:
        int: Kth largest element

    Complexity:
        Time: O(n log k)  - Process n elements, heap size k.
        Space: O(k)      - Heap stores k elements.
    """
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]


# ----------------------------------------------------------------------
# Kth Smallest Element
# ----------------------------------------------------------------------
def kth_smallest(nums: List[int], k: int) -> int:
    """
    Find kth smallest element using max heap of size k.

    Note: Python's heapq is min-heap, so negate values.

    Args:
        nums (List[int]): Input array
        k (int): Position (1-indexed)

    Returns:
        int: Kth smallest element

    Complexity:
        Time: O(n log k)  - Process n elements, heap size k.
        Space: O(k)      - Heap stores k elements.
    """
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)  # Negate for max-heap
        elif num < -heap[0]:
            heapq.heapreplace(heap, -num)
    
    return -heap[0]


# ----------------------------------------------------------------------
# Top K Largest Elements
# ----------------------------------------------------------------------
def top_k_largest(nums: List[int], k: int) -> List[int]:
    """
    Find top k largest elements.

    Args:
        nums (List[int]): Input array
        k (int): Number of elements

    Returns:
        List[int]: Top k largest elements

    Complexity:
        Time: O(n log k)  - Process n elements, heap size k.
        Space: O(k)      - Heap stores k elements.
    """
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return sorted(heap, reverse=True)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Kth Largest/Smallest Element Demonstration")
    
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    k = 3
    print(f"Array: {nums}, k = {k}")
    
    kth_large = kth_largest(nums, k)
    print(f"Kth largest: {kth_large}")
    
    kth_small = kth_smallest(nums, k)
    print(f"Kth smallest: {kth_small}")
    
    # Top k largest
    print("\n" + "="*50)
    top_k = top_k_largest(nums, k)
    print(f"Top {k} largest: {top_k}")

