"""
Substring Search Problem

Search for a substring (pattern) within a string (text).

Problem Statement:
------------------
Given a text string and a pattern string, find if pattern exists in text
and return the index(es) where it occurs.

Example:
    Input: text = "ABABDABACDABABCABCABAB", pattern = "ABABCABAB"
    Output: 10 (pattern found at index 10)

Algorithms:
1. Naive search: Simple but O(n*m)
2. KMP: Efficient O(n+m) using prefix function

Useful in:
- Text processing
- Pattern matching
- Common interview problem
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Naive Search (Language-agnostic)
# ----------------------------------------------------------------------
def naive_substring_search(text: str, pattern: str) -> Optional[int]:
    """
    Search for pattern in text using naive approach.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        Optional[int]: First index where pattern is found, None if not found

    Complexity:
        Time: O(n * m)  - For each position in text, checks pattern of length m.
        Space: O(1)    - Only uses variables for indices.
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return 0
    if m > n:
        return None
    
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i
    
    return None


def naive_substring_search_all(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using naive approach.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        List[int]: List of all starting indices where pattern is found

    Complexity:
        Time: O(n * m)  - Checks all possible positions.
        Space: O(k)    - Where k is number of occurrences.
    """
    n = len(text)
    m = len(pattern)
    occurrences = []
    
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            occurrences.append(i)
    
    return occurrences


# ----------------------------------------------------------------------
# KMP Algorithm (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def kmp_substring_search(text: str, pattern: str) -> Optional[int]:
    """
    Search for pattern in text using Knuth-Morris-Pratt algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        Optional[int]: First index where pattern is found, None if not found

    Complexity:
        Time: O(n + m)  - Preprocessing O(m), searching O(n).
        Space: O(m)    - Stores prefix function array.
    """
    if not pattern:
        return 0
    if len(pattern) > len(text):
        return None
    
    # Compute prefix function
    pi = _compute_prefix_function(pattern)
    
    j = 0  # Index in pattern
    for i in range(len(text)):
        # If characters don't match, use prefix function to skip
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        
        # If characters match, move forward in pattern
        if text[i] == pattern[j]:
            j += 1
        
        # If entire pattern matched
        if j == len(pattern):
            return i - j + 1
    
    return None


def kmp_substring_search_all(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using KMP algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        List[int]: List of all starting indices where pattern is found

    Complexity:
        Time: O(n + m)  - Preprocessing O(m), searching O(n).
        Space: O(m + k) - Prefix function array + result list.
    """
    if not pattern:
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []
    
    pi = _compute_prefix_function(pattern)
    occurrences = []
    j = 0
    
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == len(pattern):
            occurrences.append(i - j + 1)
            j = pi[j - 1]  # Continue searching
    
    return occurrences


def _compute_prefix_function(pattern: str) -> List[int]:
    """Compute prefix function for KMP algorithm."""
    m = len(pattern)
    pi = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        pi[i] = j
    
    return pi


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Substring Search Problem Demonstration")
    
    text = "ABABDABACDABABCABCABAB"
    pattern = "ABABCABAB"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    
    # Naive search
    result_naive = naive_substring_search(text, pattern)
    print(f"\nNaive search: Found at index {result_naive}")
    
    # KMP search
    result_kmp = kmp_substring_search(text, pattern)
    print(f"KMP search: Found at index {result_kmp}")
    
    # All occurrences
    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    print(f"\nText: {text2}")
    print(f"Pattern: {pattern2}")
    all_occurrences = kmp_substring_search_all(text2, pattern2)
    print(f"All occurrences (KMP): {all_occurrences}")
    print("Expected: [0, 9, 12]")

