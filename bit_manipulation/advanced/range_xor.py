"""
Range XOR Queries

Compute XOR of a range [L, R] efficiently using prefix XOR.

Why Prefix XOR?
---------------
Without optimization:
    XOR range = O(R - L) time per query
With prefix XOR:
    XOR range = O(1) time per query after O(n) preprocessing

Useful in:
- Range queries
- XOR problems
- Less common but valuable
"""

from typing import List


# ----------------------------------------------------------------------
# Range XOR Using Prefix XOR
# ----------------------------------------------------------------------
class RangeXOR:
    """
    Efficient range XOR queries using prefix XOR.
    """
    
    def __init__(self, nums: List[int]):
        """
        Initialize with array and build prefix XOR.

        Args:
            nums (List[int]): Input array

        Complexity:
            Time: O(n)     - Builds prefix XOR array.
            Space: O(n)   - Stores prefix XOR array.
        """
        self.n = len(nums)
        self.prefix_xor = [0] * (self.n + 1)
        
        for i in range(self.n):
            self.prefix_xor[i + 1] = self.prefix_xor[i] ^ nums[i]
    
    def query(self, left: int, right: int):
        """
        Query XOR of range [left, right] (inclusive).

        Property: XOR[L, R] = prefix_xor[R+1] ^ prefix_xor[L]

        Args:
            left (int): Left index (inclusive)
            right (int): Right index (inclusive)

        Returns:
            int: XOR of range [left, right]

        Complexity:
            Time: O(1)     - Direct lookup.
            Space: O(1)   - Only uses variables.
        """
        return self.prefix_xor[right + 1] ^ self.prefix_xor[left]
    
    def xor_all(self):
        """
        Get XOR of entire array.

        Returns:
            int: XOR of all elements

        Complexity:
            Time: O(1)     - Direct lookup.
            Space: O(1)   - Only uses variables.
        """
        return self.prefix_xor[self.n]


# ----------------------------------------------------------------------
# XOR of Range [0, n]
# ----------------------------------------------------------------------
def xor_range(n: int) -> int:
    """
    Compute XOR of all numbers from 0 to n.

    Pattern:
    - n % 4 == 0: result = n
    - n % 4 == 1: result = 1
    - n % 4 == 2: result = n + 1
    - n % 4 == 3: result = 0

    Args:
        n (int): Maximum number

    Returns:
        int: XOR of [0, n]

    Complexity:
        Time: O(1)     - Uses pattern.
        Space: O(1)   - Only uses variables.
    """
    mod = n % 4
    if mod == 0:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n + 1
    else:  # mod == 3
        return 0


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Range XOR Queries Demonstration")
    
    nums = [1, 2, 3, 4, 5]
    range_xor = RangeXOR(nums)
    
    print(f"Array: {nums}")
    print(f"XOR [0, 2]: {range_xor.query(0, 2)}")
    print(f"XOR [1, 3]: {range_xor.query(1, 3)}")
    print(f"XOR [0, 4]: {range_xor.query(0, 4)}")
    print(f"XOR all: {range_xor.xor_all()}")
    
    # XOR of range [0, n]
    print("\nXOR of range [0, n]:")
    for n in range(10):
        result = xor_range(n)
        print(f"  [0, {n}]: {result}")

