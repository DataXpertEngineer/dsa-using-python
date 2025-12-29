"""
Minimum Edit Distance (Levenshtein Distance)

Find minimum operations to transform one string into another.

Problem Statement:
-------------------
Given two strings, find minimum number of operations (insert, delete, replace)
needed to transform first string into second.

Operations:
- Insert: Add a character
- Delete: Remove a character
- Replace: Change a character

Why Edit Distance?
------------------
- Classic 2D DP problem
- Foundation for string comparison
- Used in spell checkers, DNA analysis
- Common interview problem

Useful in:
- String comparison
- Spell checking
- DNA sequence alignment
- Common interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Edit Distance - Tabulation (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def min_edit_distance(s1: str, s2: str) -> int:
    """
    Calculate minimum edit distance using 2D DP.

    Algorithm:
    - dp[i][j] = edit distance between s1[0..i] and s2[0..j]
    - If characters match: dp[i][j] = dp[i-1][j-1]
    - Else: min of insert, delete, replace

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        int: Minimum edit distance

    Complexity:
        Time: O(m * n)     - Fill table.
        Space: O(m * n)    - Table storage.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]


# ----------------------------------------------------------------------
# Edit Distance - Space Optimized
# ----------------------------------------------------------------------
def min_edit_distance_optimized(s1: str, s2: str) -> int:
    """
    Edit distance with O(min(m, n)) space.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        int: Minimum edit distance

    Complexity:
        Time: O(m * n)     - Fill table.
        Space: O(min(m, n)) - Two rows only.
    """
    m, n = len(s1), len(s2)
    
    # Use shorter string for columns
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
    
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    
    return prev[n]


# ----------------------------------------------------------------------
# Edit Distance - Get Operations
# ----------------------------------------------------------------------
def edit_distance_operations(s1: str, s2: str) -> List[Tuple[str, str, str]]:
    """
    Get sequence of operations to transform s1 to s2.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        List[Tuple[str, str, str]]: List of (operation, char1, char2)

    Complexity:
        Time: O(m * n)     - Build table + backtrack.
        Space: O(m * n)    - Table storage.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    # Backtrack to get operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or dp[i - 1][j] < dp[i][j - 1]):
            operations.append(("delete", s1[i - 1], ""))
            i -= 1
        elif j > 0:
            operations.append(("insert", "", s2[j - 1]))
            j -= 1
    
    return list(reversed(operations))


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Minimum Edit Distance Demonstration")
    
    s1 = "kitten"
    s2 = "sitting"
    
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    
    distance = min_edit_distance(s1, s2)
    print(f"\nMinimum edit distance: {distance}")
    
    distance_opt = min_edit_distance_optimized(s1, s2)
    print(f"Minimum edit distance (optimized): {distance_opt}")
    
    operations = edit_distance_operations(s1, s2)
    print(f"\nOperations:")
    for op, char1, char2 in operations:
        print(f"  {op}: '{char1}' -> '{char2}'")

