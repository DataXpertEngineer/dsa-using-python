"""
Iterative Binary Search

Binary search is an efficient algorithm for finding an element in a sorted array
by repeatedly dividing the search interval in half.

Why Binary Search?
------------------
- O(log n) time complexity
- Much faster than linear search O(n)
- Works only on sorted arrays
- Fundamental algorithm

Useful in:
- Searching in sorted arrays
- Finding insertion points
- Range queries
- Common interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Binary Search - Basic (Language-agnostic)
# ----------------------------------------------------------------------
def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Find target in sorted array using iterative binary search.

    Algorithm:
    1. Set left = 0, right = n - 1
    2. While left <= right:
       - Calculate mid = (left + right) // 2
       - If arr[mid] == target, return mid
       - If arr[mid] < target, search right half
       - If arr[mid] > target, search left half
    3. Return -1 if not found

    Args:
        arr (List[int]): Sorted array
        target (int): Target value to find

    Returns:
        Optional[int]: Index of target if found, None otherwise

    Complexity:
        Time: O(log n)  - Each iteration eliminates half the search space.
        Space: O(1)    - Only uses variables.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None


# ----------------------------------------------------------------------
# Binary Search - Find First Occurrence
# ----------------------------------------------------------------------
def binary_search_first(arr: List[int], target: int) -> int:
    """
    Find first occurrence of target in sorted array (may have duplicates).

    Args:
        arr (List[int]): Sorted array
        target (int): Target value

    Returns:
        int: Index of first occurrence, -1 if not found

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(1)    - Only uses variables.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# ----------------------------------------------------------------------
# Binary Search - Find Last Occurrence
# ----------------------------------------------------------------------
def binary_search_last(arr: List[int], target: int) -> int:
    """
    Find last occurrence of target in sorted array (may have duplicates).

    Args:
        arr (List[int]): Sorted array
        target (int): Target value

    Returns:
        int: Index of last occurrence, -1 if not found

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(1)    - Only uses variables.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# ----------------------------------------------------------------------
# Binary Search - Find Insertion Point
# ----------------------------------------------------------------------
def binary_search_insertion_point(arr: List[int], target: int) -> int:
    """
    Find insertion point to maintain sorted order.

    Returns index where target should be inserted.

    Args:
        arr (List[int]): Sorted array
        target (int): Target value

    Returns:
        int: Insertion index

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(1)    - Only uses variables.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Iterative Binary Search Demonstration")
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    
    print(f"Array: {arr}")
    print(f"Target: {target}")
    
    index = binary_search(arr, target)
    print(f"Found at index: {index}")
    
    # First occurrence
    print("\n" + "="*50)
    arr2 = [1, 2, 2, 2, 3, 4, 5]
    target2 = 2
    print(f"Array: {arr2}, Target: {target2}")
    first = binary_search_first(arr2, target2)
    print(f"First occurrence at index: {first}")
    
    # Last occurrence
    last = binary_search_last(arr2, target2)
    print(f"Last occurrence at index: {last}")
    
    # Insertion point
    print("\n" + "="*50)
    arr3 = [1, 3, 5, 6]
    target3 = 4
    print(f"Array: {arr3}, Target: {target3}")
    insert_idx = binary_search_insertion_point(arr3, target3)
    print(f"Insertion point: {insert_idx}")

