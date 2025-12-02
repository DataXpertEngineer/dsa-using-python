"""
Product of Array Except Self Problem

Return an array where each element is the product of all other elements.

Problem Statement:
------------------
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operator.

Example:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
    Explanation:
        answer[0] = 2 * 3 * 4 = 24
        answer[1] = 1 * 3 * 4 = 12
        answer[2] = 1 * 2 * 4 = 8
        answer[3] = 1 * 2 * 3 = 6

Useful in:
- Array manipulation
- Prefix/suffix products
- Space optimization
- Common interview problem
"""

from typing import List


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def product_except_self_naive(nums: List[int]) -> List[int]:
    """
    Calculate product except self using brute-force approach.

    This approach works in all programming languages but is inefficient.

    Args:
        nums (List[int]): Input array

    Returns:
        List[int]: Array where each element is product of all others

    Complexity:
        Time: O(n²)    - For each element, multiply all other n-1 elements.
        Space: O(1)   - Excluding output array, only uses variables.
    """
    n = len(nums)
    result = [1] * n
    
    for i in range(n):
        for j in range(n):
            if i != j:
                result[i] *= nums[j]
    
    return result


# ----------------------------------------------------------------------
# Using Division (Language-agnostic, but has limitations)
# ----------------------------------------------------------------------
def product_except_self_division(nums: List[int]) -> List[int]:
    """
    Calculate product except self using division (if zeros are handled).

    Note: This approach fails if there are zeros or if division is not allowed.

    Args:
        nums (List[int]): Input array (should not contain zeros)

    Returns:
        List[int]: Array where each element is product of all others

    Complexity:
        Time: O(n)     - Two passes: one to calculate total product, one to divide.
        Space: O(1)   - Excluding output array.
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate total product
    total_product = 1
    for num in nums:
        total_product *= num
    
    # Divide by each element
    for i in range(n):
        result[i] = total_product // nums[i]
    
    return result


# ----------------------------------------------------------------------
# Prefix and Suffix Products (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def product_except_self(nums: List[int]) -> List[int]:
    """
    Calculate product except self using prefix and suffix products.

    Algorithm:
    1. Calculate prefix products (product of all elements to the left)
    2. Calculate suffix products (product of all elements to the right)
    3. Multiply prefix[i] * suffix[i] for each position

    This approach works in all programming languages and is optimal.

    Args:
        nums (List[int]): Input array

    Returns:
        List[int]: Array where each element is product of all others

    Complexity:
        Time: O(n)     - Three passes: prefix, suffix, and result calculation.
        Space: O(n)   - Stores prefix and suffix arrays (can be optimized to O(1)).
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    
    # Calculate suffix products and multiply with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] = prefix[i] * suffix
        suffix *= nums[i]
    
    return result


# ----------------------------------------------------------------------
# Space-optimized Version (Language-agnostic)
# ----------------------------------------------------------------------
def product_except_self_optimized(nums: List[int]) -> List[int]:
    """
    Calculate product except self with O(1) extra space (excluding output).

    Uses the output array to store prefix products, then multiplies by suffix.

    Args:
        nums (List[int]): Input array

    Returns:
        List[int]: Array where each element is product of all others

    Complexity:
        Time: O(n)     - Two passes through array.
        Space: O(1)   - Excluding output array, only uses variables.
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products in result array
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    
    # Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Product of Array Except Self Demonstration")
    
    nums1 = [1, 2, 3, 4]
    print("Array:", nums1)
    
    result1 = product_except_self(nums1)
    print(f"Product except self: {result1}")
    print("Explanation:")
    for i, num in enumerate(nums1):
        others = [nums1[j] for j in range(len(nums1)) if j != i]
        product = 1
        for x in others:
            product *= x
        print(f"  result[{i}] = {' * '.join(map(str, others))} = {product}")
    
    # Test with optimized version
    print("\n" + "="*50)
    nums2 = [-1, 1, 0, -3, 3]
    print("Array:", nums2)
    result2 = product_except_self_optimized(nums2)
    print(f"Product except self (optimized): {result2}")

