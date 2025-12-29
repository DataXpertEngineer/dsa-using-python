"""
Merge K Sorted Arrays

Merge k sorted arrays into one sorted array using heap.

Problem Statement:
-------------------
Given k sorted arrays, merge them into one sorted array.

Example:
    Input: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Why Heap?
---------
- Need to find minimum among k arrays
- Heap maintains minimum efficiently
- O(n log k) solution where n is total elements

Useful in:
- Merging sorted data
- External sorting
- Medium difficulty interview problems
"""

from typing import List, Tuple
import heapq


# ----------------------------------------------------------------------
# Merge K Sorted Arrays (Language-agnostic)
# ----------------------------------------------------------------------
def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Merge k sorted arrays using min heap.

    Algorithm:
    1. Push first element of each array into heap
    2. Extract minimum and add to result
    3. Push next element from same array
    4. Repeat until all elements processed

    Args:
        arrays (List[List[int]]): List of k sorted arrays

    Returns:
        List[int]: Merged sorted array

    Complexity:
        Time: O(n log k)  - n total elements, k arrays.
        Space: O(k)      - Heap stores k elements.
    """
    heap: List[Tuple[int, int, int]] = []  # (value, array_index, element_index)
    result: List[int] = []
    
    # Push first element of each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    
    # Merge arrays
    while heap:
        value, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(value)
        
        # Push next element from same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_elem = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_elem, arr_idx, elem_idx + 1))
    
    return result


# ----------------------------------------------------------------------
# Merge K Sorted Arrays (Alternative)
# ----------------------------------------------------------------------
def merge_k_sorted_arrays_alt(arrays: List[List[int]]) -> List[int]:
    """
    Merge k sorted arrays by merging two at a time.

    Args:
        arrays (List[List[int]]): List of k sorted arrays

    Returns:
        List[int]: Merged sorted array

    Complexity:
        Time: O(n * k)    - Merge k times, each O(n).
        Space: O(n)      - Stores merged result.
    """
    if not arrays:
        return []
    
    result = arrays[0]
    
    for i in range(1, len(arrays)):
        result = _merge_two_sorted(result, arrays[i])
    
    return result


def _merge_two_sorted(arr1: List[int], arr2: List[int]) -> List[int]:
    """Merge two sorted arrays."""
    result = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Merge K Sorted Arrays Demonstration")
    
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(f"K sorted arrays: {arrays}")
    
    merged = merge_k_sorted_arrays(arrays)
    print(f"Merged array: {merged}")
    
    # Alternative approach
    merged_alt = merge_k_sorted_arrays_alt(arrays)
    print(f"Alternative approach: {merged_alt}")

