"""
Coin Change Problem

Find minimum coins or ways to make change.

Problem Statement:
-------------------
Given coin denominations and target amount, find:
1. Minimum coins needed
2. Number of ways to make change

Why Coin Change?
----------------
- Classic DP problem
- Demonstrates unbounded knapsack
- Common interview problem
- Foundation for many problems

Useful in:
- Optimization problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Coin Change - Minimum Coins
# ----------------------------------------------------------------------
def coin_change_min(coins: List[int], amount: int) -> int:
    """
    Find minimum coins needed to make amount.

    Args:
        coins (List[int]): Coin denominations
        amount (int): Target amount

    Returns:
        int: Minimum coins, -1 if impossible

    Complexity:
        Time: O(amount * coins)  - Fill DP table.
        Space: O(amount)        - DP array.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return int(dp[amount]) if dp[amount] != float('inf') else -1


# ----------------------------------------------------------------------
# Coin Change - Number of Ways
# ----------------------------------------------------------------------
def coin_change_ways(coins: List[int], amount: int) -> int:
    """
    Count number of ways to make amount.

    Args:
        coins (List[int]): Coin denominations
        amount (int): Target amount

    Returns:
        int: Number of ways

    Complexity:
        Time: O(amount * coins)  - Fill DP table.
        Space: O(amount)         - DP array.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


# ----------------------------------------------------------------------
# Coin Change - Get Coins Used
# ----------------------------------------------------------------------
def coin_change_coins(coins: List[int], amount: int) -> List[int]:
    """
    Get actual coins used to make amount.

    Args:
        coins (List[int]): Coin denominations
        amount (int): Target amount

    Returns:
        List[int]: Coins used, empty if impossible

    Complexity:
        Time: O(amount * coins)  - Fill DP table + backtrack.
        Space: O(amount)        - DP array + result.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return []
    
    # Backtrack to get coins
    result = []
    current = amount
    while current > 0:
        coin = parent[current]
        result.append(coin)
        current -= coin
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Coin Change Problem Demonstration")
    
    coins = [1, 3, 4]
    amount = 6
    
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    
    min_coins = coin_change_min(coins, amount)
    print(f"\nMinimum coins needed: {min_coins}")
    
    ways = coin_change_ways(coins, amount)
    print(f"Number of ways: {ways}")
    
    coins_used = coin_change_coins(coins, amount)
    print(f"Coins used: {coins_used}")

