"""
Reverse String / Words Problem

Reverse a string or words in a string.

Problem Statement:
------------------
1. Reverse String: Reverse a string in-place (if mutable) or return reversed copy.
2. Reverse Words: Reverse the order of words in a string.

Example:
    Input: "hello world"
    Output (reverse string): "dlrow olleh"
    Output (reverse words): "world hello"

Useful in:
- String manipulation
- Two pointers technique
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Reverse String (Language-agnostic)
# ----------------------------------------------------------------------
def reverse_string(s: List[str]) -> None:
    """
    Reverse string in-place using two pointers.

    Args:
        s (List[str]): String as list of characters (modified in-place)

    Returns:
        None: String is reversed in-place

    Complexity:
        Time: O(n)     - Swaps characters from both ends toward center, n/2 swaps.
        Space: O(1)   - Only uses variables for indices.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_copy(s: str) -> str:
    """
    Create reversed copy of string.

    Args:
        s (str): Input string

    Returns:
        str: Reversed string

    Complexity:
        Time: O(n)     - Creates new string with reversed characters.
        Space: O(n)   - Creates new string of length n.
    """
    return s[::-1]


# ----------------------------------------------------------------------
# Reverse Words in String
# ----------------------------------------------------------------------
def reverse_words(s: str) -> str:
    """
    Reverse the order of words in a string.

    Args:
        s (str): Input string with words separated by spaces

    Returns:
        str: String with words reversed

    Complexity:
        Time: O(n)     - Processes string once to split and reverse.
        Space: O(n)   - Stores words and result string.
    """
    words = s.split()
    return " ".join(reversed(words))


def reverse_words_in_place(s: List[str]) -> None:
    """
    Reverse words in-place (string as list of characters).

    Algorithm:
    1. Reverse entire string
    2. Reverse each word individually

    Args:
        s (List[str]): String as list of characters (modified in-place)

    Returns:
        None: Words are reversed in-place

    Complexity:
        Time: O(n)     - Two passes: reverse all, reverse each word.
        Space: O(1)   - Only uses variables for indices.
    """
    # Reverse entire string
    reverse_string(s)
    
    # Reverse each word
    start = 0
    for i in range(len(s) + 1):
        if i == len(s) or s[i] == ' ':
            # Reverse word from start to i-1
            left = start
            right = i - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            start = i + 1


# ----------------------------------------------------------------------
# Reverse Words II (Preserve spaces)
# ----------------------------------------------------------------------
def reverse_words_preserve_spaces(s: str) -> str:
    """
    Reverse words while preserving multiple spaces.

    Args:
        s (str): Input string

    Returns:
        str: String with reversed words, spaces preserved

    Complexity:
        Time: O(n)     - Processes string once.
        Space: O(n)   - Stores result string.
    """
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Reverse String / Words Problem Demonstration")
    
    # Reverse string
    s1 = list("hello")
    print(f"Original: {''.join(s1)}")
    reverse_string(s1)
    print(f"Reversed: {''.join(s1)}")
    
    # Reverse string copy
    s2 = "Python"
    print(f"\nOriginal: {s2}")
    print(f"Reversed copy: {reverse_string_copy(s2)}")
    
    # Reverse words
    s3 = "the sky is blue"
    print(f"\nOriginal: '{s3}'")
    print(f"Reversed words: '{reverse_words(s3)}'")
    print("Expected: 'blue is sky the'")
    
    # Reverse words in place
    s4 = list("the sky is blue")
    print(f"\nOriginal: {''.join(s4)}")
    reverse_words_in_place(s4)
    print(f"Reversed words (in-place): {''.join(s4)}")
    
    # Reverse words preserve spaces
    s5 = "Let's take LeetCode contest"
    print(f"\nOriginal: '{s5}'")
    print(f"Reverse words (preserve spaces): '{reverse_words_preserve_spaces(s5)}'")

