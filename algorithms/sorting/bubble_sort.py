"""
Bubble Sort Algorithm

Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements, and swaps them if they are in the wrong order.
The pass through the list is repeated until no swaps are needed.

The algorithm:
1. Compare adjacent elements
2. Swap if they are in wrong order
3. Repeat for all pairs
4. Continue until no swaps occur in a complete pass

Why Bubble Sort?
----------------
Advantages:
    - Simple to understand and implement
    - In-place sorting (O(1) extra space)
    - Stable sort (maintains relative order of equal elements)

Disadvantages:
    - Very slow: O(n²) time complexity
    - Not practical for large datasets
    - Many unnecessary comparisons

Useful in:
- Educational purposes
- Small datasets
- When simplicity is more important than efficiency
"""

from typing import List


# ----------------------------------------------------------------------
# Basic Bubble Sort
# ----------------------------------------------------------------------
def bubble_sort(arr: List[int]) -> None:
    """
    Sort array in-place using bubble sort algorithm.

    Args:
        arr (List[int]): Input array to be sorted (modified in-place)

    Returns:
        None: Array is sorted in-place

    Complexity:
        Time: O(n²)    - Nested loops: outer loop n times, inner loop up to n times.
        Space: O(1)    - Only uses a temporary variable for swapping.
    """
    n = len(arr)
    
    for i in range(n):
        # Flag to check if any swap occurred
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break


# ----------------------------------------------------------------------
# Optimized Bubble Sort (with early termination)
# ----------------------------------------------------------------------
def bubble_sort_optimized(arr: List[int]) -> None:
    """
    Sort array in-place using optimized bubble sort with early termination.

    This version stops early if no swaps occur in a pass, indicating
    the array is already sorted.

    Args:
        arr (List[int]): Input array to be sorted (modified in-place)

    Returns:
        None: Array is sorted in-place

    Complexity:
        Time: O(n²) worst case, O(n) best case (already sorted)
        Space: O(1)    - Only uses a temporary variable for swapping.
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


# ----------------------------------------------------------------------
# Bubble Sort (Returns new sorted array)
# ----------------------------------------------------------------------
def bubble_sort_copy(arr: List[int]) -> List[int]:
    """
    Sort array and return a new sorted array (original unchanged).

    Args:
        arr (List[int]): Input array (not modified)

    Returns:
        List[int]: New sorted array

    Complexity:
        Time: O(n²)    - Same as in-place version.
        Space: O(n)    - Creates a copy of the input array.
    """
    sorted_arr = arr.copy()
    bubble_sort(sorted_arr)
    return sorted_arr


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Bubble Sort Demonstration")
    
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr1)
    bubble_sort(arr1)
    print("Sorted array (in-place):", arr1)
    
    # Test with already sorted array (best case)
    print("\n" + "="*50)
    arr2 = [1, 2, 3, 4, 5]
    print("Already sorted array:", arr2)
    bubble_sort_optimized(arr2)
    print("After bubble sort:", arr2)
    
    # Test with copy version
    print("\n" + "="*50)
    arr3 = [5, 2, 8, 1, 9, 3]
    print("Original array:", arr3)
    sorted_arr = bubble_sort_copy(arr3)
    print("Original array (unchanged):", arr3)
    print("New sorted array:", sorted_arr)
    
    # Test with reverse sorted array (worst case)
    print("\n" + "="*50)
    arr4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Reverse sorted array:", arr4)
    bubble_sort(arr4)
    print("After bubble sort:", arr4)

