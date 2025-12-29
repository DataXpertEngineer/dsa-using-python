"""
Matrix Chain Multiplication

Find optimal way to parenthesize matrix multiplication.

Problem Statement:
-------------------
Given sequence of matrices, find optimal order to multiply them
to minimize number of scalar multiplications.

Why Matrix Chain?
-----------------
- Classic DP problem
- Demonstrates interval DP
- Optimization problem
- Medium difficulty interview problem

Useful in:
- Optimization problems
- Compiler optimization
- Medium difficulty interview problems
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Matrix Chain Multiplication - Tabulation
# ----------------------------------------------------------------------
def matrix_chain_multiplication(dims: List[int]) -> int:
    """
    Find minimum scalar multiplications using DP.

    Args:
        dims (List[int]): Matrix dimensions [p0, p1, ..., pn]
                          where matrix i has dimensions dims[i] x dims[i+1]

    Returns:
        int: Minimum scalar multiplications

    Complexity:
        Time: O(n³)     - Three nested loops.
        Space: O(n²)    - DP table.
    """
    n = len(dims) - 1
    if n <= 1:
        return 0
    
    # dp[i][j] = minimum cost to multiply matrices i to j
    dp = [[0] * n for _ in range(n)]
    
    # Length of chain
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # Try all possible splits
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] +
                       dims[i] * dims[k + 1] * dims[j + 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]


# ----------------------------------------------------------------------
# Matrix Chain - Get Optimal Parenthesization
# ----------------------------------------------------------------------
def matrix_chain_parenthesization(dims: List[int]) -> str:
    """
    Get optimal parenthesization.

    Args:
        dims (List[int]): Matrix dimensions

    Returns:
        str: Optimal parenthesization

    Complexity:
        Time: O(n³)     - Build table + backtrack.
        Space: O(n²)   - Table storage.
    """
    n = len(dims) - 1
    if n <= 1:
        return "A0"
    
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] +
                       dims[i] * dims[k + 1] * dims[j + 1])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    
    def get_parenthesization(i: int, j: int) -> str:
        if i == j:
            return f"A{i}"
        k = split[i][j]
        left = get_parenthesization(i, k)
        right = get_parenthesization(k + 1, j)
        return f"({left} x {right})"
    
    return get_parenthesization(0, n - 1)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Matrix Chain Multiplication Demonstration")
    
    # Dimensions: A0 is 10x20, A1 is 20x30, A2 is 30x40, A3 is 40x30
    dims = [10, 20, 30, 40, 30]
    
    print(f"Matrix dimensions: {dims}")
    print("Matrices: A0(10x20), A1(20x30), A2(30x40), A3(40x30)")
    
    min_cost = matrix_chain_multiplication(dims)
    print(f"\nMinimum scalar multiplications: {min_cost}")
    
    parenthesization = matrix_chain_parenthesization(dims)
    print(f"Optimal parenthesization: {parenthesization}")

