"""
Linear Search Algorithm

Linear search (also known as sequential search) is a simple searching algorithm
that checks each element in the array sequentially until the target is found
or the entire array has been searched.

The algorithm:
1. Start from the first element
2. Compare each element with the target
3. If found, return the index
4. If not found after checking all elements, return -1

Why Linear Search?
------------------
Advantages:
    - Works on unsorted arrays
    - Simple to implement
    - No preprocessing required

Disadvantages:
    - Inefficient for large arrays: O(n) time
    - For sorted arrays, binary search is much faster

Useful in:
- Small arrays or unsorted data
- When array is not sorted
- When searching for multiple occurrences
- Educational purposes to understand basic search
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# Basic Linear Search
# ----------------------------------------------------------------------
def linear_search(arr: List[int], target: int) -> int:
    """
    Search for target in array using linear search.

    Args:
        arr (List[int]): Input array (can be unsorted)
        target (int): Element to search for

    Returns:
        int: Index of target if found, -1 otherwise

    Complexity:
        Time: O(n)    - In worst case, checks all n elements.
        Space: O(1)   - Only uses a few variables for iteration.
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


def linear_search_all_occurrences(arr: List[int], target: int) -> List[int]:
    """
    Find all occurrences of target in array using linear search.

    Args:
        arr (List[int]): Input array (can be unsorted)
        target (int): Element to search for

    Returns:
        List[int]: List of all indices where target is found

    Complexity:
        Time: O(n)    - Must check all n elements to find all occurrences.
        Space: O(k)   - Where k is the number of occurrences (result list).
    """
    indices = []
    for i, num in enumerate(arr):
        if num == target:
            indices.append(i)
    return indices


def linear_search_with_sentinel(arr: List[int], target: int) -> int:
    """
    Linear search with sentinel value optimization.

    By placing target at the end as a sentinel, we eliminate one comparison
    per iteration (checking if we've reached the end).

    Args:
        arr (List[int]): Input array (can be unsorted)
        target (int): Element to search for

    Returns:
        int: Index of target if found, -1 otherwise

    Complexity:
        Time: O(n)    - Still checks up to n elements, but fewer comparisons per element.
        Space: O(1)   - Only uses variables for iteration.
    """
    if not arr:
        return -1
    
    # Store last element and place sentinel
    last = arr[-1]
    arr[-1] = target
    
    i = 0
    while arr[i] != target:
        i += 1
    
    # Restore original last element
    arr[-1] = last
    
    # Check if we found target or hit sentinel
    if i < len(arr) - 1 or arr[-1] == target:
        return i
    return -1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Linear Search Demonstration")
    
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    target = 110
    print("Array:", arr)
    print("Target:", target)
    
    # Basic linear search
    result = linear_search(arr, target)
    if result != -1:
        print(f"\n✓ Found {target} at index {result}")
    else:
        print(f"\n✗ {target} not found in array")
    
    # Search for element not in array
    target2 = 200
    result2 = linear_search(arr, target2)
    print(f"\nSearching for {target2}: {'Found at index ' + str(result2) if result2 != -1 else 'Not found'}")
    
    # Find all occurrences
    print("\n" + "="*50)
    arr2 = [10, 20, 30, 20, 40, 20, 50]
    target3 = 20
    print("Array:", arr2)
    print("Target:", target3)
    occurrences = linear_search_all_occurrences(arr2, target3)
    print(f"All occurrences of {target3} at indices: {occurrences}")

