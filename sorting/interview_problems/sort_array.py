"""
Sort Array Problem

General array sorting problem with different approaches.

Problem Statement:
-------------------
Given an array of integers, sort it in ascending order.

Example:
    Input: [5, 2, 3, 1]
    Output: [1, 2, 3, 5]

Why Different Approaches?
-------------------------
- Different algorithms for different scenarios
- Trade-offs between time, space, and stability
- Choose based on requirements

Useful in:
- Fundamental sorting problem
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Sort Array - Built-in (Python)
# ----------------------------------------------------------------------
def sort_array_builtin(arr: List[int]) -> List[int]:
    """
    Sort array using Python's built-in sort.

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n log n)  - Timsort algorithm.
        Space: O(n)      - Temporary storage.
    """
    return sorted(arr)


# ----------------------------------------------------------------------
# Sort Array - In-place
# ----------------------------------------------------------------------
def sort_array_inplace(arr: List[int]) -> None:
    """
    Sort array in-place using built-in sort.

    Args:
        arr (List[int]): Input array (modified in-place)

    Complexity:
        Time: O(n log n)  - Timsort algorithm.
        Space: O(1)      - In-place sorting.
    """
    arr.sort()


# ----------------------------------------------------------------------
# Sort Array - Custom Comparator
# ----------------------------------------------------------------------
def sort_array_custom(arr: List[int], reverse: bool = False) -> List[int]:
    """
    Sort array with custom order.

    Args:
        arr (List[int]): Input array
        reverse (bool): True for descending, False for ascending

    Returns:
        List[int]: Sorted array

    Complexity:
        Time: O(n log n)  - Sorting.
        Space: O(n)      - Creates new array.
    """
    return sorted(arr, reverse=reverse)


# ----------------------------------------------------------------------
# Sort Array - With Key Function
# ----------------------------------------------------------------------
def sort_array_by_abs(arr: List[int]) -> List[int]:
    """
    Sort array by absolute value.

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Sorted by absolute value

    Complexity:
        Time: O(n log n)  - Sorting.
        Space: O(n)      - Creates new array.
    """
    return sorted(arr, key=abs)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sort Array Demonstration")
    
    arr = [5, 2, 3, 1]
    print(f"Original array: {arr}")
    
    sorted_arr = sort_array_builtin(arr)
    print(f"Sorted: {sorted_arr}")
    
    # In-place
    print("\n" + "="*50)
    arr2 = [5, 2, 3, 1]
    print(f"Original: {arr2}")
    sort_array_inplace(arr2)
    print(f"After in-place sort: {arr2}")
    
    # Custom order
    print("\n" + "="*50)
    arr3 = [5, 2, 3, 1]
    print(f"Original: {arr3}")
    sorted_desc = sort_array_custom(arr3, reverse=True)
    print(f"Descending: {sorted_desc}")
    
    # By absolute value
    print("\n" + "="*50)
    arr4 = [-4, 2, -1, 3, -5]
    print(f"Original: {arr4}")
    sorted_abs = sort_array_by_abs(arr4)
    print(f"Sorted by absolute value: {sorted_abs}")

