"""
Group Anagrams

Group strings that are anagrams of each other using hash table.

Problem Statement:
-------------------
Given an array of strings, group the anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Why Hash Table?
---------------
- Use sorted string as key
- Group strings with same sorted key
- O(n * k log k) solution where k is string length

Useful in:
- String grouping problems
- Medium difficulty interview problems
"""

from typing import List, Dict
from collections import defaultdict


# ----------------------------------------------------------------------
# Group Anagrams (Language-agnostic)
# ----------------------------------------------------------------------
def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using sorted string as key.

    Algorithm:
    1. Sort each string to get canonical form
    2. Use sorted string as key in hash table
    3. Group strings with same key

    Args:
        strs (List[str]): List of strings

    Returns:
        List[List[str]]: Groups of anagrams

    Complexity:
        Time: O(n * k log k)  - n strings, each sorted in O(k log k).
        Space: O(n * k)     - Stores all strings.
    """
    groups: Dict[str, List[str]] = {}
    
    for s in strs:
        # Sort string to get canonical form
        key = ''.join(sorted(s))
        
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    
    return list(groups.values())


# ----------------------------------------------------------------------
# Group Anagrams (Using defaultdict)
# ----------------------------------------------------------------------
def group_anagrams_defaultdict(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using defaultdict.

    Args:
        strs (List[str]): List of strings

    Returns:
        List[List[str]]: Groups of anagrams

    Complexity:
        Time: O(n * k log k)  - Sort each string.
        Space: O(n * k)     - Stores all strings.
    """
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


# ----------------------------------------------------------------------
# Group Anagrams (Using Character Count)
# ----------------------------------------------------------------------
def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using character count as key.

    Args:
        strs (List[str]): List of strings

    Returns:
        List[List[str]]: Groups of anagrams

    Complexity:
        Time: O(n * k)     - Count characters for each string.
        Space: O(n * k)   - Stores all strings.
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Count characters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        # Use tuple as key
        key = tuple(count)
        groups[key].append(s)
    
    return list(groups.values())


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Group Anagrams Demonstration")
    
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {strs}")
    
    result = group_anagrams(strs)
    print(f"Grouped anagrams: {result}")
    
    # Using defaultdict
    result2 = group_anagrams_defaultdict(strs)
    print(f"Using defaultdict: {result2}")
    
    # Using character count
    result3 = group_anagrams_count(strs)
    print(f"Using character count: {result3}")

