"""
Generate All Permutations

Generate all possible permutations of a set using backtracking.

Problem Statement:
-------------------
Given a collection of distinct integers, return all possible permutations.

Example:
    Input: [1, 2, 3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Why Backtracking?
-----------------
- Try each element at current position
- Recurse to next position
- Backtrack after exploring all possibilities
- Systematic exploration of all arrangements

Useful in:
- Permutation generation
- Arrangement problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Generate All Permutations (Language-agnostic)
# ----------------------------------------------------------------------
def generate_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations using backtracking.

    Algorithm:
    1. Try each unused element at current position
    2. Mark element as used
    3. Recurse to next position
    4. Backtrack: unmark element

    Args:
        nums (List[int]): Input set

    Returns:
        List[List[int]]: List of all permutations

    Complexity:
        Time: O(n! * n)  - n! permutations, each takes O(n) to copy.
        Space: O(n)     - Recursion depth + used array.
    """
    permutations: List[List[int]] = []
    used = [False] * len(nums)
    
    def backtrack(current: List[int]) -> None:
        """Backtrack to generate all permutations."""
        # Base case: permutation complete
        if len(current) == len(nums):
            permutations.append(current.copy())
            return
        
        # Try each unused element
        for i in range(len(nums)):
            if not used[i]:
                # Choose
                used[i] = True
                current.append(nums[i])
                
                # Recurse
                backtrack(current)
                
                # Backtrack: unchoose
                current.pop()
                used[i] = False
    
    backtrack([])
    return permutations


# ----------------------------------------------------------------------
# Generate Permutations (Swapping)
# ----------------------------------------------------------------------
def generate_permutations_swap(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations using swapping approach.

    Args:
        nums (List[int]): Input set (will be modified)

    Returns:
        List[List[int]]: List of all permutations

    Complexity:
        Time: O(n! * n)  - n! permutations.
        Space: O(n)     - Recursion depth.
    """
    permutations: List[List[int]] = []
    
    def backtrack(index: int) -> None:
        """Backtrack using swapping."""
        # Base case: all positions filled
        if index == len(nums):
            permutations.append(nums.copy())
            return
        
        # Try each element at current position
        for i in range(index, len(nums)):
            # Swap
            nums[index], nums[i] = nums[i], nums[index]
            
            # Recurse
            backtrack(index + 1)
            
            # Backtrack: swap back
            nums[index], nums[i] = nums[i], nums[index]
    
    backtrack(0)
    return permutations


# ----------------------------------------------------------------------
# Generate Permutations with Duplicates
# ----------------------------------------------------------------------
def generate_permutations_duplicates(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations when duplicates exist.

    Args:
        nums (List[int]): Input set (may contain duplicates)

    Returns:
        List[List[int]]: List of unique permutations

    Complexity:
        Time: O(n! * n)  - n! permutations in worst case.
        Space: O(n)     - Recursion depth.
    """
    permutations: List[List[int]] = []
    nums.sort()  # Sort to handle duplicates
    used = [False] * len(nums)
    
    def backtrack(current: List[int]) -> None:
        if len(current) == len(nums):
            permutations.append(current.copy())
            return
        
        for i in range(len(nums)):
            # Skip if used or duplicate
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False
    
    backtrack([])
    return permutations


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Generate All Permutations Demonstration")
    
    nums = [1, 2, 3]
    print(f"Input set: {nums}")
    
    perms = generate_permutations(nums)
    print(f"All permutations: {perms}")
    print(f"Total permutations: {len(perms)} (expected: 3! = 6)")
    
    # Swapping approach
    print("\n" + "="*50)
    perms_swap = generate_permutations_swap(nums.copy())
    print(f"Swapping approach: {perms_swap}")
    
    # With duplicates
    print("\n" + "="*50)
    nums_dup = [1, 1, 2]
    print(f"Input with duplicates: {nums_dup}")
    perms_dup = generate_permutations_duplicates(nums_dup)
    print(f"Unique permutations: {perms_dup}")

