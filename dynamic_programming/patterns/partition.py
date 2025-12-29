"""
DP on Partitioning

Dynamic programming problems involving partitioning.

Common Problems:
- Partition Equal Sum
- Palindrome Partitioning
- Partition Array for Maximum Sum
- Minimum Cost to Cut Stick

Why Partitioning?
-----------------
- Common DP pattern
- Optimization problems
- Foundation for many problems
- Medium difficulty interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Partition Equal Sum
# ----------------------------------------------------------------------
def can_partition_equal_sum(nums: List[int]) -> bool:
    """
    Check if array can be partitioned into two equal sum subsets.

    Args:
        nums (List[int]): Input array

    Returns:
        bool: True if partitionable

    Complexity:
        Time: O(n * sum)  - Fill DP table.
        Space: O(sum)     - DP array.
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


# ----------------------------------------------------------------------
# Palindrome Partitioning - Minimum Cuts
# ----------------------------------------------------------------------
def min_palindrome_cuts(s: str) -> int:
    """
    Find minimum cuts to partition string into palindromes.

    Args:
        s (str): Input string

    Returns:
        int: Minimum cuts

    Complexity:
        Time: O(n²)     - Check palindromes + DP.
        Space: O(n²)    - Palindrome table.
    """
    n = len(s)
    
    # Precompute palindrome table
    is_palindrome = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_palindrome[i][i] = True
    
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True
    
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
    
    # DP: minimum cuts for substring [0..i]
    dp = [0] * n
    
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            dp[i] = i
            for j in range(i):
                if is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n - 1]


# ----------------------------------------------------------------------
# Partition Array for Maximum Sum
# ----------------------------------------------------------------------
def max_sum_after_partitioning(arr: List[int], k: int) -> int:
    """
    Partition array into subarrays of length at most k, maximize sum.

    Args:
        arr (List[int]): Input array
        k (int): Maximum subarray length

    Returns:
        int: Maximum sum

    Complexity:
        Time: O(n * k)  - For each position, check k previous.
        Space: O(n)     - DP array.
    """
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
    
    return dp[n]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: DP on Partitioning Demonstration")
    
    nums = [1, 5, 11, 5]
    print(f"Array: {nums}")
    can_partition = can_partition_equal_sum(nums)
    print(f"Can partition into equal sum: {can_partition}")
    
    print("\n" + "="*50)
    s = "aab"
    min_cuts = min_palindrome_cuts(s)
    print(f"String: {s}")
    print(f"Minimum palindrome cuts: {min_cuts}")
    
    print("\n" + "="*50)
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    max_sum = max_sum_after_partitioning(arr, k)
    print(f"Array: {arr}, k = {k}")
    print(f"Maximum sum after partitioning: {max_sum}")

