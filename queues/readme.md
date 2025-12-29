# Queues

A queue is a linear data structure that follows the First In First Out (FIFO) principle. Elements are added at the rear and removed from the front.

## 📁 Folder Structure

```
queues/
├── queues.py                             # Core queue operations ⭐ MOST IMPORTANT
├── types/                                # Queue types
│   ├── standard_queue.py                 # Standard FIFO queue using array/list
│   ├── circular_queue.py                 # Circular queue implementation
│   └── deque_queue.py                    # Double-ended queue (deque) implementation
├── applications/                         # Common queue applications
│   ├── sliding_window_maximum.py         # Sliding window maximum problem ⭐ MOST IMPORTANT
│   └── scheduling_algorithms.py          # CPU scheduling / task scheduling 🟡 MEDIUM
└── interview_problems/                   # Typical interview problems
    ├── recent_counter.py                 # Recent calls / events using queue ⭐ MOST IMPORTANT
    ├── moving_average.py                 # Moving average in a window 🟡 MEDIUM
    └── task_scheduler.py                 # Task scheduling with cooldown 🟡 MEDIUM
```

## 📚 Core Concepts

### Queue Operations

- **enqueue(item)**: Add element to rear - O(1)
- **dequeue()**: Remove and return front element - O(1) with deque, O(n) with list
- **peek()**: View front element without removing - O(1)
- **is_empty()**: Check if queue is empty - O(1)
- **size()**: Get number of elements - O(1)

### Characteristics

- **FIFO (First In First Out)**: First element added is first removed
- **Dynamic size**: Grows/shrinks as needed
- **Two access points**: Front (dequeue) and rear (enqueue)
- **Efficient operations**: O(1) with proper implementation

## 🏗️ Queue Types

### 1. Standard Queue (`types/standard_queue.py`)
- Uses Python list
- **Advantages**: Simple, easy to understand
- **Disadvantages**: O(n) dequeue (removing from front)
- **Time Complexity**: O(1) enqueue, O(n) dequeue
- **Space Complexity**: O(n)

### 2. Circular Queue (`types/circular_queue.py`)
- Fixed capacity with wrap-around
- **Advantages**: O(1) operations, fixed memory
- **Disadvantages**: Fixed size, more complex
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(capacity)

### 3. Deque Queue (`types/deque_queue.py`)
- Double-ended queue using collections.deque
- **Advantages**: O(1) operations on both ends, flexible
- **Disadvantages**: Extra memory for pointers
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n)

## 🎯 Applications

### 1. Sliding Window Maximum (`applications/sliding_window_maximum.py`) ⭐
- Find maximum in each sliding window
- **Algorithm**: Monotonic deque technique
- **Time Complexity**: O(n)
- **Space Complexity**: O(k) where k is window size

### 2. Scheduling Algorithms (`applications/scheduling_algorithms.py`) 🟡
- CPU scheduling (FCFS, Round Robin)
- **Algorithm**: Queue-based task processing
- **Time Complexity**: O(n log n) for FCFS, O(n*q) for RR
- **Space Complexity**: O(n)

## 💼 Interview Problems

### Most Important (⭐)

1. **Recent Counter** (`interview_problems/recent_counter.py`)
   - Count events in time window
   - Uses deque for efficient removal
   - **Time Complexity**: O(n) per operation
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

2. **Moving Average** (`interview_problems/moving_average.py`)
   - Calculate moving average in sliding window
   - Queue maintains window
   - **Time Complexity**: O(1) per operation
   - **Space Complexity**: O(k) where k is window size

3. **Task Scheduler** (`interview_problems/task_scheduler.py`)
   - Schedule tasks with cooldown period
   - Uses heap and queue
   - **Time Complexity**: O(m * log k) where m is total time
   - **Space Complexity**: O(k) where k is unique tasks

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| enqueue() | O(1) | O(1) |
| dequeue() (list) | O(n) | O(1) |
| dequeue() (deque) | O(1) | O(1) |
| peek() | O(1) | O(1) |
| is_empty() | O(1) | O(1) |
| size() | O(1) | O(1) |
| Sliding Window Maximum | O(n) | O(k) |
| Scheduling (FCFS) | O(n log n) | O(n) |
| Scheduling (RR) | O(n * q) | O(n) |
| Recent Counter | O(n) | O(n) |
| Moving Average | O(1) | O(k) |
| Task Scheduler | O(m * log k) | O(k) |

## 🎓 Learning Path

1. **Start with**: `queues.py` - Understand basic operations
2. **Learn types**: 
   - `standard_queue.py` - Basic FIFO queue
   - `circular_queue.py` - Fixed-size circular buffer
   - `deque_queue.py` - Double-ended queue
3. **Practice applications**: 
   - `sliding_window_maximum.py` - Monotonic deque
   - `scheduling_algorithms.py` - Task scheduling
4. **Solve interview problems**: Start with ⭐ marked problems
5. **Advanced topics**: Explore task scheduling and moving averages

## 💡 Key Insights

1. **FIFO Principle**: First element added is first removed
2. **Use Deque**: For O(1) operations on both ends
3. **Monotonic Deque**: Maintains increasing/decreasing sequence for efficient queries
4. **Circular Queue**: Efficient for fixed-size buffers
5. **Queue for Scheduling**: Natural fit for task/process scheduling

## 🔗 Related Topics

- **Arrays**: Array-based queue implementation
- **Linked Lists**: Linked list-based queue implementation
- **Stacks**: Another linear data structure (LIFO)
- **Heaps**: Used with queues for priority scheduling
- **Graphs**: Queue used in BFS traversal

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings
- Use `collections.deque` for efficient O(1) operations

