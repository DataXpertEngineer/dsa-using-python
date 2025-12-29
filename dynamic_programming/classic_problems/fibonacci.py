"""
Fibonacci Sequence

Calculate Fibonacci numbers using different DP approaches.

Problem Statement:
-------------------
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

Why Fibonacci?
--------------
- Classic DP problem
- Demonstrates all DP approaches
- Simple recurrence relation
- Foundation for understanding DP

Useful in:
- Learning DP concepts
- Understanding optimization
- Common interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Fibonacci - All Approaches
# ----------------------------------------------------------------------
def fibonacci_recursive(n: int) -> int:
    """
    Pure recursive (exponential time).

    Args:
        n (int): Position

    Returns:
        int: Fibonacci number

    Complexity:
        Time: O(2^n)    - Exponential.
        Space: O(n)     - Recursion stack.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """
    Memoization (top-down DP).

    Args:
        n (int): Position
        memo (Dict[int, int]): Cache

    Returns:
        int: Fibonacci number

    Complexity:
        Time: O(n)     - Each computed once.
        Space: O(n)   - Memo storage.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n: int) -> int:
    """
    Tabulation (bottom-up DP).

    Args:
        n (int): Position

    Returns:
        int: Fibonacci number

    Complexity:
        Time: O(n)     - Fill table.
        Space: O(n)   - Table storage.
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Space-optimized tabulation (O(1) space).

    Args:
        n (int): Position

    Returns:
        int: Fibonacci number

    Complexity:
        Time: O(n)     - Single pass.
        Space: O(1)   - Only variables.
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
# Fibonacci Sequence
# ----------------------------------------------------------------------
def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate first n Fibonacci numbers.

    Args:
        n (int): Count

    Returns:
        List[int]: Fibonacci sequence

    Complexity:
        Time: O(n)     - Generate n numbers.
        Space: O(n)   - Sequence storage.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Fibonacci Sequence Demonstration")
    
    n = 10
    print(f"Fibonacci numbers up to F({n}):")
    
    print("\nRecursive (slow):")
    for i in range(min(n + 1, 10)):  # Limit for demo
        print(f"  F({i}) = {fibonacci_recursive(i)}")
    
    print("\nMemoization (fast):")
    for i in range(n + 1):
        print(f"  F({i}) = {fibonacci_memo(i)}")
    
    print("\nTabulation (fast):")
    for i in range(n + 1):
        print(f"  F({i}) = {fibonacci_tabulation(i)}")
    
    print("\nOptimized (O(1) space):")
    for i in range(n + 1):
        print(f"  F({i}) = {fibonacci_optimized(i)}")
    
    print(f"\nSequence: {fibonacci_sequence(n + 1)}")

