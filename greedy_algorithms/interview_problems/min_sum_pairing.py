"""
Minimum Sum Pairing

Pair elements to minimize sum of pair differences.

Problem Statement:
-------------------
Given array of numbers, pair them such that sum of absolute
differences between pairs is minimized.

Why Greedy?
-----------
- Greedy choice: Pair smallest with smallest, largest with largest
- Sort array and pair adjacent elements
- Optimal for this problem

Useful in:
- Optimization problems
- Medium difficulty interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Minimum Sum Pairing (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def min_sum_pairing(arr: List[int]) -> List[Tuple[int, int]]:
    """
    Pair elements to minimize sum of differences.

    Algorithm:
    1. Sort array
    2. Pair adjacent elements
    3. Sum of differences is minimized

    Args:
        arr (List[int]): Array of numbers

    Returns:
        List[Tuple[int, int]]: Pairs

    Complexity:
        Time: O(n log n)  - Sort array.
        Space: O(n)      - Storage for pairs.
    """
    if len(arr) % 2 != 0:
        raise ValueError("Array must have even number of elements")
    
    sorted_arr = sorted(arr)
    pairs = []
    
    for i in range(0, len(sorted_arr), 2):
        pairs.append((sorted_arr[i], sorted_arr[i + 1]))
    
    return pairs


# ----------------------------------------------------------------------
# Minimum Sum of Differences
# ----------------------------------------------------------------------
def min_sum_differences(arr: List[int]) -> int:
    """
    Calculate minimum sum of pair differences.

    Args:
        arr (List[int]): Array of numbers

    Returns:
        int: Minimum sum of differences

    Complexity:
        Time: O(n log n)  - Sort array.
        Space: O(1)      - Only uses variables.
    """
    if len(arr) % 2 != 0:
        raise ValueError("Array must have even number of elements")
    
    sorted_arr = sorted(arr)
    total = 0
    
    for i in range(0, len(sorted_arr), 2):
        total += abs(sorted_arr[i] - sorted_arr[i + 1])
    
    return total


# ----------------------------------------------------------------------
# Maximum Sum Pairing
# ----------------------------------------------------------------------
def max_sum_pairing(arr: List[int]) -> List[Tuple[int, int]]:
    """
    Pair elements to maximize sum of differences.

    Algorithm:
    1. Sort array
    2. Pair smallest with largest
    3. This maximizes sum of differences

    Args:
        arr (List[int]): Array of numbers

    Returns:
        List[Tuple[int, int]]: Pairs

    Complexity:
        Time: O(n log n)  - Sort array.
        Space: O(n)      - Storage for pairs.
    """
    if len(arr) % 2 != 0:
        raise ValueError("Array must have even number of elements")
    
    sorted_arr = sorted(arr)
    pairs = []
    n = len(sorted_arr)
    
    for i in range(n // 2):
        pairs.append((sorted_arr[i], sorted_arr[n - 1 - i]))
    
    return pairs


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Minimum Sum Pairing Demonstration")
    
    arr = [4, 2, 1, 3]
    print(f"Array: {arr}")
    
    pairs = min_sum_pairing(arr)
    print(f"Pairs (min sum): {pairs}")
    
    min_sum = min_sum_differences(arr)
    print(f"Minimum sum of differences: {min_sum}")
    
    # Maximum sum pairing
    print("\n" + "="*50)
    max_pairs = max_sum_pairing(arr)
    print(f"Pairs (max sum): {max_pairs}")
    max_sum = sum(abs(a - b) for a, b in max_pairs)
    print(f"Maximum sum of differences: {max_sum}")

