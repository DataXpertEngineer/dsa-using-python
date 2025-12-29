"""
Add Two Numbers Without Plus Operator

Add two integers using only bitwise operations (no +, -, *, / operators).

Why Bitwise Addition?
---------------------
Demonstrates understanding of:
- Binary addition logic
- Bit manipulation
- Carry propagation

Algorithm:
----------
Use XOR for sum and AND for carry, repeat until no carry.

Useful in:
- Understanding binary arithmetic
- Low-level programming
- Interview problems
"""


# ----------------------------------------------------------------------
# Add Without Plus (Language-agnostic)
# ----------------------------------------------------------------------
def add_without_plus(a: int, b: int) -> int:
    """
    Add two numbers using only bitwise operations.

    Algorithm:
    - XOR gives sum without carry
    - AND gives carry bits
    - Shift carry left and add recursively

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b

    Complexity:
        Time: O(log n)  - Where n is max(a, b), processes each bit.
        Space: O(1)   - Only uses variables.
    """
    while b != 0:
        # Calculate sum without carry
        sum_without_carry = a ^ b
        # Calculate carry
        carry = (a & b) << 1
        # Update a and b
        a = sum_without_carry
        b = carry
    
    return a


# ----------------------------------------------------------------------
# Add Without Plus (Recursive)
# ----------------------------------------------------------------------
def add_without_plus_recursive(a: int, b: int) -> int:
    """
    Add two numbers recursively using bitwise operations.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b

    Complexity:
        Time: O(log n)  - Recursive calls until no carry.
        Space: O(log n) - Recursion stack depth.
    """
    if b == 0:
        return a
    
    return add_without_plus_recursive(a ^ b, (a & b) << 1)


# ----------------------------------------------------------------------
# Subtract Without Minus
# ----------------------------------------------------------------------
def subtract_without_minus(a: int, b: int) -> int:
    """
    Subtract b from a using only bitwise operations.

    Algorithm: a - b = a + (~b + 1) = a + (-b)

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Difference a - b

    Complexity:
        Time: O(log n)  - Uses addition which is O(log n).
        Space: O(1)   - Only uses variables.
    """
    return add_without_plus(a, add_without_plus(~b, 1))


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Add Without Plus Operator Demonstration")
    
    a, b = 15, 27
    result = add_without_plus(a, b)
    print(f"{a} + {b} = {result}")
    print(f"Verification: {a} + {b} = {a + b}")
    
    # Recursive version
    result2 = add_without_plus_recursive(a, b)
    print(f"\nRecursive: {a} + {b} = {result2}")
    
    # Subtract
    result3 = subtract_without_minus(a, b)
    print(f"\nSubtract: {a} - {b} = {result3}")
    print(f"Verification: {a} - {b} = {a - b}")

