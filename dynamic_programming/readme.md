# Dynamic Programming

**Dynamic Programming (DP)** is an optimization technique that solves problems by breaking them down into simpler subproblems and storing results to avoid recomputing them.

## 📁 Folder Structure

```
dynamic_programming/
├── dp.py                                     # Core DP concepts and techniques ⭐ MOST IMPORTANT
├── approaches/                               # DP implementation approaches
│   ├── recursion.py                          # Pure recursive solutions 🟡 MEDIUM
│   ├── memoization.py                        # Top-down DP ⭐ MOST IMPORTANT
│   └── tabulation.py                        # Bottom-up DP ⭐ MOST IMPORTANT
├── classic_problems/                         # Classic DP problems
│   ├── fibonacci.py                          # Fibonacci sequence ⭐ MOST IMPORTANT
│   ├── knapsack.py                           # 0/1 Knapsack problem ⭐ MOST IMPORTANT
│   └── lcs.py                                # Longest Common Subsequence ⭐ MOST IMPORTANT
├── patterns/                                 # Common DP patterns
│   ├── subsequences.py                       # DP on subsequences ⭐ MOST IMPORTANT
│   └── partition.py                          # Partitioning problems 🟡 MEDIUM
└── interview_problems/                       # Typical interview questions
    ├── min_edit_distance.py                  # Edit distance problem ⭐ MOST IMPORTANT
    ├── matrix_chain_multiplication.py        # Matrix chain multiplication 🟡 MEDIUM
    └── coin_change.py                        # Coin change problem ⭐ MOST IMPORTANT
```

## 📚 Definition and Concepts

### What is Dynamic Programming?

**Dynamic Programming** is a method for solving complex problems by breaking them down into simpler subproblems, solving each subproblem only once, and storing their solutions.

#### Key Characteristics:

1. **Overlapping Subproblems**: Same subproblems solved multiple times
2. **Optimal Substructure**: Optimal solution contains optimal sub-solutions
3. **Memoization**: Store results of subproblems (top-down)
4. **Tabulation**: Build solution table bottom-up (bottom-up)

### When to Use DP?

#### DP Works Well For:

- ✅ **Optimization Problems**: Maximum, minimum, optimal
- ✅ **Counting Problems**: Number of ways, distinct solutions
- ✅ **Decision Problems**: Can/cannot, exists/doesn't exist
- ✅ **Overlapping Subproblems**: Same calculations repeated
- ✅ **Optimal Substructure**: Optimal solution = optimal sub-solutions

#### DP Doesn't Work For:

- ❌ **No Overlapping Subproblems**: Each subproblem unique
- ❌ **No Optimal Substructure**: Local optimum ≠ global optimum
- ❌ **Greedy Works Better**: Simpler solution available

### DP Approaches

#### 1. Recursion (`approaches/recursion.py`) 🟡

- **Pure recursive**: No optimization
- **Time Complexity**: O(2^n) typically
- **Space Complexity**: O(n) recursion stack
- **Use**: Understanding problem structure

#### 2. Memoization (`approaches/memoization.py`) ⭐

- **Top-down DP**: Recursive + cache
- **Time Complexity**: O(n) typically
- **Space Complexity**: O(n) memo + stack
- **Use**: Natural recursive solutions

#### 3. Tabulation (`approaches/tabulation.py`) ⭐

- **Bottom-up DP**: Iterative + table
- **Time Complexity**: O(n) typically
- **Space Complexity**: O(n) table
- **Use**: Space optimization possible

## 🔑 Classic Problems

### 1. Fibonacci (`classic_problems/fibonacci.py`) ⭐

- **Problem**: Calculate nth Fibonacci number
- **Approaches**: Recursive, memoization, tabulation, optimized
- **Time Complexity**: O(2^n) → O(n) → O(n) → O(n)
- **Space Complexity**: O(n) → O(n) → O(n) → O(1)

### 2. 0/1 Knapsack (`classic_problems/knapsack.py`) ⭐

- **Problem**: Select items to maximize value within weight limit
- **Approaches**: Recursive, memoization, tabulation, optimized
- **Time Complexity**: O(2^n) → O(n*W) → O(n*W) → O(n*W)
- **Space Complexity**: O(n) → O(n*W) → O(n*W) → O(W)

### 3. Longest Common Subsequence (`classic_problems/lcs.py`) ⭐

- **Problem**: Find longest subsequence common to two strings
- **Approaches**: Recursive, tabulation, optimized
- **Time Complexity**: O(2^(m+n)) → O(m*n) → O(m*n)
- **Space Complexity**: O(m+n) → O(m*n) → O(min(m,n))

## 🎯 DP Patterns

