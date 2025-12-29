"""
Dynamic Programming (DP)

Dynamic Programming is an optimization technique that solves problems by
breaking them down into simpler subproblems and storing results to avoid
recomputing them.

Why Dynamic Programming?
------------------------
- Optimizes recursive solutions
- Avoids redundant calculations
- Solves optimization problems efficiently
- Foundation for many algorithms

Key Concepts:
- Overlapping subproblems
- Optimal substructure
- Memoization (top-down)
- Tabulation (bottom-up)

Useful in:
- Optimization problems
- Counting problems
- Decision problems
- Common interview problems
"""

from typing import Dict, List, Callable, Any


# ----------------------------------------------------------------------
# DP Problem Identification
# ----------------------------------------------------------------------
def is_dp_problem(problem: str) -> bool:
    """
    Check if problem can be solved with DP.

    Characteristics:
    1. Overlapping subproblems
    2. Optimal substructure
    3. Can be broken into smaller problems

    Args:
        problem (str): Problem description

    Returns:
        bool: True if DP applicable

    Complexity:
        Time: O(1)     - Constant time check.
        Space: O(1)   - Only uses variables.
    """
    dp_keywords = [
        "optimal", "maximum", "minimum", "count",
        "subsequence", "substring", "path", "ways"
    ]
    return any(keyword in problem.lower() for keyword in dp_keywords)


# ----------------------------------------------------------------------
# DP Template - Memoization
# ----------------------------------------------------------------------
def dp_memo_template(func: Callable) -> Callable:
    """
    Decorator for memoization (top-down DP).

    Args:
        func (Callable): Function to memoize

    Returns:
        Callable: Memoized function

    Complexity:
        Time: O(n)     - Each subproblem solved once.
        Space: O(n)   - Memo table storage.
    """
    memo: Dict[tuple, Any] = {}
    
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    
    return wrapper


# ----------------------------------------------------------------------
# DP Template - Tabulation
# ----------------------------------------------------------------------
def dp_tabulation_template(n: int, base_cases: Dict[int, Any],
                          recurrence: Callable) -> List[Any]:
    """
    Template for bottom-up DP (tabulation).

    Args:
        n (int): Problem size
        base_cases (Dict[int, Any]): Base case values
        recurrence (Callable): Recurrence relation

    Returns:
        List[Any]: DP table

    Complexity:
        Time: O(n)     - Fill table once.
        Space: O(n)   - Table storage.
    """
    dp = [0] * (n + 1)
    
    # Fill base cases
    for i, value in base_cases.items():
        dp[i] = value
    
    # Fill table bottom-up
    for i in range(max(base_cases.keys()) + 1, n + 1):
        dp[i] = recurrence(i, dp)
    
    return dp


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Dynamic Programming Concepts Demonstration")
    
    print("DP Problem Identification:")
    problems = [
        "Find maximum sum subsequence",
        "Count ways to reach destination",
        "Find shortest path"
    ]
    for problem in problems:
        print(f"  '{problem}': {is_dp_problem(problem)}")
    
    print("\n" + "="*60)
    print("DYNAMIC PROGRAMMING CONCEPTS SUMMARY")
    print("="*60)
    print("""
DP Properties:
1. Overlapping Subproblems: Same subproblems solved multiple times
2. Optimal Substructure: Optimal solution contains optimal sub-solutions
3. Memoization: Store results of subproblems (top-down)
4. Tabulation: Build table bottom-up (bottom-up)

DP Approaches:
1. Recursion: Pure recursive (inefficient, exponential)
2. Memoization: Recursive + cache (top-down, O(n) space)
3. Tabulation: Iterative + table (bottom-up, O(n) space)

When to Use DP:
- Optimization problems
- Counting problems
- Problems with overlapping subproblems
- Problems with optimal substructure

Common DP Patterns:
- 1D DP: Fibonacci, climbing stairs
- 2D DP: LCS, edit distance, grid paths
- Knapsack: 0/1, unbounded, fractional
- Subsequences: LIS, LCS, palindromic
- Partitioning: Equal sum, palindrome partitioning
""")

