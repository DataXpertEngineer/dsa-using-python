"""
CPU Scheduling Algorithms

Implement common CPU scheduling algorithms using queues.

Scheduling Algorithms:
1. First Come First Served (FCFS)
2. Round Robin (RR)
3. Shortest Job First (SJF)

Why Queue?
----------
- Tasks arrive in order (FIFO)
- Need to process tasks sequentially
- Queue naturally models task scheduling

Useful in:
- Operating systems
- Task scheduling
- Process management
- Medium difficulty interview problems
"""

from typing import List, Tuple, Optional
from collections import deque


class Task:
    """
    Task class representing a process/job.
    """
    def __init__(self, name: str, arrival_time: int, burst_time: int):
        """
        Initialize a task.

        Args:
            name: Task name/ID
            arrival_time: Time when task arrives
            burst_time: Time required to complete task
        """
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


# ----------------------------------------------------------------------
# First Come First Served (FCFS)
# ----------------------------------------------------------------------
def fcfs_scheduling(tasks: List[Task]) -> List[Task]:
    """
    First Come First Served scheduling algorithm.

    Algorithm:
    1. Sort tasks by arrival time
    2. Process tasks in order
    3. Calculate completion, turnaround, and waiting times

    Args:
        tasks (List[Task]): List of tasks to schedule

    Returns:
        List[Task]: Tasks with calculated times

    Complexity:
        Time: O(n log n)  - Sorting tasks by arrival time.
        Space: O(n)     - Stores sorted tasks.
    """
    # Sort by arrival time
    sorted_tasks = sorted(tasks, key=lambda t: t.arrival_time)
    
    current_time = 0
    
    for task in sorted_tasks:
        # Wait if task hasn't arrived
        if current_time < task.arrival_time:
            current_time = task.arrival_time
        
        # Process task
        task.completion_time = current_time + task.burst_time
        task.turnaround_time = task.completion_time - task.arrival_time
        task.waiting_time = task.turnaround_time - task.burst_time
        
        current_time = task.completion_time
    
    return sorted_tasks


# ----------------------------------------------------------------------
# Round Robin (RR)
# ----------------------------------------------------------------------
def round_robin_scheduling(tasks: List[Task], time_quantum: int) -> List[Task]:
    """
    Round Robin scheduling algorithm.

    Algorithm:
    1. Sort tasks by arrival time
    2. Use queue to process tasks
    3. Each task gets time_quantum time
    4. If not complete, add back to queue

    Args:
        tasks (List[Task]): List of tasks to schedule
        time_quantum (int): Time slice for each task

    Returns:
        List[Task]: Tasks with calculated times

    Complexity:
        Time: O(n * q)  - n tasks, each may need multiple quanta.
        Space: O(n)    - Queue storage.
    """
    # Sort by arrival time
    sorted_tasks = sorted(tasks, key=lambda t: t.arrival_time)
    
    queue = deque()
    current_time = 0
    task_index = 0
    completed_tasks: List[Task] = []
    
    while task_index < len(sorted_tasks) or queue:
        # Add tasks that have arrived
        while task_index < len(sorted_tasks) and sorted_tasks[task_index].arrival_time <= current_time:
            queue.append(sorted_tasks[task_index])
            task_index += 1
        
        if queue:
            task = queue.popleft()
            
            # Process for time quantum or until complete
            if task.remaining_time <= time_quantum:
                current_time += task.remaining_time
                task.remaining_time = 0
                task.completion_time = current_time
                task.turnaround_time = task.completion_time - task.arrival_time
                task.waiting_time = task.turnaround_time - task.burst_time
                completed_tasks.append(task)
            else:
                current_time += time_quantum
                task.remaining_time -= time_quantum
                # Add back to queue
                queue.append(task)
        else:
            # No tasks ready, advance time
            if task_index < len(sorted_tasks):
                current_time = sorted_tasks[task_index].arrival_time
    
    return completed_tasks


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: CPU Scheduling Algorithms Demonstration")
    
    # Create tasks: (name, arrival_time, burst_time)
    tasks_fcfs = [
        Task("P1", 0, 5),
        Task("P2", 1, 3),
        Task("P3", 2, 8),
        Task("P4", 3, 6)
    ]
    
    print("Tasks:")
    for task in tasks_fcfs:
        print(f"  {task.name}: Arrival={task.arrival_time}, Burst={task.burst_time}")
    
    # FCFS Scheduling
    print("\n" + "="*50)
    print("First Come First Served (FCFS) Scheduling:")
    fcfs_result = fcfs_scheduling([Task(t.name, t.arrival_time, t.burst_time) for t in tasks_fcfs])
    for task in fcfs_result:
        print(f"  {task.name}: Completion={task.completion_time}, "
              f"Turnaround={task.turnaround_time}, Waiting={task.waiting_time}")
    
    # Round Robin Scheduling
    print("\n" + "="*50)
    print("Round Robin Scheduling (Time Quantum=3):")
    rr_result = round_robin_scheduling(
        [Task(t.name, t.arrival_time, t.burst_time) for t in tasks_fcfs],
        time_quantum=3
    )
    for task in rr_result:
        print(f"  {task.name}: Completion={task.completion_time}, "
              f"Turnaround={task.turnaround_time}, Waiting={task.waiting_time}")

