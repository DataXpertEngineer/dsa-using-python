"""
Fast Exponentiation (Binary Exponentiation)

Compute a^b efficiently using binary representation of exponent.

Why Binary Exponentiation?
--------------------------
Without optimization:
    a^b = a * a * ... * a (b times) = O(b) time
With binary exponentiation:
    O(log b) time using bit manipulation

Algorithm:
----------
Express exponent in binary, multiply corresponding powers.

Example: 3^13
    13 = 1101 (binary)
    3^13 = 3^8 * 3^4 * 3^1

Useful in:
- Modular arithmetic
- Large number calculations
- Competitive programming
"""


# ----------------------------------------------------------------------
# Fast Exponentiation (Language-agnostic)
# ----------------------------------------------------------------------
def fast_exponentiation(base: int, exponent: int) -> int:
    """
    Compute base^exponent using binary exponentiation.

    Args:
        base (int): Base number
        exponent (int): Exponent (non-negative)

    Returns:
        int: base^exponent

    Complexity:
        Time: O(log exponent)  - Processes each bit of exponent.
        Space: O(1)          - Only uses variables.
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    
    result = 1
    current_power = base
    
    while exponent > 0:
        if exponent & 1:  # If current bit is set
            result *= current_power
        current_power *= current_power
        exponent >>= 1
    
    return result


# ----------------------------------------------------------------------
# Modular Exponentiation
# ----------------------------------------------------------------------
def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    Compute (base^exponent) % modulus efficiently.

    Args:
        base (int): Base number
        exponent (int): Exponent (non-negative)
        modulus (int): Modulus

    Returns:
        int: (base^exponent) % modulus

    Complexity:
        Time: O(log exponent)  - Processes each bit of exponent.
        Space: O(1)          - Only uses variables.
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Fast Exponentiation Demonstration")
    
    base, exp = 3, 13
    result = fast_exponentiation(base, exp)
    print(f"{base}^{exp} = {result}")
    print(f"Verification: {base}**{exp} = {base**exp}")
    
    # Modular exponentiation
    base2, exp2, mod = 2, 10, 1000
    result2 = modular_exponentiation(base2, exp2, mod)
    print(f"\n({base2}^{exp2}) % {mod} = {result2}")
    print(f"Verification: ({base2}**{exp2}) % {mod} = {(base2**exp2) % mod}")

