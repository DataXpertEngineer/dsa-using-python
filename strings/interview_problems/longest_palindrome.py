"""
Longest Palindromic Substring Problem

Given a string s, return the longest palindromic substring in s.

Problem Statement:
------------------
Given a string s, return the longest palindromic substring in s.

Example:
    Input: s = "babad"
    Output: "bab" or "aba"

Example:
    Input: s = "cbbd"
    Output: "bb"

Useful in:
- Dynamic programming
- Two pointers technique
- Expand around centers
- Common interview problem
"""

from typing import Tuple


# ----------------------------------------------------------------------
# Expand Around Centers (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def longest_palindrome(s: str) -> str:
    """
    Find longest palindromic substring using expand around centers.

    Algorithm:
    For each position, expand around it as center (odd length) and
    between positions (even length), keep track of longest.

    Args:
        s (str): Input string

    Returns:
        str: Longest palindromic substring

    Complexity:
        Time: O(n²)    - For each of n positions, expand up to n/2 in worst case.
        Space: O(1)   - Only uses variables for tracking.
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    for i in range(len(s)):
        # Check odd length palindromes (center at i)
        len1 = _expand_around_center(s, i, i)
        # Check even length palindromes (center between i and i+1)
        len2 = _expand_around_center(s, i, i + 1)
        
        current_max = max(len1, len2)
        
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]


def _expand_around_center(s: str, left: int, right: int) -> int:
    """
    Expand around center and return length of palindrome.

    Args:
        s (str): Input string
        left (int): Left boundary
        right (int): Right boundary

    Returns:
        int: Length of palindrome
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left - 1


# ----------------------------------------------------------------------
# Dynamic Programming Approach
# ----------------------------------------------------------------------
def longest_palindrome_dp(s: str) -> str:
    """
    Find longest palindromic substring using dynamic programming.

    Args:
        s (str): Input string

    Returns:
        str: Longest palindromic substring

    Complexity:
        Time: O(n²)    - Fills DP table of size n×n.
        Space: O(n²)  - Stores DP table.
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Longest Palindromic Substring Problem Demonstration")
    
    # Example 1
    s1 = "babad"
    print(f"String: {s1}")
    result1 = longest_palindrome(s1)
    print(f"Longest palindrome (expand): '{result1}'")
    print("Expected: 'bab' or 'aba'")
    
    result1_dp = longest_palindrome_dp(s1)
    print(f"Longest palindrome (DP): '{result1_dp}'")
    
    # Example 2
    s2 = "cbbd"
    print(f"\nString: {s2}")
    result2 = longest_palindrome(s2)
    print(f"Longest palindrome: '{result2}'")
    print("Expected: 'bb'")

