"""
Pure Recursive Solutions

Recursive solutions without optimization (exponential time complexity).

Why Pure Recursion?
-------------------
- Simple to understand
- Natural problem decomposition
- Foundation for DP
- Educational purposes

Disadvantages:
- Exponential time complexity
- Redundant calculations
- Stack overflow for large inputs

Useful in:
- Understanding problem structure
- First step before DP optimization
"""

from typing import List


# ----------------------------------------------------------------------
# Fibonacci - Pure Recursion
# ----------------------------------------------------------------------
def fibonacci_recursive(n: int) -> int:
    """
    Calculate nth Fibonacci number using pure recursion.

    Args:
        n (int): Position in Fibonacci sequence

    Returns:
        int: Nth Fibonacci number

    Complexity:
        Time: O(2^n)    - Exponential, many redundant calculations.
        Space: O(n)     - Recursion stack depth.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ----------------------------------------------------------------------
# Climbing Stairs - Pure Recursion
# ----------------------------------------------------------------------
def climb_stairs_recursive(n: int) -> int:
    """
    Count ways to climb n stairs (1 or 2 steps at a time).

    Args:
        n (int): Number of stairs

    Returns:
        int: Number of ways

    Complexity:
        Time: O(2^n)    - Exponential.
        Space: O(n)     - Recursion stack.
    """
    if n <= 2:
        return n
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


# ----------------------------------------------------------------------
# Coin Change - Pure Recursion
# ----------------------------------------------------------------------
def coin_change_recursive(coins: List[int], amount: int) -> int:
    """
    Count minimum coins needed (pure recursion).

    Args:
        coins (List[int]): Available coin denominations
        amount (int): Target amount

    Returns:
        int: Minimum coins, -1 if impossible

    Complexity:
        Time: O(amount^coins)  - Exponential.
        Space: O(amount)       - Recursion stack.
    """
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    
    min_coins = float('inf')
    for coin in coins:
        result = coin_change_recursive(coins, amount - coin)
        if result != -1:
            min_coins = min(min_coins, result + 1)
    
    return int(min_coins) if min_coins != float('inf') else -1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Pure Recursive Solutions Demonstration")
    
    print("Fibonacci (recursive):")
    for i in range(10):
        print(f"  F({i}) = {fibonacci_recursive(i)}")
    
    print("\nClimbing Stairs (recursive):")
    for i in range(1, 8):
        ways = climb_stairs_recursive(i)
        print(f"  {i} stairs: {ways} ways")
    
    print("\n" + "="*50)
    print("NOTE: Pure recursion is inefficient!")
    print("These solutions have exponential time complexity.")
    print("Use memoization or tabulation for optimization.")

