"""
Gray Code Generation

Gray code is a binary numeral system where two successive values differ
in only one bit. Used in error correction, digital communications, etc.

Problem Statement:
------------------
Generate n-bit Gray code sequence.

Example:
    Input: n = 2
    Output: [0, 1, 3, 2]
    Explanation:
        00 - 0
        01 - 1
        11 - 3
        10 - 2

Useful in:
- Error correction codes
- Digital communications
- Less common but valuable algorithm
"""

from typing import List


# ----------------------------------------------------------------------
# Gray Code Generation (Language-agnostic)
# ----------------------------------------------------------------------
def gray_code(n: int) -> List[int]:
    """
    Generate n-bit Gray code sequence.

    Algorithm:
    Start with [0, 1] for 1-bit.
    For each additional bit, reflect and prepend 1 to reflected part.

    Args:
        n (int): Number of bits

    Returns:
        List[int]: Gray code sequence

    Complexity:
        Time: O(2^n)    - Generates 2^n Gray codes.
        Space: O(2^n)  - Stores all Gray codes.
    """
    if n == 0:
        return [0]
    
    result = [0, 1]
    
    for i in range(1, n):
        # Reflect and prepend 1
        reflected = [x | (1 << i) for x in reversed(result)]
        result.extend(reflected)
    
    return result


# ----------------------------------------------------------------------
# Convert Binary to Gray Code
# ----------------------------------------------------------------------
def binary_to_gray(binary: int) -> int:
    """
    Convert binary number to Gray code.

    Formula: gray = binary ^ (binary >> 1)

    Args:
        binary (int): Binary number

    Returns:
        int: Gray code equivalent

    Complexity:
        Time: O(1)     - Single XOR and shift operation.
        Space: O(1)   - Only uses variables.
    """
    return binary ^ (binary >> 1)


# ----------------------------------------------------------------------
# Convert Gray Code to Binary
# ----------------------------------------------------------------------
def gray_to_binary(gray: int) -> int:
    """
    Convert Gray code to binary number.

    Args:
        gray (int): Gray code number

    Returns:
        int: Binary equivalent

    Complexity:
        Time: O(log n)  - Processes each bit position.
        Space: O(1)   - Only uses variables.
    """
    binary = gray
    while gray:
        gray >>= 1
        binary ^= gray
    return binary


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Gray Code Generation Demonstration")
    
    # Generate 3-bit Gray code
    n = 3
    gray_codes = gray_code(n)
    print(f"{n}-bit Gray code sequence:")
    for i, code in enumerate(gray_codes):
        print(f"  {i}: {code} (binary: {bin(code)[2:].zfill(n)})")
    
    # Binary to Gray
    binary_num = 5
    gray_num = binary_to_gray(binary_num)
    print(f"\nBinary {binary_num} (binary: {bin(binary_num)})")
    print(f"Gray code: {gray_num} (binary: {bin(gray_num)})")
    
    # Gray to Binary
    gray_num2 = 7
    binary_num2 = gray_to_binary(gray_num2)
    print(f"\nGray code {gray_num2} (binary: {bin(gray_num2)})")
    print(f"Binary: {binary_num2} (binary: {bin(binary_num2)})")

