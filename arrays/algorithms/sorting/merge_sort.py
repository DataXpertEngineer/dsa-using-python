"""
Merge Sort Algorithm

Merge sort is a divide-and-conquer sorting algorithm that divides the array
into two halves, sorts them recursively, and then merges the sorted halves.

The algorithm:
1. Divide: Split array into two halves
2. Conquer: Recursively sort both halves
3. Combine: Merge the two sorted halves

Why Merge Sort?
---------------
Advantages:
    - Guaranteed O(n log n) time complexity
    - Stable sort (maintains relative order of equal elements)
    - Predictable performance (no worst-case scenarios)
    - Good for linked lists

Disadvantages:
    - Requires O(n) extra space
    - Not in-place (needs temporary arrays)
    - Slower than quick sort in practice for arrays

Useful in:
- When stable sorting is required
- External sorting (sorting data too large for memory)
- Linked list sorting
- When worst-case O(n log n) is important
"""

from typing import List


# ----------------------------------------------------------------------
# Merge Sort (Top-down)
# ----------------------------------------------------------------------
def merge_sort(arr: List[int], left: int = 0, right: int = None) -> None:
    """
    Sort array in-place using merge sort algorithm (top-down approach).

    Args:
        arr (List[int]): Input array to be sorted (modified in-place)
        left (int): Left boundary of subarray (default: 0)
        right (int): Right boundary of subarray (default: len(arr) - 1)

    Returns:
        None: Array is sorted in-place

    Complexity:
        Time: O(n log n)    - Divides array log n times, merges n elements each time.
        Space: O(n)         - Requires temporary array for merging.
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = left + (right - left) // 2
        
        # Recursively sort both halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge the sorted halves
        _merge(arr, left, mid, right)


def _merge(arr: List[int], left: int, mid: int, right: int) -> None:
    """
    Merge two sorted subarrays arr[left:mid+1] and arr[mid+1:right+1].

    Args:
        arr (List[int]): Array containing subarrays to merge
        left (int): Start index of first subarray
        mid (int): End index of first subarray
        right (int): End index of second subarray

    Returns:
        None: Merges in-place
    """
    # Create temporary arrays for left and right subarrays
    n1 = mid - left + 1
    n2 = right - mid
    
    left_arr = [0] * n1
    right_arr = [0] * n2
    
    # Copy data to temporary arrays
    for i in range(n1):
        left_arr[i] = arr[left + i]
    for j in range(n2):
        right_arr[j] = arr[mid + 1 + j]
    
    # Merge the temporary arrays back into arr[left:right+1]
    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = left  # Initial index of merged subarray
    
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr, if any
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_arr, if any
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


# ----------------------------------------------------------------------
# Merge Sort (Returns new sorted array)
# ----------------------------------------------------------------------
def merge_sort_copy(arr: List[int]) -> List[int]:
    """
    Sort array and return a new sorted array (original unchanged).

    Args:
        arr (List[int]): Input array (not modified)

    Returns:
        List[int]: New sorted array

    Complexity:
        Time: O(n log n)    - Same as in-place version.
        Space: O(n)        - Creates copies during merge process.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_copy(arr[:mid])
    right = merge_sort_copy(arr[mid:])
    
    return _merge_sorted_arrays(left, right)


def _merge_sorted_arrays(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array.

    Args:
        left (List[int]): First sorted array
        right (List[int]): Second sorted array

    Returns:
        List[int]: Merged sorted array
    """
    result = []
    i = j = 0
    
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
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Merge Sort Demonstration")
    
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr1)
    merge_sort(arr1)
    print("Sorted array (in-place):", arr1)
    
    # Test with copy version
    print("\n" + "="*50)
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr2)
    sorted_arr = merge_sort_copy(arr2)
    print("Original array (unchanged):", arr2)
    print("New sorted array:", sorted_arr)
    
    # Test with already sorted array
    print("\n" + "="*50)
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    print("Already sorted array:", arr3)
    merge_sort(arr3)
    print("After merge sort:", arr3)
    
    # Test with reverse sorted array
    print("\n" + "="*50)
    arr4 = [7, 6, 5, 4, 3, 2, 1]
    print("Reverse sorted array:", arr4)
    merge_sort(arr4)
    print("After merge sort:", arr4)

