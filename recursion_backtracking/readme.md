# Recursion and Backtracking

Recursion is a programming technique where a function calls itself, and backtracking is an algorithmic technique for solving problems by trying partial solutions and abandoning them if they cannot lead to a complete solution.

## 📁 Folder Structure

```
recursion_backtracking/
├── recursion.py                           # Core recursion concepts ⭐ MOST IMPORTANT
├── backtracking/                          # Backtracking techniques
│   ├── n_queens.py                        # N-Queens problem ⭐ MOST IMPORTANT
│   ├── generate_subsets.py                # Generate all subsets of a set ⭐ MOST IMPORTANT
│   └── permutations.py                    # Generate all permutations ⭐ MOST IMPORTANT
├── applications/                          # Applications and common patterns
│   ├── sudoku_solver.py                   # Sudoku solver using backtracking 🟡 MEDIUM
│   ├── rat_in_maze.py                     # Maze solving using backtracking 🟡 MEDIUM
│   └── combination_sum.py                # Sum combinations problem 🟡 MEDIUM
└── interview_problems/                    # Typical interview questions
    ├── subset_sum.py                      # Subset sum problem ⭐ MOST IMPORTANT
    ├── palindrome_partitioning.py         # Partition string into palindromes 🟡 MEDIUM
    └── word_search.py                     # Word search in grid using backtracking 🟡 MEDIUM
```

## 📚 Definition and Concepts

### What is Recursion?

**Recursion** is a programming technique where a function calls itself directly or indirectly to solve a problem. The problem is broken down into smaller subproblems of the same type, and the function solves these subproblems recursively.

#### Key Components of Recursion:

1. **Base Case**: The condition that stops the recursion. Without a base case, recursion would continue infinitely.
2. **Recursive Case**: The part where the function calls itself with a smaller or simpler input.
3. **Call Stack**: The stack data structure that stores function calls during execution. Each recursive call adds a new frame to the stack.

#### Example Structure:
```python
def recursive_function(n):
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * recursive_function(n - 1)
```

### Properties of Recursion:

1. **Self-Referential**: Function calls itself
2. **Problem Reduction**: Breaks problem into smaller subproblems
3. **Stack-Based**: Uses call stack to manage function calls
4. **Termination**: Must have base case to stop recursion
5. **Memory Usage**: Each recursive call uses stack space

### What is Backtracking?

**Backtracking** is an algorithmic technique for solving problems by trying partial solutions and abandoning them ("backtracking") if they cannot lead to a complete solution. It systematically explores all possible solutions by building candidates incrementally and abandoning partial candidates as soon as it determines they cannot lead to a valid solution.

#### Key Components of Backtracking:

1. **Choice**: Make a choice (e.g., place a queen, include an element)
2. **Constraint**: Check if choice is valid
3. **Recurse**: Move to next subproblem
4. **Backtrack**: Undo choice if it doesn't lead to solution

#### Backtracking Template:
```python
def backtrack(current_solution, remaining_input):
    # Base case: solution complete
    if is_complete(current_solution):
        save_solution(current_solution)
        return
    
    # Try each possible choice
    for choice in possible_choices:
        if is_valid(choice):
            # Make choice
            current_solution.append(choice)
            
            # Recurse
            backtrack(current_solution, remaining_input)
            
            # Backtrack: undo choice
            current_solution.pop()
```

### Properties of Backtracking:

1. **Systematic Search**: Explores all possibilities systematically
2. **Pruning**: Abandons invalid partial solutions early
3. **State Restoration**: Restores previous state when backtracking
4. **Exponential Complexity**: Often O(2^n) or O(n!) in worst case
5. **Constraint Satisfaction**: Naturally handles constraint problems

## 🔑 Core Concepts

### Recursion Concepts (`recursion.py`) ⭐

1. **Base Case**: Condition that stops recursion
   - Must be reached to avoid infinite recursion
   - Usually handles smallest subproblem

2. **Recursive Case**: Function calls itself
   - Solves smaller subproblem
   - Combines result with current problem

3. **Call Stack**: Stack of function calls
   - Each recursive call adds frame
   - Base case returns, frames pop
   - Stack overflow if too deep

4. **Memoization**: Cache results to avoid recomputation
   - Reduces time complexity
   - Trades space for time

## 🎯 Backtracking Techniques

### 1. N-Queens (`backtracking/n_queens.py`) ⭐
- Place N queens on N×N board
- **Algorithm**: Try each column, check validity, recurse
- **Time Complexity**: O(n!)
- **Space Complexity**: O(n)

