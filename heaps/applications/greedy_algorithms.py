"""
Greedy Algorithms Using Heaps

Solve greedy problems efficiently using heaps.

Common Problems:
1. Meeting Rooms / Scheduling
2. Minimum Cost to Connect Ropes
3. Task Scheduler

Why Heaps for Greedy?
---------------------
- Need to repeatedly find minimum/maximum
- Heap provides O(log n) access to extremum
- Natural fit for greedy choices

Useful in:
- Scheduling problems
- Optimization problems
- Medium difficulty interview problems
"""

from typing import List
import heapq


# ----------------------------------------------------------------------
# Minimum Cost to Connect Ropes
# ----------------------------------------------------------------------
def min_cost_connect_ropes(ropes: List[int]) -> int:
    """
    Find minimum cost to connect all ropes.

    Problem: Connect ropes with costs equal to sum of lengths.
    Goal: Minimize total cost.

    Algorithm:
    1. Always connect two shortest ropes first (greedy)
    2. Use min heap to get shortest ropes efficiently

    Args:
        ropes (List[int]): Lengths of ropes

    Returns:
        int: Minimum total cost

    Complexity:
        Time: O(n log n)  - n ropes, heap operations.
        Space: O(n)      - Heap storage.
    """
    if len(ropes) < 2:
        return 0
    
    heap = ropes.copy()
    heapq.heapify(heap)
    total_cost = 0
    
    while len(heap) > 1:
        # Get two shortest ropes
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        # Connect them
        cost = first + second
        total_cost += cost
        
        # Add connected rope back
        heapq.heappush(heap, cost)
    
    return total_cost


# ----------------------------------------------------------------------
# Meeting Rooms II (Minimum Meeting Rooms)
# ----------------------------------------------------------------------
def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Find minimum number of meeting rooms needed.

    Problem: Given meeting intervals, find minimum rooms needed.

    Algorithm:
    1. Sort intervals by start time
    2. Use min heap to track end times of ongoing meetings
    3. If new meeting starts after earliest ending, reuse room

    Args:
        intervals (List[List[int]]): List of [start, end] intervals

    Returns:
        int: Minimum number of rooms needed

    Complexity:
        Time: O(n log n)  - Sort + heap operations.
        Space: O(n)      - Heap storage.
    """
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times
    heap = []
    heapq.heappush(heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        # If current meeting starts after earliest ending, reuse room
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        
        heapq.heappush(heap, intervals[i][1])
    
    return len(heap)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Greedy Algorithms Using Heaps Demonstration")
    
    # Minimum cost to connect ropes
    ropes = [4, 3, 2, 6]
    print(f"Rope lengths: {ropes}")
    cost = min_cost_connect_ropes(ropes)
    print(f"Minimum cost to connect all ropes: {cost}")
    print("Explanation: Connect 2+3=5, then 4+5=9, then 6+9=15, total=5+9+15=29")
    
    # Meeting rooms
    print("\n" + "="*50)
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(f"Meeting intervals: {intervals}")
    rooms = min_meeting_rooms(intervals)
    print(f"Minimum meeting rooms needed: {rooms}")

