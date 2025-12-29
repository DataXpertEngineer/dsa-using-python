"""
Palindrome Partitioning

Partition string into all possible palindrome substrings using backtracking.

Problem Statement:
-------------------
Given a string, partition it such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning.

Example:
    Input: "aab"
    Output: [["a","a","b"], ["aa","b"]]

Why Backtracking?
-----------------
- Try partitioning at each position
- Check if substring is palindrome
- If valid, recurse with remaining string
- If entire string partitioned, save partition
- Backtrack to try other partitions

Useful in:
- String partitioning
- Palindrome problems
- Medium difficulty interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Palindrome Partitioning (Language-agnostic)
# ----------------------------------------------------------------------
def partition_palindrome(s: str) -> List[List[str]]:
    """
    Find all palindrome partitions of string.

    Algorithm:
    1. Try partitioning at each position
    2. Check if substring is palindrome
    3. If valid, recurse with remaining string
    4. If entire string partitioned, save partition
    5. Backtrack to try other partitions

    Args:
        s (str): Input string

    Returns:
        List[List[str]]: List of all palindrome partitions

    Complexity:
        Time: O(2^n * n)  - 2^n partitions, each checked in O(n).
        Space: O(n)      - Recursion depth + partition storage.
    """
    partitions: List[List[str]] = []
    
    def is_palindrome(start: int, end: int) -> bool:
        """Check if substring is palindrome."""
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def backtrack(current: List[str], start: int) -> None:
        """Backtrack to find all partitions."""
        # Base case: entire string partitioned
        if start == len(s):
            partitions.append(current.copy())
            return
        
        # Try partitioning at each position
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                # Choose
                current.append(s[start:end + 1])
                
                # Recurse
                backtrack(current, end + 1)
                
                # Backtrack
                current.pop()
    
    backtrack([], 0)
    return partitions


# ----------------------------------------------------------------------
# Palindrome Partitioning (With Memoization)
# ----------------------------------------------------------------------
def partition_palindrome_memo(s: str) -> List[List[str]]:
    """
    Find all palindrome partitions with memoization.

    Args:
        s (str): Input string

    Returns:
        List[List[str]]: List of all palindrome partitions

    Complexity:
        Time: O(2^n * n)  - Still exponential.
        Space: O(n^2)    - Memo storage.
    """
    partitions: List[List[str]] = []
    memo: dict[tuple[int, int], bool] = {}
    
    def is_palindrome(start: int, end: int) -> bool:
        """Check palindrome with memoization."""
        if (start, end) in memo:
            return memo[(start, end)]
        
        i, j = start, end
        while i < j:
            if s[i] != s[j]:
                memo[(start, end)] = False
                return False
            i += 1
            j -= 1
        
        memo[(start, end)] = True
        return True
    
    def backtrack(current: List[str], start: int) -> None:
        if start == len(s):
            partitions.append(current.copy())
            return
        
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                current.append(s[start:end + 1])
                backtrack(current, end + 1)
                current.pop()
    
    backtrack([], 0)
    return partitions


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Palindrome Partitioning Demonstration")
    
    s = "aab"
    print(f"String: '{s}'")
    
    partitions = partition_palindrome(s)
    print(f"Palindrome partitions: {partitions}")
    print("Explanation: ['a','a','b'] and ['aa','b']")
    
    # Another example
    print("\n" + "="*50)
    s2 = "racecar"
    print(f"String: '{s2}'")
    partitions2 = partition_palindrome(s2)
    print(f"Number of partitions: {len(partitions2)}")
    print(f"Sample partitions: {partitions2[:3]}")

