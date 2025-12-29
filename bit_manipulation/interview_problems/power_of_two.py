"""
Power of Two Check

Check if a number is a power of 2 using bit manipulation.

Problem Statement:
-------------------
Given an integer n, return true if it is a power of 2, otherwise false.

Example:
    Input: n = 16
    Output: true (16 = 2^4)

    Input: n = 15
    Output: false

Useful in:
- Fast power checks
- Algorithm optimizations
- Common interview problems
"""


# ----------------------------------------------------------------------
# Power of 2 Check - Bit Manipulation (Optimal)
# ----------------------------------------------------------------------
def is_power_of_two(n: int) -> bool:
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


# ----------------------------------------------------------------------
# Power of 2 Check - Naive
# ----------------------------------------------------------------------
def is_power_of_two_naive(n: int) -> bool:
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
# Get Next Power of 2
# ----------------------------------------------------------------------
def next_power_of_two(n: int) -> int:
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
    if is_power_of_two(n):
        return n
    
    # Find position of leftmost set bit
    pos = 0
    temp = n
    while temp:
        temp >>= 1
        pos += 1
    
    return 1 << pos


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Power of Two Check Demonstration")
    
    test_nums = [1, 2, 4, 8, 16, 15, 20, 32, 0, -4]
    print("Power of 2 checks:")
    for num in test_nums:
        result = is_power_of_two(num)
        binary = bin(num) if num > 0 else "N/A"
        print(f"  {num}: {result} (binary: {binary})")
    
    # Next power of 2
    print("\nNext power of 2:")
    for num in [5, 10, 17, 31]:
        next_pow = next_power_of_two(num)
        print(f"  {num} -> {next_pow}")

