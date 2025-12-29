"""
XOR Tricks and Properties

XOR (exclusive OR) has unique properties that make it useful for many algorithms.

Key Properties:
1. a ^ a = 0 (XOR with itself is zero)
2. a ^ 0 = a (XOR with zero is identity)
3. a ^ b = b ^ a (commutative)
4. (a ^ b) ^ c = a ^ (b ^ c) (associative)
5. a ^ b ^ b = a (XOR twice cancels out)

Why XOR Tricks?
---------------
- Efficient swapping without temporary variable
- Finding unique elements in arrays
- Canceling out pairs
- Useful in many bit manipulation problems

Useful in:
- Finding single/double unique elements
- Swapping without extra space
- Array manipulation
- Common interview problems
"""

from typing import List, Optional, Tuple


# ----------------------------------------------------------------------
# Swap Without Temporary Variable
# ----------------------------------------------------------------------
def swap_xor(a: int, b: int) -> Tuple[int, int]:
    """
    Swap two numbers using XOR (no temporary variable).

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        Tuple[int, int]: Swapped numbers (b, a)

    Complexity:
        Time: O(1)     - Three XOR operations.
        Space: O(1)   - Only uses variables (no temporary needed).
    """
    a = a ^ b
    b = a ^ b  # b = (a ^ b) ^ b = a
    a = a ^ b  # a = (a ^ b) ^ a = b
    return (a, b)


# ----------------------------------------------------------------------
# Find Single Unique Element
# ----------------------------------------------------------------------
def single_number(nums: List[int]) -> int:
    """
    Find the single number that appears once (others appear twice).

    Uses property: a ^ a = 0, so all pairs cancel out.

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
# Find Two Unique Elements
# ----------------------------------------------------------------------
def two_unique_numbers(nums: List[int]) -> Tuple[int, int]:
    """
    Find two numbers that appear once (others appear twice).

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
# Find Missing Number
# ----------------------------------------------------------------------
def missing_number(nums: List[int], n: int) -> int:
    """
    Find missing number in array [0, n] using XOR.

    Args:
        nums (List[int]): Array with n numbers (missing one from 0 to n)
        n (int): Maximum number (array should have 0 to n, one missing)

    Returns:
        int: Missing number

    Complexity:
        Time: O(n)     - XOR all numbers and all indices.
        Space: O(1)   - Only uses variables.
    """
    result = 0
    # XOR all numbers in array
    for num in nums:
        result ^= num
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        result ^= i
    return result


# ----------------------------------------------------------------------
# XOR Properties Demonstration
# ----------------------------------------------------------------------
def demonstrate_xor_properties() -> None:
    """
    Demonstrate key XOR properties.

    Complexity:
        Time: O(1)     - Constant time demonstrations.
        Space: O(1)   - Only uses variables.
    """
    a, b = 5, 3
    
    print("XOR Properties:")
    print(f"a ^ a = {a} ^ {a} = {a ^ a} (should be 0)")
    print(f"a ^ 0 = {a} ^ 0 = {a ^ 0} (should be {a})")
    print(f"a ^ b = {a} ^ {b} = {a ^ b}")
    print(f"b ^ a = {b} ^ {a} = {b ^ a} (commutative)")
    print(f"(a ^ b) ^ b = {a} (XOR twice cancels)")


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: XOR Tricks Demonstration")
    
    # Swap without temporary
    a, b = 5, 10
    print(f"Before swap: a={a}, b={b}")
    a, b = swap_xor(a, b)
    print(f"After swap: a={a}, b={b}")
    
    # Single unique number
    nums1 = [2, 2, 1, 1, 3, 4, 4]
    print(f"\nArray: {nums1}")
    print(f"Single unique number: {single_number(nums1)}")
    print("Expected: 3")
    
    # Two unique numbers
    nums2 = [1, 2, 1, 3, 2, 5]
    print(f"\nArray: {nums2}")
    num1, num2 = two_unique_numbers(nums2)
    print(f"Two unique numbers: {num1}, {num2}")
    print("Expected: 3, 5")
    
    # Missing number
    nums3 = [0, 1, 3, 4]
    n3 = 4
    print(f"\nArray: {nums3}, n={n3}")
    print(f"Missing number: {missing_number(nums3, n3)}")
    print("Expected: 2")
    
    # XOR properties
    print("\n" + "="*50)
    demonstrate_xor_properties()

