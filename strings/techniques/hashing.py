"""
Rolling Hash Technique (Rabin-Karp)

Rolling hash is a technique used in the Rabin-Karp algorithm for efficient
substring search. It allows computing hash of a sliding window in O(1) time
after initial computation.

Why Rolling Hash?
-----------------
Without rolling hash (naive search):
    Substring search = O(n * m) where n is text length, m is pattern length
With rolling hash (Rabin-Karp):
    Average case = O(n + m), worst case = O(n * m) but rare

Useful in:
- Rabin-Karp string matching
- Substring search
- Pattern matching
- Common interview problems
"""

from typing import Optional, List


# ----------------------------------------------------------------------
# Rolling Hash Implementation (Language-agnostic)
# ----------------------------------------------------------------------
class RollingHash:
    """
    Rolling hash implementation for string matching.
    
    Uses polynomial rolling hash: hash = (s[0] * base^(n-1) + s[1] * base^(n-2) + ... + s[n-1]) % mod
    """
    
    def __init__(self, base: int = 256, mod: int = 10**9 + 7):
        """
        Initialize rolling hash.

        Args:
            base (int): Base for polynomial hash (default: 256 for ASCII)
            mod (int): Modulo to prevent overflow (default: large prime)
        """
        self.base = base
        self.mod = mod
        self.power = 1
    
    def compute_hash(self, s: str):
        """
        Compute hash of string.

        Args:
            s (str): Input string

        Returns:
            int: Hash value

        Complexity:
            Time: O(n)     - Processes each character once.
            Space: O(1)   - Only uses variables for computation.
        """
        hash_value = 0
        for char in s:
            hash_value = (hash_value * self.base + ord(char)) % self.mod
        return hash_value
    
    def roll_hash(self, old_hash: int, old_char: str, new_char: str, pattern_len: int):
        """
        Roll hash from old window to new window.

        Args:
            old_hash (int): Hash of previous window
            old_char (str): Character leaving the window
            new_char (str): Character entering the window
            pattern_len (int): Length of pattern/window

        Returns:
            int: New hash value

        Complexity:
            Time: O(1)     - Constant time hash update.
            Space: O(1)   - Only uses variables.
        """
        # Remove old character contribution
        old_hash = (old_hash - ord(old_char) * pow(self.base, pattern_len - 1, self.mod)) % self.mod
        # Add new character
        new_hash = (old_hash * self.base + ord(new_char)) % self.mod
        return new_hash


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
        Time: O(n + m) average, O(n * m) worst case (rare with good hash).
        Space: O(1)   - Only uses variables for hash computation.
    """
    if not pattern:
        return 0
    if len(pattern) > len(text):
        return None
    
    rh = RollingHash()
    pattern_hash = rh.compute_hash(pattern)
    text_hash = rh.compute_hash(text[:len(pattern)])
    
    # Precompute base power
    base_power = pow(rh.base, len(pattern) - 1, rh.mod)
    
    # Check first window
    if text_hash == pattern_hash and text[:len(pattern)] == pattern:
        return 0
    
    # Slide window
    for i in range(len(pattern), len(text)):
        # Remove leftmost character, add rightmost character
        text_hash = (text_hash - ord(text[i - len(pattern)]) * base_power) % rh.mod
        text_hash = (text_hash * rh.base + ord(text[i])) % rh.mod
        
        # Handle negative modulo
        text_hash = (text_hash + rh.mod) % rh.mod
        
        # Check if hash matches and verify (to handle collisions)
        if text_hash == pattern_hash:
            if text[i - len(pattern) + 1:i + 1] == pattern:
                return i - len(pattern) + 1
    
    return None


def rabin_karp_all_occurrences(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text using Rabin-Karp.

    Args:
        text (str): Text to search in
        pattern (str): Pattern to search for

    Returns:
        List[int]: List of all starting indices where pattern is found

    Complexity:
        Time: O(n + m) average, O(n * m) worst case.
        Space: O(k)   - Where k is number of occurrences.
    """
    if not pattern:
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []
    
    rh = RollingHash()
    pattern_hash = rh.compute_hash(pattern)
    text_hash = rh.compute_hash(text[:len(pattern)])
    base_power = pow(rh.base, len(pattern) - 1, rh.mod)
    
    occurrences = []
    
    if text_hash == pattern_hash and text[:len(pattern)] == pattern:
        occurrences.append(0)
    
    for i in range(len(pattern), len(text)):
        text_hash = (text_hash - ord(text[i - len(pattern)]) * base_power) % rh.mod
        text_hash = (text_hash * rh.base + ord(text[i])) % rh.mod
        text_hash = (text_hash + rh.mod) % rh.mod
        
        if text_hash == pattern_hash:
            if text[i - len(pattern) + 1:i + 1] == pattern:
                occurrences.append(i - len(pattern) + 1)
    
    return occurrences


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Rolling Hash (Rabin-Karp) Demonstration")
    
    # Rabin-Karp search
    text1 = "ABABDABACDABABCABCABAB"
    pattern1 = "ABABCABAB"
    print(f"Text: {text1}")
    print(f"Pattern: {pattern1}")
    result = rabin_karp_search(text1, pattern1)
    print(f"Pattern found at index: {result}")
    
    # All occurrences
    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    print(f"\nText: {text2}")
    print(f"Pattern: {pattern2}")
    occurrences = rabin_karp_all_occurrences(text2, pattern2)
    print(f"All occurrences at indices: {occurrences}")

