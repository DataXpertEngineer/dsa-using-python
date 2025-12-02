"""
Majority Element Problem

Find the majority element in an array (appears more than n/2 times).

Problem Statement:
------------------
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊n/2⌋ times.

You may assume that the array is non-empty and the majority element always exists
in the array.

Example:
    Input: nums = [3, 2, 3]
    Output: 3

Example:
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Useful in:
- Hash tables
- Boyer-Moore voting algorithm
- Array manipulation
- Common interview problem
"""

from typing import List, Optional
from collections import Counter


# ----------------------------------------------------------------------
# Hash Table Approach (Language-agnostic)
# ----------------------------------------------------------------------
def majority_element_hashmap(nums: List[int]) -> int:
    """
    Find majority element using hash map to count occurrences.

    This approach works in all programming languages.

    Args:
        nums (List[int]): Input array

    Returns:
        int: Majority element

    Complexity:
        Time: O(n)     - Single pass to count, single pass to find majority.
        Space: O(n)   - Stores count for each unique element.
    """
    count = {}
    n = len(nums)
    majority_count = n // 2
    
    # Count occurrences
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > majority_count:
            return num
    
    # Should not reach here if majority exists
    return nums[0]


# ----------------------------------------------------------------------
# Boyer-Moore Voting Algorithm (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def majority_element_voting(nums: List[int]) -> int:
    """
    Find majority element using Boyer-Moore voting algorithm.

    This is the optimal O(n) time, O(1) space solution that works in all languages.

    Algorithm:
    1. Assume first element is candidate, count = 1
    2. For each element:
       - If same as candidate, increment count
       - If different, decrement count
       - If count becomes 0, set current element as new candidate
    3. The candidate at the end is the majority element

    Args:
        nums (List[int]): Input array

    Returns:
        int: Majority element

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(1)   - Only uses variables for candidate and count.
    """
    candidate = None
    count = 0
    
    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Verify candidate (if problem guarantees majority exists, this is optional)
    # For this problem, we assume majority always exists
    return candidate


def majority_element_voting_with_verification(nums: List[int]) -> Optional[int]:
    """
    Find majority element with verification step (handles case where no majority exists).

    Args:
        nums (List[int]): Input array

    Returns:
        Optional[int]: Majority element if exists, None otherwise

    Complexity:
        Time: O(n)     - Two passes: one to find candidate, one to verify.
        Space: O(1)   - Only uses variables for candidate and count.
    """
    candidate = None
    count = 0
    
    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Verify candidate
    if candidate is not None:
        count = sum(1 for num in nums if num == candidate)
        if count > len(nums) // 2:
            return candidate
    
    return None


# ----------------------------------------------------------------------
# Sorting Approach (Language-agnostic)
# ----------------------------------------------------------------------
def majority_element_sorting(nums: List[int]) -> int:
    """
    Find majority element using sorting.

    After sorting, the majority element will always be at index n/2.

    Args:
        nums (List[int]): Input array (will be sorted)

    Returns:
        int: Majority element

    Complexity:
        Time: O(n log n)  - Sorting takes O(n log n) time.
        Space: O(1)      - If sorting is in-place, otherwise O(n).
    """
    nums.sort()
    return nums[len(nums) // 2]


# ----------------------------------------------------------------------
# Python-specific Approach (Using Counter)
# ----------------------------------------------------------------------
def majority_element_counter(nums: List[int]) -> int:
    """
    Find majority element using Python's Counter (Python-specific).

    Args:
        nums (List[int]): Input array

    Returns:
        int: Majority element

    Complexity:
        Time: O(n)     - Counter counts all elements in one pass.
        Space: O(n)   - Counter stores count for each unique element.
    """
    counter = Counter(nums)
    n = len(nums)
    majority_count = n // 2
    
    for num, count in counter.items():
        if count > majority_count:
            return num
    
    return nums[0]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Majority Element Problem Demonstration")
    
    nums1 = [3, 2, 3]
    print("Array:", nums1)
    
    # Hash map approach
    result1 = majority_element_hashmap(nums1)
    print(f"Majority element (hash map): {result1}")
    
    # Voting algorithm (optimal)
    result2 = majority_element_voting(nums1)
    print(f"Majority element (voting algorithm): {result2}")
    
    # Python Counter
    result3 = majority_element_counter(nums1)
    print(f"Majority element (Counter): {result3}")
    
    # Test with larger array
    print("\n" + "="*50)
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print("Array:", nums2)
    result = majority_element_voting(nums2)
    print(f"Majority element: {result}")
    print(f"Count of {result}: {nums2.count(result)} (>{len(nums2)//2})")
    
    # Test with verification
    print("\n" + "="*50)
    nums3 = [1, 1, 2, 2, 3]  # No majority
    print("Array (no majority):", nums3)
    result = majority_element_voting_with_verification(nums3)
    print(f"Majority element: {result}")

