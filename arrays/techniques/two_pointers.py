"""
Two Pointers Technique for Arrays

The two pointers technique uses two pointers (indices) that traverse the array
in a coordinated manner to solve problems efficiently.

Common patterns:
1. Opposite ends: Start from both ends and move toward center
2. Same direction: Both pointers move in the same direction (fast/slow)
3. Different speeds: One pointer moves faster than the other

Why Two Pointers?
-----------------
Without two pointers (naive approach):
    Nested loops = O(n²) or O(n³)
With two pointers:
    Single pass through array = O(n)

Useful in:
- Sorted array problems (pair sum, triplet sum)
- Palindrome checking
- Removing duplicates
- Partitioning problems
- Finding pairs/triplets with specific properties
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Brute-force / Naive Approach
# ----------------------------------------------------------------------
def pair_sum_naive(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that sum to target using naive approach.

    Args:
        arr (List[int]): Input array (sorted)
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int]]: Indices of the two numbers, or None if not found

    Complexity:
        Time: O(n²)    - Nested loops check all pairs of elements.
        Space: O(1)    - Only uses a few variables for indices.
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None


# ----------------------------------------------------------------------
# Two Pointers Approach (Optimized)
# ----------------------------------------------------------------------
def pair_sum_two_pointers(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that sum to target using two pointers technique.

    Args:
        arr (List[int]): Input array (must be sorted)
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int]]: Indices of the two numbers, or None if not found

    Complexity (on sorted array):
        Time: O(n)    - Each pointer moves at most n steps total.
        Space: O(1)   - Only uses a couple of indices.
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1  # Need larger sum, move left pointer right
        else:
            right -= 1  # Need smaller sum, move right pointer left
    
    return None


def remove_duplicates_sorted(arr: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place using two pointers.

    Args:
        arr (List[int]): Input sorted array (modified in-place)

    Returns:
        int: Length of array after removing duplicates

    Complexity (on sorted array):
        Time: O(n)    - Fast pointer traverses array once, slow pointer moves forward.
        Space: O(1)   - Only uses two pointer indices, modifies array in-place.
    """
    if not arr:
        return 0
    
    # Slow pointer: position to place next unique element
    slow = 0
    
    # Fast pointer: traverses the array
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using two pointers.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, False otherwise

    Complexity:
        Time: O(n)    - Pointers meet at the center after at most n/2 comparisons.
        Space: O(1)   - Only uses two pointer indices.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def triplet_sum(arr: List[int], target: int) -> Optional[Tuple[int, int, int]]:
    """
    Find three numbers that sum to target using two pointers.

    Args:
        arr (List[int]): Input array (must be sorted)
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int, int]]: Indices of the three numbers, or None if not found

    Complexity (on sorted array):
        Time: O(n²)   - Outer loop O(n), inner two-pointer search O(n) per iteration.
        Space: O(1)   - Only uses a few indices for pointers.
    """
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return (i, left, right)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Two Pointers Demonstration")
    
    # Example 1: Pair Sum
    arr1 = [1, 2, 3, 4, 5, 6]
    target1 = 9
    print("Example 1: Pair Sum")
    print("Array:", arr1)
    print("Target sum:", target1)
    
    print("\nNaive Approach:")
    result_naive = pair_sum_naive(arr1, target1)
    if result_naive:
        print(f"Found pair at indices {result_naive}: ({arr1[result_naive[0]]}, {arr1[result_naive[1]]})")
    
    print("\nTwo Pointers Approach:")
    result = pair_sum_two_pointers(arr1, target1)
    if result:
        print(f"Found pair at indices {result}: ({arr1[result[0]]}, {arr1[result[1]]})")
    
    # Example 2: Remove Duplicates
    print("\n" + "="*50)
    arr2 = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print("Example 2: Remove Duplicates")
    print("Original array:", arr2)
    new_length = remove_duplicates_sorted(arr2)
    print(f"After removing duplicates (length = {new_length}):", arr2[:new_length])
    
    # Example 3: Palindrome Check
    print("\n" + "="*50)
    test_strings = ["racecar", "hello", "level", "python"]
    print("Example 3: Palindrome Check")
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' is {'a palindrome' if result else 'not a palindrome'}")
    
    # Example 4: Triplet Sum
    print("\n" + "="*50)
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    target3 = 12
    print("Example 4: Triplet Sum")
    print("Array:", arr3)
    print("Target sum:", target3)
    result = triplet_sum(arr3, target3)
    if result:
        print(f"Found triplet at indices {result}: ({arr3[result[0]]}, {arr3[result[1]]}, {arr3[result[2]]})")

