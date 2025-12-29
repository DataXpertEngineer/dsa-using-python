"""
First Unique Character

Find first non-repeating character in string using hash table.

Problem Statement:
-------------------
Given a string, find the first non-repeating character and return its index.
If it doesn't exist, return -1.

Example:
    Input: "leetcode"
    Output: 0 (character 'l' at index 0)

    Input: "loveleetcode"
    Output: 2 (character 'v' at index 2)

Why Hash Table?
---------------
- Count character frequency
- Find first character with count = 1
- O(n) solution

Useful in:
- String processing
- Medium difficulty interview problems
"""

from typing import Dict
from collections import Counter, OrderedDict


# ----------------------------------------------------------------------
# First Unique Character (Language-agnostic)
# ----------------------------------------------------------------------
def first_unique_char(s: str) -> int:
    """
    Find first non-repeating character using hash table.

    Algorithm:
    1. Count frequency of each character
    2. Traverse string to find first character with count = 1

    Args:
        s (str): Input string

    Returns:
        int: Index of first unique character, -1 if not found

    Complexity:
        Time: O(n)     - Two passes through string.
        Space: O(k)   - k is number of unique characters.
    """
    freq_map: Dict[str, int] = {}
    
    # Count frequencies
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
    
    # Find first unique character
    for i, char in enumerate(s):
        if freq_map[char] == 1:
            return i
    
    return -1


# ----------------------------------------------------------------------
# First Unique Character (Using Counter)
# ----------------------------------------------------------------------
def first_unique_char_counter(s: str) -> int:
    """
    Find first unique character using Counter.

    Args:
        s (str): Input string

    Returns:
        int: Index of first unique character, -1 if not found

    Complexity:
        Time: O(n)     - Counter + traversal.
        Space: O(k)   - Stores character counts.
    """
    count = Counter(s)
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    
    return -1


# ----------------------------------------------------------------------
# First Unique Character (Single Pass)
# ----------------------------------------------------------------------
def first_unique_char_single_pass(s: str) -> int:
    """
    Find first unique character in single pass using OrderedDict.

    Args:
        s (str): Input string

    Returns:
        int: Index of first unique character, -1 if not found

    Complexity:
        Time: O(n)     - Single pass through string.
        Space: O(k)   - Stores unique characters.
    """
    seen = OrderedDict()
    repeated = set()
    
    for i, char in enumerate(s):
        if char in repeated:
            continue
        if char in seen:
            del seen[char]
            repeated.add(char)
        else:
            seen[char] = i
    
    return next(iter(seen.values())) if seen else -1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: First Unique Character Demonstration")
    
    test_cases = ["leetcode", "loveleetcode", "aabb", "abc"]
    
    for s in test_cases:
        print(f"\nString: '{s}'")
        result1 = first_unique_char(s)
        print(f"  First unique char index: {result1}")
        if result1 != -1:
            print(f"  Character: '{s[result1]}'")
        
        result2 = first_unique_char_counter(s)
        print(f"  Using Counter: {result2}")
        
        result3 = first_unique_char_single_pass(s)
        print(f"  Single pass: {result3}")

