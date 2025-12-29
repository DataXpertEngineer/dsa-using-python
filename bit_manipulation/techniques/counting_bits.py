"""
Counting Set Bits Techniques

Counting the number of set bits (1s) in the binary representation of a number
is a fundamental bit manipulation problem.

Algorithms:
1. Naive: Check each bit
2. Brian Kernighan's Algorithm: Clears rightmost set bit
3. Lookup table: Precompute counts for small numbers
4. Built-in: Python's bit_count() (Python 3.10+)

Why Count Bits?
--------------
- Useful in many bit manipulation problems
- Population count (popcount) is a common operation
- Used in subset generation, bitmasking problems
- Performance optimization in algorithms

Useful in:
- Bit manipulation problems
- Subset counting
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Naive Approach (Language-agnostic)
# ----------------------------------------------------------------------
def count_bits_naive(n: int) -> int:
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
# Brian Kernighan's Algorithm (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def count_bits_kernighan(n: int) -> int:
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
# Lookup Table Approach
# ----------------------------------------------------------------------
def count_bits_lookup(n: int) -> int:
    """
    Count set bits using lookup table (for 8-bit chunks).

    Args:
        n (int): Number

    Returns:
        int: Number of set bits

    Complexity:
        Time: O(1)     - Processes number in 8-bit chunks (constant for 32/64-bit).
        Space: O(1)   - Lookup table is fixed size (256 entries).
    """
    # Lookup table for 8-bit numbers (0-255)
    lookup = [0] * 256
    for i in range(256):
        lookup[i] = (i & 1) + lookup[i >> 1]
    
    count = 0
    # Process 8-bit chunks
    while n:
        count += lookup[n & 0xFF]
        n >>= 8
    
    return count


# ----------------------------------------------------------------------
# Count Bits for Range
# ----------------------------------------------------------------------
def count_bits_range(n: int) -> List[int]:
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
# Python Built-in (Python 3.10+)
# ----------------------------------------------------------------------
def count_bits_builtin(n: int) -> int:
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
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Counting Set Bits Demonstration")
    
    num = 42  # Binary: 101010
    print(f"Number: {num} (binary: {bin(num)})")
    
    print(f"Naive approach: {count_bits_naive(num)} set bits")
    print(f"Kernighan's algorithm: {count_bits_kernighan(num)} set bits")
    print(f"Lookup table: {count_bits_lookup(num)} set bits")
    print(f"Built-in (bit_count): {count_bits_builtin(num)} set bits")
    print("Expected: 3 set bits")
    
    # Count bits for range
    print("\n" + "="*50)
    n = 8
    print(f"Count bits for numbers 0 to {n}:")
    counts = count_bits_range(n)
    for i, count in enumerate(counts):
        print(f"  {i} (binary: {bin(i)}) has {count} set bit(s)")

