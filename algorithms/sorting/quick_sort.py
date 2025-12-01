"""
Quick Sort Algorithm

Quick sort is a divide-and-conquer sorting algorithm that works by selecting
a 'pivot' element and partitioning the array around the pivot, such that
elements smaller than pivot are on the left and elements greater are on the right.

The algorithm:
1. Choose a pivot element
2. Partition: Rearrange array so elements < pivot are left, > pivot are right
3. Recursively sort left and right subarrays

Why Quick Sort?
---------------
Advantages:
    - Average case O(n log n) time complexity
    - In-place sorting (O(log n) space for recursion stack)
    - Often faster than merge sort in practice
    - Cache-friendly due to good locality of reference

Disadvantages:
    - Worst case O(n²) if pivot is always smallest/largest
    - Not stable (may change relative order of equal elements)
    - Performance depends on pivot selection

Useful in:
- General-purpose sorting
- When average performance matters more than worst-case
- In-place sorting requirements
- Large datasets where cache performance matters
"""

from typing import List
import random


# ----------------------------------------------------------------------
# Quick Sort (Lomuto Partition Scheme)
# ----------------------------------------------------------------------
def quick_sort(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    Sort array in-place using quick sort with Lomuto partition scheme.

    Args:
        arr (List[int]): Input array to be sorted (modified in-place)
        low (int): Starting index (default: 0)
        high (int): Ending index (default: len(arr) - 1)

    Returns:
        None: Array is sorted in-place

    Complexity:
        Time: O(n log n) average, O(n²) worst case
        Space: O(log n)    - Recursion stack depth is log n on average.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition array and get pivot index
        pivot_idx = _partition_lomuto(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def _partition_lomuto(arr: List[int], low: int, high: int) -> int:
    """
    Partition array using Lomuto scheme (pivot is last element).

    Args:
        arr (List[int]): Array to partition
        low (int): Starting index
        high (int): Ending index

    Returns:
        int: Final position of pivot element
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # Place pivot in correct position
    arr[i], arr[high] = arr[high], arr[i]
    return i


# ----------------------------------------------------------------------
# Quick Sort (Hoare Partition Scheme)
# ----------------------------------------------------------------------
def quick_sort_hoare(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    Sort array in-place using quick sort with Hoare partition scheme.

    Hoare partition is generally more efficient than Lomuto as it does
    fewer swaps on average.

    Args:
        arr (List[int]): Input array to be sorted (modified in-place)
        low (int): Starting index (default: 0)
        high (int): Ending index (default: len(arr) - 1)

    Returns:
        None: Array is sorted in-place

    Complexity:
        Time: O(n log n) average, O(n²) worst case
        Space: O(log n)    - Recursion stack depth is log n on average.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = _partition_hoare(arr, low, high)
        quick_sort_hoare(arr, low, pivot_idx)
        quick_sort_hoare(arr, pivot_idx + 1, high)


def _partition_hoare(arr: List[int], low: int, high: int) -> int:
    """
    Partition array using Hoare scheme (pivot is first element).

    Args:
        arr (List[int]): Array to partition
        low (int): Starting index
        high (int): Ending index

    Returns:
        int: Final position of pivot element
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Find element on left that should be on right
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Find element on right that should be on left
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        # If pointers crossed, partitioning is done
        if i >= j:
            return j
        
        # Swap elements
        arr[i], arr[j] = arr[j], arr[i]


# ----------------------------------------------------------------------
# Quick Sort (Randomized Pivot)
# ----------------------------------------------------------------------
def quick_sort_randomized(arr: List[int], low: int = 0, high: int = None) -> None:
    """
    Sort array using quick sort with randomized pivot selection.

    Random pivot selection helps avoid worst-case O(n²) performance
    on already sorted arrays.

    Args:
        arr (List[int]): Input array to be sorted (modified in-place)
        low (int): Starting index (default: 0)
        high (int): Ending index (default: len(arr) - 1)

    Returns:
        None: Array is sorted in-place

    Complexity:
        Time: O(n log n) average, O(n²) worst case (rare with randomization)
        Space: O(log n)    - Recursion stack depth is log n on average.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Randomly select pivot and swap with last element
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        # Partition using Lomuto scheme
        pivot_pos = _partition_lomuto(arr, low, high)
        
        # Recursively sort
        quick_sort_randomized(arr, low, pivot_pos - 1)
        quick_sort_randomized(arr, pivot_pos + 1, high)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Quick Sort Demonstration")
    
    arr1 = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr1)
    quick_sort(arr1.copy())
    print("Sorted array (Lomuto):", arr1)
    
    # Test with Hoare partition
    print("\n" + "="*50)
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr2)
    arr2_copy = arr2.copy()
    quick_sort_hoare(arr2_copy)
    print("Sorted array (Hoare):", arr2_copy)
    
    # Test with randomized pivot
    print("\n" + "="*50)
    arr3 = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    print("Original array:", arr3)
    arr3_copy = arr3.copy()
    quick_sort_randomized(arr3_copy)
    print("Sorted array (Randomized):", arr3_copy)
    
    # Test with already sorted array (worst case for naive quick sort)
    print("\n" + "="*50)
    arr4 = [1, 2, 3, 4, 5, 6, 7]
    print("Already sorted array:", arr4)
    arr4_copy = arr4.copy()
    quick_sort_randomized(arr4_copy)  # Randomized handles this better
    print("After randomized quick sort:", arr4_copy)

