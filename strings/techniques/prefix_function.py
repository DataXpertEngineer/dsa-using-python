"""
Prefix Function (KMP Preprocessing)

The prefix function (also known as failure function or LPS array) is used in
the Knuth-Morris-Pratt (KMP) algorithm for efficient string pattern matching.

The prefix function π[i] is the length of the longest proper prefix of the
substring s[0:i+1] that is also a suffix.

Why Prefix Function?
--------------------
Without prefix function (naive search):
    Pattern matching = O(n * m) where n is text length, m is pattern length
With prefix function (KMP):
    Pattern matching = O(n + m) - linear time

Useful in:
- KMP string matching algorithm
- Pattern matching preprocessing
- Finding longest border of string
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Compute Prefix Function (Language-agnostic)
# ----------------------------------------------------------------------
def compute_prefix_function(pattern: str) -> List[int]:
    """
    Compute prefix function (LPS array) for KMP algorithm.

    Args:
        pattern (str): Pattern string

    Returns:
        List[int]: Prefix function array where π[i] is length of longest
                   proper prefix that is also a suffix for pattern[0:i+1]

    Complexity:
        Time: O(m)     - Single pass through pattern of length m.
        Space: O(m)   - Stores prefix function array.
    """
    m = len(pattern)
    pi = [0] * m
    j = 0  # Length of previous longest prefix suffix
    
    for i in range(1, m):
        # If characters don't match, try shorter prefix
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        # If characters match, increment length
        if pattern[i] == pattern[j]:
            j += 1
        
        pi[i] = j
    
    return pi


# ----------------------------------------------------------------------
# Find Longest Border
# ----------------------------------------------------------------------
def longest_border(s: str) -> int:
    """
    Find length of longest border (proper prefix that is also a suffix).

    Args:
        s (str): Input string

    Returns:
        int: Length of longest border

    Complexity:
        Time: O(n)     - Uses prefix function computation.
        Space: O(n)   - Stores prefix function array.
    """
    if not s:
        return 0
    
    pi = compute_prefix_function(s)
    return pi[-1] if pi else 0


# ----------------------------------------------------------------------
# Count Occurrences of Prefix as Suffix
# ----------------------------------------------------------------------
def count_prefix_suffix_matches(s: str) -> List[int]:
    """
    Count occurrences of each prefix as a suffix in the string.

    Args:
        s (str): Input string

    Returns:
        List[int]: Array where result[i] is count of prefix s[0:i+1] as suffix

    Complexity:
        Time: O(n)     - Uses prefix function computation.
        Space: O(n)   - Stores result array.
    """
    n = len(s)
    pi = compute_prefix_function(s)
    result = [0] * n
    
    # Count occurrences using prefix function
    for i in range(n):
        if pi[i] > 0:
            result[pi[i] - 1] += 1
    
    # Accumulate counts
    for i in range(n - 2, -1, -1):
        if pi[i] > 0:
            result[pi[i] - 1] += result[i]
    
    # Add self-occurrence
    for i in range(n):
        result[i] += 1
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Prefix Function (KMP Preprocessing) Demonstration")
    
    # Compute prefix function
    pattern1 = "ababaca"
    print(f"Pattern: {pattern1}")
    pi = compute_prefix_function(pattern1)
    print(f"Prefix function: {pi}")
    print("Explanation:")
    for i, val in enumerate(pi):
        print(f"  π[{i}] = {val} (longest border of '{pattern1[:i+1]}')")
    
    # Longest border
    s2 = "ababab"
    print(f"\nString: {s2}")
    border = longest_border(s2)
    print(f"Longest border length: {border}")
    print(f"Border: '{s2[:border]}'")
    
    # Count prefix-suffix matches
    s3 = "ababab"
    print(f"\nString: {s3}")
    counts = count_prefix_suffix_matches(s3)
    print("Prefix-suffix match counts:")
    for i, count in enumerate(counts):
        print(f"  '{s3[:i+1]}' appears as suffix {count} time(s)")

