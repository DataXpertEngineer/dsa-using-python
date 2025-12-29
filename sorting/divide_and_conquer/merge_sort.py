"""
Merge Sort Algorithm

Merge sort is a divide-and-conquer algorithm that divides the array into
two halves, sorts them recursively, and then merges the sorted halves.

Why Merge Sort?
---------------
- Guaranteed O(n log n) time complexity
- Stable sorting algorithm
- Predictable performance
- Good for large datasets
- Parallelizable

Disadvantages:
- Requires O(n) extra space
- Not in-place

Useful in:
- Large datasets
- When stability is required
- External sorting
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Merge Sort (Language-agnostic)
# ----------------------------------------------------------------------
def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort array using merge sort algorithm.

    Algorithm:
    1. Divide array into two halves
    2. Recursively sort both halves
    3. Merge the sorted halves

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n log n)  - Divide O(log n) levels, merge O(n) at each level.
        Space: O(n)      - Temporary arrays for merging.
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays.

    Args:
        left (List[int]): First sorted array
        right (List[int]): Second sorted array

    Returns:
        List[int]: Merged sorted array

    Complexity:
        Time: O(n + m)  - n and m are sizes of left and right.
        Space: O(n + m) - Creates merged array.
    """
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# ----------------------------------------------------------------------
# Merge Sort (In-place)
# ----------------------------------------------------------------------
def merge_sort_inplace(arr: List[int], left: int = 0, right: int = None) -> None:
    """
    Sort array in-place using merge sort.

    Args:
        arr (List[int]): Input array (modified in-place)
        left (int): Left index
        right (int): Right index

    Complexity:
        Time: O(n log n)  - Same as standard merge sort.
        Space: O(n)      - Temporary array for merging.
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        # Sort halves
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        
        # Merge
        _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr: List[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted portions in-place."""
    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i, j, k = 0, 0, left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Merge Sort Demonstration")
    
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {arr}")
    
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # In-place
    print("\n" + "="*50)
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {arr2}")
    merge_sort_inplace(arr2)
    print(f"After in-place sort: {arr2}")

