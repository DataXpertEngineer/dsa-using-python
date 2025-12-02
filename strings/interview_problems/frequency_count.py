"""
Character Frequency Count Problem

Count the frequency of each character in a string.

Problem Statement:
------------------
Given a string, count the frequency of each character.

Example:
    Input: s = "hello"
    Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Variations:
- Count all characters
- Count only alphabetic characters
- Find most frequent character
- Count words instead of characters

Useful in:
- Character analysis
- Hash tables
- Common interview problem
"""

from typing import Dict
from collections import Counter, defaultdict


# ----------------------------------------------------------------------
# Dictionary Approach (Language-agnostic)
# ----------------------------------------------------------------------
def count_frequency(s: str) -> Dict[str, int]:
    """
    Count frequency of each character in string.

    Args:
        s (str): Input string

    Returns:
        Dict[str, int]: Dictionary mapping character to frequency

    Complexity:
        Time: O(n)     - Processes each character once.
        Space: O(k)   - Stores frequency for each unique character, k is character set size.
    """
    frequency: Dict[str, int] = {}
    
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    
    return frequency


# ----------------------------------------------------------------------
# Using DefaultDict (Python-specific)
# ----------------------------------------------------------------------
def count_frequency_defaultdict(s: str) -> Dict[str, int]:
    """
    Count frequency using defaultdict.

    Args:
        s (str): Input string

    Returns:
        Dict[str, int]: Dictionary mapping character to frequency

    Complexity:
        Time: O(n)     - Processes each character once.
        Space: O(k)   - Stores frequency for each unique character.
    """
    frequency = defaultdict(int)
    
    for char in s:
        frequency[char] += 1
    
    return dict(frequency)


# ----------------------------------------------------------------------
# Using Counter (Python-specific)
# ----------------------------------------------------------------------
def count_frequency_counter(s: str) -> Dict[str, int]:
    """
    Count frequency using Python's Counter.

    Args:
        s (str): Input string

    Returns:
        Dict[str, int]: Dictionary mapping character to frequency

    Complexity:
        Time: O(n)     - Counter counts all characters in one pass.
        Space: O(k)   - Counter stores frequency for each unique character.
    """
    return dict(Counter(s))


# ----------------------------------------------------------------------
# Most Frequent Character
# ----------------------------------------------------------------------
def most_frequent_char(s: str) -> tuple[str, int]:
    """
    Find the most frequent character and its count.

    Args:
        s (str): Input string

    Returns:
        tuple: (Most frequent character, its count)

    Complexity:
        Time: O(n)     - Counts characters and finds maximum.
        Space: O(k)   - Stores character frequencies.
    """
    if not s:
        return ("", 0)
    
    frequency = count_frequency(s)
    max_char = max(frequency, key=frequency.get)
    return (max_char, frequency[max_char])


# ----------------------------------------------------------------------
# Count Only Alphabetic Characters
# ----------------------------------------------------------------------
def count_alphabetic(s: str) -> Dict[str, int]:
    """
    Count frequency of only alphabetic characters (ignore digits, spaces, etc.).

    Args:
        s (str): Input string

    Returns:
        Dict[str, int]: Dictionary mapping alphabetic character to frequency

    Complexity:
        Time: O(n)     - Processes each character once.
        Space: O(k)   - Stores frequency for alphabetic characters only.
    """
    frequency: Dict[str, int] = {}
    
    for char in s:
        if char.isalpha():
            frequency[char.lower()] = frequency.get(char.lower(), 0) + 1
    
    return frequency


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Character Frequency Count Problem Demonstration")
    
    # Count all characters
    s1 = "hello world"
    print(f"String: '{s1}'")
    freq1 = count_frequency(s1)
    print(f"Character frequencies: {freq1}")
    
    # Most frequent character
    s2 = "programming"
    print(f"\nString: '{s2}'")
    char, count = most_frequent_char(s2)
    print(f"Most frequent character: '{char}' (appears {count} times)")
    
    # Count only alphabetic
    s3 = "Hello World 123!"
    print(f"\nString: '{s3}'")
    alphabetic_freq = count_alphabetic(s3)
    print(f"Alphabetic frequencies: {alphabetic_freq}")

