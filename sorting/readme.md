# Sorting Algorithms

Sorting is the process of arranging data in a particular order (ascending or descending). Understanding different sorting algorithms, their properties, and when to use them is crucial for efficient programming.

## 📁 Folder Structure

```
sorting/
├── sorting.py                             # Core sorting concepts ⭐ MOST IMPORTANT
├── basic/                                  # Simple / elementary sorting
│   ├── bubble_sort.py                      # Bubble Sort 🟡 MEDIUM
│   ├── selection_sort.py                   # Selection Sort 🟡 MEDIUM
│   └── insertion_sort.py                   # Insertion Sort 🟡 MEDIUM
├── divide_and_conquer/                     # Advanced sorting algorithms
│   ├── merge_sort.py                       # Merge Sort ⭐ MOST IMPORTANT
│   └── quick_sort.py                       # Quick Sort ⭐ MOST IMPORTANT
├── applications/                           # Applications of sorting
│   ├── kth_smallest_largest.py            # Find kth smallest/largest element ⭐ MOST IMPORTANT
│   └── sort_colors.py                      # Dutch national flag problem 🟡 MEDIUM
└── interview_problems/                      # Typical interview questions
    ├── sort_array.py                       # General array sorting ⭐ MOST IMPORTANT
    ├── largest_number.py                    # Form largest number from array 🟡 MEDIUM
    └── count_inversions.py                 # Count inversions using merge sort ⭐ MOST IMPORTANT
```

## 📚 Core Concepts

### What is Sorting?

**Sorting** is the process of arranging data in a particular order (ascending or descending) based on some criteria. It's one of the most fundamental operations in computer science.

### Properties of Sorting Algorithms

#### 1. **Stability**
- **Definition**: A sorting algorithm is **stable** if it maintains the relative order of elements with equal keys.
- **Example**: 
  - Input: `[(3, 'a'), (2, 'b'), (3, 'c')]`
  - Stable sort: `[(2, 'b'), (3, 'a'), (3, 'c')]` - 'a' comes before 'c'
  - Unstable sort: `[(2, 'b'), (3, 'c'), (3, 'a')]` - order may change
- **Why Important**: Needed when sorting by multiple criteria or preserving original order matters.

#### 2. **In-place vs Out-of-place**
- **In-place**: Uses O(1) extra space (excluding input array)
  - Examples: Bubble sort, Selection sort, Insertion sort, Quick sort
  - Advantage: Memory efficient
- **Out-of-place**: Requires O(n) or more extra space
  - Examples: Merge sort
  - Advantage: Can be more stable, easier to implement

#### 3. **Comparison-based vs Non-comparison**
- **Comparison-based**: Compares elements to determine order
  - Examples: All basic sorts, Merge sort, Quick sort
  - Lower bound: O(n log n) for comparison-based sorts
- **Non-comparison**: Uses other properties (e.g., counting, radix)
  - Examples: Counting sort, Radix sort, Bucket sort
  - Can achieve O(n) time complexity

#### 4. **Time Complexity**
- **Best Case**: Minimum time for best input
- **Average Case**: Expected time for random input
- **Worst Case**: Maximum time for worst input

#### 5. **Adaptive vs Non-adaptive**
- **Adaptive**: Performs better on nearly sorted data
  - Examples: Insertion sort, Bubble sort (optimized)
- **Non-adaptive**: Performance doesn't depend on input order
  - Examples: Selection sort, Merge sort

## 🔑 Basic Sorting Algorithms

### 1. Bubble Sort (`basic/bubble_sort.py`) 🟡
- **How it works**: Repeatedly compares adjacent elements and swaps if wrong order
- **Time Complexity**: O(n²) worst/average, O(n) best (optimized)
- **Space Complexity**: O(1)
- **Stable**: Yes
- **In-place**: Yes
- **Use when**: Small datasets, educational purposes

