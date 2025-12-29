"""
Binary Search in Rotated Sorted Array

Search for target in a rotated sorted array.

Problem Statement:
-------------------
Given a rotated sorted array (e.g., [4,5,6,7,0,1,2] from [0,1,2,4,5,6,7]),
find target in O(log n) time.

Why Rotated Array?
------------------
- Common interview problem
- Tests understanding of binary search
- Requires identifying sorted portion
- Real-world scenario (circular buffers)

Useful in:
- Rotated array problems
- Common interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Search in Rotated Array (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def search_rotated_array(arr: List[int], target: int) -> Optional[int]:
    """
    Search target in rotated sorted array.

    Algorithm:
    1. Find which half is sorted
    2. Check if target is in sorted half
    3. If yes, search in sorted half
    4. If no, search in other half

    Args:
        arr (List[int]): Rotated sorted array
        target (int): Target value

    Returns:
        Optional[int]: Index if found, None otherwise

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(1)    - Only uses variables.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return None


# ----------------------------------------------------------------------
# Find Minimum in Rotated Array
# ----------------------------------------------------------------------
def find_min_rotated(arr: List[int]) -> int:
    """
    Find minimum element in rotated sorted array.

    Args:
        arr (List[int]): Rotated sorted array (no duplicates)

    Returns:
        int: Minimum element

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(1)    - Only uses variables.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Right half is unsorted, minimum is here
        if arr[mid] > arr[right]:
            left = mid + 1
        # Left half is unsorted or both sorted
        else:
            right = mid
    
    return arr[left]


# ----------------------------------------------------------------------
# Search with Duplicates
# ----------------------------------------------------------------------
def search_rotated_with_duplicates(arr: List[int], target: int) -> bool:
    """
    Search target in rotated sorted array with duplicates.

    Args:
        arr (List[int]): Rotated sorted array (may have duplicates)
        target (int): Target value

    Returns:
        bool: True if found, False otherwise

    Complexity:
        Time: O(n) worst case  - When many duplicates, may need linear scan.
        Space: O(1)           - Only uses variables.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return True
        
        # Handle duplicates
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
        # Left half is sorted
        elif arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Binary Search in Rotated Array Demonstration")
    
    # Rotated array: [4,5,6,7,0,1,2] (rotated from [0,1,2,4,5,6,7])
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    
    print(f"Rotated array: {arr}")
    print(f"Target: {target}")
    
    index = search_rotated_array(arr, target)
    print(f"Found at index: {index}")
    
    # Find minimum
    print("\n" + "="*50)
    min_val = find_min_rotated(arr)
    print(f"Minimum element: {min_val}")
    
    # With duplicates
    print("\n" + "="*50)
    arr2 = [2, 5, 6, 0, 0, 1, 2]
    target2 = 0
    print(f"Array with duplicates: {arr2}, Target: {target2}")
    found = search_rotated_with_duplicates(arr2, target2)
    print(f"Found: {found}")