### 2. Generate Subsets (`backtracking/generate_subsets.py`) ⭐
- Generate all subsets of a set
- **Algorithm**: For each element, include or exclude
- **Time Complexity**: O(2^n)
- **Space Complexity**: O(n)

### 3. Permutations (`backtracking/permutations.py`) ⭐
- Generate all permutations
- **Algorithm**: Try each unused element at each position
- **Time Complexity**: O(n!)
- **Space Complexity**: O(n)

## 🎯 Applications

### 1. Sudoku Solver (`applications/sudoku_solver.py`) 🟡
- Solve 9×9 Sudoku puzzle
- **Algorithm**: Try digits 1-9, check validity, backtrack
- **Time Complexity**: O(9^m) where m is empty cells
- **Space Complexity**: O(1) in-place

### 2. Rat in Maze (`applications/rat_in_maze.py`) 🟡
- Find path from source to destination
- **Algorithm**: Try all directions, mark visited, backtrack
- **Time Complexity**: O(2^(n×m))
- **Space Complexity**: O(n×m)

### 3. Combination Sum (`applications/combination_sum.py`) 🟡
- Find combinations that sum to target
- **Algorithm**: Try including each candidate, recurse
- **Time Complexity**: O(2^target)
- **Space Complexity**: O(target)

## 💼 Interview Problems

### Most Important (⭐)

1. **Subset Sum** (`interview_problems/subset_sum.py`)
   - Check if subset sums to target
   - **Algorithm**: Include/exclude each element
   - **Time Complexity**: O(2^n)
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

2. **Palindrome Partitioning** (`interview_problems/palindrome_partitioning.py`)
   - Partition string into palindromes
   - **Algorithm**: Try partitioning at each position
   - **Time Complexity**: O(2^n × n)
   - **Space Complexity**: O(n)

3. **Word Search** (`interview_problems/word_search.py`)
   - Find word in 2D grid
   - **Algorithm**: Try each cell, explore 4 directions
   - **Time Complexity**: O(m×n×4^L)
   - **Space Complexity**: O(L)

## 📊 Complexity Summary

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Factorial | O(n) | O(n) |
| Fibonacci (memo) | O(n) | O(n) |
| N-Queens | O(n!) | O(n) |
| Generate Subsets | O(2^n) | O(n) |
| Permutations | O(n!) | O(n) |
| Sudoku Solver | O(9^m) | O(1) |
| Rat in Maze | O(2^(n×m)) | O(n×m) |
| Combination Sum | O(2^target) | O(target) |
| Subset Sum | O(2^n) | O(n) |
| Palindrome Partitioning | O(2^n × n) | O(n) |
| Word Search | O(m×n×4^L) | O(L) |

## 🎓 Learning Path

1. **Start with**: `recursion.py` - Understand recursion fundamentals
2. **Learn backtracking**: 
   - `n_queens.py` - Classic backtracking problem
   - `generate_subsets.py` - Subset generation
   - `permutations.py` - Permutation generation
3. **Practice applications**: 
   - `sudoku_solver.py` - Constraint satisfaction
   - `rat_in_maze.py` - Path finding
   - `combination_sum.py` - Combination problems
4. **Solve interview problems**: Start with ⭐ marked problems
5. **Advanced topics**: Explore optimization techniques

## 💡 Key Insights

### Recursion:
1. **Base Case is Critical**: Must be reached to avoid infinite recursion
2. **Call Stack Depth**: Limited by system, can cause stack overflow
3. **Memoization**: Can reduce time complexity significantly
4. **Tail Recursion**: Can be optimized to reduce space

### Backtracking:
1. **Systematic Exploration**: Tries all possibilities systematically
2. **Early Pruning**: Abandons invalid solutions early
3. **State Restoration**: Must restore state when backtracking
4. **Template Pattern**: Most backtracking problems follow similar template
5. **Constraint Checking**: Validate choices before recursing

## 🔗 Related Topics

- **Trees**: Recursion natural for tree traversals
- **Graphs**: DFS uses recursion/backtracking
- **Dynamic Programming**: Often uses recursion with memoization
- **Divide and Conquer**: Uses recursion to break problems
- **Stacks**: Call stack manages recursive calls

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings
- Backtracking problems often have exponential time complexity
- Memoization can optimize recursive solutions

## 🚨 Common Pitfalls

1. **Missing Base Case**: Causes infinite recursion
2. **Incorrect State Restoration**: Backtracking doesn't restore state properly
3. **Stack Overflow**: Too deep recursion causes stack overflow
4. **Inefficient Pruning**: Not pruning early enough increases time
5. **Forgetting to Backtrack**: Must undo choices after recursion

