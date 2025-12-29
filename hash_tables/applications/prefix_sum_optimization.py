"""
Prefix Sum Optimization with Hash Tables

Use prefix sum + hash table to solve problems in O(n) time.

Problem Statement:
-------------------
Many problems involving subarray sums can be optimized using prefix sum
combined with hash tables to achieve O(n) time complexity.

Example:
    Find subarray with sum = k
    Without optimization: O(n²) - check all subarrays
    With prefix sum + hash: O(n) - single pass

Why Prefix Sum + Hash?
----------------------
- Prefix sum: sum[i] = arr[0] + arr[1] + ... + arr[i]
- Hash table: Store prefix sums for O(1) lookup
- Find subarray sum: prefix[j] - prefix[i] = sum of arr[i+1...j]

Useful in:
- Subarray sum problems
- Range sum queries
- Common interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Subarray Sum Equals K (Optimized)
# ----------------------------------------------------------------------
def subarray_sum_k_optimized(nums: List[int], k: int) -> int:
    """
    Count subarrays with sum = k using prefix sum + hash table.

    Algorithm:
    1. Calculate prefix sum as we traverse
    2. For each prefix sum, check if (prefix_sum - k) exists
    3. If exists, we found a subarray with sum k

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
# Longest Subarray with Sum K
# ----------------------------------------------------------------------
def longest_subarray_sum_k(nums: List[int], k: int) -> int:
    """
    Find length of longest subarray with sum = k.

    Args:
        nums (List[int]): Input array
        k (int): Target sum

    Returns:
        int: Length of longest subarray, -1 if not found

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores prefix sum map.
    """
    prefix_sum = 0
    prefix_map: Dict[int, int] = {0: -1}  # prefix_sum: first_index
    max_length = -1
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_length = max(max_length, length)
        
        # Store first occurrence of prefix sum
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    
    return max_length


# ----------------------------------------------------------------------
# Subarray Sum in Range
# ----------------------------------------------------------------------
def subarray_sum_in_range(nums: List[int], lower: int, upper: int) -> int:
    """
    Count subarrays with sum in range [lower, upper].

    Args:
        nums (List[int]): Input array
        lower (int): Lower bound
        upper (int): Upper bound

    Returns:
        int: Number of subarrays with sum in range

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores prefix sum map.
    """
    count = 0
    prefix_sum = 0
    prefix_map: Dict[int, int] = {0: 1}
    
    for num in nums:
        prefix_sum += num
        
        # Count subarrays with sum in [lower, upper]
        for target in range(lower, upper + 1):
            if (prefix_sum - target) in prefix_map:
                count += prefix_map[prefix_sum - target]
        
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Prefix Sum Optimization Demonstration")
    
    # Subarray sum equals k
    nums = [1, 1, 1]
    k = 2
    print(f"Array: {nums}, Target sum: {k}")
    count = subarray_sum_k_optimized(nums, k)
    print(f"Number of subarrays with sum = {k}: {count}")
    print("Explanation: [1,1], [1,1] (two subarrays)")
    
    # Longest subarray with sum k
    print("\n" + "="*50)
    nums2 = [1, -1, 5, -2, 3]
    k2 = 3
    print(f"Array: {nums2}, Target sum: {k2}")
    length = longest_subarray_sum_k(nums2, k2)
    print(f"Length of longest subarray with sum = {k2}: {length}")
    print("Explanation: [5, -2] has sum 3, length = 2")

