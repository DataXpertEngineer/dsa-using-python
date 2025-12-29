"""
Combination Sum Problem

Find all unique combinations that sum to target using backtracking.

Problem Statement:
-------------------
Given an array of distinct integers and a target, find all unique combinations
where numbers sum to target. Same number may be used unlimited times.

Example:
    Input: candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]

Why Backtracking?
-----------------
- Try including each candidate
- Recurse with remaining target
- If target reached, save combination
- If target exceeded, backtrack
- Systematic exploration

Useful in:
- Combination problems
- Sum problems
- Medium difficulty interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Combination Sum (Language-agnostic)
# ----------------------------------------------------------------------
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target.

    Algorithm:
    1. Sort candidates
    2. Try including each candidate (can use multiple times)
    3. Recurse with remaining target
    4. If target == 0, save combination
    5. If target < 0, backtrack
    6. Skip duplicates to avoid duplicate combinations

    Args:
        candidates (List[int]): Array of distinct integers
        target (int): Target sum

    Returns:
        List[List[int]]: List of all unique combinations

    Complexity:
        Time: O(2^target) worst case  - Exponential in target value.
        Space: O(target)              - Recursion depth.
    """
    combinations: List[List[int]] = []
    candidates.sort()  # Sort to handle duplicates
    
    def backtrack(current: List[int], remaining: int, start: int) -> None:
        """Backtrack to find all combinations."""
        # Base case: target reached
        if remaining == 0:
            combinations.append(current.copy())
            return
        
        # Base case: target exceeded
        if remaining < 0:
            return
        
        # Try each candidate starting from 'start'
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # Choose
            current.append(candidates[i])
            
            # Recurse (can reuse same candidate)
            backtrack(current, remaining - candidates[i], i)
            
            # Backtrack
            current.pop()
    
    backtrack([], target, 0)
    return combinations


# ----------------------------------------------------------------------
# Combination Sum II (Each number used once)
# ----------------------------------------------------------------------
def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find combinations where each number used at most once.

    Args:
        candidates (List[int]): Array (may contain duplicates)
        target (int): Target sum

    Returns:
        List[List[int]]: List of unique combinations

    Complexity:
        Time: O(2^n)     - n is number of candidates.
        Space: O(target) - Recursion depth.
    """
    combinations: List[List[int]] = []
    candidates.sort()
    
    def backtrack(current: List[int], remaining: int, start: int) -> None:
        if remaining == 0:
            combinations.append(current.copy())
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])
            # Move to next index (can't reuse)
            backtrack(current, remaining - candidates[i], i + 1)
            current.pop()
    
    backtrack([], target, 0)
    return combinations


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Combination Sum Demonstration")
    
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Candidates: {candidates}, Target: {target}")
    
    combinations = combination_sum(candidates, target)
    print(f"Combinations: {combinations}")
    print("Explanation: [2,2,3] and [7] sum to 7")
    
    # Combination Sum II
    print("\n" + "="*50)
    candidates2 = [10, 1, 2, 7, 6, 1, 5]
    target2 = 8
    print(f"Candidates: {candidates2}, Target: {target2}")
    combinations2 = combination_sum2(candidates2, target2)
    print(f"Combinations (each used once): {combinations2}")

