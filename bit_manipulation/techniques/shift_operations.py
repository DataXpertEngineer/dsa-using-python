"""
Shift Operations in Bit Manipulation

Shift operations move bits left or right in a number's binary representation.

Types:
1. Left shift (<<): Multiply by powers of 2
2. Right shift (>>): Divide by powers of 2
3. Arithmetic vs Logical shift (Python uses arithmetic)

Why Shift Operations?
---------------------
- Efficient multiplication/division by powers of 2
- Bit manipulation and extraction
- Fast operations (hardware-level)
- Foundation for many bit algorithms

Useful in:
- Fast multiplication/division
- Bit extraction
- Power calculations
- Common bit manipulation problems
"""


# ----------------------------------------------------------------------
# Left Shift (Language-agnostic)
# ----------------------------------------------------------------------
def left_shift(num: int, positions: int) -> int:
    """
    Left shift number by given positions (multiply by 2^positions).

    Args:
        num (int): Number to shift
        positions (int): Number of positions to shift left

    Returns:
        int: Shifted number

    Complexity:
        Time: O(1)     - Single shift operation.
        Space: O(1)   - Only uses variables.
    """
    return num << positions


def multiply_by_power_of_2(num: int, power: int) -> int:
    """
    Multiply number by 2^power using left shift.

    Args:
        num (int): Number to multiply
        power (int): Power of 2

    Returns:
        int: num * (2^power)

    Complexity:
        Time: O(1)     - Single shift operation.
        Space: O(1)   - Only uses variables.
    """
    return num << power


# ----------------------------------------------------------------------
# Right Shift (Language-agnostic)
# ----------------------------------------------------------------------
def right_shift(num: int, positions: int) -> int:
    """
    Right shift number by given positions (divide by 2^positions).

    Note: Python uses arithmetic right shift (sign-extending).

    Args:
        num (int): Number to shift
        positions (int): Number of positions to shift right

    Returns:
        int: Shifted number

    Complexity:
        Time: O(1)     - Single shift operation.
        Space: O(1)   - Only uses variables.
    """
    return num >> positions


def divide_by_power_of_2(num: int, power: int) -> int:
    """
    Divide number by 2^power using right shift.

    Args:
        num (int): Number to divide
        power (int): Power of 2

    Returns:
        int: num // (2^power)

    Complexity:
        Time: O(1)     - Single shift operation.
        Space: O(1)   - Only uses variables.
    """
    return num >> power


# ----------------------------------------------------------------------
# Extract Bits
# ----------------------------------------------------------------------
def extract_bits(num: int, start: int, end: int) -> int:
    """
    Extract bits from position start to end (inclusive).

    Args:
        num (int): Number
        start (int): Start bit position (0-indexed from right)
        end (int): End bit position (inclusive)

    Returns:
        int: Extracted bits

    Complexity:
        Time: O(1)     - Bitwise operations.
        Space: O(1)   - Only uses variables.
    """
    # Create mask for bits from start to end
    mask = ((1 << (end - start + 1)) - 1) << start
    return (num & mask) >> start


# ----------------------------------------------------------------------
# Rotate Bits
# ----------------------------------------------------------------------
def rotate_left(num: int, positions: int, bits: int = 32) -> int:
    """
    Rotate bits left (circular shift).

    Args:
        num (int): Number to rotate
        positions (int): Number of positions to rotate
        bits (int): Number of bits (default: 32)

    Returns:
        int: Rotated number

    Complexity:
        Time: O(1)     - Bitwise operations.
        Space: O(1)   - Only uses variables.
    """
    mask = (1 << bits) - 1
    num &= mask
    return ((num << positions) | (num >> (bits - positions))) & mask


def rotate_right(num: int, positions: int, bits: int = 32) -> int:
    """
    Rotate bits right (circular shift).

    Args:
        num (int): Number to rotate
        positions (int): Number of positions to rotate
        bits (int): Number of bits (default: 32)

    Returns:
        int: Rotated number

    Complexity:
        Time: O(1)     - Bitwise operations.
        Space: O(1)   - Only uses variables.
    """
    mask = (1 << bits) - 1
    num &= mask
    return ((num >> positions) | (num << (bits - positions))) & mask


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Shift Operations Demonstration")
    
    num = 5  # Binary: 0101
    print(f"Original: {num} (binary: {bin(num)})")
    
    # Left shift
    left = left_shift(num, 2)
    print(f"Left shift by 2: {left} (binary: {bin(left)})")
    print(f"  Equivalent to: {num} * 2^2 = {num * 4}")
    
    # Right shift
    right = right_shift(num, 1)
    print(f"Right shift by 1: {right} (binary: {bin(right)})")
    print(f"  Equivalent to: {num} // 2^1 = {num // 2}")
    
    # Multiply/divide by power of 2
    print(f"\nMultiply {num} by 2^3: {multiply_by_power_of_2(num, 3)}")
    print(f"Divide {num} by 2^1: {divide_by_power_of_2(num, 1)}")
    
    # Extract bits
    num2 = 0b11010110  # 214
    print(f"\nNumber: {num2} (binary: {bin(num2)})")
    extracted = extract_bits(num2, 2, 5)
    print(f"Extract bits [2:5]: {extracted} (binary: {bin(extracted)})")
    
    # Rotate
    num3 = 0b1011  # 11
    print(f"\nNumber: {num3} (binary: {bin(num3)})")
    rotated = rotate_left(num3, 2, 4)
    print(f"Rotate left by 2: {rotated} (binary: {bin(rotated)})")

