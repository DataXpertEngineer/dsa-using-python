"""
Kth Smallest/Largest Element

Find kth smallest or largest element efficiently using sorting/selection.

Problem Statement:
-------------------
Given an array and integer k, find the kth smallest or largest element.

Example:
    Input: [7, 10, 4, 3, 20, 15], k = 3
    Kth smallest: 7
    Kth largest: 10

Why Sorting/Selection?
----------------------
- Sort and access: O(n log n) time
- Quickselect: O(n) average time
- Heap: O(n log k) time

Useful in:
- Finding order statistics
- Common interview problems
"""

from typing import List
import heapq


# ----------------------------------------------------------------------
# Kth Smallest - Using Sorting
# ----------------------------------------------------------------------
def kth_smallest_sort(arr: List[int], k: int) -> int:
    """
    Find kth smallest element using sorting.

    Args:
        arr (List[int]): Input array
        k (int): Position (1-indexed)

    Returns:
        int: Kth smallest element

    Complexity:
        Time: O(n log n)  - Sorting the array.
        Space: O(1)      - Only uses variables.
    """
    arr_sorted = sorted(arr)
    return arr_sorted[k - 1]


# ----------------------------------------------------------------------
# Kth Smallest - Using Quickselect (Optimal)
# ----------------------------------------------------------------------
def kth_smallest_quickselect(arr: List[int], k: int) -> int:
    """
    Find kth smallest element using quickselect algorithm.

    Algorithm:
    1. Partition array around pivot
    2. If pivot is at k-1, return it
    3. If pivot > k-1, search left partition
    4. If pivot < k-1, search right partition

    Args:
        arr (List[int]): Input array
        k (int): Position (1-indexed)

    Returns:
        int: Kth smallest element

    Complexity:
        Time: O(n) average  - O(n²) worst case.
        Space: O(1)        - In-place partitioning.
    """
    arr = arr.copy()
    
    def quickselect(left: int, right: int, k: int) -> int:
        if left == right:
            return arr[left]
        
        pivot_idx = _partition_select(arr, left, right)
        
        if pivot_idx == k - 1:
            return arr[pivot_idx]
        elif pivot_idx > k - 1:
            return quickselect(left, pivot_idx - 1, k)
        else:
            return quickselect(pivot_idx + 1, right, k)
    
    return quickselect(0, len(arr) - 1, k)


def _partition_select(arr: List[int], left: int, right: int) -> int:
    """Partition for quickselect."""
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# ----------------------------------------------------------------------
# Kth Largest - Using Heap
# ----------------------------------------------------------------------
def kth_largest_heap(arr: List[int], k: int) -> int:
    """
    Find kth largest element using min heap of size k.

    Args:
        arr (List[int]): Input array
        k (int): Position (1-indexed)

    Returns:
        int: Kth largest element

    Complexity:
        Time: O(n log k)  - Process n elements, heap size k.
        Space: O(k)      - Heap storage.
    """
    heap = []
    
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Kth Smallest/Largest Element Demonstration")
    
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"Array: {arr}, k = {k}")
    
    kth_small = kth_smallest_sort(arr, k)
    print(f"Kth smallest (sorting): {kth_small}")
    
    kth_small_qs = kth_smallest_quickselect(arr, k)
    print(f"Kth smallest (quickselect): {kth_small_qs}")
    
    kth_large = kth_largest_heap(arr, k)
    print(f"Kth largest (heap): {kth_large}")

