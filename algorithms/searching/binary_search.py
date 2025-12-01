"""
Binary Search Algorithm

Binary search is an efficient searching algorithm that works on **sorted arrays**.
It repeatedly divides the search space in half by comparing the target with
the middle element.

The algorithm:
1. Compare target with middle element
2. If equal, return the index
3. If target is smaller, search left half
4. If target is larger, search right half
5. Repeat until found or search space is exhausted

Why Binary Search?
------------------
Without binary search (linear search):
    Time complexity = O(n)
With binary search:
    Time complexity = O(log n)

The key requirement: Array must be sorted!

Useful in:
- Sorted arrays or sorted data structures
- Finding insertion points
- Range queries on sorted data
- Optimization problems with monotonic properties
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Iterative Binary Search
# ----------------------------------------------------------------------
def binary_search_iterative(arr: List[int], target: int) -> int:
    """
    Search for target in sorted array using iterative binary search.

    Args:
        arr (List[int]): Input array (must be sorted in ascending order)
        target (int): Element to search for

    Returns:
        int: Index of target if found, -1 otherwise

    Complexity (on sorted array):
        Time: O(log n)    - Each iteration eliminates half of remaining elements.
        Space: O(1)      - Only uses variables for left, right, and mid indices.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# ----------------------------------------------------------------------
# Recursive Binary Search
# ----------------------------------------------------------------------
def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: Optional[int] = None) -> int:
    """
    Search for target in sorted array using recursive binary search.

    Args:
        arr (List[int]): Input array (must be sorted in ascending order)
        target (int): Element to search for
        left (int): Left boundary of search space (default: 0)
        right (Optional[int]): Right boundary of search space (default: len(arr) - 1)

    Returns:
        int: Index of target if found, -1 otherwise

    Complexity (on sorted array):
        Time: O(log n)    - Each recursive call eliminates half of remaining elements.
        Space: O(log n)  - Recursion stack depth is log n in worst case.
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ----------------------------------------------------------------------
# Binary Search Variants
# ----------------------------------------------------------------------
def find_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find the first occurrence of target in sorted array (may have duplicates).

    Args:
        arr (List[int]): Input array (must be sorted in ascending order)
        target (int): Element to search for

    Returns:
        int: Index of first occurrence if found, -1 otherwise

    Complexity (on sorted array):
        Time: O(log n)    - Binary search with additional check for first occurrence.
        Space: O(1)      - Only uses variables for indices.
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_occurrence(arr: List[int], target: int) -> int:
    """
    Find the last occurrence of target in sorted array (may have duplicates).

    Args:
        arr (List[int]): Input array (must be sorted in ascending order)
        target (int): Element to search for

    Returns:
        int: Index of last occurrence if found, -1 otherwise

    Complexity (on sorted array):
        Time: O(log n)    - Binary search with additional check for last occurrence.
        Space: O(1)      - Only uses variables for indices.
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right for later occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_insertion_point(arr: List[int], target: int) -> int:
    """
    Find the insertion point for target in sorted array (where target should be inserted).

    Args:
        arr (List[int]): Input array (must be sorted in ascending order)
        target (int): Element to find insertion point for

    Returns:
        int: Index where target should be inserted to maintain sorted order

    Complexity (on sorted array):
        Time: O(log n)    - Binary search to find the correct position.
        Space: O(1)      - Only uses variables for indices.
    """
    left = 0
    right = len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Binary Search Demonstration")
    
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
    target = 40
    print("Sorted array:", arr)
    print("Target:", target)
    
    # Iterative binary search
    result = binary_search_iterative(arr, target)
    print(f"\nIterative Binary Search: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
    
    # Recursive binary search
    result_rec = binary_search_recursive(arr, target)
    print(f"Recursive Binary Search: {'Found at index ' + str(result_rec) if result_rec != -1 else 'Not found'}")
    
    # Search for element not in array
    target2 = 35
    result2 = binary_search_iterative(arr, target2)
    print(f"\nSearching for {target2}: {'Found at index ' + str(result2) if result2 != -1 else 'Not found'}")
    
    # Find first and last occurrence
    print("\n" + "="*50)
    arr2 = [1, 2, 2, 2, 3, 4, 4, 5, 6]
    target3 = 2
    print("Array with duplicates:", arr2)
    print("Target:", target3)
    first = find_first_occurrence(arr2, target3)
    last = find_last_occurrence(arr2, target3)
    print(f"First occurrence at index: {first}")
    print(f"Last occurrence at index: {last}")
    
    # Find insertion point
    print("\n" + "="*50)
    arr3 = [1, 3, 5, 7, 9, 11]
    target4 = 6
    print("Array:", arr3)
    print("Target to insert:", target4)
    insert_pos = find_insertion_point(arr3, target4)
    print(f"Insertion point (index): {insert_pos}")
    print(f"Array after insertion would be: {arr3[:insert_pos] + [target4] + arr3[insert_pos:]}")

