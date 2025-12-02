"""
Palindrome Check Problem

Determine if a string is a palindrome.

Problem Statement:
------------------
Given a string s, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Useful in:
- Two pointers technique
- String manipulation
- Common interview problem
"""


# ----------------------------------------------------------------------
# Basic Palindrome Check (Language-agnostic)
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
# Palindrome Check (Recursive)
# ----------------------------------------------------------------------
def is_palindrome_recursive(s: str) -> bool:
    """
    Check if string is a palindrome using recursive approach.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, False otherwise

    Complexity:
        Time: O(n)     - Recursively checks n/2 characters.
        Space: O(n)   - Recursion stack depth is n/2.
    """
    def _check(left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return _check(left + 1, right - 1)
    
    return _check(0, len(s) - 1)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Palindrome Check Problem Demonstration")
    
    # Basic palindrome
    s1 = "racecar"
    print(f"String: {s1}")
    print(f"Is palindrome: {is_palindrome(s1)}")
    
    # Not a palindrome
    s2 = "hello"
    print(f"\nString: {s2}")
    print(f"Is palindrome: {is_palindrome(s2)}")
    
    # Valid palindrome with special characters
    s3 = "A man, a plan, a canal: Panama"
    print(f"\nString: {s3}")
    print(f"Is valid palindrome: {is_valid_palindrome(s3)}")
    print("Expected: True")
    
    # Recursive check
    s4 = "level"
    print(f"\nString: {s4}")
    print(f"Is palindrome (recursive): {is_palindrome_recursive(s4)}")

