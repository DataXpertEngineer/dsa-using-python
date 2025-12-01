"""
Prefix Sum Technique for Arrays

The prefix sum array helps answer **range sum queries** efficiently.

Instead of summing elements from L to R repeatedly, we preprocess the array
into a prefix sum array, where:

    prefix[i] = sum of elements from index 0 to i

Then any range sum can be computed in O(1):

    sum[L:R] = prefix[R] - prefix[L-1]  (if L > 0)
    sum[0:R] = prefix[R]                (if L == 0)

Why Prefix Sum?
---------------
Without prefix sums (naive approach):
    Query sum in a range = O(n) each time
With prefix sums:
    Preprocessing = O(n)
    Range sum query = O(1)

Useful in:
- Subarray sum problems
- Sliding window optimizations
- Frequency or cumulative distributions
- Competitive programming & interviews
"""

from typing import List


# ----------------------------------------------------------------------
# Brute-force / Naive Approach
# ----------------------------------------------------------------------
def range_sum_naive(arr: List[int], left: int, right: int) -> int:
    """
    Compute the sum from index left to right (inclusive) using naive summation.

    Args:
        arr (List[int]): Input array
        left (int): Start index
        right (int): End index

    Returns:
        int: Sum of elements from left to right

    Complexity:
        Time: O(n) per query
        Space: O(1)
    """
    return sum(arr[left:right + 1])


# ----------------------------------------------------------------------
# Prefix Sum Approach (Optimized)
# ----------------------------------------------------------------------
def build_prefix_sum(arr: List[int]) -> List[int]:
    """
    Build prefix sum array.

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Prefix sum array

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    prefix = [0] * len(arr)
    running_sum = 0
    for i, num in enumerate(arr):
        running_sum += num
        prefix[i] = running_sum
    return prefix


def range_sum_prefix(prefix: List[int], left: int, right: int) -> int:
    """
    Compute range sum using a prefix sum array.

    Args:
        prefix (List[int]): Prefix sum array
        left (int): Start index
        right (int): End index

    Returns:
        int: Sum of elements from left to right

    Complexity:
        Time: O(1)
        Space: O(1)
    """
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Prefix Sum Demonstration")

    arr = [2, 4, 1, 3, 5]
    print("Original array:", arr)

    # Naive approach
    print("\nNaive Range Sum Queries:")
    print("Sum [0:2] ->", range_sum_naive(arr, 0, 2))  # 2+4+1 = 7
    print("Sum [1:3] ->", range_sum_naive(arr, 1, 3))  # 4+1+3 = 8
    print("Sum [2:4] ->", range_sum_naive(arr, 2, 4))  # 1+3+5 = 9

    # Prefix sum approach
    prefix = build_prefix_sum(arr)
    print("\nPrefix sum array:", prefix)
    print("\nPrefix Sum Range Queries:")
    print("Sum [0:2] ->", range_sum_prefix(prefix, 0, 2))
    print("Sum [1:3] ->", range_sum_prefix(prefix, 1, 3))
    print("Sum [2:4] ->", range_sum_prefix(prefix, 2, 4))
