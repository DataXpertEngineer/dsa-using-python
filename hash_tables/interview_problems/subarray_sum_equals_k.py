"""
Subarray Sum Equals K

Count subarrays with sum equal to k using prefix sum and hash table.

Problem Statement:
-------------------
Given an array of integers and an integer k, find the total number of
continuous subarrays whose sum equals k.

Example:
    Input: nums = [1, 1, 1], k = 2
    Output: 2
    Explanation: [1, 1] and [1, 1] (two subarrays)

Why Prefix Sum + Hash Table?
-----------------------------
Without optimization:
    Check all subarrays = O(n²) time
With prefix sum + hash:
    Single pass = O(n) time

Useful in:
- Subarray sum problems
- Common interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Count Subarrays with Sum K (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Count subarrays with sum = k using prefix sum + hash table.

    Algorithm:
    1. Calculate prefix sum as we traverse
    2. For each prefix sum, check if (prefix_sum - k) exists
    3. If exists, we found subarray(s) with sum k
    4. Count all such occurrences

    Args:
        nums (List[int]): Input array
        k (int): Target sum

    Returns:
        int: Number of subarrays with sum = k

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores prefix sum map.
    """
    count = 0
    prefix_sum = 0
    prefix_map: Dict[int, int] = {0: 1}  # prefix_sum: count
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]
        
        # Update prefix sum count
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count


# ----------------------------------------------------------------------
# Subarray Sum Equals K (Brute Force)
# ----------------------------------------------------------------------
def subarray_sum_equals_k_bruteforce(nums: List[int], k: int) -> int:
    """
    Count subarrays with sum = k using brute force.

    Args:
        nums (List[int]): Input array
        k (int): Target sum

    Returns:
        int: Number of subarrays with sum = k

    Complexity:
        Time: O(n²)    - Check all subarrays.
        Space: O(1)   - Only uses counter.
    """
    count = 0
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    
    return count


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Subarray Sum Equals K Demonstration")
    
    nums = [1, 1, 1]
    k = 2
    print(f"Array: {nums}, Target sum: {k}")
    
    result = subarray_sum_equals_k(nums, k)
    print(f"Number of subarrays with sum = {k}: {result}")
    print("Explanation: [1, 1] and [1, 1] (two subarrays)")
    
    # Compare with brute force
    result_bf = subarray_sum_equals_k_bruteforce(nums, k)
    print(f"Brute force result: {result_bf}")
    print(f"Results match: {result == result_bf}")
    
    # Another example
    print("\n" + "="*50)
    nums2 = [1, 2, 3]
    k2 = 3
    print(f"Array: {nums2}, Target sum: {k2}")
    result2 = subarray_sum_equals_k(nums2, k2)
    print(f"Number of subarrays with sum = {k2}: {result2}")
    print("Explanation: [1, 2] and [3] (two subarrays)")

