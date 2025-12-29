"""
Sorting Algorithms in Python

Sorting is the process of arranging data in a particular order (ascending or descending).
Understanding different sorting algorithms and their properties is crucial for efficient programming.

Core Concepts:
1. Stability: Maintains relative order of equal elements
2. In-place vs Out-of-place: Whether algorithm uses extra space
3. Comparison-based vs Non-comparison: Based on comparisons or not
4. Time Complexity: Best, average, and worst case

Why Sorting?
------------
- Fundamental operation in computer science
- Many algorithms require sorted data
- Improves search efficiency (binary search)
- Common in real-world applications

Useful in:
- Data organization
- Search optimization
- Common interview problems
"""

from typing import List, Callable, Any


# ----------------------------------------------------------------------
# Sorting Concepts Overview
# ----------------------------------------------------------------------
def is_sorted(arr: List[Any], reverse: bool = False) -> bool:
    """
    Check if array is sorted.

    Args:
        arr (List[Any]): Array to check
        reverse (bool): True for descending, False for ascending

    Returns:
        bool: True if sorted, False otherwise

    Complexity:
        Time: O(n)     - Checks each adjacent pair.
        Space: O(1)   - Only uses variables.
    """
    if reverse:
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    else:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def is_stable_sort(original: List[tuple], sorted_arr: List[tuple]) -> bool:
    """
    Check if sorting algorithm is stable.

    Stability: Equal elements maintain their relative order.

    Args:
        original (List[tuple]): Original array with (value, index) pairs
        sorted_arr (List[tuple]): Sorted array

    Returns:
        bool: True if stable, False otherwise

    Complexity:
        Time: O(n)     - Checks relative order of equal elements.
        Space: O(1)   - Only uses variables.
    """
    # Group by value
    value_groups = {}
    for val, idx in original:
        if val not in value_groups:
            value_groups[val] = []
        value_groups[val].append(idx)
    
    # Check if relative order maintained
    for val, idx in sorted_arr:
        if val in value_groups and value_groups[val]:
            if idx != value_groups[val][0]:
                return False
            value_groups[val].pop(0)
    
    return True


# ----------------------------------------------------------------------
# Sorting Properties Summary
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sorting Concepts Demonstration")
    
    # Check if sorted
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    arr3 = [1, 3, 2, 4, 5]
    
    print(f"Is {arr1} sorted? {is_sorted(arr1)}")
    print(f"Is {arr2} sorted (descending)? {is_sorted(arr2, reverse=True)}")
    print(f"Is {arr3} sorted? {is_sorted(arr3)}")
    
    # Stability check
    print("\n" + "="*60)
    print("STABILITY CONCEPT")
    print("="*60)
    print("""
Stability: A sorting algorithm is stable if it maintains the relative
order of elements with equal keys.

Example:
  Original: [(3, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
  Stable sort by first element: [(1, 'd'), (2, 'b'), (3, 'a'), (3, 'c')]
  Note: (3, 'a') comes before (3, 'c') - relative order maintained
""")
    
    print("\n" + "="*60)
    print("SORTING ALGORITHMS COMPARISON")
    print("="*60)
    print("""
Algorithm          Best      Average    Worst     Space    Stable    In-place
----------------------------------------------------------------------------
Bubble Sort        O(n)      O(n²)      O(n²)     O(1)     Yes       Yes
Selection Sort     O(n²)     O(n²)      O(n²)     O(1)     No        Yes
Insertion Sort     O(n)      O(n²)      O(n²)     O(1)     Yes       Yes
Merge Sort         O(n log n) O(n log n) O(n log n) O(n)    Yes       No
Quick Sort         O(n log n) O(n log n) O(n²)     O(log n) No        Yes
Heap Sort          O(n log n) O(n log n) O(n log n) O(1)    No        Yes

Key Terms:
- Stable: Maintains relative order of equal elements
- In-place: Uses O(1) extra space (excluding input)
- Comparison-based: Compares elements to determine order
""")

