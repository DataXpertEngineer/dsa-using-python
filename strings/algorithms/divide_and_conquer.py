"""
Divide and Conquer Algorithms for Strings

Divide and conquer techniques applied to strings, including problems that can
be solved by splitting strings and solving subproblems.

Common Problems:
- Longest common prefix
- String reversal
- Palindrome checking
- String merging

Useful in:
- Understanding recursive approaches on strings
- Solving complex string problems
- Common interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Longest Common Prefix (Divide and Conquer)
# ----------------------------------------------------------------------
def longest_common_prefix(strings: List[str]) -> str:
    """
    Find longest common prefix among array of strings using divide and conquer.

    Args:
        strings (List[str]): Array of strings

    Returns:
        str: Longest common prefix

    Complexity:
        Time: O(n * m)  - Where n is number of strings, m is average length.
        Space: O(m * log n) - Recursion stack depth is log n, each level processes m chars.
    """
    if not strings:
        return ""
    
    return _lcp_divide(strings, 0, len(strings) - 1)


def _lcp_divide(strings: List[str], left: int, right: int) -> str:
    """
    Divide and conquer helper for longest common prefix.

    Args:
        strings (List[str]): Array of strings
        left (int): Left boundary
        right (int): Right boundary

    Returns:
        str: Longest common prefix in range
    """
    if left == right:
        return strings[left]
    
    mid = (left + right) // 2
    left_lcp = _lcp_divide(strings, left, mid)
    right_lcp = _lcp_divide(strings, mid + 1, right)
    
    return _common_prefix(left_lcp, right_lcp)


def _common_prefix(s1: str, s2: str) -> str:
    """Find common prefix of two strings."""
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1[:min_len]


# ----------------------------------------------------------------------
# Longest Common Prefix (Iterative)
# ----------------------------------------------------------------------
def longest_common_prefix_iterative(strings: List[str]) -> str:
    """
    Find longest common prefix using iterative approach.

    Args:
        strings (List[str]): Array of strings

    Returns:
        str: Longest common prefix

    Complexity:
        Time: O(n * m)  - Where n is number of strings, m is minimum length.
        Space: O(1)    - Only uses variables.
    """
    if not strings:
        return ""
    
    prefix = strings[0]
    
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


# ----------------------------------------------------------------------
# Merge Strings (Divide and Conquer)
# ----------------------------------------------------------------------
def merge_strings_divide_conquer(strings: List[str]) -> str:
    """
    Merge strings using divide and conquer approach.

    Args:
        strings (List[str]): Array of strings to merge

    Returns:
        str: Merged string

    Complexity:
        Time: O(n * m)  - Where n is number of strings, m is average length.
        Space: O(n * m) - Stores merged result.
    """
    if not strings:
        return ""
    if len(strings) == 1:
        return strings[0]
    
    mid = len(strings) // 2
    left = merge_strings_divide_conquer(strings[:mid])
    right = merge_strings_divide_conquer(strings[mid:])
    
    return left + right


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Divide and Conquer for Strings Demonstration")
    
    # Longest common prefix
    strings1 = ["flower", "flow", "flight"]
    print(f"Strings: {strings1}")
    lcp1 = longest_common_prefix(strings1)
    print(f"Longest common prefix (divide & conquer): '{lcp1}'")
    print("Expected: 'fl'")
    
    lcp2 = longest_common_prefix_iterative(strings1)
    print(f"Longest common prefix (iterative): '{lcp2}'")
    
    # No common prefix
    strings2 = ["dog", "racecar", "car"]
    print(f"\nStrings: {strings2}")
    lcp3 = longest_common_prefix(strings2)
    print(f"Longest common prefix: '{lcp3}'")
    print("Expected: ''")
    
    # Merge strings
    strings3 = ["Hello", " ", "World", "!"]
    merged = merge_strings_divide_conquer(strings3)
    print(f"\nMerge {strings3}: '{merged}'")

