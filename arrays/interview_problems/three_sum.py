"""
3Sum Problem

Find all unique triplets that sum to zero (or target).

Problem Statement:
------------------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

This is an extension of the two sum problem.

Useful in:
- Two pointers technique
- Sorting
- Array manipulation
- Common interview problem
"""

from typing import List, Set, Tuple


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def three_sum_naive(nums: List[int], target: int = 0) -> List[List[int]]:
    """
    Find all triplets that sum to target using brute-force approach.

    This approach works in all programming languages but is inefficient.

    Args:
        nums (List[int]): Input array
        target (int): Target sum (default: 0)

    Returns:
        List[List[int]]: List of unique triplets that sum to target

    Complexity:
        Time: O(n³)    - Nested loops check all triplets.
        Space: O(1)   - Excluding output, only uses variables.
    """
    n = len(nums)
    result = []
    seen = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append([nums[i], nums[j], nums[k]])
    
    return result


# ----------------------------------------------------------------------
# Two Pointers Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def three_sum(nums: List[int], target: int = 0) -> List[List[int]]:
    """
    Find all unique triplets that sum to target using two pointers.

    Algorithm:
    1. Sort the array
    2. Fix first element, use two pointers for remaining two
    3. Skip duplicates to avoid duplicate triplets

    This approach works in all programming languages and is optimal.

    Args:
        nums (List[int]): Input array (will be sorted)
        target (int): Target sum (default: 0)

    Returns:
        List[List[int]]: List of unique triplets that sum to target

    Complexity:
        Time: O(n²)    - Outer loop O(n), inner two-pointer search O(n).
        Space: O(1)   - Excluding output, only uses variables for pointers.
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result


# ----------------------------------------------------------------------
# 3Sum Closest (Find triplet with sum closest to target)
# ----------------------------------------------------------------------
def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Find three integers whose sum is closest to target.

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        int: Sum of the three integers closest to target

    Complexity:
        Time: O(n²)    - Sorting O(n log n) + two-pointer search O(n²).
        Space: O(1)   - Only uses variables for tracking.
    """
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    
    return closest_sum


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: 3Sum Problem Demonstration")
    
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("Array:", nums1)
    
    result1 = three_sum(nums1, 0)
    print(f"Triplets that sum to 0: {result1}")
    print("Expected: [[-1, -1, 2], [-1, 0, 1]]")
    
    # Test with different target
    print("\n" + "="*50)
    nums2 = [-1, 0, 1, 2, -1, -4]
    target2 = 1
    print("Array:", nums2)
    print(f"Target: {target2}")
    result2 = three_sum(nums2, target2)
    print(f"Triplets that sum to {target2}: {result2}")
    
    # Test 3Sum closest
    print("\n" + "="*50)
    nums3 = [-1, 2, 1, -4]
    target3 = 1
    print("Array:", nums3)
    print(f"Target: {target3}")
    closest = three_sum_closest(nums3, target3)
    print(f"Closest sum to {target3}: {closest}")
    print("Explanation: -1 + 2 + 1 = 2 (closest to 1)")

