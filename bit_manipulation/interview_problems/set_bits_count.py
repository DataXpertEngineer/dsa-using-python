"""
Count Set Bits (Number of 1s in Binary)

Count the number of set bits (1s) in the binary representation of a number.

Problem Statement:
-------------------
Given an integer n, count the number of 1s in its binary representation.

Example:
    Input: n = 42 (binary: 101010)
    Output: 3

Useful in:
- Bit manipulation problems
- Population count
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Count Set Bits - Naive (Language-agnostic)
# ----------------------------------------------------------------------
def count_set_bits_naive(n: int) -> int:
    """
    Count set bits using naive approach (check each bit).

    Args:
        n (int): Number

    Returns:
        int: Number of set bits

    Complexity:
        Time: O(log n)  - Checks each bit, log n bits in number.
        Space: O(1)   - Only uses counter variable.
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


# ----------------------------------------------------------------------
# Count Set Bits - Kernighan's Algorithm (Optimal)
# ----------------------------------------------------------------------
def count_set_bits_kernighan(n: int) -> int:
    """
    Count set bits using Brian Kernighan's algorithm.

    Algorithm:
    n & (n - 1) clears the rightmost set bit.
    Repeat until n becomes 0.

    Args:
        n (int): Number

    Returns:
        int: Number of set bits

    Complexity:
        Time: O(k)     - Where k is number of set bits (better than O(log n)).
        Space: O(1)   - Only uses counter variable.
    """
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count


# ----------------------------------------------------------------------
# Count Set Bits - Built-in (Python 3.10+)
# ----------------------------------------------------------------------
def count_set_bits_builtin(n: int) -> int:
    """
    Count set bits using Python's built-in bit_count() method.

    Args:
        n (int): Number

    Returns:
        int: Number of set bits

    Complexity:
        Time: O(log n)  - Built-in implementation.
        Space: O(1)   - Constant space.
    """
    return n.bit_count()


# ----------------------------------------------------------------------
# Count Set Bits for Range
# ----------------------------------------------------------------------
def count_set_bits_range(n: int) -> List[int]:
    """
    Count set bits for all numbers from 0 to n.

    Uses dynamic programming: count[i] = count[i >> 1] + (i & 1)

    Args:
        n (int): Maximum number

    Returns:
        List[int]: Array where result[i] is count of set bits in i

    Complexity:
        Time: O(n)     - Processes each number once.
        Space: O(n)   - Stores result array.
    """
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Count Set Bits Demonstration")
    
    num = 42  # Binary: 101010
    print(f"Number: {num} (binary: {bin(num)})")
    
    print(f"Naive approach: {count_set_bits_naive(num)} set bits")
    print(f"Kernighan's algorithm: {count_set_bits_kernighan(num)} set bits")
    print(f"Built-in (bit_count): {count_set_bits_builtin(num)} set bits")
    print("Expected: 3 set bits")
    
    # Count bits for range
    print("\n" + "="*50)
    n = 8
    print(f"Count bits for numbers 0 to {n}:")
    counts = count_set_bits_range(n)
    for i, count in enumerate(counts):
        print(f"  {i} (binary: {bin(i)}) has {count} set bit(s)")

