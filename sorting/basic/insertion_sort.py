"""
Insertion Sort Algorithm

Insertion sort builds the sorted array one element at a time by inserting
each element into its correct position in the already sorted portion.

Why Insertion Sort?
-------------------
- Simple to understand and implement
- Efficient for small datasets
- Stable and in-place
- Adaptive: Efficient for nearly sorted arrays (O(n))
- Online: Can sort as it receives input

Note: O(n²) worst case, but good for small arrays

Useful in:
- Small datasets
- Nearly sorted arrays
- Hybrid sorting algorithms (e.g., Timsort uses insertion sort)
"""

from typing import List


# ----------------------------------------------------------------------
# Insertion Sort (Language-agnostic)
# ----------------------------------------------------------------------
def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sort array using insertion sort algorithm.

    Algorithm:
    1. Start with second element (first is already sorted)
    2. Compare with elements in sorted portion
    3. Shift elements greater than current to the right
    4. Insert current element in correct position
    5. Repeat for all elements

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n²)     - Nested loops, n² comparisons in worst case.
        Space: O(1)    - Only uses temporary variables (in-place).
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key in correct position
        arr[j + 1] = key
    
    return arr


# ----------------------------------------------------------------------
# Insertion Sort (In-place)
# ----------------------------------------------------------------------
def insertion_sort_inplace(arr: List[int]) -> None:
    """
    Sort array in-place using insertion sort.

    Args:
        arr (List[int]): Input array (modified in-place)

    Complexity:
        Time: O(n²)     - Worst case, O(n) for nearly sorted.
        Space: O(1)    - Only uses temporary variables.
    """
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key


# ----------------------------------------------------------------------
# Insertion Sort (Recursive)
# ----------------------------------------------------------------------
def insertion_sort_recursive(arr: List[int], n: int = None) -> None:
    """
    Sort array using recursive insertion sort.

    Args:
        arr (List[int]): Input array (modified in-place)
        n (int): Size of array (defaults to len(arr))

    Complexity:
        Time: O(n²)     - Same as iterative version.
        Space: O(n)    - Recursion stack depth.
    """
    if n is None:
        n = len(arr)
    
    # Base case
    if n <= 1:
        return
    
    # Sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert last element in sorted portion
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = last


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Insertion Sort Demonstration")
    
    arr = [12, 11, 13, 5, 6]
    print(f"Original array: {arr}")
    
    sorted_arr = insertion_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # In-place
    print("\n" + "="*50)
    arr2 = [12, 11, 13, 5, 6]
    print(f"Original: {arr2}")
    insertion_sort_inplace(arr2)
    print(f"After in-place sort: {arr2}")
    
    # Nearly sorted array (best case)
    print("\n" + "="*50)
    arr3 = [1, 2, 3, 5, 4]
    print(f"Nearly sorted: {arr3}")
    insertion_sort_inplace(arr3)
    print(f"After sort: {arr3}")

