"""
0/1 Knapsack Problem

Select items to maximize value without exceeding weight capacity.

Problem Statement:
-------------------
Given items with weights and values, select items to maximize
total value without exceeding weight capacity. Each item can be
taken at most once (0/1).

Why Knapsack?
-------------
- Classic DP problem
- Demonstrates 2D DP
- Foundation for many problems
- Common interview problem

Useful in:
- Resource allocation
- Optimization problems
- Common interview problems
"""

from typing import List, Tuple, Dict


# ----------------------------------------------------------------------
# 0/1 Knapsack - Recursive
# ----------------------------------------------------------------------
def knapsack_recursive(weights: List[int], values: List[int],
                      capacity: int, n: int = None) -> int:
    """
    Knapsack using pure recursion.

    Args:
        weights (List[int]): Item weights
        values (List[int]): Item values
        capacity (int): Knapsack capacity
        n (int): Number of items

    Returns:
        int: Maximum value

    Complexity:
        Time: O(2^n)    - Exponential.
        Space: O(n)     - Recursion stack.
    """
    if n is None:
        n = len(weights)
    
    if n == 0 or capacity == 0:
        return 0
    
    # Don't include current item
    value1 = knapsack_recursive(weights, values, capacity, n - 1)
    
    # Include current item (if possible)
    if weights[n - 1] <= capacity:
        value2 = values[n - 1] + knapsack_recursive(
            weights, values, capacity - weights[n - 1], n - 1
        )
        return max(value1, value2)
    
    return value1


# ----------------------------------------------------------------------
# 0/1 Knapsack - Memoization
# ----------------------------------------------------------------------
def knapsack_memo(weights: List[int], values: List[int],
                 capacity: int, n: int = None,
                 memo: Dict[Tuple[int, int], int] = None) -> int:
    """
    Knapsack using memoization.

    Args:
        weights (List[int]): Item weights
        values (List[int]): Item values
        capacity (int): Knapsack capacity
        n (int): Number of items
        memo (Dict): Memoization cache

    Returns:
        int: Maximum value

    Complexity:
        Time: O(n * capacity)  - Each subproblem once.
        Space: O(n * capacity) - Memo storage.
    """
    if n is None:
        n = len(weights)
    if memo is None:
        memo = {}
    
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    
    if n == 0 or capacity == 0:
        return 0
    
    value1 = knapsack_memo(weights, values, capacity, n - 1, memo)
    
    if weights[n - 1] <= capacity:
        value2 = values[n - 1] + knapsack_memo(
            weights, values, capacity - weights[n - 1], n - 1, memo
        )
        memo[(n, capacity)] = max(value1, value2)
    else:
        memo[(n, capacity)] = value1
    
    return memo[(n, capacity)]


# ----------------------------------------------------------------------
# 0/1 Knapsack - Tabulation
# ----------------------------------------------------------------------
def knapsack_tabulation(weights: List[int], values: List[int],
                       capacity: int) -> int:
    """
    Knapsack using tabulation (2D DP).

    Args:
        weights (List[int]): Item weights
        values (List[int]): Item values
        capacity (int): Knapsack capacity

    Returns:
        int: Maximum value

    Complexity:
        Time: O(n * capacity)  - Fill table.
        Space: O(n * capacity) - Table storage.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include item
            dp[i][w] = dp[i - 1][w]
            
            # Include item if possible
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
    
    return dp[n][capacity]


# ----------------------------------------------------------------------
# 0/1 Knapsack - Space Optimized
# ----------------------------------------------------------------------
def knapsack_optimized(weights: List[int], values: List[int],
                      capacity: int) -> int:
    """
    Knapsack with O(capacity) space.

    Args:
        weights (List[int]): Item weights
        values (List[int]): Item values
        capacity (int): Knapsack capacity

    Returns:
        int: Maximum value

    Complexity:
        Time: O(n * capacity)  - Fill table.
        Space: O(capacity)     - Single row.
    """
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        # Process backwards to avoid overwriting
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: 0/1 Knapsack Problem Demonstration")
    
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    
    max_value = knapsack_tabulation(weights, values, capacity)
    print(f"\nMaximum value (tabulation): {max_value}")
    
    max_value_opt = knapsack_optimized(weights, values, capacity)
    print(f"Maximum value (optimized): {max_value_opt}")

