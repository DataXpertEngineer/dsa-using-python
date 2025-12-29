"""
Count Inversions Using Merge Sort

Count number of inversions in an array using modified merge sort.

Problem Statement:
-------------------
Given an array, count the number of inversions. An inversion is a pair
(i, j) where i < j and arr[i] > arr[j].

Example:
    Input: [2, 4, 1, 3, 5]
    Output: 3
    Inversions: (2,1), (4,1), (4,3)

Why Merge Sort?
---------------
- Merge sort naturally counts inversions during merge
- O(n log n) solution instead of O(n²) brute force
- Efficient and elegant

Useful in:
- Inversion counting
- Common interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Count Inversions (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def count_inversions(arr: List[int]) -> int:
    """
    Count inversions using modified merge sort.

    Algorithm:
    1. Divide array into two halves
    2. Recursively count inversions in each half
    3. Count inversions during merge
    4. Return total count

    Args:
        arr (List[int]): Input array

    Returns:
        int: Number of inversions

    Complexity:
        Time: O(n log n)  - Modified merge sort.
        Space: O(n)      - Temporary arrays for merging.
    """
    def merge_and_count(arr: List[int], left: int, mid: int, right: int) -> int:
        """Merge two halves and count inversions."""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i, j, k = 0, 0, left
        inversions = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                # All remaining elements in left_arr are inversions
                inversions += len(left_arr) - i
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
        
        return inversions
    
    def merge_sort_and_count(arr: List[int], left: int, right: int) -> int:
        """Merge sort with inversion counting."""
        inversions = 0
        
        if left < right:
            mid = (left + right) // 2
            
            # Count inversions in left and right halves
            inversions += merge_sort_and_count(arr, left, mid)
            inversions += merge_sort_and_count(arr, mid + 1, right)
            
            # Count inversions during merge
            inversions += merge_and_count(arr, left, mid, right)
        
        return inversions
    
    arr_copy = arr.copy()
    return merge_sort_and_count(arr_copy, 0, len(arr_copy) - 1)


# ----------------------------------------------------------------------
# Count Inversions (Brute Force)
# ----------------------------------------------------------------------
def count_inversions_bruteforce(arr: List[int]) -> int:
    """
    Count inversions using brute force approach.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Number of inversions

    Complexity:
        Time: O(n²)     - Check all pairs.
        Space: O(1)    - Only uses counter.
    """
    inversions = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    
    return inversions


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Count Inversions Demonstration")
    
    arr = [2, 4, 1, 3, 5]
    print(f"Array: {arr}")
    
    inversions = count_inversions(arr)
    print(f"Number of inversions: {inversions}")
    print("Inversions: (2,1), (4,1), (4,3)")
    
    # Compare with brute force
    print("\n" + "="*50)
    inversions_bf = count_inversions_bruteforce(arr)
    print(f"Brute force result: {inversions_bf}")
    print(f"Results match: {inversions == inversions_bf}")

