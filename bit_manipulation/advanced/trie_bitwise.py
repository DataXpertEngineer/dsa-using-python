"""
Bitwise Trie for Maximum XOR Problems

Trie data structure optimized for bitwise operations, particularly
useful for maximum XOR problems.

Why Bitwise Trie?
-----------------
- Efficient maximum XOR queries: O(32) per query
- Space-efficient: O(n * 32) for n numbers
- Useful for range XOR queries

Useful in:
- Maximum XOR problems
- Range XOR queries
- Advanced bit manipulation
- Less common but valuable
"""

from typing import List, Optional


class BitwiseTrie:
    """
    Trie data structure for bitwise operations.
    """
    
    def __init__(self):
        self.root = {}
    
    def insert(self, num: int):
        """
        Insert number into trie.

        Args:
            num (int): Number to insert

        Complexity:
            Time: O(32)    - Processes 32 bits.
            Space: O(32)  - Creates nodes for each bit.
        """
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    
    def find_max_xor(self, num: int):
        """
        Find maximum XOR with given number.

        Args:
            num (int): Number to find maximum XOR with

        Returns:
            int: Maximum XOR value

        Complexity:
            Time: O(32)    - Traverses 32 bits.
            Space: O(1)   - Only uses variables.
        """
        node = self.root
        xor_value = 0
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite = 1 - bit
            
            if opposite in node:
                xor_value |= (1 << i)
                node = node[opposite]
            else:
                node = node[bit]
        
        return xor_value


# ----------------------------------------------------------------------
# Maximum XOR Using Trie
# ----------------------------------------------------------------------
def maximum_xor_trie(nums: List[int]) -> int:
    """
    Find maximum XOR of any two numbers using Trie.

    Args:
        nums (List[int]): Array of integers

    Returns:
        int: Maximum XOR value

    Complexity:
        Time: O(n * 32)  - n insertions and queries, 32 bits each.
        Space: O(n * 32) - Trie storage.
    """
    trie = BitwiseTrie()
    
    # Insert all numbers
    for num in nums:
        trie.insert(num)
    
    # Find maximum XOR
    max_xor = 0
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num))
    
    return max_xor


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Bitwise Trie Demonstration")
    
    nums = [3, 10, 5, 25, 2, 8]
    print(f"Array: {nums}")
    
    max_xor = maximum_xor_trie(nums)
    print(f"Maximum XOR: {max_xor}")
    print("Expected: 28 (25 XOR 5)")

