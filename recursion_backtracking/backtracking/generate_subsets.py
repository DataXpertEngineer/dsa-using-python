"""
Generate All Subsets

Generate all possible subsets of a set using backtracking.

Problem Statement:
-------------------
Given a set of distinct integers, return all possible subsets (power set).

Example:
    Input: [1, 2, 3]
    Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

Why Backtracking?
-----------------
- For each element, choose to include or exclude
- Build subset incrementally
- Backtrack after exploring both choices
- Systematic exploration of all possibilities

Useful in:
- Subset generation
- Combinatorial problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Generate All Subsets (Language-agnostic)
# ----------------------------------------------------------------------
def generate_subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using backtracking.

    Algorithm:
    1. For each element, choose to include or exclude
    2. Recurse with next element
    3. Add current subset when all elements processed
    4. Backtrack by removing last element

    Args:
        nums (List[int]): Input set

    Returns:
        List[List[int]]: List of all subsets

    Complexity:
        Time: O(2^n)    - 2^n subsets, each takes O(n) to copy.
        Space: O(n)    - Recursion depth + subset storage.
    """
    subsets: List[List[int]] = []
    
    def backtrack(current: List[int], index: int) -> None:
        """Backtrack to generate all subsets."""
        # Base case: processed all elements
        if index == len(nums):
            subsets.append(current.copy())
            return
        
        # Choice 1: Include current element
        current.append(nums[index])
        backtrack(current, index + 1)
        
        # Backtrack: exclude current element
        current.pop()
        backtrack(current, index + 1)
    
    backtrack([], 0)
    return subsets


# ----------------------------------------------------------------------
# Generate Subsets (Iterative)
# ----------------------------------------------------------------------
def generate_subsets_iterative(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using iterative approach.

    Args:
        nums (List[int]): Input set

    Returns:
        List[List[int]]: List of all subsets

    Complexity:
        Time: O(2^n * n)  - 2^n subsets, each takes O(n) to create.
        Space: O(2^n * n) - Stores all subsets.
    """
    subsets = [[]]
    
    for num in nums:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])
        subsets.extend(new_subsets)
    
    return subsets


# ----------------------------------------------------------------------
# Generate Subsets of Size K
# ----------------------------------------------------------------------
def generate_subsets_size_k(nums: List[int], k: int) -> List[List[int]]:
    """
    Generate all subsets of size k.

    Args:
        nums (List[int]): Input set
        k (int): Size of subsets

    Returns:
        List[List[int]]: List of all subsets of size k

    Complexity:
        Time: O(C(n,k) * k)  - C(n,k) combinations, each takes O(k).
        Space: O(k)         - Recursion depth.
    """
    subsets: List[List[int]] = []
    
    def backtrack(current: List[int], index: int) -> None:
        # Base case: subset of size k found
        if len(current) == k:
            subsets.append(current.copy())
            return
        
        # Not enough elements remaining
        if len(current) + len(nums) - index < k:
            return
        
        # Include current element
        current.append(nums[index])
        backtrack(current, index + 1)
        
        # Exclude current element
        current.pop()
        backtrack(current, index + 1)
    
    backtrack([], 0)
    return subsets


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Generate All Subsets Demonstration")
    
    nums = [1, 2, 3]
    print(f"Input set: {nums}")
    
    subsets = generate_subsets(nums)
    print(f"All subsets: {subsets}")
    print(f"Total subsets: {len(subsets)} (expected: 2^3 = 8)")
    
    # Iterative approach
    print("\n" + "="*50)
    subsets_iter = generate_subsets_iterative(nums)
    print(f"Iterative approach: {subsets_iter}")
    print(f"Results match: {subsets == subsets_iter}")
    
    # Subsets of size k
    print("\n" + "="*50)
    k = 2
    subsets_k = generate_subsets_size_k(nums, k)
    print(f"Subsets of size {k}: {subsets_k}")

