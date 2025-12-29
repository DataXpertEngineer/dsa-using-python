"""
Peak Finding Problem

Find a peak element in an array. A peak is an element that is greater than
its neighbors.

Problem Statement:
-------------------
Given array where arr[i] != arr[i+1], find any peak element.
- For edges: arr[0] > arr[1] or arr[n-1] > arr[n-2]
- For middle: arr[i] > arr[i-1] and arr[i] > arr[i+1]

Why Peak Finding?
-----------------
- Common interview problem
- Uses binary search on unsorted array
- Demonstrates binary search flexibility
- Real-world applications (signal processing)

Useful in:
- Array analysis
- Medium difficulty interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Find Peak Element (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def find_peak_element(arr: List[int]) -> Optional[int]:
    """
    Find any peak element using binary search.

    Algorithm:
    1. Check if mid is peak
    2. If arr[mid] < arr[mid+1], peak is in right half
    3. If arr[mid] < arr[mid-1], peak is in left half
    4. Otherwise, mid is peak

    Args:
        arr (List[int]): Array (arr[i] != arr[i+1])

    Returns:
        Optional[int]: Index of peak element, None if empty

    Complexity:
        Time: O(log n)  - Binary search.
        Space: O(1)    - Only uses variables.
    """
    if not arr:
        return None
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid is less than right neighbor, peak is in right half
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        # Otherwise, peak is in left half (including mid)
        else:
            right = mid
    
    return left


# ----------------------------------------------------------------------
# Find Peak Element (2D)
# ----------------------------------------------------------------------
def find_peak_2d(matrix: List[List[int]]) -> Optional[tuple]:
    """
    Find peak in 2D matrix (greedy ascent).

    Args:
        matrix (List[List[int]]): 2D matrix

    Returns:
        Optional[tuple]: (row, col) of peak, None if empty

    Complexity:
        Time: O(m log n)  - Binary search on columns, linear on rows.
        Space: O(1)      - Only uses variables.
    """
    if not matrix or not matrix[0]:
        return None
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, cols - 1
    
    while left <= right:
        mid_col = (left + right) // 2
        
        # Find max element in this column
        max_row = 0
        for i in range(rows):
            if matrix[i][mid_col] > matrix[max_row][mid_col]:
                max_row = i
        
        # Check if it's a peak
        is_peak = True
        if mid_col > 0 and matrix[max_row][mid_col] < matrix[max_row][mid_col - 1]:
            is_peak = False
            right = mid_col - 1
        elif mid_col < cols - 1 and matrix[max_row][mid_col] < matrix[max_row][mid_col + 1]:
            is_peak = False
            left = mid_col + 1
        
        if is_peak:
            return (max_row, mid_col)
    
    return None


# ----------------------------------------------------------------------
# Find All Peaks
# ----------------------------------------------------------------------
def find_all_peaks(arr: List[int]) -> List[int]:
    """
    Find all peak elements in array.

    Args:
        arr (List[int]): Array

    Returns:
        List[int]: Indices of all peaks

    Complexity:
        Time: O(n)     - Must check all elements.
        Space: O(1)   - Only uses result list.
    """
    peaks = []
    n = len(arr)
    
    # Check first element
    if n > 1 and arr[0] > arr[1]:
        peaks.append(0)
    
    # Check middle elements
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append(i)
    
    # Check last element
    if n > 1 and arr[n - 1] > arr[n - 2]:
        peaks.append(n - 1)
    
    # Single element
    if n == 1:
        peaks.append(0)
    
    return peaks


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Peak Finding Demonstration")
    
    arr = [1, 2, 3, 1]
    print(f"Array: {arr}")
    
    peak = find_peak_element(arr)
    print(f"Peak at index: {peak}, value: {arr[peak] if peak is not None else None}")
    print("Explanation: arr[2] = 3 is greater than neighbors")
    
    # All peaks
    print("\n" + "="*50)
    arr2 = [1, 3, 2, 4, 1, 5, 2]
    print(f"Array: {arr2}")
    all_peaks = find_all_peaks(arr2)
    print(f"All peaks at indices: {all_peaks}")

