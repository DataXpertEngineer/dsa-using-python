"""
Merge Sorted Arrays Problem

Merge two sorted arrays into one sorted array.

Problem Statement:
------------------
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough space
to hold additional elements from nums2.

Example:
    Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    Output: [1, 2, 2, 3, 5, 6]

Variations:
- Merge into first array (in-place)
- Merge into new array
- Merge k sorted arrays

Useful in:
- Two pointers technique
- Merge sort implementation
- Array manipulation
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Extra Space Approach (Language-agnostic)
# ----------------------------------------------------------------------
def merge_sorted_arrays_extra_space(nums1: List[int], m: int, 
                                     nums2: List[int], n: int) -> List[int]:
    """
    Merge two sorted arrays using extra space.

    This approach works in all programming languages.

    Args:
        nums1 (List[int]): First sorted array
        m (int): Number of elements in nums1
        nums2 (List[int]): Second sorted array
        n (int): Number of elements in nums2

    Returns:
        List[int]: Merged sorted array

    Complexity:
        Time: O(m + n)  - Single pass through both arrays.
        Space: O(m + n) - Creates new array to store merged result.
    """
    result = []
    i = j = 0
    
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # Add remaining elements
    while i < m:
        result.append(nums1[i])
        i += 1
    
    while j < n:
        result.append(nums2[j])
        j += 1
    
    return result


# ----------------------------------------------------------------------
# In-place Merge (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place (nums1 has size m + n).

    Algorithm:
    1. Start from the end of both arrays
    2. Compare and place larger element at the end of nums1
    3. Continue until all elements are merged

    This approach works in all programming languages and is space-efficient.

    Args:
        nums1 (List[int]): First sorted array with extra space at end
        m (int): Number of elements in nums1
        nums2 (List[int]): Second sorted array
        n (int): Number of elements in nums2

    Returns:
        None: nums1 is modified in-place

    Complexity:
        Time: O(m + n)  - Single pass from end to beginning.
        Space: O(1)    - Only uses variables for pointers.
    """
    # Start from the end
    i = m - 1  # Last element in nums1
    j = n - 1  # Last element in nums2
    k = m + n - 1  # Last position in merged array
    
    # Merge from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Copy remaining elements from nums2 (if any)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    
    # Remaining elements in nums1 are already in correct position


# ----------------------------------------------------------------------
# Merge into New Array (Language-agnostic)
# ----------------------------------------------------------------------
def merge_sorted_arrays_new(nums1: List[int], m: int, 
                            nums2: List[int], n: int) -> List[int]:
    """
    Merge two sorted arrays into a new sorted array.

    Args:
        nums1 (List[int]): First sorted array
        m (int): Number of elements in nums1
        nums2 (List[int]): Second sorted array
        n (int): Number of elements in nums2

    Returns:
        List[int]: New merged sorted array

    Complexity:
        Time: O(m + n)  - Single pass through both arrays.
        Space: O(m + n) - Creates new array for result.
    """
    result = []
    i = j = 0
    
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # Add remaining elements
    result.extend(nums1[i:m])
    result.extend(nums2[j:n])
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Merge Sorted Arrays Demonstration")
    
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print("nums1:", nums1, f"(m={m})")
    print("nums2:", nums2, f"(n={n})")
    
    # In-place merge
    arr1 = nums1.copy()
    merge_sorted_arrays(arr1, m, nums2, n)
    print(f"\nMerged in-place: {arr1}")
    print("Expected: [1, 2, 2, 3, 5, 6]")
    
    # Merge into new array
    result = merge_sorted_arrays_new([1, 2, 3], 3, [2, 5, 6], 3)
    print(f"Merged into new array: {result}")
    
    # Test with one empty array
    print("\n" + "="*50)
    nums3 = [1, 2, 3, 0, 0]
    nums4 = [4, 5]
    print("nums1:", [1, 2, 3], "(m=3)")
    print("nums2:", nums4, "(n=2)")
    arr3 = nums3.copy()
    merge_sorted_arrays(arr3, 3, nums4, 2)
    print(f"Merged: {arr3}")

