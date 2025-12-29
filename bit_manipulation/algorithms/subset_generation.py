"""
Subset Generation Using Bitmasking

Generate all subsets of an array using bitmasking technique.

Why Bitmasking for Subsets?
---------------------------
Without bitmasking:
    Recursive approach = O(2^n) time and space
With bitmasking:
    Iterative approach = O(n * 2^n) time, O(n * 2^n) space
    More intuitive and easier to understand

Useful in:
- Combinatorial problems
- Power set generation
- Subset sum problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Generate All Subsets (Language-agnostic)
# ----------------------------------------------------------------------
def generate_subsets(arr: List[int]) -> List[List[int]]:
    """
    Generate all subsets using bitmasking.

    Algorithm:
    For each number from 0 to 2^n - 1, use its binary representation
    as a mask to select elements from array.

    Args:
        arr (List[int]): Input array

    Returns:
        List[List[int]]: List of all subsets (including empty set)

    Complexity:
        Time: O(n * 2^n)  - For each of 2^n masks, process n elements.
        Space: O(n * 2^n) - Stores all subsets.
    """
    n = len(arr)
    subsets = []
    
    # Generate all possible masks (0 to 2^n - 1)
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        subsets.append(subset)
    
    return subsets


# ----------------------------------------------------------------------
# Generate Subsets of Specific Size
# ----------------------------------------------------------------------
def generate_subsets_size_k(arr: List[int], k: int) -> List[List[int]]:
    """
    Generate all subsets of size k using bitmasking.

    Args:
        arr (List[int]): Input array
        k (int): Size of subsets

    Returns:
        List[List[int]]: List of all subsets of size k

    Complexity:
        Time: O(n * 2^n)  - Checks all masks, filters by size.
        Space: O(C(n,k) * k) - Stores subsets of size k.
    """
    # Count set bits using Kernighan's algorithm
    def count_bits(mask):
        count = 0
        while mask:
            mask &= mask - 1
            count += 1
        return count
    
    n = len(arr)
    subsets = []
    
    for mask in range(1 << n):
        if count_bits(mask) == k:
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(arr[i])
            subsets.append(subset)
    
    return subsets


# ----------------------------------------------------------------------
# Generate Subsets with Condition
# ----------------------------------------------------------------------
def generate_subsets_condition(arr: List[int], condition_func) -> List[List[int]]:
    """
    Generate subsets that satisfy a condition.

    Args:
        arr (List[int]): Input array
        condition_func: Function that takes subset and returns bool

    Returns:
        List[List[int]]: List of subsets satisfying condition

    Complexity:
        Time: O(n * 2^n)  - Generates all subsets and filters.
        Space: O(n * 2^n) - Stores filtered subsets.
    """
    all_subsets = generate_subsets(arr)
    return [subset for subset in all_subsets if condition_func(subset)]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Subset Generation Using Bitmasking Demonstration")
    
    arr = [1, 2, 3]
    print(f"Array: {arr}")
    
    subsets = generate_subsets(arr)
    print(f"\nAll subsets: {subsets}")
    print(f"Total subsets: {len(subsets)} (expected: 2^3 = 8)")
    
    # Subsets of size 2
    subsets_k = generate_subsets_size_k(arr, 2)
    print(f"\nSubsets of size 2: {subsets_k}")
    print(f"Total: {len(subsets_k)} (expected: C(3,2) = 3)")

