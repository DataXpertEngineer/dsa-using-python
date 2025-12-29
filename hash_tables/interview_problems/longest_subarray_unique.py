"""
Longest Subarray with Unique Elements

Find longest subarray with all unique elements using hash table.

Problem Statement:
-------------------
Given an array, find the length of the longest subarray with all unique elements.

Example:
    Input: [1, 2, 3, 2, 4, 5]
    Output: 4
    Explanation: [1, 2, 3, 2] -> longest is [2, 3, 2, 4, 5] (length 4)
                 Actually: [1, 2, 3] or [2, 4, 5] (length 3)
                 Better example: [1, 2, 3, 4, 2, 5] -> [1, 2, 3, 4] (length 4)

Why Hash Table?
---------------
- Track last occurrence of each element
- Sliding window technique
- O(n) solution

Useful in:
- Longest substring problems
- Common interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Longest Subarray with Unique Elements (Language-agnostic)
# ----------------------------------------------------------------------
def longest_subarray_unique(nums: List[int]) -> int:
    """
    Find length of longest subarray with all unique elements.

    Algorithm:
    1. Use sliding window with hash table
    2. Track last occurrence of each element
    3. Move left pointer when duplicate found
    4. Update maximum length

    Args:
        nums (List[int]): Input array

    Returns:
        int: Length of longest subarray with unique elements

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores last occurrence map.
    """
    last_occurrence: Dict[int, int] = {}
    max_length = 0
    left = 0
    
    for right, num in enumerate(nums):
        # If duplicate found, move left pointer
        if num in last_occurrence and last_occurrence[num] >= left:
            left = last_occurrence[num] + 1
        
        # Update last occurrence
        last_occurrence[num] = right
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ----------------------------------------------------------------------
# Longest Subarray with Unique Elements (Alternative)
# ----------------------------------------------------------------------
def longest_subarray_unique_alt(nums: List[int]) -> int:
    """
    Alternative implementation using set.

    Args:
        nums (List[int]): Input array

    Returns:
        int: Length of longest subarray with unique elements

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores elements in set.
    """
    seen: set[int] = set()
    max_length = 0
    left = 0
    
    for right, num in enumerate(nums):
        # Remove elements until current is unique
        while num in seen:
            seen.remove(nums[left])
            left += 1
        
        seen.add(num)
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Longest Subarray with Unique Elements Demonstration")
    
    nums = [1, 2, 3, 4, 2, 5]
    print(f"Array: {nums}")
    
    result = longest_subarray_unique(nums)
    print(f"Length of longest subarray with unique elements: {result}")
    print("Explanation: [1, 2, 3, 4] has length 4")
    
    # Alternative approach
    result_alt = longest_subarray_unique_alt(nums)
    print(f"Alternative approach: {result_alt}")
    print(f"Results match: {result == result_alt}")
    
    # Another example
    print("\n" + "="*50)
    nums2 = [1, 2, 2, 3, 4, 5]
    print(f"Array: {nums2}")
    result2 = longest_subarray_unique(nums2)
    print(f"Length: {result2}")

