# Merge Sort Implementation

## What is Merge Sort?

Merge Sort is a divide-and-conquer sorting algorithm that works by:
1. **Dividing** the array into two halves
2. **Recursively sorting** both halves
3. **Merging** the two sorted halves back together

It's one of the most efficient sorting algorithms with a guaranteed O(n log n) time complexity.

## Why Merge Sort?

### Advantages:
- ✅ **Guaranteed O(n log n) performance** - No worst-case scenarios
- ✅ **Stable sort** - Maintains relative order of equal elements
- ✅ **Predictable** - Consistent performance regardless of input
- ✅ **Works well with linked lists** - Doesn't require random access
- ✅ **Parallelizable** - Can be easily parallelized

### Disadvantages:
- ❌ **Requires extra space** - O(n) additional memory
- ❌ **Not in-place** - Needs temporary arrays (unless optimized)
- ❌ **Slower than Quick Sort** - In practice, often slower for arrays

## How Merge Sort Works?

### Algorithm Steps:

1. **Base Case**: If array has 0 or 1 element, it's already sorted
2. **Divide**: Split array into two halves
3. **Conquer**: Recursively sort both halves
4. **Combine**: Merge the two sorted halves

### Merge Process:

The merge operation combines two sorted arrays:
- Compare elements from both arrays
- Take the smaller element and add to result
- Continue until one array is exhausted
- Add remaining elements from the other array

## Implementation Approaches

### 1. Primitive Approach (`merge_sort_primitive.py`)
- **Returns a new sorted array** - Original array remains unchanged
- **Most intuitive version** - Ideal for learning the algorithm
- **Functional programming style** - Non-destructive (doesn't modify input)
- **More memory usage** - Creates new arrays at each recursive level (O(n log n) space)

### 2. Optimized Approach (`merge_sort_optimised.py`)
- **Sorts in-place** - Modifies the original array directly
- **More memory efficient** - Uses temporary arrays only during merge (O(n) space)
- **Better for production use** - More space-efficient implementation
- **Imperative programming style** - Destructive (modifies input)

## Time Complexity

- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

The algorithm always divides the array log n times, and each merge processes n elements.

## Space Complexity

- **Primitive Approach**: O(n log n) - Creates new arrays at each recursive level
- **Optimized Approach**: O(n) - Uses temporary arrays only during merge

## When to Use Merge Sort?

- ✅ When stable sorting is required
- ✅ When worst-case O(n log n) is important
- ✅ For linked lists (efficient for sequential access)
- ✅ External sorting (sorting data too large for memory)
- ✅ When you need predictable performance

## Example Walkthrough

**Input**: `[10, 3, 15, 7, 8, 23, 98, 29]`

```
Divide:
[10, 3, 15, 7] | [8, 23, 98, 29]

Divide further:
[10, 3] | [15, 7] | [8, 23] | [98, 29]

Divide to base case:
[10] | [3] | [15] | [7] | [8] | [23] | [98] | [29]

Merge:
[3, 10] | [7, 15] | [8, 23] | [29, 98]

Merge:
[3, 7, 10, 15] | [8, 23, 29, 98]

Final Merge:
[3, 7, 8, 10, 15, 23, 29, 98]
```

## Key Concepts

### Divide and Conquer
Merge sort is a classic example of the divide-and-conquer paradigm:
- **Divide**: Break problem into smaller subproblems
- **Conquer**: Solve subproblems recursively
- **Combine**: Merge solutions to solve original problem

### Stability
Merge sort is stable because when merging, if two elements are equal, the element from the left array is taken first, preserving the original order.

### Recursion
The algorithm uses recursion to break down the problem:
- Each recursive call handles a smaller subarray
- Base case: arrays of size 0 or 1 are already sorted
- Recursive case: divide, sort, and merge

## Comparison with Other Sorts

| Algorithm | Time (Best) | Time (Worst) | Space | Stable |
|-----------|-------------|--------------|-------|--------|
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(1) | No |
| Bubble Sort | O(n) | O(n²) | O(1) | Yes |

## Learning Path

1. **Start with Primitive Approach**: Understand the basic concept
2. **Study the Merge Operation**: Key to understanding merge sort
3. **Move to Optimized Approach**: Learn space-efficient version
4. **Practice**: Implement both versions yourself
5. **Analyze**: Understand time/space trade-offs
