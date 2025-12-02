"""
String Searching Algorithms

String searching (pattern matching) algorithms find occurrences of a pattern
within a text string.

Algorithms:
1. Naive search: Simple but inefficient O(n*m)
2. KMP (Knuth-Morris-Pratt): Efficient O(n+m) using prefix function
3. Rabin-Karp: Hash-based O(n+m) average case

Why Different Algorithms?
--------------------------
- Naive: Simple to understand, good for small patterns
- KMP: Guaranteed linear time, no hash collisions
- Rabin-Karp: Simple implementation, good average case

Useful in:
- Text processing
- Pattern matching
- Search engines
- Common interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Naive Search (Language-agnostic)
# ----------------------------------------------------------------------
def naive_search(text: str, pattern: str) -> Optional[int]:
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


def naive_search_all(text: str, pattern: str) -> List[int]:
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
def kmp_search(text: str, pattern: str) -> Optional[int]:
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


def kmp_search_all(text: str, pattern: str) -> List[int]:
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
# Rabin-Karp Algorithm
# ----------------------------------------------------------------------
def rabin_karp_search(text: str, pattern: str) -> Optional[int]:
    """
    Search for pattern in text using Rabin-Karp algorithm.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        Optional[int]: First index where pattern is found, None if not found

    Complexity:
        Time: O(n + m) average, O(n * m) worst case (rare hash collisions).
        Space: O(1)   - Only uses variables for hash computation.
    """
    if not pattern:
        return 0
    if len(pattern) > len(text):
        return None
    
    base = 256
    mod = 10**9 + 7
    
    def compute_hash(s: str) -> int:
        hash_val = 0
        for char in s:
            hash_val = (hash_val * base + ord(char)) % mod
        return hash_val
    
    pattern_hash = compute_hash(pattern)
    text_hash = compute_hash(text[:len(pattern)])
    base_power = pow(base, len(pattern) - 1, mod)
    
    if text_hash == pattern_hash and text[:len(pattern)] == pattern:
        return 0
    
    for i in range(len(pattern), len(text)):
        text_hash = (text_hash - ord(text[i - len(pattern)]) * base_power) % mod
        text_hash = (text_hash * base + ord(text[i])) % mod
        text_hash = (text_hash + mod) % mod
        
        if text_hash == pattern_hash:
            if text[i - len(pattern) + 1:i + 1] == pattern:
                return i - len(pattern) + 1
    
    return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: String Searching Algorithms Demonstration")
    
    text = "ABABDABACDABABCABCABAB"
    pattern = "ABABCABAB"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    
    # Naive search
    result_naive = naive_search(text, pattern)
    print(f"\nNaive search: Found at index {result_naive}")
    
    # KMP search
    result_kmp = kmp_search(text, pattern)
    print(f"KMP search: Found at index {result_kmp}")
    
    # Rabin-Karp search
    result_rk = rabin_karp_search(text, pattern)
    print(f"Rabin-Karp search: Found at index {result_rk}")
    
    # All occurrences
    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    print(f"\nText: {text2}")
    print(f"Pattern: {pattern2}")
    all_occurrences = kmp_search_all(text2, pattern2)
    print(f"All occurrences (KMP): {all_occurrences}")

