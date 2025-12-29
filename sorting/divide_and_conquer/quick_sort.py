"""
Quick Sort Algorithm

Quick sort is a divide-and-conquer algorithm that picks a pivot element,
partitions the array around the pivot, and recursively sorts the partitions.

Why Quick Sort?
---------------
- Average O(n log n) time complexity
- In-place sorting (O(log n) space for recursion)
- Cache-friendly
- Often faster than merge sort in practice

Disadvantages:
- Worst case O(n²) time
- Not stable
- Pivot selection affects performance

Useful in:
- General-purpose sorting
- When average performance matters
- Common interview problems
"""

from typing import List
import random


# ----------------------------------------------------------------------
# Quick Sort (Language-agnostic)
# ----------------------------------------------------------------------
def quick_sort(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """
    Sort array using quick sort algorithm.

    Algorithm:
    1. Choose pivot element
    2. Partition array around pivot
    3. Recursively sort left and right partitions

    Args:
        arr (List[int]): Input array
        low (int): Starting index
        high (int): Ending index

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n log n) average  - O(n²) worst case.
        Space: O(log n)           - Recursion stack depth.
    """
    arr = arr.copy()  # Don't modify original
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pivot_idx = _partition(arr, low, high)
        
        # Recursively sort partitions
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    
    return arr


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition array using Lomuto partition scheme.

    Args:
        arr (List[int]): Array to partition
        low (int): Starting index
        high (int): Ending index

    Returns:
        int: Final position of pivot

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(1)   - Only uses variables.
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ----------------------------------------------------------------------
# Quick Sort (Hoare Partition)
# ----------------------------------------------------------------------
def quick_sort_hoare(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    Sort array using quick sort with Hoare partition scheme.

    Args:
        arr (List[int]): Input array (modified in-place)
        low (int): Starting index
        high (int): Ending index

    Complexity:
        Time: O(n log n) average  - O(n²) worst case.
        Space: O(log n)          - Recursion stack.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = _partition_hoare(arr, low, high)
        quick_sort_hoare(arr, low, pivot_idx)
        quick_sort_hoare(arr, pivot_idx + 1, high)


def _partition_hoare(arr: List[int], low: int, high: int) -> int:
    """Partition using Hoare partition scheme."""
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]


# ----------------------------------------------------------------------
# Quick Sort (Randomized Pivot)
# ----------------------------------------------------------------------
def quick_sort_randomized(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    Sort array using quick sort with randomized pivot.

    Args:
        arr (List[int]): Input array (modified in-place)
        low (int): Starting index
        high (int): Ending index

    Complexity:
        Time: O(n log n) average  - Randomized pivot avoids worst case.
        Space: O(log n)          - Recursion stack.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Randomize pivot
        random_idx = random.randint(low, high)
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
        
        pivot_idx = _partition(arr, low, high)
        quick_sort_randomized(arr, low, pivot_idx - 1)
        quick_sort_randomized(arr, pivot_idx + 1, high)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Quick Sort Demonstration")
    
    arr = [10, 7, 8, 9, 1, 5]
    print(f"Original array: {arr}")
    
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # Hoare partition
    print("\n" + "="*50)
    arr2 = [10, 7, 8, 9, 1, 5]
    print(f"Original: {arr2}")
    quick_sort_hoare(arr2)
    print(f"After Hoare partition: {arr2}")
    
    # Randomized
    print("\n" + "="*50)
    arr3 = [10, 7, 8, 9, 1, 5]
    print(f"Original: {arr3}")
    quick_sort_randomized(arr3)
    print(f"After randomized pivot: {arr3}")