### 2. Selection Sort (`basic/selection_sort.py`) 🟡
- **How it works**: Finds minimum and places at beginning, repeats
- **Time Complexity**: O(n²) all cases
- **Space Complexity**: O(1)
- **Stable**: No
- **In-place**: Yes
- **Use when**: Small datasets, minimum swaps needed

### 3. Insertion Sort (`basic/insertion_sort.py`) 🟡
- **How it works**: Builds sorted array one element at a time
- **Time Complexity**: O(n²) worst/average, O(n) best
- **Space Complexity**: O(1)
- **Stable**: Yes
- **In-place**: Yes
- **Use when**: Small datasets, nearly sorted data

## 🎯 Advanced Sorting Algorithms

### 1. Merge Sort (`divide_and_conquer/merge_sort.py`) ⭐
- **How it works**: Divide array, sort halves, merge
- **Time Complexity**: O(n log n) all cases
- **Space Complexity**: O(n)
- **Stable**: Yes
- **In-place**: No
- **Use when**: Large datasets, stability required, guaranteed O(n log n)

### 2. Quick Sort (`divide_and_conquer/quick_sort.py`) ⭐
- **How it works**: Choose pivot, partition, recursively sort partitions
- **Time Complexity**: O(n log n) average, O(n²) worst
- **Space Complexity**: O(log n) recursion stack
- **Stable**: No
- **In-place**: Yes
- **Use when**: General-purpose sorting, average performance matters

## 🎯 Applications

### 1. Kth Smallest/Largest (`applications/kth_smallest_largest.py`) ⭐
- Find kth order statistic efficiently
- **Approaches**: Sorting O(n log n), Quickselect O(n), Heap O(n log k)
- **Time Complexity**: O(n) average with quickselect
- **Space Complexity**: O(1) with quickselect

### 2. Sort Colors (`applications/sort_colors.py`) 🟡
- Dutch National Flag problem
- **Algorithm**: Three-way partitioning
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## 💼 Interview Problems

### Most Important (⭐)

1. **Sort Array** (`interview_problems/sort_array.py`)
   - General sorting problem
   - Multiple approaches available
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(1) in-place

2. **Count Inversions** (`interview_problems/count_inversions.py`)
   - Count pairs (i, j) where i < j and arr[i] > arr[j]
   - Uses modified merge sort
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

3. **Largest Number** (`interview_problems/largest_number.py`)
   - Form largest number from array
   - Custom sorting with string comparison
   - **Time Complexity**: O(n log n × k)
   - **Space Complexity**: O(n)

## 📊 Complexity Comparison

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |

## 🎓 Learning Path

1. **Start with**: `sorting.py` - Understand core concepts
2. **Learn basic sorts**: 
   - `bubble_sort.py` - Simplest to understand
   - `selection_sort.py` - Minimum swaps
   - `insertion_sort.py` - Good for small arrays
3. **Master advanced sorts**: 
   - `merge_sort.py` - Guaranteed O(n log n)
   - `quick_sort.py` - Fast in practice
4. **Practice applications**: 
   - `kth_smallest_largest.py` - Order statistics
   - `sort_colors.py` - Three-way partitioning
5. **Solve interview problems**: Start with ⭐ marked problems

## 💡 Key Insights

1. **Stability Matters**: Important when sorting by multiple criteria
2. **In-place vs Space**: Trade-off between memory and implementation
3. **Best Case Matters**: Some algorithms adapt to input (insertion sort)
4. **Worst Case Matters**: Quick sort can degrade to O(n²)
5. **Hybrid Approaches**: Real-world sorts combine multiple algorithms (e.g., Timsort)

## 🔗 Related Topics

- **Arrays**: Most sorting works on arrays
- **Heaps**: Heap sort uses heap data structure
- **Divide and Conquer**: Merge sort and quick sort use this technique
- **Recursion**: Many sorts use recursion
- **Search**: Sorted arrays enable binary search

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings
- Python's built-in `sort()` uses Timsort (hybrid of merge sort and insertion sort)

