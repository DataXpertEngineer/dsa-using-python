# Greedy Algorithms

**Greedy algorithms** make locally optimal choices at each step with the hope of finding a global optimum. They are simple, intuitive, and often efficient for optimization problems.

## 📁 Folder Structure

```
greedy_algorithms/
├── greedy.py                                # Core concepts and examples ⭐ MOST IMPORTANT
├── applications/                             # Greedy algorithm applications
│   ├── interval_scheduling.py               # Interval scheduling problem ⭐ MOST IMPORTANT
│   └── huffman_encoding.py                  # Huffman coding ⭐ MOST IMPORTANT
└── interview_problems/                      # Typical interview questions
    ├── activity_selection.py                # Activity selection problem ⭐ MOST IMPORTANT
    └── min_sum_pairing.py                   # Minimum sum pairing 🟡 MEDIUM
```

## 📚 Definition and Concepts

### What is a Greedy Algorithm?

A **greedy algorithm** is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum.

#### Key Characteristics:

1. **Greedy Choice Property**: Locally optimal choice leads to globally optimal solution
2. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
3. **No Backtracking**: Once a choice is made, it's never reconsidered
4. **Simple and Efficient**: Often simpler than dynamic programming

### When to Use Greedy?

#### Greedy Works Well For:

- ✅ **Activity Selection**: Maximum non-overlapping activities
- ✅ **Interval Scheduling**: Maximum intervals
- ✅ **Huffman Coding**: Optimal prefix codes
- ✅ **Minimum Spanning Tree**: Prim's, Kruskal's
- ✅ **Shortest Path**: Dijkstra's (with non-negative weights)
- ✅ **Fractional Knapsack**: Items can be divided

#### Greedy Doesn't Work For:

- ❌ **0/1 Knapsack**: Items cannot be divided
- ❌ **Coin Change (general)**: Greedy may not give optimal
- ❌ **Job Scheduling (general)**: Need dynamic programming

### Greedy Algorithm Template

```python
def greedy_algorithm(items):
    # 1. Sort items by some criteria
    sorted_items = sort(items, key=criterion)
    
    # 2. Process items in order
    solution = []
    for item in sorted_items:
        # 3. Make greedy choice
        if is_valid(item, solution):
            solution.append(item)
    
    return solution
```

## 🔑 Core Concepts

### 1. Greedy Choice Property

- **Definition**: A global optimum can be arrived at by selecting a local optimum
- **Example**: In activity selection, choosing activity that ends earliest is always part of optimal solution

### 2. Optimal Substructure

- **Definition**: Optimal solution contains optimal solutions to subproblems
- **Example**: In MST, optimal tree contains optimal subtrees

### 3. Common Patterns

1. **Sort and Select**: Sort by some criteria, select in order
2. **Priority Queue**: Use heap for greedy selection
3. **Two Pointers**: Process from both ends
4. **Greedy Matching**: Match elements optimally

## 🎯 Applications

### 1. Interval Scheduling (`applications/interval_scheduling.py`) ⭐

- **Problem**: Select maximum non-overlapping intervals
- **Greedy Choice**: Always pick interval that ends earliest
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

**Key Functions:**
- `interval_scheduling()`: Find maximum intervals
- `max_intervals_count()`: Count maximum intervals
- `weighted_interval_scheduling()`: Weighted version (DP)

### 2. Huffman Encoding (`applications/huffman_encoding.py`) ⭐

- **Problem**: Create optimal prefix code for compression
- **Greedy Choice**: Always merge two least frequent nodes
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

**Key Functions:**
- `build_huffman_tree()`: Build Huffman tree
- `generate_codes()`: Generate character codes
- `huffman_encode()`: Encode text
- `huffman_decode()`: Decode text

## 💼 Interview Problems

### Most Important (⭐)

1. **Activity Selection** (`interview_problems/activity_selection.py`)
   - Select maximum non-overlapping activities
   - **Greedy Choice**: Pick activity that finishes earliest
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

2. **Minimum Sum Pairing** (`interview_problems/min_sum_pairing.py`)
   - Pair elements to minimize sum of differences
   - **Greedy Choice**: Pair adjacent elements after sorting
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(n)

## 📊 Complexity Analysis

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Activity Selection | O(n log n) | O(n) |
| Interval Scheduling | O(n log n) | O(n) |
| Huffman Encoding | O(n log n) | O(n) |
| Minimum Sum Pairing | O(n log n) | O(n) |
| Fractional Knapsack | O(n log n) | O(1) |

Where:
- n = number of items/intervals/activities

## 🎓 Learning Path

1. **Start with**: `greedy.py` - Understand greedy concepts
2. **Learn applications**: 
   - `interval_scheduling.py` - Classic greedy problem
   - `huffman_encoding.py` - Real-world application
3. **Solve problems**: 
   - `activity_selection.py` - Common interview problem
   - `min_sum_pairing.py` - Medium difficulty

## 💡 Key Insights

### Greedy Strategy:

1. **Identify Greedy Choice**: What's the locally optimal choice?
2. **Prove Greedy Choice Property**: Show it's always part of optimal solution
3. **Prove Optimal Substructure**: Show subproblems are optimal
4. **Implement**: Sort, process, make greedy choice

### Common Mistakes:

1. **Assuming Greedy Always Works**: Not all problems are greedy
2. **Wrong Sorting Criteria**: Must sort by correct property
3. **Not Verifying Solution**: Always check if greedy gives optimal
4. **Missing Edge Cases**: Handle empty inputs, single element

### Tips:

1. **Start with Sorting**: Most greedy problems require sorting
2. **Think Locally**: What's best choice right now?
3. **Prove Correctness**: Understand why greedy works
4. **Compare with DP**: When greedy fails, consider DP

## 🔗 Related Topics

- **Dynamic Programming**: Alternative for problems where greedy fails
- **Sorting**: Most greedy algorithms start with sorting
- **Graphs**: Many graph algorithms use greedy (MST, shortest path)
- **Heaps**: Priority queues for greedy selection

## 📝 Notes

- All implementations include detailed docstrings
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles
- Both basic and advanced implementations included

## 🚨 Common Pitfalls

1. **Greedy Doesn't Always Work**: Verify greedy choice property
2. **Wrong Sorting**: Sort by correct criteria (end time, ratio, etc.)
3. **Edge Cases**: Handle empty inputs, single element
4. **Ties**: Decide how to handle ties in sorting

## 🎯 Real-World Applications

### 1. Data Compression
- **Huffman Coding**: Variable-length prefix codes
- **File Compression**: ZIP, GZIP use Huffman

### 2. Scheduling
- **Activity Selection**: Resource allocation
- **Interval Scheduling**: Meeting room booking

### 3. Network Design
- **Minimum Spanning Tree**: Connect all nodes at minimum cost
- **Shortest Path**: Route packets efficiently

### 4. Resource Allocation
- **Fractional Knapsack**: Optimal resource distribution
- **Job Scheduling**: Assign jobs to machines

## 🔍 Comparison with Other Paradigms

| Aspect | Greedy | Dynamic Programming | Divide & Conquer |
|--------|--------|---------------------|-----------------|
| Approach | Local optimum | Optimal substructure | Divide problem |
| Time | Often O(n log n) | Often O(n²) or O(2ⁿ) | Often O(n log n) |
| Space | Usually O(1) or O(n) | Usually O(n) or O(n²) | Usually O(log n) |
| Backtracking | No | No | No |
| Overlapping Subproblems | No | Yes | No |

