"""
Bit Difference (Flip Bits to Convert)

Find the number of bits needed to flip to convert A to B.

Problem Statement:
-------------------
Given two integers A and B, find the number of bits that need to be
flipped to convert A to B.

Example:
    Input: A = 10 (binary: 1010), B = 20 (binary: 10100)
    Output: 4

Useful in:
- Hamming distance
- Error detection
- Common interview problems
"""


# ----------------------------------------------------------------------
# Bit Difference - XOR (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def bit_difference(a: int, b: int) -> int:
    """
    Find number of bits to flip to convert A to B.

    Algorithm:
    XOR gives differing bits, count set bits in XOR result.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Number of bits to flip

    Complexity:
        Time: O(log n)  - Where n is max(a, b), counts set bits.
        Space: O(1)   - Only uses variables.
    """
    xor_result = a ^ b
    count = 0
    
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1
    
    return count


# ----------------------------------------------------------------------
# Bit Difference - Kernighan's Algorithm
# ----------------------------------------------------------------------
def bit_difference_kernighan(a: int, b: int) -> int:
    """
    Find bit difference using Brian Kernighan's algorithm.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Number of bits to flip

    Complexity:
        Time: O(k)     - Where k is number of differing bits.
        Space: O(1)   - Only uses variables.
    """
    xor_result = a ^ b
    count = 0
    
    while xor_result:
        xor_result &= xor_result - 1  # Clear rightmost set bit
        count += 1
    
    return count


# ----------------------------------------------------------------------
# Bit Difference - Built-in (Python)
# ----------------------------------------------------------------------
def bit_difference_builtin(a: int, b: int) -> int:
    """
    Find bit difference using Python's built-in bit_count().

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Number of bits to flip

    Complexity:
        Time: O(log n)  - Built-in implementation.
        Space: O(1)   - Constant space.
    """
    return (a ^ b).bit_count()


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Bit Difference Demonstration")
    
    a, b = 10, 20
    print(f"A = {a} (binary: {bin(a)})")
    print(f"B = {b} (binary: {bin(b)})")
    
    diff = bit_difference(a, b)
    print(f"Bits to flip: {diff}")
    
    # Kernighan's
    diff_k = bit_difference_kernighan(a, b)
    print(f"Kernighan's: {diff_k}")
    
    # Built-in
    diff_builtin = bit_difference_builtin(a, b)
    print(f"Built-in: {diff_builtin}")

