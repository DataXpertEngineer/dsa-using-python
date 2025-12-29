"""
Recursive Binary Search

Recursive implementation of binary search using function calls.

Why Recursive?
--------------
- Cleaner code structure
- Natural for divide-and-conquer
- Easier to understand
- Same time complexity

Disadvantages:
- Uses O(log n) stack space
- Slightly slower due to function call overhead

Useful in:
- Learning binary search
- Divide-and-conquer problems
- Common interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Binary Search - Recursive (Language-agnostic)
# ----------------------------------------------------------------------
def binary_search_recursive(arr: List[int], target: int, 
                           left: int = 0, right: int = None) -> Optional[int]:
    """
    Find target in sorted array using recursive binary search.

    Args:
        arr (List[int]): Sorted array
        target (int): Target value
        left (int): Left boundary
        right (int): Right boundary

    Returns:
        Optional[int]: Index of target if found, None otherwise

    Complexity:
        Time: O(log n)  - Each recursion eliminates half the search space.
        Space: O(log n) - Recursion stack depth.
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case
    if left > right:
        return None
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ----------------------------------------------------------------------
# Binary Search - Recursive Helper Pattern
# ----------------------------------------------------------------------
def binary_search_recursive_helper(arr: List[int], target: int) -> Optional[int]:
    """
    Wrapper function for recursive binary search.

    Args:
        arr (List[int]): Sorted array
        target (int): Target value

    Returns:
        Optional[int]: Index of target if found, None otherwise

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(log n) - Recursion stack.
    """
    def search(left: int, right: int) -> Optional[int]:
        if left > right:
            return None
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)
    
    return search(0, len(arr) - 1)


# ----------------------------------------------------------------------
# Binary Search - Find Range
# ----------------------------------------------------------------------
def binary_search_range(arr: List[int], target: int) -> List[int]:
    """
    Find range of target in sorted array (first and last occurrence).

    Args:
        arr (List[int]): Sorted array
        target (int): Target value

    Returns:
        List[int]: [first_index, last_index] or [-1, -1] if not found

    Complexity:
        Time: O(log n)  - Two binary searches.
        Space: O(log n) - Recursion stack.
    """
    def find_first(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            return find_first(left, mid - 1)
        elif arr[mid] < target:
            return find_first(mid + 1, right)
        else:
            return find_first(left, mid - 1)
    
    def find_last(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            return find_last(mid + 1, right)
        elif arr[mid] < target:
            return find_last(mid + 1, right)
        else:
            return find_last(left, mid - 1)
    
    first = find_first(0, len(arr) - 1)
    if first == -1:
        return [-1, -1]
    
    last = find_last(0, len(arr) - 1)
    return [first, last]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Recursive Binary Search Demonstration")
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    
    print(f"Array: {arr}")
    print(f"Target: {target}")
    
    index = binary_search_recursive(arr, target)
    print(f"Found at index: {index}")
    
    # Using helper pattern
    print("\n" + "="*50)
    index2 = binary_search_recursive_helper(arr, target)
    print(f"Found at index (helper): {index2}")
    
    # Find range
    print("\n" + "="*50)
    arr3 = [1, 2, 2, 2, 3, 4, 5]
    target3 = 2
    print(f"Array: {arr3}, Target: {target3}")
    range_result = binary_search_range(arr3, target3)
    print(f"Range: {range_result}")

