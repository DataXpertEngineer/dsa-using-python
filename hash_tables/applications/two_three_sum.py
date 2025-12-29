"""
Two Sum and Three Sum Problems

Find pairs/triplets that sum to target using hash tables.

Problem Statement:
-------------------
1. Two Sum: Find two numbers that add up to target
2. Three Sum: Find three numbers that add up to target

Example (Two Sum):
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1] (indices of 2 and 7)

Why Hash Tables?
---------------
- O(1) lookup for complement
- O(n) solution instead of O(n²)
- Simple and efficient

Useful in:
- Pair finding problems
- Common interview problems
"""

from typing import List, Optional, Tuple, Set


# ----------------------------------------------------------------------
# Two Sum (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that sum to target using hash table.

    Algorithm:
    1. For each number, check if complement (target - num) exists
    2. Store numbers and their indices in hash table
    3. Return indices when complement found

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        Optional[Tuple[int, int]]: Indices of two numbers, None if not found

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores number-index map.
    """
    num_map: dict[int, int] = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    
    return None


# ----------------------------------------------------------------------
# Two Sum (All Pairs)
# ----------------------------------------------------------------------
def two_sum_all_pairs(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Find all pairs of indices that sum to target.

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        List[Tuple[int, int]]: List of index pairs

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores number-index map.
    """
    pairs: List[Tuple[int, int]] = []
    num_map: dict[int, List[int]] = {}
    
    # Build index map (handle duplicates)
    for i, num in enumerate(nums):
        if num not in num_map:
            num_map[num] = []
        num_map[num].append(i)
    
    # Find pairs
    seen = set()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and (num, complement) not in seen:
            for j in num_map[complement]:
                if i != j:
                    pairs.append((i, j))
            seen.add((num, complement))
            seen.add((complement, num))
    
    return pairs


# ----------------------------------------------------------------------
# Three Sum (Using Hash Table)
# ----------------------------------------------------------------------
def three_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all triplets that sum to target using hash table.

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        List[List[int]]: List of triplets (values, not indices)

    Complexity:
        Time: O(n²)    - Two nested loops.
        Space: O(n)   - Stores number map.
    """
    nums.sort()  # Sort for easier duplicate handling
    triplets: List[List[int]] = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        
        num_map: dict[int, int] = {}
        for j in range(i + 1, n):
            complement = target - nums[i] - nums[j]
            if complement in num_map:
                triplets.append([nums[i], complement, nums[j]])
                # Skip duplicates
                while j < n - 1 and nums[j] == nums[j + 1]:
                    j += 1
            num_map[nums[j]] = j
    
    return triplets


# ----------------------------------------------------------------------
# Three Sum (Two Pointers - Alternative)
# ----------------------------------------------------------------------
def three_sum_two_pointers(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all triplets using two pointers (alternative approach).

    Args:
        nums (List[int]): Input array
        target (int): Target sum

    Returns:
        List[List[int]]: List of triplets

    Complexity:
        Time: O(n²)    - Sort + two pointers.
        Space: O(1)   - Only uses variables (not counting output).
    """
    nums.sort()
    triplets: List[List[int]] = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return triplets


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Two Sum and Three Sum Demonstration")
    
    # Two Sum
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Array: {nums1}, Target: {target1}")
    result1 = two_sum(nums1, target1)
    print(f"Two Sum indices: {result1}")
    if result1:
        print(f"  Values: {nums1[result1[0]]}, {nums1[result1[1]]}")
    
    # Three Sum
    print("\n" + "="*50)
    nums2 = [-1, 0, 1, 2, -1, -4]
    target2 = 0
    print(f"Array: {nums2}, Target: {target2}")
    result2 = three_sum(nums2, target2)
    print(f"Three Sum triplets: {result2}")
    
    # Three Sum with two pointers
    result3 = three_sum_two_pointers(nums2, target2)
    print(f"Three Sum (two pointers): {result3}")

