"""
Task Scheduler with Cooldown

Schedule tasks with cooldown period using queue/heap.

Problem Statement:
-------------------
Given a list of tasks and a cooldown period, find the minimum time to
complete all tasks. Same tasks must be separated by at least cooldown time.

Example:
    Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
                 Time: 0, 1, 2, 3, 4, 5, 6, 7, 8

Why Queue/Heap?
---------------
- Need to track tasks in cooldown
- Process tasks with highest frequency first
- Queue helps manage cooldown periods

Useful in:
- Task scheduling
- CPU scheduling
- Medium difficulty interview problems
"""

from typing import List
from collections import Counter, deque
import heapq


# ----------------------------------------------------------------------
# Task Scheduler (Language-agnostic)
# ----------------------------------------------------------------------
def least_interval(tasks: List[str], n: int) -> int:
    """
    Find minimum time to complete all tasks with cooldown.

    Algorithm:
    1. Count frequency of each task
    2. Use max heap to get most frequent tasks
    3. Use queue to track tasks in cooldown
    4. Process tasks, respecting cooldown period

    Args:
        tasks (List[str]): List of task names
        n (int): Cooldown period

    Returns:
        int: Minimum time to complete all tasks

    Complexity:
        Time: O(m * log k)  - m is total time, k is number of unique tasks.
        Space: O(k)        - Heap and queue storage.
    """
    if n == 0:
        return len(tasks)
    
    # Count task frequencies
    count = Counter(tasks)
    
    # Max heap (use negative for max heap)
    heap = [-freq for freq in count.values()]
    heapq.heapify(heap)
    
    # Queue: (count, time_available)
    queue = deque()
    time = 0
    
    while heap or queue:
        time += 1
        
        # Process task from heap
        if heap:
            count = heapq.heappop(heap)
            count += 1  # Decrease count (negative value)
            
            if count < 0:  # Still has tasks remaining
                queue.append((count, time + n))
        
        # Check if any task is ready (cooldown finished)
        if queue and queue[0][1] == time:
            ready_count, _ = queue.popleft()
            heapq.heappush(heap, ready_count)
    
    return time


# ----------------------------------------------------------------------
# Task Scheduler (Mathematical Approach)
# ----------------------------------------------------------------------
def least_interval_math(tasks: List[str], n: int) -> int:
    """
    Find minimum time using mathematical approach.

    Formula:
    - If most frequent task appears f times
    - Need at least (f-1) * (n+1) + count_of_max_freq tasks
    - Or just len(tasks) if no idle time needed

    Args:
        tasks (List[str]): List of task names
        n (int): Cooldown period

    Returns:
        int: Minimum time to complete all tasks

    Complexity:
        Time: O(n)     - Count frequencies and find max.
        Space: O(k)   - Frequency counter.
    """
    if n == 0:
        return len(tasks)
    
    # Count frequencies
    count = Counter(tasks)
    max_freq = max(count.values())
    
    # Count tasks with max frequency
    max_freq_count = sum(1 for freq in count.values() if freq == max_freq)
    
    # Calculate minimum time
    min_time = (max_freq - 1) * (n + 1) + max_freq_count
    
    return max(min_time, len(tasks))


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Task Scheduler with Cooldown Demonstration")
    
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(f"Tasks: {tasks}")
    print(f"Cooldown period: {n}")
    
    result = least_interval(tasks, n)
    print(f"Minimum time: {result}")
    print("Explanation: A -> B -> idle -> A -> B -> idle -> A -> B")
    print("            Time slots: 0, 1, 2, 3, 4, 5, 6, 7, 8")
    
    # Mathematical approach
    print("\n" + "="*50)
    result_math = least_interval_math(tasks, n)
    print(f"Mathematical approach result: {result_math}")
    print(f"Results match: {result == result_math}")
    
    # Another example
    print("\n" + "="*50)
    tasks2 = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    n2 = 2
    print(f"Tasks: {tasks2}")
    print(f"Cooldown period: {n2}")
    result2 = least_interval(tasks2, n2)
    print(f"Minimum time: {result2}")

