"""
Maximum XOR of Two Numbers

Find the maximum XOR value of two numbers in an array.

Problem Statement:
-------------------
Given an array of integers, find the maximum XOR value of any two numbers.

Example:
    Input: nums = [3, 10, 5, 25, 2, 8]
    Output: 28 (25 XOR 5 = 28)

Useful in:
- Bit manipulation
- Trie data structure
- Medium difficulty interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Maximum XOR - Brute Force (Language-agnostic)
# ----------------------------------------------------------------------
def maximum_xor_bruteforce(nums: List[int]) -> int:
    """
    Find maximum XOR using brute force approach.

    Args:
        nums (List[int]): Array of integers

    Returns:
        int: Maximum XOR value

    Complexity:
        Time: O(n²)    - Checks all pairs.
        Space: O(1)   - Only uses variables.
    """
    max_xor = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            max_xor = max(max_xor, nums[i] ^ nums[j])
    
    return max_xor


# ----------------------------------------------------------------------
# Maximum XOR - Optimized (Trie-based)
# ----------------------------------------------------------------------
def maximum_xor_optimized(nums: List[int]) -> int:
    """
    Find maximum XOR using Trie data structure.

    Algorithm:
    1. Build Trie with binary representations
    2. For each number, find best complement in Trie
    3. Track maximum XOR

    Args:
        nums (List[int]): Array of integers

    Returns:
        int: Maximum XOR value

    Complexity:
        Time: O(n * 32)  - n numbers, 32 bits each.
        Space: O(n * 32) - Trie storage.
    """
    class TrieNode:
        def __init__(self):
            self.children = {}
    
    # Build Trie
    root = TrieNode()
    for num in nums:
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    # Find maximum XOR
    max_xor = 0
    for num in nums:
        node = root
        xor_value = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try opposite bit first
            opposite = 1 - bit
            if opposite in node.children:
                xor_value |= (1 << i)
                node = node.children[opposite]
            else:
                node = node.children[bit]
        max_xor = max(max_xor, xor_value)
    
    return max_xor


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Maximum XOR Demonstration")
    
    nums = [3, 10, 5, 25, 2, 8]
    print(f"Array: {nums}")
    
    max_xor_bf = maximum_xor_bruteforce(nums)
    print(f"Maximum XOR (brute force): {max_xor_bf}")
    
    max_xor_opt = maximum_xor_optimized(nums)
    print(f"Maximum XOR (optimized): {max_xor_opt}")
    print("Expected: 28 (25 XOR 5)")