### 1. Subsequences (`patterns/subsequences.py`) ⭐

- **LIS**: Longest Increasing Subsequence
- **Count Distinct**: Count distinct subsequences
- **Max Sum**: Maximum sum increasing subsequence
- **Time Complexity**: O(n²) or O(n log n)

### 2. Partitioning (`patterns/partition.py`) 🟡

- **Equal Sum**: Partition into equal sum subsets
- **Palindrome**: Minimum palindrome cuts
- **Array Partition**: Partition for maximum sum
- **Time Complexity**: O(n²) or O(n*sum)

## 💼 Interview Problems

### Most Important (⭐)

1. **Minimum Edit Distance** (`interview_problems/min_edit_distance.py`)
   - Transform one string to another
   - **Time Complexity**: O(m*n)
   - **Space Complexity**: O(m*n) or O(min(m,n))

2. **Coin Change** (`interview_problems/coin_change.py`)
   - Minimum coins or number of ways
   - **Time Complexity**: O(amount*coins)
   - **Space Complexity**: O(amount)

### Medium Difficulty (🟡)

3. **Matrix Chain Multiplication** (`interview_problems/matrix_chain_multiplication.py`)
   - Optimal matrix multiplication order
   - **Time Complexity**: O(n³)
   - **Space Complexity**: O(n²)

## 📊 Complexity Analysis

| Problem | Recursive | Memoization | Tabulation | Optimized |
|---------|-----------|-------------|------------|-----------|
| Fibonacci | O(2^n) | O(n) | O(n) | O(n) |
| Knapsack | O(2^n) | O(n*W) | O(n*W) | O(n*W) |
| LCS | O(2^(m+n)) | O(m*n) | O(m*n) | O(m*n) |
| Edit Distance | O(3^(m+n)) | O(m*n) | O(m*n) | O(min(m,n)) |
| Coin Change | O(amount^coins) | O(amount*coins) | O(amount*coins) | O(amount) |

Where:
- n = problem size
- W = knapsack capacity
- m, n = string lengths

## 🎓 Learning Path

1. **Start with**: `dp.py` - Understand DP concepts
2. **Learn approaches**: 
   - `recursion.py` - Pure recursive
   - `memoization.py` - Top-down DP
   - `tabulation.py` - Bottom-up DP
3. **Master classics**: 
   - `fibonacci.py` - Simple DP
   - `knapsack.py` - 2D DP
   - `lcs.py` - String DP
4. **Understand patterns**: 
   - `subsequences.py` - Subsequence problems
   - `partition.py` - Partitioning problems
5. **Solve interviews**: 
   - `min_edit_distance.py` - Edit distance
   - `coin_change.py` - Coin change
   - `matrix_chain_multiplication.py` - Matrix chain

## 💡 Key Insights

### DP Strategy:

1. **Identify Subproblems**: What are the smaller problems?
2. **Find Recurrence**: How do subproblems relate?
3. **Base Cases**: What are the smallest problems?
4. **Choose Approach**: Memoization or tabulation?
5. **Optimize Space**: Can we reduce space complexity?

### Common Patterns:

1. **1D DP**: Fibonacci, climbing stairs, coin change
2. **2D DP**: LCS, edit distance, grid paths
3. **Interval DP**: Matrix chain, palindrome partitioning
4. **State DP**: Bitmask DP, traveling salesman

### Tips:

1. **Start with Recursion**: Understand problem first
2. **Add Memoization**: Easy optimization
3. **Convert to Tabulation**: Better space efficiency
4. **Optimize Space**: Reduce dimensions when possible
5. **Practice Patterns**: Recognize common DP patterns

## 🔗 Related Topics

- **Recursion**: Foundation for DP
- **Greedy Algorithms**: Alternative for some problems
- **Divide & Conquer**: Similar but no overlapping subproblems
- **Backtracking**: Explores all possibilities

## 📝 Notes

- All implementations include detailed docstrings
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles
- Multiple approaches included for comparison

## 🚨 Common Pitfalls

1. **Not Identifying DP**: Miss overlapping subproblems
2. **Wrong Recurrence**: Incorrect relation between subproblems
3. **Missing Base Cases**: Forgot to handle base cases
4. **Space Complexity**: Not optimizing when possible
5. **Index Errors**: Off-by-one errors in DP tables

## 🎯 Real-World Applications

### 1. String Processing
- **Edit Distance**: Spell checkers, DNA alignment
- **LCS**: Version control (diff), plagiarism detection

### 2. Optimization
- **Knapsack**: Resource allocation, portfolio optimization
- **Matrix Chain**: Compiler optimization

### 3. Counting
- **Coin Change**: Payment systems
- **Paths**: Grid navigation, game theory

