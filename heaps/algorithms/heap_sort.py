"""
Heap Sort Algorithm

Sort array using heap data structure.

Algorithm:
1. Build max heap from array
2. Repeatedly extract maximum and place at end
3. Array is sorted in-place

Why Heap Sort?
--------------
- O(n log n) worst case (guaranteed)
- In-place sorting
- No worst-case O(n²) like quicksort
- Stable performance

Useful in:
- Sorting algorithms
- When guaranteed O(n log n) needed
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Heap Sort (Language-agnostic)
# ----------------------------------------------------------------------
def heap_sort(arr: List[int]) -> List[int]:
    """
    Sort array using heap sort algorithm.

    Algorithm:
    1. Build max heap from array
    2. Repeatedly extract max and place at end
    3. Array is sorted

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n log n)  - Build heap O(n) + n extractions O(n log n).
        Space: O(1)      - In-place sorting.
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_down(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify reduced heap
        _heapify_down(arr, i, 0)
    
    return arr


def _heapify_down(arr: List[int], heap_size: int, index: int) -> None:
    """
    Heapify down for max heap.

    Args:
        arr (List[int]): Array
        heap_size (int): Size of heap
        index (int): Index to heapify from

    Complexity:
        Time: O(log n)  - Moves down at most log n levels.
        Space: O(1)    - Only uses variables.
    """
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        _heapify_down(arr, heap_size, largest)


# ----------------------------------------------------------------------
# Heap Sort (Using Built-in Heap)
# ----------------------------------------------------------------------
def heap_sort_builtin(arr: List[int]) -> List[int]:
    """
    Sort array using Python's heapq (min-heap).

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n log n)  - n insertions and extractions.
        Space: O(n)      - Creates new heap.
    """
    import heapq
    
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Heap Sort Demonstration")
    
    arr = [12, 11, 13, 5, 6, 7]
    print(f"Original array: {arr}")
    
    sorted_arr = heap_sort(arr.copy())
    print(f"Sorted array: {sorted_arr}")
    
    # Using built-in
    sorted_arr2 = heap_sort_builtin(arr)
    print(f"Using built-in heapq: {sorted_arr2}")

