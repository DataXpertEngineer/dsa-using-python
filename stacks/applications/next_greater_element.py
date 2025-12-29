"""
Next Greater Element Problem

Find the next greater element for each element in an array using stack.

Problem Statement:
-------------------
Given an array, find the next greater element for each element.
The next greater element is the first element to the right that is greater.

Example:
    Input: [4, 5, 2, 25]
    Output: [5, 25, 25, -1]
    Explanation:
        Next greater for 4 is 5
        Next greater for 5 is 25
        Next greater for 2 is 25
        Next greater for 25 is -1 (none)

Why Stack?
----------
- Need to process elements in order
- Maintain candidates for next greater
- Stack helps track elements waiting for their next greater

Useful in:
- Array processing
- Monotonic stack problems
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Next Greater Element (Language-agnostic)
# ----------------------------------------------------------------------
def next_greater_element(nums: List[int]) -> List[int]:
    """
    Find next greater element for each element using stack.

    Algorithm:
    1. Use stack to store indices of elements
    2. For each element, pop indices where current > stack top
    3. Current is next greater for popped elements
    4. Push current index to stack

    Args:
        nums (List[int]): Input array

    Returns:
        List[int]: Array where result[i] is next greater element for nums[i]

    Complexity:
        Time: O(n)     - Each element pushed and popped at most once.
        Space: O(n)   - Stack and result array storage.
    """
    n = len(nums)
    result = [-1] * n
    stack: List[int] = []  # Store indices
    
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result


# ----------------------------------------------------------------------
# Next Greater Element (Circular Array)
# ----------------------------------------------------------------------
def next_greater_element_circular(nums: List[int]) -> List[int]:
    """
    Find next greater element in circular array.

    Args:
        nums (List[int]): Input array (treated as circular)

    Returns:
        List[int]: Next greater elements

    Complexity:
        Time: O(n)     - Process array twice (circular).
        Space: O(n)   - Stack and result storage.
    """
    n = len(nums)
    result = [-1] * n
    stack: List[int] = []
    
    # Process circular array (2 * n - 1 iterations)
    for i in range(2 * n):
        idx = i % n
        while stack and nums[idx] > nums[stack[-1]]:
            popped_idx = stack.pop()
            result[popped_idx] = nums[idx]
        if i < n:
            stack.append(idx)
    
    return result


# ----------------------------------------------------------------------
# Next Smaller Element
# ----------------------------------------------------------------------
def next_smaller_element(nums: List[int]) -> List[int]:
    """
    Find next smaller element for each element.

    Args:
        nums (List[int]): Input array

    Returns:
        List[int]: Next smaller elements (-1 if none)

    Complexity:
        Time: O(n)     - Each element processed once.
        Space: O(n)   - Stack and result storage.
    """
    n = len(nums)
    result = [-1] * n
    stack: List[int] = []
    
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Next Greater Element Demonstration")
    
    # Basic next greater
    nums1 = [4, 5, 2, 25]
    print(f"Array: {nums1}")
    result1 = next_greater_element(nums1)
    print(f"Next greater: {result1}")
    print("Explanation:")
    for i, (num, nge) in enumerate(zip(nums1, result1)):
        print(f"  {num} -> {nge}")
    
    # Circular array
    print("\n" + "="*50)
    nums2 = [1, 2, 1]
    print(f"Circular array: {nums2}")
    result2 = next_greater_element_circular(nums2)
    print(f"Next greater (circular): {result2}")
    
    # Next smaller
    print("\n" + "="*50)
    nums3 = [4, 5, 2, 10, 8]
    print(f"Array: {nums3}")
    result3 = next_smaller_element(nums3)
    print(f"Next smaller: {result3}")

