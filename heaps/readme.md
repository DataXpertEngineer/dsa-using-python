# Heaps

A heap is a complete binary tree that satisfies the heap property. Heaps are used to implement priority queues efficiently.

## 📁 Folder Structure

```
heaps/
├── heaps.py                              # Core heap operations ⭐ MOST IMPORTANT
├── types/                                # Heap types
│   ├── min_heap.py                       # Min Heap implementation ⭐ MOST IMPORTANT
│   └── max_heap.py                       # Max Heap implementation ⭐ MOST IMPORTANT
├── algorithms/                           # Heap-based algorithms
│   ├── heap_sort.py                      # Heap sort algorithm ⭐ MOST IMPORTANT
│   ├── kth_largest_smallest.py          # Kth largest/smallest element ⭐ MOST IMPORTANT
│   └── merge_k_sorted_arrays.py         # Merge k sorted arrays 🟡 MEDIUM
├── applications/                         # Applications in algorithms
│   ├── greedy_algorithms.py              # Greedy problems using heaps 🟡 MEDIUM
│   └── graph_algorithms.py               # Dijkstra's, Prim's using heaps 🟡 MEDIUM
└── interview_problems/                   # Typical interview questions
    ├── top_k_frequent.py                # Top K frequent elements ⭐ MOST IMPORTANT
    ├── median_from_stream.py            # Median in a running stream ⭐ MOST IMPORTANT
    └── sliding_window_maximum.py         # Sliding window max using heap 🟡 MEDIUM
```

## 📚 Definition and Properties

### What is a Heap?

A **heap** is a complete binary tree data structure that satisfies the **heap property**:

- **Complete Binary Tree**: All levels are filled except possibly the last, which is filled from left to right
- **Heap Property**: 
  - **Min-Heap**: Parent ≤ Children (root is minimum)
  - **Max-Heap**: Parent ≥ Children (root is maximum)

### Properties of Heaps

1. **Complete Binary Tree Structure**
   - All levels except last are completely filled
   - Last level filled from left to right
   - Height: O(log n) where n is number of elements

2. **Array Representation**
   - Parent at index `i`
   - Left child at index `2i + 1`
   - Right child at index `2i + 2`
   - No need for pointers, efficient memory usage

3. **Heap Property**
   - **Min-Heap**: `heap[parent] ≤ heap[child]` for all nodes
   - **Max-Heap**: `heap[parent] ≥ heap[child]` for all nodes
   - Root always contains extremum (min or max)

4. **Efficient Operations**
   - Insert: O(log n) - Add at end, heapify up
   - Extract: O(log n) - Remove root, heapify down
   - Peek: O(1) - Access root directly
   - Build Heap: O(n) - Linear time construction

5. **Heap Invariants**
   - Heap property maintained after every operation
   - Complete binary tree structure preserved
   - Efficient for priority queue operations

## 🔑 Core Concepts

### Heap Operations

- **insert(item)**: Add element - O(log n)
- **extract()**: Remove and return root - O(log n)
- **peek()**: View root without removing - O(1)
- **heapify()**: Build heap from array - O(n)
- **is_empty()**: Check if empty - O(1)
- **size()**: Get number of elements - O(1)

### Heap Types

#### 1. Min Heap (`types/min_heap.py`) ⭐
- Parent ≤ Children
- Root contains minimum element
- **Use Cases**: Priority queues, finding minimum
- **Time Complexity**: O(log n) insert/extract, O(1) peek

#### 2. Max Heap (`types/max_heap.py`) ⭐
- Parent ≥ Children
- Root contains maximum element
- **Use Cases**: Priority queues, finding maximum
- **Time Complexity**: O(log n) insert/extract, O(1) peek

## 🎯 Algorithms

### 1. Heap Sort (`algorithms/heap_sort.py`) ⭐
- Sort array using heap
- **Algorithm**: Build max heap, repeatedly extract max
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) in-place

### 2. Kth Largest/Smallest (`algorithms/kth_largest_smallest.py`) ⭐
- Find kth largest using min heap of size k
- Find kth smallest using max heap of size k
- **Time Complexity**: O(n log k)
- **Space Complexity**: O(k)

### 3. Merge K Sorted Arrays (`algorithms/merge_k_sorted_arrays.py`) 🟡
- Merge k sorted arrays efficiently
- **Algorithm**: Min heap of first elements
- **Time Complexity**: O(n log k) where n is total elements
- **Space Complexity**: O(k)

## 🎯 Applications

### 1. Greedy Algorithms (`applications/greedy_algorithms.py`) 🟡
- Minimum cost to connect ropes
- Meeting rooms scheduling
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

### 2. Graph Algorithms (`applications/graph_algorithms.py`) 🟡
- Dijkstra's shortest path
- Prim's minimum spanning tree
- **Time Complexity**: O((V + E) log V)
- **Space Complexity**: O(V)

## 💼 Interview Problems

### Most Important (⭐)

1. **Top K Frequent Elements** (`interview_problems/top_k_frequent.py`)
   - Find k most frequent elements
   - Uses min heap of size k
   - **Time Complexity**: O(n log k)
   - **Space Complexity**: O(n)

2. **Median from Stream** (`interview_problems/median_from_stream.py`)
   - Maintain median of data stream
   - Uses two heaps (max + min)
   - **Time Complexity**: O(log n) insert, O(1) find median
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

3. **Sliding Window Maximum** (`interview_problems/sliding_window_maximum.py`)
   - Find maximum in each sliding window
   - Uses max heap (alternative to deque)
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(k)

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| insert() | O(log n) | O(1) |
| extract() | O(log n) | O(1) |
| peek() | O(1) | O(1) |
| heapify() | O(n) | O(1) |
| is_empty() | O(1) | O(1) |
| size() | O(1) | O(1) |
| Heap Sort | O(n log n) | O(1) |
| Kth Largest | O(n log k) | O(k) |
| Merge K Arrays | O(n log k) | O(k) |
| Top K Frequent | O(n log k) | O(n) |
| Median Stream | O(log n) insert | O(n) |

## 🎓 Learning Path

1. **Start with**: `heaps.py` - Understand basic operations
2. **Learn types**: 
   - `min_heap.py` - Min heap implementation
   - `max_heap.py` - Max heap implementation
3. **Practice algorithms**: 
   - `heap_sort.py` - Sorting with heaps
   - `kth_largest_smallest.py` - Finding kth elements
4. **Solve interview problems**: Start with ⭐ marked problems
5. **Advanced topics**: Explore graph algorithms and greedy problems

## 💡 Key Insights

1. **Complete Binary Tree**: Efficient array representation
2. **Heap Property**: Maintains order for efficient access
3. **O(log n) Operations**: Insert and extract maintain heap property
4. **O(n) Build**: Can build heap from array in linear time
5. **Priority Queues**: Natural implementation using heaps
6. **Two Heaps**: Useful for median and other statistics

## 🔗 Related Topics

- **Trees**: Heap is a complete binary tree
- **Priority Queues**: Heaps implement priority queues
- **Sorting**: Heap sort algorithm
- **Graphs**: Used in Dijkstra's and Prim's algorithms
- **Arrays**: Heap stored as array

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings
- Python's `heapq` module provides min-heap implementation

