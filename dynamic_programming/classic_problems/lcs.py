"""
Longest Common Subsequence (LCS)

Find longest subsequence common to two strings.

Problem Statement:
-------------------
Given two strings, find length of longest subsequence present
in both. A subsequence is obtained by deleting some characters
without changing order.

Why LCS?
--------
- Classic 2D DP problem
- Foundation for edit distance
- String comparison problems
- Common interview problem

Useful in:
- String comparison
- Version control (diff)
- Common interview problems
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# LCS - Recursive
# ----------------------------------------------------------------------
def lcs_recursive(s1: str, s2: str, m: int = None, n: int = None) -> int:
    """
    LCS using pure recursion.

    Args:
        s1 (str): First string
        s2 (str): Second string
        m (int): Length of s1
        n (int): Length of s2

    Returns:
        int: LCS length

    Complexity:
        Time: O(2^(m+n))  - Exponential.
        Space: O(m + n)   - Recursion stack.
    """
    if m is None:
        m = len(s1)
    if n is None:
        n = len(s2)
    
    if m == 0 or n == 0:
        return 0
    
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs_recursive(s1, s2, m - 1, n - 1)
    else:
        return max(
            lcs_recursive(s1, s2, m - 1, n),
            lcs_recursive(s1, s2, m, n - 1)
        )


# ----------------------------------------------------------------------
# LCS - Tabulation (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def lcs_tabulation(s1: str, s2: str) -> int:
    """
    LCS using tabulation (2D DP).

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        int: LCS length

    Complexity:
        Time: O(m * n)     - Fill table.
        Space: O(m * n)    - Table storage.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


# ----------------------------------------------------------------------
# LCS - Get Actual Sequence
# ----------------------------------------------------------------------
def lcs_sequence(s1: str, s2: str) -> str:
    """
    Get actual LCS sequence.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        str: LCS sequence

    Complexity:
        Time: O(m * n)     - Build table + backtrack.
        Space: O(m * n)    - Table storage.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to get sequence
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return "".join(reversed(lcs))


# ----------------------------------------------------------------------
# LCS - Space Optimized
# ----------------------------------------------------------------------
def lcs_optimized(s1: str, s2: str) -> int:
    """
    LCS with O(min(m, n)) space.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        int: LCS length

    Complexity:
        Time: O(m * n)     - Fill table.
        Space: O(min(m, n)) - Two rows only.
    """
    m, n = len(s1), len(s2)
    
    # Use shorter string for columns
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
    
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev
    
    return prev[n]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Longest Common Subsequence Demonstration")
    
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    
    length = lcs_tabulation(s1, s2)
    print(f"\nLCS length: {length}")
    
    sequence = lcs_sequence(s1, s2)
    print(f"LCS sequence: {sequence}")
    
    length_opt = lcs_optimized(s1, s2)
    print(f"LCS length (optimized): {length_opt}")

