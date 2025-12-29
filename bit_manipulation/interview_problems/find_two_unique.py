"""
Find Two Unique Numbers

Find two numbers that appear once in an array where all other numbers appear twice.

Problem Statement:
-------------------
Given an array where every element appears twice except two elements,
find the two unique elements.

Example:
    Input: nums = [1, 2, 1, 3, 2, 5]
    Output: [3, 5]

Useful in:
- Finding unique elements
- XOR properties
- Common interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Find Two Unique - XOR (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def find_two_unique(nums: List[int]) -> Tuple[int, int]:
    """
    Find two numbers that appear once using XOR.

    Algorithm:
    1. XOR all numbers to get XOR of the two unique numbers
    2. Find a set bit in the XOR result (differentiates the two numbers)
    3. Partition array based on this bit
    4. XOR each partition to get the two unique numbers

    Args:
        nums (List[int]): Array where every element appears twice except two

    Returns:
        Tuple[int, int]: The two unique elements

    Complexity:
        Time: O(n)     - Two passes through array.
        Space: O(1)   - Only uses variables.
    """
    # XOR all numbers
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    # Find rightmost set bit
    rightmost_set = xor_all & (-xor_all)
    
    # Partition and find unique numbers
    num1 = 0
    num2 = 0
    
    for num in nums:
        if num & rightmost_set:
            num1 ^= num
        else:
            num2 ^= num
    
    return (num1, num2)


# ----------------------------------------------------------------------
# Find Two Unique - Hash Map (Alternative)
# ----------------------------------------------------------------------
def find_two_unique_hashmap(nums: List[int]) -> Tuple[int, int]:
    """
    Find two unique numbers using hash map.

    Args:
        nums (List[int]): Array

    Returns:
        Tuple[int, int]: The two unique elements

    Complexity:
        Time: O(n)     - Single pass to count, another to find.
        Space: O(n)   - Stores frequency map.
    """
    from collections import Counter
    
    count = Counter(nums)
    unique = [num for num, freq in count.items() if freq == 1]
    return (unique[0], unique[1])


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Find Two Unique Numbers Demonstration")
    
    nums = [1, 2, 1, 3, 2, 5]
    print(f"Array: {nums}")
    num1, num2 = find_two_unique(nums)
    print(f"Two unique numbers (XOR): {num1}, {num2}")
    print("Expected: 3, 5")
    
    # Hash map approach
    num1_hm, num2_hm = find_two_unique_hashmap(nums)
    print(f"Two unique numbers (HashMap): {num1_hm}, {num2_hm}")

