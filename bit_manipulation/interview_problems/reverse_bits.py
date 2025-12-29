"""
Reverse Bits of an Integer

Reverse the bits of a 32-bit unsigned integer.

Problem Statement:
-------------------
Given a 32-bit unsigned integer, reverse its bits.

Example:
    Input: n = 43261596 (binary: 00000010100101000001111010011100)
    Output: 964176192 (binary: 00111001011110000010100101000000)

Useful in:
- Bit manipulation
- Low-level programming
- Medium difficulty interview problems
"""


# ----------------------------------------------------------------------
# Reverse Bits - Bit by Bit (Language-agnostic)
# ----------------------------------------------------------------------
def reverse_bits(n: int) -> int:
    """
    Reverse bits of a 32-bit unsigned integer.

    Args:
        n (int): 32-bit unsigned integer

    Returns:
        int: Number with reversed bits

    Complexity:
        Time: O(32)    - Processes each of 32 bits.
        Space: O(1)   - Only uses variables.
    """
    result = 0
    
    for i in range(32):
        # Extract bit at position i
        bit = (n >> i) & 1
        # Set bit at position (31 - i) in result
        result |= (bit << (31 - i))
    
    return result


# ----------------------------------------------------------------------
# Reverse Bits - Optimized
# ----------------------------------------------------------------------
def reverse_bits_optimized(n: int) -> int:
    """
    Reverse bits using optimized approach (swap pairs).

    Args:
        n (int): 32-bit unsigned integer

    Returns:
        int: Number with reversed bits

    Complexity:
        Time: O(log 32)  - Logarithmic number of swaps.
        Space: O(1)     - Only uses variables.
    """
    # Swap adjacent bits
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    # Swap adjacent pairs
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    # Swap adjacent nibbles
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    # Swap adjacent bytes
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    # Swap adjacent 16-bit words
    n = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16)
    
    return n


# ----------------------------------------------------------------------
# Reverse Bits - Python String (Pythonic)
# ----------------------------------------------------------------------
def reverse_bits_pythonic(n: int) -> int:
    """
    Reverse bits using Python string manipulation.

    Args:
        n (int): 32-bit unsigned integer

    Returns:
        int: Number with reversed bits

    Complexity:
        Time: O(32)    - String operations.
        Space: O(32)  - Creates string representation.
    """
    binary = bin(n)[2:].zfill(32)
    reversed_binary = binary[::-1]
    return int(reversed_binary, 2)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Reverse Bits Demonstration")
    
    n = 43261596
    print(f"Original: {n}")
    print(f"Binary: {bin(n)[2:].zfill(32)}")
    
    reversed_n = reverse_bits(n)
    print(f"\nReversed: {reversed_n}")
    print(f"Binary: {bin(reversed_n)[2:].zfill(32)}")
    
    # Optimized
    reversed_n_opt = reverse_bits_optimized(n)
    print(f"\nOptimized: {reversed_n_opt}")
    print(f"Verification: {reversed_n == reversed_n_opt}")

