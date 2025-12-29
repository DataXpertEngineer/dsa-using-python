"""
Activity Selection Problem

Select maximum number of activities that don't overlap.

Problem Statement:
-------------------
Given n activities with start and finish times, select maximum
number of activities that can be performed by a single person.

Why Greedy?
-----------
- Greedy choice: Always pick activity that finishes earliest
- This leaves maximum time for remaining activities
- Optimal substructure property holds

Useful in:
- Resource scheduling
- Common interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Activity Selection - Greedy (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def activity_selection(activities: List[Tuple[int, int]]) -> List[int]:
    """
    Select maximum activities using greedy algorithm.

    Algorithm:
    1. Sort activities by finish time
    2. Select first activity
    3. For each subsequent activity:
       - If start >= last finish, select it

    Args:
        activities (List[Tuple[int, int]]): List of (start, finish) times

    Returns:
        List[int]: Indices of selected activities

    Complexity:
        Time: O(n log n)  - Sort activities.
        Space: O(n)      - Storage for result.
    """
    if not activities:
        return []
    
    # Sort by finish time, keep original indices
    indexed = [(i, start, finish) for i, (start, finish) in enumerate(activities)]
    indexed.sort(key=lambda x: x[2])  # Sort by finish time
    
    selected = [indexed[0][0]]  # First activity
    last_finish = indexed[0][2]
    
    for i, start, finish in indexed[1:]:
        if start >= last_finish:
            selected.append(i)
            last_finish = finish
    
    return selected


# ----------------------------------------------------------------------
# Activity Selection - Count Only
# ----------------------------------------------------------------------
def max_activities_count(activities: List[Tuple[int, int]]) -> int:
    """
    Count maximum number of activities.

    Args:
        activities (List[Tuple[int, int]]): List of activities

    Returns:
        int: Maximum count

    Complexity:
        Time: O(n log n)  - Sort activities.
        Space: O(1)      - Only uses counter.
    """
    if not activities:
        return 0
    
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    count = 1
    last_finish = sorted_activities[0][1]
    
    for start, finish in sorted_activities[1:]:
        if start >= last_finish:
            count += 1
            last_finish = finish
    
    return count


# ----------------------------------------------------------------------
# Activity Selection - With Weights
# ----------------------------------------------------------------------
def weighted_activity_selection(activities: List[Tuple[int, int, int]]) -> int:
    """
    Find maximum total weight of non-overlapping activities.

    Args:
        activities (List[Tuple[int, int, int]]): List of (start, finish, weight)

    Returns:
        int: Maximum total weight

    Complexity:
        Time: O(n²)     - For each activity, find previous compatible.
        Space: O(n)    - DP array.
    """
    if not activities:
        return 0
    
    # Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    n = len(sorted_activities)
    
    # DP: dp[i] = max weight using first i activities
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        start, finish, weight = sorted_activities[i - 1]
        
        # Don't include current activity
        dp[i] = dp[i - 1]
        
        # Find last compatible activity
        for j in range(i - 1, 0, -1):
            prev_start, prev_finish, _ = sorted_activities[j - 1]
            if prev_finish <= start:
                dp[i] = max(dp[i], dp[j] + weight)
                break
        else:
            # No compatible activity, take current alone
            dp[i] = max(dp[i], weight)
    
    return dp[n]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Activity Selection Demonstration")
    
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(f"Activities (start, finish): {activities}")
    
    selected = activity_selection(activities)
    print(f"Selected activity indices: {selected}")
    print(f"Selected activities: {[activities[i] for i in selected]}")
    print(f"Maximum count: {max_activities_count(activities)}")
    
    # Weighted
    print("\n" + "="*50)
    weighted_activities = [(1, 4, 3), (3, 5, 2), (0, 6, 1), (5, 7, 4), (8, 9, 2)]
    print(f"Weighted activities (start, finish, weight): {weighted_activities}")
    max_weight = weighted_activity_selection(weighted_activities)
    print(f"Maximum total weight: {max_weight}")

