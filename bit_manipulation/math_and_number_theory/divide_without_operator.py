"""
Divide Without Division Operator

Divide two integers using only bitwise operations and addition/subtraction.

Why Bitwise Division?
---------------------
Demonstrates understanding of:
- Binary division algorithm
- Bit manipulation
- Edge cases handling

Algorithm:
----------
Use left shift to find largest multiple, subtract and repeat.

Useful in:
- Understanding binary arithmetic
- Low-level programming
- Less common but valuable
"""


# ----------------------------------------------------------------------
# Divide Without Operator (Language-agnostic)
# ----------------------------------------------------------------------
def divide_without_operator(dividend: int, divisor: int) -> int:
    """
    Divide dividend by divisor using only bitwise operations.

    Algorithm:
    1. Handle sign
    2. Find largest multiple of divisor using left shift
    3. Subtract and accumulate quotient

    Args:
        dividend (int): Number to divide
        divisor (int): Divisor (non-zero)

    Returns:
        int: Quotient (dividend // divisor)

    Complexity:
        Time: O(log n)  - Where n is dividend, processes each bit.
        Space: O(1)   - Only uses variables.
    """
    if divisor == 0:
        raise ValueError("Division by zero")
    
    # Handle sign
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    
    while dividend >= divisor:
        # Find largest multiple of divisor
        temp = divisor
        multiple = 1
        
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        dividend -= temp
        quotient += multiple
    
    return sign * quotient


# ----------------------------------------------------------------------
# Divide with Remainder
# ----------------------------------------------------------------------
def divide_with_remainder(dividend: int, divisor: int) -> tuple:
    """
    Divide and return both quotient and remainder.

    Args:
        dividend (int): Number to divide
        divisor (int): Divisor (non-zero)

    Returns:
        tuple: (quotient, remainder)

    Complexity:
        Time: O(log n)  - Uses division which is O(log n).
        Space: O(1)   - Only uses variables.
    """
    quotient = divide_without_operator(dividend, divisor)
    remainder = dividend - (quotient * divisor)
    return (quotient, remainder)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Divide Without Operator Demonstration")
    
    dividend, divisor = 20, 3
    result = divide_without_operator(dividend, divisor)
    print(f"{dividend} // {divisor} = {result}")
    print(f"Verification: {dividend} // {divisor} = {dividend // divisor}")
    
    # With remainder
    quotient, remainder = divide_with_remainder(dividend, divisor)
    print(f"\n{dividend} / {divisor} = {quotient} remainder {remainder}")
    print(f"Verification: {dividend} / {divisor} = {dividend // divisor} remainder {dividend % divisor}")

