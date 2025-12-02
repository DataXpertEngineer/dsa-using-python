"""
Sliding Window Technique for Strings

The sliding window technique maintains a "window" of characters and slides it
across the string to solve substring problems efficiently.

Common Applications:
1. Longest substring without repeating characters
2. Minimum window substring
3. Substring with exactly k distinct characters
4. Longest substring with at most k distinct characters

Why Sliding Window?
-------------------
Without sliding window (naive approach):
    Check all substrings = O(n²) or O(n³)
With sliding window:
    Single pass through string = O(n)

Useful in:
- Substring problems
- Character frequency problems
- Window optimization problems
- Common interview problems
"""

from typing import Dict


# ----------------------------------------------------------------------
# Longest Substring Without Repeating Characters
# ----------------------------------------------------------------------
def longest_substring_no_repeat(s: str) -> int:
    """
    Find length of longest substring without repeating characters.

    Args:
        s (str): Input string

    Returns:
        int: Length of longest substring without repeating characters

    Complexity:
        Time: O(n)     - Single pass through string, each character visited at most twice.
        Space: O(min(n, m)) - Hash set stores characters, m is size of character set.
    """
    if not s:
        return 0
    
    char_map: Dict[str, int] = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ----------------------------------------------------------------------
# Minimum Window Substring
# ----------------------------------------------------------------------
def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window in s which contains all characters of t.

    Args:
        s (str): Source string
        t (str): Target string

    Returns:
        str: Minimum window substring, empty string if not found

    Complexity:
        Time: O(|s| + |t|)  - Traverses both strings, each character visited at most twice.
        Space: O(|s| + |t|) - Stores character frequencies.
    """
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters in t
    need: Dict[str, int] = {}
    for char in t:
        need[char] = need.get(char, 0) + 1
    
    # Sliding window
    have: Dict[str, int] = {}
    left = 0
    min_len = float('inf')
    min_start = 0
    required = len(need)
    formed = 0
    
    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1
        
        if char in need and have[char] == need[char]:
            formed += 1
        
        # Try to shrink window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            
            left += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""


# ----------------------------------------------------------------------
# Longest Substring with At Most K Distinct Characters
# ----------------------------------------------------------------------
def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find length of longest substring with at most k distinct characters.

    Args:
        s (str): Input string
        k (int): Maximum number of distinct characters

    Returns:
        int: Length of longest substring

    Complexity:
        Time: O(n)     - Single pass through string, each character visited at most twice.
        Space: O(k)   - Hash map stores at most k distinct characters.
    """
    if not s or k == 0:
        return 0
    
    char_count: Dict[str, int] = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window if distinct chars exceed k
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ----------------------------------------------------------------------
# Substring with Exactly K Distinct Characters
# ----------------------------------------------------------------------
def substring_exactly_k_distinct(s: str, k: int) -> int:
    """
    Count substrings with exactly k distinct characters.

    Args:
        s (str): Input string
        k (int): Exact number of distinct characters

    Returns:
        int: Number of substrings with exactly k distinct characters

    Complexity:
        Time: O(n)     - Uses sliding window technique.
        Space: O(k)   - Hash map stores character frequencies.
    """
    def at_most_k(s: str, k: int) -> int:
        """Count substrings with at most k distinct characters."""
        char_count: Dict[str, int] = {}
        left = 0
        result = 0
        
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            while len(char_count) > k:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
            
            result += right - left + 1
        
        return result
    
    return at_most_k(s, k) - at_most_k(s, k - 1)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sliding Window Technique for Strings Demonstration")
    
    # Longest substring without repeating characters
    s1 = "abcabcbb"
    print(f"String: {s1}")
    print(f"Longest substring without repeating: {longest_substring_no_repeat(s1)}")
    print("Expected: 3 (abc)")
    
    # Minimum window substring
    s2 = "ADOBECODEBANC"
    t2 = "ABC"
    print(f"\nString: {s2}, Target: {t2}")
    print(f"Minimum window: '{min_window_substring(s2, t2)}'")
    print("Expected: 'BANC'")
    
    # Longest substring with k distinct
    s3 = "eceba"
    k3 = 2
    print(f"\nString: {s3}, k={k3}")
    print(f"Longest substring with at most {k3} distinct: {longest_substring_k_distinct(s3, k3)}")
    print("Expected: 3 (ece)")
    
    # Substrings with exactly k distinct
    s4 = "aabacbebebe"
    k4 = 3
    print(f"\nString: {s4}, k={k4}")
    print(f"Substrings with exactly {k4} distinct: {substring_exactly_k_distinct(s4, k4)}")

