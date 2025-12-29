"""
Bitmasking Technique

Bitmasking uses binary numbers to represent sets and perform set operations efficiently.
Each bit position represents whether an element is in the set (1) or not (0).

Common Applications:
1. Set operations (union, intersection, subset)
2. Subset generation
3. State representation in DP
4. Permutation problems

Why Bitmasking?
---------------
Without bitmasking:
    Set operations require arrays/hash sets = O(n) space
    Subset generation = O(2^n) space for all subsets
With bitmasking:
    Set representation = O(1) space (for small sets)
    Efficient set operations = O(1) time

Useful in:
- Subset generation
- Dynamic programming with state
- Combinatorial problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Basic Bit Operations
# ----------------------------------------------------------------------
def set_bit(num: int, pos: int) -> int:
    """
    Set bit at given position (make it 1).

    Args:
        num (int): Number
        pos (int): Bit position (0-indexed from right)

    Returns:
        int: Number with bit set

    Complexity:
        Time: O(1)     - Single bitwise operation.
        Space: O(1)   - Only uses variables.
    """
    return num | (1 << pos)


def clear_bit(num: int, pos: int) -> int:
    """
    Clear bit at given position (make it 0).

    Args:
        num (int): Number
        pos (int): Bit position

    Returns:
        int: Number with bit cleared

    Complexity:
        Time: O(1)     - Single bitwise operation.
        Space: O(1)   - Only uses variables.
    """
    return num & ~(1 << pos)


def toggle_bit(num: int, pos: int) -> int:
    """
    Toggle bit at given position (flip it).

    Args:
        num (int): Number
        pos (int): Bit position

    Returns:
        int: Number with bit toggled

    Complexity:
        Time: O(1)     - Single bitwise operation.
        Space: O(1)   - Only uses variables.
    """
    return num ^ (1 << pos)


def is_bit_set(num: int, pos: int) -> bool:
    """
    Check if bit at given position is set.

    Args:
        num (int): Number
        pos (int): Bit position

    Returns:
        bool: True if bit is set, False otherwise

    Complexity:
        Time: O(1)     - Single bitwise operation.
        Space: O(1)   - Only uses variables.
    """
    return (num >> pos) & 1 == 1


# ----------------------------------------------------------------------
# Subset Generation
# ----------------------------------------------------------------------
def generate_subsets_bitmasking(arr: List[int]) -> List[List[int]]:
    """
    Generate all subsets using bitmasking.

    Algorithm:
    For each number from 0 to 2^n - 1, use its binary representation
    as a mask to select elements.

    Args:
        arr (List[int]): Input array

    Returns:
        List[List[int]]: List of all subsets

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
# Set Operations with Bitmasks
# ----------------------------------------------------------------------
def set_union(set1: int, set2: int) -> int:
    """
    Union of two sets represented as bitmasks.

    Args:
        set1 (int): First set as bitmask
        set2 (int): Second set as bitmask

    Returns:
        int: Union as bitmask

    Complexity:
        Time: O(1)     - Single bitwise OR operation.
        Space: O(1)   - Only uses variables.
    """
    return set1 | set2


def set_intersection(set1: int, set2: int) -> int:
    """
    Intersection of two sets represented as bitmasks.

    Args:
        set1 (int): First set as bitmask
        set2 (int): Second set as bitmask

    Returns:
        int: Intersection as bitmask

    Complexity:
        Time: O(1)     - Single bitwise AND operation.
        Space: O(1)   - Only uses variables.
    """
    return set1 & set2


def set_difference(set1: int, set2: int) -> int:
    """
    Difference of two sets (set1 - set2) represented as bitmasks.

    Args:
        set1 (int): First set as bitmask
        set2 (int): Second set as bitmask

    Returns:
        int: Difference as bitmask

    Complexity:
        Time: O(1)     - Single bitwise operation.
        Space: O(1)   - Only uses variables.
    """
    return set1 & ~set2


def count_set_bits(mask: int) -> int:
    """
    Count number of set bits in bitmask.

    Args:
        mask (int): Bitmask

    Returns:
        int: Number of set bits

    Complexity:
        Time: O(log n)  - Processes each bit, n is the number value.
        Space: O(1)   - Only uses counter variable.
    """
    count = 0
    while mask:
        count += mask & 1
        mask >>= 1
    return count


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Bitmasking Technique Demonstration")
    
    # Basic bit operations
    num = 5  # Binary: 0101
    print(f"Original: {num} (binary: {bin(num)})")
    print(f"Set bit 0: {set_bit(num, 0)} (binary: {bin(set_bit(num, 0))})")
    print(f"Clear bit 2: {clear_bit(num, 2)} (binary: {bin(clear_bit(num, 2))})")
    print(f"Toggle bit 1: {toggle_bit(num, 1)} (binary: {bin(toggle_bit(num, 1))})")
    print(f"Bit 0 is set: {is_bit_set(num, 0)}")
    
    # Subset generation
    arr = [1, 2, 3]
    print(f"\nArray: {arr}")
    subsets = generate_subsets_bitmasking(arr)
    print(f"All subsets: {subsets}")
    print(f"Total subsets: {len(subsets)} (expected: 2^3 = 8)")
    
    # Set operations
    set1 = 0b1010  # Elements at positions 1 and 3
    set2 = 0b1100  # Elements at positions 2 and 3
    print(f"\nSet 1: {bin(set1)} (elements 1, 3)")
    print(f"Set 2: {bin(set2)} (elements 2, 3)")
    print(f"Union: {bin(set_union(set1, set2))}")
    print(f"Intersection: {bin(set_intersection(set1, set2))}")
    print(f"Difference (set1 - set2): {bin(set_difference(set1, set2))}")
    print(f"Set bits in set1: {count_set_bits(set1)}")

