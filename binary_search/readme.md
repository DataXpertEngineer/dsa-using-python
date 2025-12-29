# Binary Search

Binary search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half. It's one of the most fundamental and powerful algorithms in computer science.

## 📁 Folder Structure

```
binary_search/
├── iterative.py                            # Iterative binary search ⭐ MOST IMPORTANT
├── recursive.py                            # Recursive binary search ⭐ MOST IMPORTANT
├── rotated_array.py                        # Binary search in rotated array ⭐ MOST IMPORTANT
├── peak_finding.py                         # Peak finding problem 🟡 MEDIUM
└── binary_search_on_answer.py             # Advanced technique: search on answer 🟡 MEDIUM
```

## 📚 Definition and Concepts

### What is Binary Search?

**Binary search** is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array.

#### Key Characteristics:

1. **Requires Sorted Array**: Array must be sorted (ascending or descending)
2. **Divide and Conquer**: Eliminates half of the search space at each step
3. **Time Complexity**: O(log n) - extremely efficient
4. **Space Complexity**: O(1) iterative, O(log n) recursive

### How Binary Search Works

#### Algorithm Steps:

1. **Initialize**: Set `left = 0`, `right = n - 1`
2. **Loop**: While `left <= right`:
   - Calculate `mid = (left + right) // 2`
   - Compare `arr[mid]` with target:
     - If equal: Found! Return `mid`
     - If `arr[mid] < target`: Search right half (`left = mid + 1`)
     - If `arr[mid] > target`: Search left half (`right = mid - 1`)
3. **Not Found**: If loop ends, target doesn't exist

#### Visual Example:

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 7

Step 1: [1, 3, 5, 7, 9, 11, 13, 15]
         ↑           ↑           ↑
       left=0      mid=3      right=7
       arr[3] = 7 == target ✓ Found!
```

### Why Binary Search?

#### Advantages:

1. **Efficient**: O(log n) vs O(n) for linear search
2. **Fast**: For 1 million elements, only ~20 comparisons needed
3. **Simple**: Easy to understand and implement
4. **Versatile**: Can be adapted for many problems

#### When to Use:

- ✅ Array is sorted
- ✅ Need to find element or insertion point
- ✅ Need O(log n) search time
- ✅ Array doesn't change frequently

#### When NOT to Use:

- ❌ Array is not sorted
- ❌ Need to find all occurrences (use linear search)
- ❌ Array changes frequently (consider hash table)

## 🔑 Core Implementations

### 1. Iterative Binary Search (`iterative.py`) ⭐

- **How it works**: Uses while loop with left/right pointers
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Use Cases**: Standard search, first/last occurrence, insertion point

**Key Functions:**
- `binary_search()`: Basic search
- `binary_search_first()`: First occurrence
- `binary_search_last()`: Last occurrence
- `binary_search_insertion_point()`: Insertion index

### 2. Recursive Binary Search (`recursive.py`) ⭐

- **How it works**: Uses function recursion
- **Time Complexity**: O(log n)
- **Space Complexity**: O(log n) - recursion stack
- **Use Cases**: Cleaner code, divide-and-conquer problems

**Key Functions:**
- `binary_search_recursive()`: Basic recursive search
- `binary_search_range()`: Find range of target

## 🎯 Advanced Problems

### 1. Rotated Array (`rotated_array.py`) ⭐

- **Problem**: Search in rotated sorted array
- **Example**: `[4,5,6,7,0,1,2]` (rotated from `[0,1,2,4,5,6,7]`)
- **Key Insight**: Identify which half is sorted
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

**Key Functions:**
- `search_rotated_array()`: Search target in rotated array
- `find_min_rotated()`: Find minimum element
- `search_rotated_with_duplicates()`: Handle duplicates

### 2. Peak Finding (`peak_finding.py`) 🟡

- **Problem**: Find peak element (greater than neighbors)
- **Key Insight**: Binary search works even on unsorted array
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

**Key Functions:**
- `find_peak_element()`: Find any peak
- `find_all_peaks()`: Find all peaks
- `find_peak_2d()`: 2D peak finding

### 3. Binary Search on Answer (`binary_search_on_answer.py`) 🟡

- **Concept**: Search for answer in answer space
- **Key Insight**: Monotonic property enables binary search
- **Use Cases**: Optimization problems, when direct calculation is hard

**Key Functions:**
- `sqrt_binary_search()`: Integer square root
- `split_array_largest_sum()`: Split array problem
- `min_eating_speed()`: Koko eating bananas

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Basic Search | O(log n) | O(1) |
| Recursive Search | O(log n) | O(log n) |
| First/Last Occurrence | O(log n) | O(1) |
| Rotated Array Search | O(log n) | O(1) |
| Peak Finding | O(log n) | O(1) |
| Binary Search on Answer | O(log n × f(n)) | O(1) |

Where:
- n = array size
- f(n) = complexity of validation function

## 🎓 Learning Path

1. **Start with**: `iterative.py` - Understand basic binary search
2. **Learn recursive**: `recursive.py` - Alternative implementation
3. **Master rotated**: `rotated_array.py` - Advanced pattern
4. **Explore advanced**: 
   - `peak_finding.py` - Binary search on unsorted
   - `binary_search_on_answer.py` - Optimization problems

## 💡 Key Insights

### Binary Search Patterns:

1. **Standard Pattern**: Search for exact value
2. **First/Last Pattern**: Search for boundary
3. **Rotated Pattern**: Identify sorted half
4. **Peak Pattern**: Compare with neighbors
5. **Answer Pattern**: Search in answer space

### Common Mistakes:

1. **Off-by-one errors**: `left <= right` vs `left < right`
2. **Integer overflow**: `mid = (left + right) // 2` (safe in Python)
3. **Not checking boundaries**: Always validate array bounds
4. **Wrong comparison**: Ensure array is sorted
5. **Infinite loops**: Ensure `left` or `right` changes

### Tips:

1. **Use iterative for production**: Better space efficiency
2. **Use recursive for clarity**: Easier to understand
3. **Handle edge cases**: Empty array, single element
4. **Test with duplicates**: First/last occurrence matters
5. **Practice variations**: Rotated, peak, answer space

## 🔗 Related Topics

- **Arrays**: Binary search works on sorted arrays
- **Sorting**: Array must be sorted first
- **Divide and Conquer**: Binary search uses this technique
- **Two Pointers**: Similar pointer manipulation
- **Search Algorithms**: Part of search algorithm family

## 📝 Notes

- All implementations include detailed docstrings
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles
- Both iterative and recursive approaches included

## 🚨 Common Pitfalls

1. **Unsorted Array**: Binary search requires sorted array
2. **Wrong Mid Calculation**: Use `(left + right) // 2`
3. **Boundary Updates**: `left = mid + 1`, not `left = mid`
4. **Base Case**: Check `left <= right` condition
5. **Edge Cases**: Handle empty array, single element

## 🎯 Problem Patterns

### Pattern 1: Exact Match
```python
# Find target in sorted array
if arr[mid] == target:
    return mid
```

### Pattern 2: First Occurrence
```python
# Continue searching left when found
if arr[mid] == target:
    result = mid
    right = mid - 1
```

### Pattern 3: Last Occurrence
```python
# Continue searching right when found
if arr[mid] == target:
    result = mid
    left = mid + 1
```

### Pattern 4: Rotated Array
```python
# Identify sorted half
if arr[left] <= arr[mid]:  # Left half sorted
    # Check if target in sorted half
```

### Pattern 5: Binary Search on Answer
```python
# Search in answer space
if is_valid(mid):
    result = mid
    # Adjust boundaries based on problem
```

