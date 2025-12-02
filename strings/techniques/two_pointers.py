"""
Two Pointers Technique for Strings

The two pointers technique uses two pointers (indices) that traverse the string
in a coordinated manner to solve problems efficiently.

Common Applications:
1. Palindrome checking
2. Anagram checking
3. Reverse string
4. Valid palindrome (with special characters)
5. String compression

Why Two Pointers?
-----------------
Without two pointers (naive approach):
    Nested loops or multiple passes = O(n²) or O(n)
With two pointers:
    Single pass from both ends = O(n)

Useful in:
- Palindrome problems
- Anagram problems
- String reversal
- Common interview problems
"""

from typing import Dict


# ----------------------------------------------------------------------
# Palindrome Check (Language-agnostic)
# ----------------------------------------------------------------------
def is_palindrome(s: str) -> bool:
    """
    Check if string is a palindrome using two pointers.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, False otherwise

    Complexity:
        Time: O(n)     - Pointers meet at center after at most n/2 comparisons.
        Space: O(1)   - Only uses two pointer indices.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


# ----------------------------------------------------------------------
# Valid Palindrome (with special characters)
# ----------------------------------------------------------------------
def is_valid_palindrome(s: str) -> bool:
    """
    Check if string is a valid palindrome (ignoring non-alphanumeric, case-insensitive).

    Args:
        s (str): Input string (may contain special characters)

    Returns:
        bool: True if valid palindrome, False otherwise

    Complexity:
        Time: O(n)     - Single pass through string, skipping non-alphanumeric.
        Space: O(1)   - Only uses pointer variables.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


# ----------------------------------------------------------------------
# Reverse String (Language-agnostic, in-place)
# ----------------------------------------------------------------------
def reverse_string(s: list[str]) -> None:
    """
    Reverse string in-place using two pointers.

    Args:
        s (list[str]): String as list of characters (modified in-place)

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


# ----------------------------------------------------------------------
# Anagram Check (Language-agnostic)
# ----------------------------------------------------------------------
def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using character frequency.

    Args:
        s1 (str): First string
        s2 (str): Second string

    Returns:
        bool: True if anagrams, False otherwise

    Complexity:
        Time: O(n)     - Counts characters in both strings.
        Space: O(k)   - Stores character frequencies, k is size of character set.
    """
    if len(s1) != len(s2):
        return False
    
    count: Dict[str, int] = {}
    
    # Count characters in s1
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    # Decrement for s2
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0


# ----------------------------------------------------------------------
# String Compression
# ----------------------------------------------------------------------
def compress_string(s: str) -> str:
    """
    Compress string using run-length encoding.

    Example: "aabcccccaaa" -> "a2b1c5a3"

    Args:
        s (str): Input string

    Returns:
        str: Compressed string

    Complexity:
        Time: O(n)     - Single pass through string.
        Space: O(n)   - Stores compressed string.
    """
    if not s:
        return s
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Two Pointers Technique for Strings Demonstration")
    
    # Palindrome check
    s1 = "racecar"
    print(f"String: {s1}")
    print(f"Is palindrome: {is_palindrome(s1)}")
    
    # Valid palindrome
    s2 = "A man, a plan, a canal: Panama"
    print(f"\nString: {s2}")
    print(f"Is valid palindrome: {is_valid_palindrome(s2)}")
    
    # Reverse string
    s3 = list("Hello")
    print(f"\nOriginal: {''.join(s3)}")
    reverse_string(s3)
    print(f"Reversed: {''.join(s3)}")
    
    # Anagram check
    s4, s5 = "listen", "silent"
    print(f"\nStrings: '{s4}' and '{s5}'")
    print(f"Are anagrams: {is_anagram(s4, s5)}")
    
    # String compression
    s6 = "aabcccccaaa"
    print(f"\nString: {s6}")
    print(f"Compressed: {compress_string(s6)}")

