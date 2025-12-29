"""
Interval Scheduling Problem

Schedule maximum number of non-overlapping intervals.

Problem Statement:
-------------------
Given list of intervals [start, end], select maximum number of
non-overlapping intervals.

Why Greedy?
-----------
- Greedy choice: Always pick interval that ends earliest
- This leaves maximum room for future intervals
- Optimal substructure property holds

Useful in:
- Resource allocation
- Meeting room scheduling
- Common interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Interval Scheduling - Greedy (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def interval_scheduling(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Find maximum number of non-overlapping intervals using greedy.

    Algorithm:
    1. Sort intervals by end time
    2. Select first interval
    3. For each subsequent interval:
       - If it doesn't overlap with last selected, select it

    Args:
        intervals (List[Tuple[int, int]]): List of (start, end) intervals

    Returns:
        List[Tuple[int, int]]: Selected intervals

    Complexity:
        Time: O(n log n)  - Sort intervals.
        Space: O(n)      - Storage for result.
    """
    if not intervals:
        return []
    
    # Sort by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    selected = [sorted_intervals[0]]
    last_end = sorted_intervals[0][1]
    
    for start, end in sorted_intervals[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected


# ----------------------------------------------------------------------
# Interval Scheduling - Count Only
# ----------------------------------------------------------------------
def max_intervals_count(intervals: List[Tuple[int, int]]) -> int:
    """
    Count maximum number of non-overlapping intervals.

    Args:
        intervals (List[Tuple[int, int]]): List of intervals

    Returns:
        int: Maximum count

    Complexity:
        Time: O(n log n)  - Sort intervals.
        Space: O(1)      - Only uses counter.
    """
    if not intervals:
        return 0
    
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    count = 1
    last_end = sorted_intervals[0][1]
    
    for start, end in sorted_intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count


# ----------------------------------------------------------------------
# Interval Scheduling - Weighted
# ----------------------------------------------------------------------
def weighted_interval_scheduling(intervals: List[Tuple[int, int, int]]) -> int:
    """
    Find maximum weight of non-overlapping intervals.

    Args:
        intervals (List[Tuple[int, int, int]]): List of (start, end, weight)

    Returns:
        int: Maximum total weight

    Complexity:
        Time: O(n²)     - For each interval, find previous compatible.
        Space: O(n)    - DP array.
    """
    if not intervals:
        return 0
    
    # Sort by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    n = len(sorted_intervals)
    
    # DP: dp[i] = max weight using first i intervals
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        start, end, weight = sorted_intervals[i - 1]
        
        # Don't include current interval
        dp[i] = dp[i - 1]
        
        # Find last compatible interval
        for j in range(i - 1, 0, -1):
            prev_start, prev_end, _ = sorted_intervals[j - 1]
            if prev_end <= start:
                dp[i] = max(dp[i], dp[j] + weight)
                break
        else:
            # No compatible interval, take current alone
            dp[i] = max(dp[i], weight)
    
    return dp[n]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Interval Scheduling Demonstration")
    
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(f"Intervals: {intervals}")
    
    selected = interval_scheduling(intervals)
    print(f"Selected intervals: {selected}")
    print(f"Maximum count: {max_intervals_count(intervals)}")
    
    # Weighted
    print("\n" + "="*50)
    weighted_intervals = [(1, 4, 3), (3, 5, 2), (0, 6, 1), (5, 7, 4), (8, 9, 2)]
    print(f"Weighted intervals: {weighted_intervals}")
    max_weight = weighted_interval_scheduling(weighted_intervals)
    print(f"Maximum weight: {max_weight}")

