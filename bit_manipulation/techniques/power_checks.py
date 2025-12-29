"""
Power Checks Using Bit Manipulation

Check if a number is a power of 2, 4, etc. using efficient bit operations.

Why Bit Manipulation for Power Checks?
--------------------------------------
Without bit manipulation:
    Check powers by division/loop = O(log n)
With bit manipulation:
    Power of 2 check = O(1) using bit properties

Key Insight:
- Power of 2: Has exactly one set bit
- Power of 4: Has one set bit at even position
- n & (n - 1) clears rightmost set bit

Useful in:
- Fast power checks
- Algorithm optimizations
- Common interview problems
"""


# ----------------------------------------------------------------------
# Power of 2 Check (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def is_power_of_2(n: int) -> bool:
    """
    Check if number is a power of 2 using bit manipulation.

    Property: Power of 2 has exactly one set bit.
    n & (n - 1) clears rightmost set bit.
    If result is 0 and n > 0, it's a power of 2.

    Args:
        n (int): Number to check

    Returns:
        bool: True if power of 2, False otherwise

    Complexity:
        Time: O(1)     - Single bitwise operation.
        Space: O(1)   - Only uses variables.
    """
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_2_naive(n: int) -> bool:
    """
    Check if number is a power of 2 using division (naive approach).

    Args:
        n (int): Number to check

    Returns:
        bool: True if power of 2, False otherwise

    Complexity:
        Time: O(log n)  - Divides by 2 until result is 1 or odd.
        Space: O(1)   - Only uses variables.
    """
    if n <= 0:
        return False
    
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    
    return True


# ----------------------------------------------------------------------
# Power of 4 Check
# ----------------------------------------------------------------------
def is_power_of_4(n: int) -> bool:
    """
    Check if number is a power of 4 using bit manipulation.

    Property: Power of 4 has one set bit at even position (0, 2, 4, ...).

    Args:
        n (int): Number to check

    Returns:
        bool: True if power of 4, False otherwise

    Complexity:
        Time: O(1)     - Bitwise operations and mask check.
        Space: O(1)   - Only uses variables.
    """
    # Must be power of 2 and set bit at even position
    return (n > 0 and 
            (n & (n - 1)) == 0 and  # Power of 2
            (n & 0xAAAAAAAA) == 0)  # Set bit at even position (mask: 1010...1010)


# ----------------------------------------------------------------------
# Get Next Power of 2
# ----------------------------------------------------------------------
def next_power_of_2(n: int) -> int:
    """
    Find next power of 2 greater than or equal to n.

    Args:
        n (int): Number

    Returns:
        int: Next power of 2

    Complexity:
        Time: O(log n)  - Finds position of leftmost set bit.
        Space: O(1)   - Only uses variables.
    """
    if n <= 0:
        return 1
    if is_power_of_2(n):
        return n
    
    # Find position of leftmost set bit
    pos = 0
    temp = n
    while temp:
        temp >>= 1
        pos += 1
    
    return 1 << pos


# ----------------------------------------------------------------------
# Power of 3 Check (using different approach)
# ----------------------------------------------------------------------
def is_power_of_3(n: int) -> bool:
    """
    Check if number is a power of 3.

    Note: No direct bit manipulation trick for power of 3.
    Uses division approach.

    Args:
        n (int): Number to check

    Returns:
        bool: True if power of 3, False otherwise

    Complexity:
        Time: O(log n)  - Divides by 3 until result is 1 or not divisible.
        Space: O(1)   - Only uses variables.
    """
    if n <= 0:
        return False
    
    while n % 3 == 0:
        n //= 3
    
    return n == 1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Power Checks Using Bit Manipulation Demonstration")
    
    # Power of 2
    test_nums = [1, 2, 4, 8, 16, 15, 20]
    print("Power of 2 checks:")
    for num in test_nums:
        result = is_power_of_2(num)
        print(f"  {num}: {result} (binary: {bin(num)})")
    
    # Power of 4
    print("\nPower of 4 checks:")
    for num in [1, 4, 16, 64, 8, 12]:
        result = is_power_of_4(num)
        print(f"  {num}: {result}")
    
    # Next power of 2
    print("\nNext power of 2:")
    for num in [5, 10, 17, 31]:
        next_pow = next_power_of_2(num)
        print(f"  {num} -> {next_pow}")

