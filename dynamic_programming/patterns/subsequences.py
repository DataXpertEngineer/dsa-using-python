"""
DP on Subsequences

Dynamic programming problems involving subsequences.

Common Problems:
- Longest Increasing Subsequence (LIS)
- Longest Common Subsequence (LCS)
- Count distinct subsequences
- Subsequence sum problems

Why Subsequences?
-----------------
- Common DP pattern
- String/array problems
- Foundation for many problems
- Common interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Longest Increasing Subsequence (LIS)
# ----------------------------------------------------------------------
def lis_tabulation(arr: List[int]) -> int:
    """
    Find length of longest increasing subsequence.

    Args:
        arr (List[int]): Input array

    Returns:
        int: LIS length

    Complexity:
        Time: O(n²)     - For each element, check previous.
        Space: O(n)    - DP array.
    """
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


# ----------------------------------------------------------------------
# LIS - O(n log n) Solution
# ----------------------------------------------------------------------
def lis_optimized(arr: List[int]) -> int:
    """
    LIS using binary search (O(n log n)).

    Args:
        arr (List[int]): Input array

    Returns:
        int: LIS length

    Complexity:
        Time: O(n log n)  - Binary search for each element.
        Space: O(n)      - Tail array.
    """
    if not arr:
        return 0
    
    tail = []
    
    for num in arr:
        # Binary search for insertion point
        left, right = 0, len(tail)
        while left < right:
            mid = (left + right) // 2
            if tail[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tail):
            tail.append(num)
        else:
            tail[left] = num
    
    return len(tail)


# ----------------------------------------------------------------------
# Count Distinct Subsequences
# ----------------------------------------------------------------------
def count_distinct_subsequences(s: str) -> int:
    """
    Count distinct subsequences of string.

    Args:
        s (str): Input string

    Returns:
        int: Count of distinct subsequences

    Complexity:
        Time: O(n)     - Single pass.
        Space: O(n)    - Last occurrence map.
    """
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty subsequence
    last_occurrence: Dict[str, int] = {}
    
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]
        
        if s[i - 1] in last_occurrence:
            dp[i] -= dp[last_occurrence[s[i - 1]] - 1]
        
        last_occurrence[s[i - 1]] = i
    
    return dp[n] - 1  # Exclude empty subsequence


# ----------------------------------------------------------------------
# Maximum Sum Increasing Subsequence
# ----------------------------------------------------------------------
def max_sum_increasing_subsequence(arr: List[int]) -> int:
    """
    Find maximum sum of increasing subsequence.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Maximum sum

    Complexity:
        Time: O(n²)     - For each element, check previous.
        Space: O(n)    - DP array.
    """
    if not arr:
        return 0
    
    n = len(arr)
    dp = arr.copy()  # Initialize with array values
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    return max(dp)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: DP on Subsequences Demonstration")
    
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(f"Array: {arr}")
    
    lis_length = lis_tabulation(arr)
    print(f"LIS length (O(n²)): {lis_length}")
    
    lis_length_opt = lis_optimized(arr)
    print(f"LIS length (O(n log n)): {lis_length_opt}")
    
    max_sum = max_sum_increasing_subsequence(arr)
    print(f"Maximum sum increasing subsequence: {max_sum}")
    
    print("\n" + "="*50)
    s = "gfg"
    distinct_count = count_distinct_subsequences(s)
    print(f"String: {s}")
    print(f"Distinct subsequences: {distinct_count}")

