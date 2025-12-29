# DSA Using Python

A comprehensive collection of **Data Structures** and **Algorithms** implemented in **Python**. This repository provides clean, well-documented code examples with detailed explanations, complexity analysis, and real-world applications.

## 🚀 Features

- **Well-structured code** for a variety of data structures and algorithms
- **Detailed documentation** with complexity analysis for each implementation
- **Multiple approaches** (recursive, iterative, optimized) for learning
- **Real-world examples** and interview problems
- **Clean code principles** with type hints and comprehensive docstrings
- **Importance markers** (⭐ Most Important, 🟡 Medium) for prioritization

## 📁 Repository Structure

### Core Data Structures

| Module | Description | Programs |
|--------|-------------|----------|
| **arrays/** | Array data structures and algorithms | Core operations, techniques, algorithms, interview problems |
| **linked_lists/** | Linked list implementations | Singly, doubly, circular lists with techniques and algorithms |
| **strings/** | String manipulation and algorithms | Core operations, techniques, algorithms, interview problems |
| **trees/** | Tree data structures and algorithms | Traversals, search algorithms, properties, interview problems |
| **graphs/** | Graph data structures and algorithms | Representations, DFS/BFS, algorithms (Dijkstra, MST), interview problems |
| **tries/** | Trie (Prefix Tree) data structures | Core implementation, insert, search, autocomplete |

### Advanced Data Structures

| Module | Description | Programs |
|--------|-------------|----------|
| **stacks/** | Stack data structure and applications | Implementations, applications, interview problems |
| **queues/** | Queue data structures and algorithms | Types, applications, interview problems |
| **hash_tables/** | Hash table concepts and algorithms | Concepts, applications, interview problems |
| **heaps/** | Heap and priority queue concepts | Types, algorithms, applications, interview problems |

### Algorithms & Techniques

| Module | Description | Programs |
|--------|-------------|----------|
| **sorting/** | Sorting algorithms and concepts | Basic sorts, divide & conquer, applications, interview problems |
| **binary_search/** | Binary search techniques and problems | Iterative, recursive, rotated arrays, peak finding, search on answer |
| **bit_manipulation/** | Bit manipulation techniques and algorithms | Core operations, techniques, algorithms, interview problems |
| **recursion_backtracking/** | Recursion and backtracking concepts | Core recursion, backtracking techniques, applications, interview problems |
| **greedy_algorithms/** | Greedy algorithm implementations | Core concepts, applications, interview problems |
| **dynamic_programming/** | Dynamic programming techniques | Approaches, classic problems, patterns, interview problems |

## 📊 Module Overview

### Arrays (`arrays/`)
- Core array operations and Python list internals
- Techniques: Prefix sum, sliding window, two pointers, Kadane's algorithm
- Algorithms: Searching, sorting, divide & conquer
- Interview problems: Two sum, max subarray, rotate array, and more

### Linked Lists (`linked_lists/`)
- Singly, doubly, and circular linked lists
- Techniques: Slow/fast pointers, reversal, dummy node technique
- Algorithms: Sorting, searching, divide & conquer
- Interview problems: Cycle detection, remove nth node, add two numbers, and more

### Strings (`strings/`)
- Core string operations and manipulations
- Techniques: Sliding window, two pointers, prefix function, hashing
- Algorithms: Searching (KMP, Rabin-Karp), sorting, divide & conquer
- Interview problems: Reversal, longest palindrome, anagram check, and more

### Trees (`trees/`)
- Binary tree data structure
- Traversals: Inorder, preorder, postorder
- Search algorithms: DFS, BFS
- Properties: Height, diameter, LCA
- Interview problems: Max/min depth, balanced tree, path sum

### Graphs (`graphs/`)
- Graph representations (adjacency list/matrix)
- Traversals: DFS, BFS
- Algorithms: Dijkstra's, Prim's MST, Kruskal's MST, Union-Find
- Types: Directed/undirected, weighted/unweighted
- Interview problems: Cycle detection, connected components, shortest path

### Sorting (`sorting/`)
- Basic sorts: Bubble, selection, insertion
- Advanced sorts: Merge sort, quick sort
- Applications: Kth smallest/largest, sort colors
- Interview problems: Sort array, largest number, count inversions

### Binary Search (`binary_search/`)
- Iterative and recursive implementations
- Rotated array search
- Peak finding
- Binary search on answer (advanced technique)

### Bit Manipulation (`bit_manipulation/`)
- Core bit operations (AND, OR, XOR, NOT, shifts)
- Techniques: Bitmasking, XOR tricks, counting bits
- Algorithms: Single number, subset generation, Hamming distance
- Interview problems: Set bits count, power of two, missing number, and more

### Dynamic Programming (`dynamic_programming/`)
- Approaches: Recursion, memoization, tabulation
- Classic problems: Fibonacci, 0/1 Knapsack, LCS
- Patterns: Subsequences, partitioning
- Interview problems: Edit distance, coin change, matrix chain multiplication

### Greedy Algorithms (`greedy_algorithms/`)
- Core greedy concepts and examples
- Applications: Interval scheduling, Huffman encoding
- Interview problems: Activity selection, minimum sum pairing

### Stacks (`stacks/`)
- Stack implementations (array, linked list)
- Applications: Parentheses checker, infix to postfix, next greater element
- Interview problems: Min stack, largest rectangle histogram

### Queues (`queues/`)
- Queue types: Standard, circular, deque
- Applications: Sliding window maximum, scheduling algorithms
- Interview problems: Recent counter, moving average, task scheduler

### Hash Tables (`hash_tables/`)
- Core concepts: Hashing, collision handling
- Applications: Frequency maps, prefix sum optimization, two-sum/three-sum
- Interview problems: Subarray sum equals k, longest subarray unique, group anagrams

### Heaps (`heaps/`)
- Heap types: Min heap, max heap
- Algorithms: Heap sort, kth largest/smallest, merge k sorted arrays
- Applications: Greedy algorithms, graph algorithms
- Interview problems: Top K frequent, median from stream

### Recursion & Backtracking (`recursion_backtracking/`)
- Core recursion concepts
- Backtracking: N-Queens, subsets, permutations
- Applications: Sudoku solver, rat in maze, combination sum
- Interview problems: Subset sum, palindrome partitioning, word search

### Tries (`tries/`)
- Trie implementation from scratch
- Operations: Insert, search (prefix/exact word)
- Applications: Autocomplete system

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher
- `uv` package manager (optional, for virtual environment)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd dsa-using-python
   ```

2. **Create virtual environment (using uv):**
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. **Navigate to a module:**
   ```bash
   cd arrays
   python arrays.py
   ```

4. **Run examples:**
   Each file contains example usage at the bottom. Run any file to see demonstrations:
   ```bash
   python arrays/arrays.py
   python trees/traversals/inorder_traversal.py
   python graphs/algorithms/dijkstra.py
   ```

## 📚 Learning Path

### Beginner
1. **Arrays** → Core operations and basic techniques
2. **Strings** → String manipulation basics
3. **Linked Lists** → Understanding pointers and references
4. **Sorting** → Basic sorting algorithms
5. **Binary Search** → Efficient searching

### Intermediate
1. **Stacks & Queues** → Linear data structures
2. **Hash Tables** → Fast lookups and mappings
3. **Trees** → Hierarchical data structures
4. **Graphs** → Network and relationship modeling
5. **Recursion** → Problem decomposition

### Advanced
1. **Dynamic Programming** → Optimization techniques
2. **Greedy Algorithms** → Local optimization
3. **Bit Manipulation** → Low-level operations
4. **Tries** → String-based data structures
5. **Graph Algorithms** → Dijkstra's, MST, Union-Find

## 🎯 Key Features of Each Module

- **Core Concepts**: Fundamental operations and definitions
- **Techniques**: Common problem-solving patterns
- **Algorithms**: Classic algorithmic solutions
- **Interview Problems**: Real-world coding problems
- **Comprehensive README**: Detailed explanations and complexity analysis

## 📝 Code Standards

All code follows these principles:
- **Type Hints**: Full type annotations for clarity
- **Docstrings**: Comprehensive documentation with complexity analysis
- **Clean Code**: Readable, maintainable, and well-structured
- **Multiple Approaches**: Recursive, iterative, and optimized versions
- **Example Usage**: Working examples in each file
- **Language-Agnostic**: Core logic applicable to any language

## 🔍 Complexity Analysis

Each function includes:
- **Time Complexity**: Best, average, and worst case
- **Space Complexity**: Memory requirements
- **Detailed Explanations**: Why the complexity is what it is

## 💡 Importance Markers

- ⭐ **MOST IMPORTANT**: Essential concepts, must-know problems
- 🟡 **MEDIUM**: Important but less critical
- 🔴 **LEAST IMPORTANT**: Advanced or less common (where applicable)

## 🤝 Contributing

Contributions are welcome! If you have improvements, additional problems, or better implementations, please:
1. Fork the repository
2. Create a feature branch
3. Make your changes following the existing code style
4. Submit a pull request

## 📚 Related Resources

- [Python Documentation](https://docs.python.org/3/)
- [GeeksforGeeks DSA](https://www.geeksforgeeks.org/data-structures/)
- [LeetCode](https://leetcode.com/)
- [Algorithm Visualizations](https://visualgo.net/)

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

This repository is designed to help learners master Data Structures and Algorithms through clean, well-documented Python implementations.

---

**Happy Coding! 🚀**
