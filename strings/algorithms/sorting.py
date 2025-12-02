"""
Sorting Algorithms for Strings

Sorting strings involves arranging them in lexicographic (dictionary) order.
Python provides built-in sorting, but understanding custom sorting is important.

Approaches:
1. Built-in sorted() - Uses Timsort, O(n log n)
2. Custom comparator - Sort by length, frequency, etc.
3. Radix sort - For strings of same length

Why Sort Strings?
-----------------
- Organize data alphabetically
- Group similar strings
- Prepare for binary search
- Common preprocessing step

Useful in:
- Organizing string data
- Anagram grouping
- Custom sorting requirements
- Common interview problems
"""

from typing import List, Callable, Optional
from collections import Counter


# ----------------------------------------------------------------------
# Basic String Sorting (Python built-in)
# ----------------------------------------------------------------------
def sort_strings(strings: List[str]) -> List[str]:
    """
    Sort list of strings in lexicographic order.

    Args:
        strings (List[str]): List of strings to sort

    Returns:
        List[str]: Sorted list of strings

    Complexity:
        Time: O(n * m * log n)  - n strings, average length m, comparison O(m).
        Space: O(n)            - Creates new sorted list.
    """
    return sorted(strings)


# ----------------------------------------------------------------------
# Sort by Length
# ----------------------------------------------------------------------
def sort_by_length(strings: List[str]) -> List[str]:
    """
    Sort strings by length (shortest first).

    Args:
        strings (List[str]): List of strings to sort

    Returns:
        List[str]: Strings sorted by length

    Complexity:
        Time: O(n * log n)  - Sorting n strings, length comparison O(1).
        Space: O(n)        - Creates new sorted list.
    """
    return sorted(strings, key=len)


# ----------------------------------------------------------------------
# Sort by Custom Comparator
# ----------------------------------------------------------------------
def sort_by_custom(strings: List[str], key_func: Callable[[str], int]) -> List[str]:
    """
    Sort strings using custom key function.

    Args:
        strings (List[str]): List of strings to sort
        key_func (Callable): Function that returns sort key for each string

    Returns:
        List[str]: Strings sorted by custom key

    Complexity:
        Time: O(n * log n)  - Sorting with custom key.
        Space: O(n)        - Creates new sorted list.
    """
    return sorted(strings, key=key_func)


# ----------------------------------------------------------------------
# Sort by Character Frequency
# ----------------------------------------------------------------------
def sort_by_frequency(strings: List[str]) -> List[str]:
    """
    Sort strings by character frequency (most frequent first).

    Args:
        strings (List[str]): List of strings to sort

    Returns:
        List[str]: Strings sorted by total character frequency

    Complexity:
        Time: O(n * m * log n)  - n strings, average length m, frequency counting.
        Space: O(n)            - Creates new sorted list.
    """
    def get_frequency(s: str) -> int:
        return sum(Counter(s).values())
    
    return sorted(strings, key=get_frequency, reverse=True)


# ----------------------------------------------------------------------
# Group Anagrams (Sorting-based)
# ----------------------------------------------------------------------
def group_anagrams(strings: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.

    Args:
        strings (List[str]): List of strings

    Returns:
        List[List[str]]: Groups of anagrams

    Complexity:
        Time: O(n * m * log m)  - n strings, average length m, sorting each string.
        Space: O(n * m)        - Stores grouped anagrams.
    """
    anagram_map = {}
    
    for s in strings:
        # Use sorted string as key
        key = ''.join(sorted(s))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
    
    return list(anagram_map.values())


# ----------------------------------------------------------------------
# Sort Characters in String
# ----------------------------------------------------------------------
def sort_string_chars(s: str) -> str:
    """
    Sort characters in a string.

    Args:
        s (str): Input string

    Returns:
        str: String with sorted characters

    Complexity:
        Time: O(n * log n)  - Sorting n characters.
        Space: O(n)        - Creates new string.
    """
    return ''.join(sorted(s))


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: String Sorting Algorithms Demonstration")
    
    # Basic sorting
    strings1 = ["banana", "apple", "cherry"]
    print(f"Original: {strings1}")
    print(f"Sorted: {sort_strings(strings1)}")
    
    # Sort by length
    strings2 = ["apple", "pie", "banana", "a"]
    print(f"\nOriginal: {strings2}")
    print(f"Sorted by length: {sort_by_length(strings2)}")
    
    # Group anagrams
    strings3 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"\nOriginal: {strings3}")
    grouped = group_anagrams(strings3)
    print(f"Grouped anagrams: {grouped}")
    
    # Sort characters in string
    s = "programming"
    print(f"\nString: {s}")
    print(f"Sorted characters: {sort_string_chars(s)}")

