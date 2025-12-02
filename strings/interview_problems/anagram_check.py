"""
Anagram Check Problem

Determine if two strings are anagrams of each other.

Problem Statement:
------------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example:
    Input: s = "rat", t = "car"
    Output: false

Useful in:
- Character frequency counting
- Hash tables
- Common interview problem
"""

from typing import Dict
from collections import Counter


# ----------------------------------------------------------------------
# Sorting Approach (Language-agnostic)
# ----------------------------------------------------------------------
def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams by sorting.

    Args:
        s (str): First string
        t (str): Second string

    Returns:
        bool: True if anagrams, False otherwise

    Complexity:
        Time: O(n log n)  - Sorting both strings takes O(n log n).
        Space: O(n)     - Stores sorted strings.
    """
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)


# ----------------------------------------------------------------------
# Hash Map Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using character frequency.

    Args:
        s (str): First string
        t (str): Second string

    Returns:
        bool: True if anagrams, False otherwise

    Complexity:
        Time: O(n)     - Counts characters in both strings.
        Space: O(k)   - Stores character frequencies, k is size of character set.
    """
    if len(s) != len(t):
        return False
    
    count: Dict[str, int] = {}
    
    # Count characters in s
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Decrement for t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0


# ----------------------------------------------------------------------
# Using Counter (Python-specific)
# ----------------------------------------------------------------------
def is_anagram_counter(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using Python's Counter.

    Args:
        s (str): First string
        t (str): Second string

    Returns:
        bool: True if anagrams, False otherwise

    Complexity:
        Time: O(n)     - Counter counts characters in both strings.
        Space: O(k)   - Counter stores character frequencies.
    """
    return Counter(s) == Counter(t)


# ----------------------------------------------------------------------
# Group Anagrams
# ----------------------------------------------------------------------
def group_anagrams(strings: list[str]) -> list[list[str]]:
    """
    Group strings that are anagrams of each other.

    Args:
        strings (list[str]): List of strings

    Returns:
        list[list[str]]: Groups of anagrams

    Complexity:
        Time: O(n * m * log m)  - n strings, average length m, sorting each string.
        Space: O(n * m)        - Stores grouped anagrams.
    """
    anagram_map: Dict[str, list[str]] = {}
    
    for s in strings:
        key = ''.join(sorted(s))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
    
    return list(anagram_map.values())


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Anagram Check Problem Demonstration")
    
    # Anagram check
    s1, t1 = "anagram", "nagaram"
    print(f"Strings: '{s1}' and '{t1}'")
    print(f"Are anagrams (hash map): {is_anagram(s1, t1)}")
    print(f"Are anagrams (sorting): {is_anagram_sorting(s1, t1)}")
    print(f"Are anagrams (Counter): {is_anagram_counter(s1, t1)}")
    print("Expected: True")
    
    # Not anagrams
    s2, t2 = "rat", "car"
    print(f"\nStrings: '{s2}' and '{t2}'")
    print(f"Are anagrams: {is_anagram(s2, t2)}")
    print("Expected: False")
    
    # Group anagrams
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"\nStrings: {strings}")
    grouped = group_anagrams(strings)
    print(f"Grouped anagrams: {grouped}")

