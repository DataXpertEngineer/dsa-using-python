"""
Bubble Sort Algorithm

Bubble sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order. The pass through the list
is repeated until no swaps are needed.

Why Bubble Sort?
----------------
- Simple to understand and implement
- Good for educational purposes
- Can detect if list is already sorted (optimized version)
- In-place and stable

Note: Not efficient for large datasets (O(n²))

Useful in:
- Learning sorting fundamentals
- Small datasets
- When simplicity is preferred
"""

from typing import List


# ----------------------------------------------------------------------
# Bubble Sort (Language-agnostic)
# ----------------------------------------------------------------------
def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort array using bubble sort algorithm.

    Algorithm:
    1. Compare adjacent elements
    2. Swap if they are in wrong order
    3. Repeat for all pairs
    4. Continue until no swaps needed

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
    
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps, array is sorted
        if not swapped:
            break
    
    return arr


# ----------------------------------------------------------------------
# Bubble Sort (In-place)
# ----------------------------------------------------------------------
def bubble_sort_inplace(arr: List[int]) -> None:
    """
    Sort array in-place using bubble sort.

    Args:
        arr (List[int]): Input array (modified in-place)

    Complexity:
        Time: O(n²)     - Nested loops.
        Space: O(1)    - Only uses temporary variables.
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
# Bubble Sort (Recursive)
# ----------------------------------------------------------------------
def bubble_sort_recursive(arr: List[int], n: int = None) -> None:
    """
    Sort array using recursive bubble sort.

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
    if n == 1:
        return
    
    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recurse for remaining elements
    bubble_sort_recursive(arr, n - 1)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Bubble Sort Demonstration")
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # In-place
    print("\n" + "="*50)
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr2}")
    bubble_sort_inplace(arr2)
    print(f"After in-place sort: {arr2}")
    
    # Recursive
    print("\n" + "="*50)
    arr3 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr3}")
    bubble_sort_recursive(arr3)
    print(f"After recursive sort: {arr3}")

