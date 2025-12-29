"""
Single Number Problem (Bit-based Algorithms)

Find element(s) that appear once, twice, or thrice in an array where
all other elements appear a different number of times.

Variations:
1. Single number: All appear twice except one
2. Single number II: All appear three times except one
3. Single number III: All appear twice except two

Why Bit Manipulation?
---------------------
Without bit manipulation:
    Use hash map = O(n) time, O(n) space
With bit manipulation:
    O(n) time, O(1) space using XOR and bit counting

Useful in:
- Finding unique elements
- XOR properties
- Common interview problems
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Single Number (appears once, others twice)
# ----------------------------------------------------------------------
def single_number(nums: List[int]) -> int:
    """
    Find the single number that appears once (others appear twice).

    Uses XOR property: a ^ a = 0, so all pairs cancel out.

    Args:
        nums (List[int]): Array where every element appears twice except one

    Returns:
        int: The single unique element

    Complexity:
        Time: O(n)     - Single pass through array, XOR all elements.
        Space: O(1)   - Only uses a variable to store XOR result.
    """
    result = 0
    for num in nums:
        result ^= num
    return result


# ----------------------------------------------------------------------
# Single Number II (appears once, others three times)
# ----------------------------------------------------------------------
def single_number_ii(nums: List[int]) -> int:
    """
    Find the single number that appears once (others appear three times).

    Algorithm:
    Count set bits at each position. If count % 3 != 0, that bit
    belongs to the single number.

    Args:
        nums (List[int]): Array where every element appears three times except one

    Returns:
        int: The single unique element

    Complexity:
        Time: O(n)     - Processes each number and each bit position.
        Space: O(1)   - Only uses variables for bit counting.
    """
    result = 0
    
    # Check each bit position
    for i in range(32):
        count = 0
        # Count set bits at position i
        for num in nums:
            if (num >> i) & 1:
                count += 1
        # If count is not multiple of 3, set this bit in result
        if count % 3 != 0:
            result |= (1 << i)
    
    # Handle negative numbers (two's complement)
    if result >= (1 << 31):
        result -= (1 << 32)
    
    return result


# ----------------------------------------------------------------------
# Single Number III (two unique numbers)
# ----------------------------------------------------------------------
def single_number_iii(nums: List[int]) -> Tuple[int, int]:
    """
    Find two numbers that appear once (others appear twice).

    Algorithm:
    1. XOR all numbers to get XOR of the two unique numbers
    2. Find a set bit in the XOR result
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
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Single Number Problems Demonstration")
    
    # Single number
    nums1 = [2, 2, 1, 1, 3, 4, 4]
    print(f"Array: {nums1}")
    print(f"Single number: {single_number(nums1)}")
    print("Expected: 3")
    
    # Single number II
    nums2 = [2, 2, 3, 2]
    print(f"\nArray: {nums2}")
    print(f"Single number II: {single_number_ii(nums2)}")
    print("Expected: 3")
    
    # Single number III
    nums3 = [1, 2, 1, 3, 2, 5]
    print(f"\nArray: {nums3}")
    num1, num2 = single_number_iii(nums3)
    print(f"Two unique numbers: {num1}, {num2}")
    print("Expected: 3, 5")

