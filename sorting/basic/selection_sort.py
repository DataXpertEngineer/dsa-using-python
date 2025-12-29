"""
Selection Sort Algorithm

Selection sort finds the minimum element and places it at the beginning.
This process is repeated for the remaining unsorted portion.

Why Selection Sort?
-------------------
- Simple to understand and implement
- In-place sorting (O(1) extra space)
- Performs well on small datasets
- Makes minimum number of swaps (n swaps)

Note: Not stable, O(n²) time complexity

Useful in:
- Learning sorting fundamentals
- Small datasets
- When memory is limited
"""

from typing import List


# ----------------------------------------------------------------------
# Selection Sort (Language-agnostic)
# ----------------------------------------------------------------------
def selection_sort(arr: List[int]) -> List[int]:
    """
    Sort array using selection sort algorithm.

    Algorithm:
    1. Find minimum element in unsorted portion
    2. Swap with first element of unsorted portion
    3. Move boundary of unsorted portion one position right
    4. Repeat until array is sorted

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n²)     - Nested loops, always n² comparisons.
        Space: O(1)    - Only uses temporary variables (in-place).
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    for i in range(n):
        # Find minimum element in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum with first element of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


# ----------------------------------------------------------------------
# Selection Sort (In-place)
# ----------------------------------------------------------------------
def selection_sort_inplace(arr: List[int]) -> None:
    """
    Sort array in-place using selection sort.

    Args:
        arr (List[int]): Input array (modified in-place)

    Complexity:
        Time: O(n²)     - Always performs n² comparisons.
        Space: O(1)    - Only uses temporary variables.
    """
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# ----------------------------------------------------------------------
# Selection Sort (Recursive)
# ----------------------------------------------------------------------
def selection_sort_recursive(arr: List[int], start: int = 0) -> None:
    """
    Sort array using recursive selection sort.

    Args:
        arr (List[int]): Input array (modified in-place)
        start (int): Starting index

    Complexity:
        Time: O(n²)     - Same as iterative version.
        Space: O(n)    - Recursion stack depth.
    """
    n = len(arr)
    
    # Base case
    if start >= n - 1:
        return
    
    # Find minimum in unsorted portion
    min_idx = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    # Swap
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    
    # Recurse
    selection_sort_recursive(arr, start + 1)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Selection Sort Demonstration")
    
    arr = [64, 25, 12, 22, 11]
    print(f"Original array: {arr}")
    
    sorted_arr = selection_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # In-place
    print("\n" + "="*50)
    arr2 = [64, 25, 12, 22, 11]
    print(f"Original: {arr2}")
    selection_sort_inplace(arr2)
    print(f"After in-place sort: {arr2}")

