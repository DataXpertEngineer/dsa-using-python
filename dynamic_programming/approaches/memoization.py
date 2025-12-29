"""
Memoization (Top-Down DP)

Store results of subproblems to avoid redundant calculations.

Why Memoization?
---------------
- Optimizes recursive solutions
- Top-down approach (natural recursion)
- Only computes needed subproblems
- Easy to implement

Characteristics:
- Cache results in dictionary
- Check cache before computing
- O(n) time, O(n) space typically

Useful in:
- Optimizing recursive solutions
- Top-down DP problems
- When not all subproblems needed
"""

from typing import Dict, List, Callable


# ----------------------------------------------------------------------
# Memoization Decorator
# ----------------------------------------------------------------------
def memoize(func: Callable) -> Callable:
    """
    Memoization decorator for functions.

    Args:
        func (Callable): Function to memoize

    Returns:
        Callable: Memoized function

    Complexity:
        Time: O(n)     - Each subproblem solved once.
        Space: O(n)   - Memo storage.
    """
    memo: Dict[tuple, any] = {}
    
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    
    wrapper.__name__ = func.__name__
    return wrapper


# ----------------------------------------------------------------------
# Fibonacci - Memoization
# ----------------------------------------------------------------------
def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculate nth Fibonacci using memoization.

    Args:
        n (int): Position in sequence
        memo (Dict[int, int]): Memoization cache

    Returns:
        int: Nth Fibonacci number

    Complexity:
        Time: O(n)     - Each number computed once.
        Space: O(n)   - Memo storage + recursion stack.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# ----------------------------------------------------------------------
# Climbing Stairs - Memoization
# ----------------------------------------------------------------------
def climb_stairs_memo(n: int, memo: Dict[int, int] = None) -> int:
    """
    Count ways to climb stairs using memoization.

    Args:
        n (int): Number of stairs
        memo (Dict[int, int]): Memoization cache

    Returns:
        int: Number of ways

    Complexity:
        Time: O(n)     - Each step computed once.
        Space: O(n)   - Memo storage.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


# ----------------------------------------------------------------------
# Coin Change - Memoization
# ----------------------------------------------------------------------
def coin_change_memo(coins: List[int], amount: int,
                    memo: Dict[int, int] = None) -> int:
    """
    Count minimum coins using memoization.

    Args:
        coins (List[int]): Coin denominations
        amount (int): Target amount
        memo (Dict[int, int]): Memoization cache

    Returns:
        int: Minimum coins, -1 if impossible

    Complexity:
        Time: O(amount * coins)  - Each amount computed once.
        Space: O(amount)        - Memo storage.
    """
    if memo is None:
        memo = {}
    
    if amount in memo:
        return memo[amount]
    
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    
    min_coins = float('inf')
    for coin in coins:
        result = coin_change_memo(coins, amount - coin, memo)
        if result != -1:
            min_coins = min(min_coins, result + 1)
    
    memo[amount] = int(min_coins) if min_coins != float('inf') else -1
    return memo[amount]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Memoization (Top-Down DP) Demonstration")
    
    print("Fibonacci (memoization):")
    for i in range(10):
        result = fibonacci_memo(i)
        print(f"  F({i}) = {result}")
    
    print("\nClimbing Stairs (memoization):")
    for i in range(1, 8):
        ways = climb_stairs_memo(i)
        print(f"  {i} stairs: {ways} ways")
    
    print("\nCoin Change (memoization):")
    coins = [1, 3, 4]
    amount = 6
    min_coins = coin_change_memo(coins, amount)
    print(f"  Coins: {coins}, Amount: {amount}")
    print(f"  Minimum coins: {min_coins}")

