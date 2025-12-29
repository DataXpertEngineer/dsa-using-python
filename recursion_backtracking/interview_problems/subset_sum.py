"""
Subset Sum Problem

Find if there exists a subset that sums to target using backtracking.

Problem Statement:
-------------------
Given an array of integers and a target sum, determine if there exists
a subset whose elements sum to the target.

Example:
    Input: [3, 34, 4, 12, 5, 2], target = 9
    Output: True (subset [4, 5] sums to 9)

Why Backtracking?
-----------------
- For each element, choose to include or exclude
- Recurse with remaining target
- If target == 0, solution found
- If target < 0 or no elements left, backtrack
- Systematic exploration

Useful in:
- Subset problems
- Sum problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Subset Sum - Existence Check (Language-agnostic)
# ----------------------------------------------------------------------
def subset_sum(nums: List[int], target: int) -> bool:
    """
    Check if subset exists that sums to target.

    Algorithm:
    1. For each element, choose to include or exclude
    2. Recurse with remaining target
    3. If target == 0, return True
    4. If target < 0 or no elements, return False
    5. Backtrack after exploring both choices

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        bool: True if subset exists, False otherwise

    Complexity:
        Time: O(2^n)     - Explores all subsets.
        Space: O(n)     - Recursion depth.
    """
    def backtrack(index: int, remaining: int) -> bool:
        """Backtrack to find subset sum."""
        # Base case: target reached
        if remaining == 0:
            return True
        
        # Base case: no elements left or target exceeded
        if index >= len(nums) or remaining < 0:
            return False
        
        # Choice 1: Include current element
        if backtrack(index + 1, remaining - nums[index]):
            return True
        
        # Choice 2: Exclude current element
        return backtrack(index + 1, remaining)
    
    return backtrack(0, target)


# ----------------------------------------------------------------------
# Subset Sum - Find All Subsets
# ----------------------------------------------------------------------
def subset_sum_all(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all subsets that sum to target.

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        List[List[int]]: List of all subsets that sum to target

    Complexity:
        Time: O(2^n)     - Explores all subsets.
        Space: O(n)     - Recursion depth + subset storage.
    """
    subsets: List[List[int]] = []
    
    def backtrack(current: List[int], index: int, remaining: int) -> None:
        if remaining == 0:
            subsets.append(current.copy())
            return
        
        if index >= len(nums) or remaining < 0:
            return
        
        # Include current element
        current.append(nums[index])
        backtrack(current, index + 1, remaining - nums[index])
        current.pop()
        
        # Exclude current element
        backtrack(current, index + 1, remaining)
    
    backtrack([], 0, target)
    return subsets


# ----------------------------------------------------------------------
# Subset Sum - Dynamic Programming (Optimized)
# ----------------------------------------------------------------------
def subset_sum_dp(nums: List[int], target: int) -> bool:
    """
    Check subset sum using dynamic programming (optimized).

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        bool: True if subset exists

    Complexity:
        Time: O(n * target)  - Fill DP table.
        Space: O(target)     - DP array.
    """
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Subset Sum Problem Demonstration")
    
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(f"Array: {nums}, Target: {target}")
    
    exists = subset_sum(nums, target)
    print(f"Subset exists: {exists}")
    
    # Find all subsets
    print("\n" + "="*50)
    all_subsets = subset_sum_all(nums, target)
    print(f"All subsets that sum to {target}: {all_subsets}")
    
    # DP approach
    print("\n" + "="*50)
    exists_dp = subset_sum_dp(nums, target)
    print(f"DP approach: {exists_dp}")

