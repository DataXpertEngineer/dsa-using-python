"""
Tabulation (Bottom-Up DP)

Build solution table iteratively from base cases.

Why Tabulation?
---------------
- More space efficient (can optimize)
- No recursion overhead
- Iterative approach
- Often faster than memoization

Characteristics:
- Build table bottom-up
- Fill from base cases
- O(n) time, O(n) space typically
- Can optimize to O(1) space sometimes

Useful in:
- Bottom-up DP problems
- When space optimization needed
- Iterative solutions preferred
"""

from typing import List


# ----------------------------------------------------------------------
# Fibonacci - Tabulation
# ----------------------------------------------------------------------
def fibonacci_tabulation(n: int) -> int:
    """
    Calculate nth Fibonacci using tabulation.

    Args:
        n (int): Position in sequence

    Returns:
        int: Nth Fibonacci number

    Complexity:
        Time: O(n)     - Fill table once.
        Space: O(n)   - Table storage.
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# ----------------------------------------------------------------------
# Fibonacci - Space Optimized
# ----------------------------------------------------------------------
def fibonacci_optimized(n: int) -> int:
    """
    Calculate nth Fibonacci with O(1) space.

    Args:
        n (int): Position in sequence

    Returns:
        int: Nth Fibonacci number

    Complexity:
        Time: O(n)     - Single pass.
        Space: O(1)   - Only uses variables.
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


# ----------------------------------------------------------------------
# Climbing Stairs - Tabulation
# ----------------------------------------------------------------------
def climb_stairs_tabulation(n: int) -> int:
    """
    Count ways to climb stairs using tabulation.

    Args:
        n (int): Number of stairs

    Returns:
        int: Number of ways

    Complexity:
        Time: O(n)     - Fill table once.
        Space: O(n)   - Table storage.
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# ----------------------------------------------------------------------
# Coin Change - Tabulation
# ----------------------------------------------------------------------
def coin_change_tabulation(coins: List[int], amount: int) -> int:
    """
    Count minimum coins using tabulation.

    Args:
        coins (List[int]): Coin denominations
        amount (int): Target amount

    Returns:
        int: Minimum coins, -1 if impossible

    Complexity:
        Time: O(amount * coins)  - Fill table.
        Space: O(amount)        - Table storage.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return int(dp[amount]) if dp[amount] != float('inf') else -1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Tabulation (Bottom-Up DP) Demonstration")
    
    print("Fibonacci (tabulation):")
    for i in range(10):
        result = fibonacci_tabulation(i)
        print(f"  F({i}) = {result}")
    
    print("\nFibonacci (space optimized):")
    for i in range(10):
        result = fibonacci_optimized(i)
        print(f"  F({i}) = {result}")
    
    print("\nClimbing Stairs (tabulation):")
    for i in range(1, 8):
        ways = climb_stairs_tabulation(i)
        print(f"  {i} stairs: {ways} ways")
    
    print("\nCoin Change (tabulation):")
    coins = [1, 3, 4]
    amount = 6
    min_coins = coin_change_tabulation(coins, amount)
    print(f"  Coins: {coins}, Amount: {amount}")
    print(f"  Minimum coins: {min_coins}")

