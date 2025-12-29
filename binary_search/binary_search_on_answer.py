"""
Binary Search on Answer

Advanced technique: Use binary search to find answer in search space.

Concept:
--------
Instead of searching for a value, search for the answer itself.
The answer space is monotonic (either increasing or decreasing).

Why Binary Search on Answer?
----------------------------
- Solves optimization problems
- When direct calculation is hard
- Monotonic property enables binary search
- Common in competitive programming

Useful in:
- Optimization problems
- Advanced interview problems
"""

from typing import List, Callable


# ----------------------------------------------------------------------
# Binary Search on Answer - Template
# ----------------------------------------------------------------------
def binary_search_on_answer(left: int, right: int, 
                           is_valid: Callable[[int], bool]) -> int:
    """
    Binary search on answer space.

    Args:
        left (int): Left boundary of answer space
        right (int): Right boundary of answer space
        is_valid (Callable): Function that checks if answer is valid

    Returns:
        int: Maximum/minimum valid answer

    Complexity:
        Time: O(log n * f(n))  - n = search space, f(n) = is_valid complexity.
        Space: O(1)           - Only uses variables.
    """
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_valid(mid):
            result = mid
            left = mid + 1  # For maximum valid answer
            # right = mid - 1  # For minimum valid answer
        else:
            right = mid - 1  # For maximum valid answer
            # left = mid + 1   # For minimum valid answer
    
    return result


# ----------------------------------------------------------------------
# Example: Square Root
# ----------------------------------------------------------------------
def sqrt_binary_search(x: int) -> int:
    """
    Find integer square root using binary search on answer.

    Args:
        x (int): Number

    Returns:
        int: Integer square root

    Complexity:
        Time: O(log x)  - Binary search on answer space.
        Space: O(1)    - Only uses variables.
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# ----------------------------------------------------------------------
# Example: Split Array Largest Sum
# ----------------------------------------------------------------------
def split_array_largest_sum(nums: List[int], m: int) -> int:
    """
    Split array into m subarrays with minimum largest sum.

    Problem: Given array and m, split into m subarrays.
    Find minimum possible largest sum among subarrays.

    Args:
        nums (List[int]): Array
        m (int): Number of subarrays

    Returns:
        int: Minimum largest sum

    Complexity:
        Time: O(n * log(sum))  - Binary search on answer, O(n) validation.
        Space: O(1)           - Only uses variables.
    """
    def can_split(max_sum: int) -> bool:
        """Check if array can be split with max_sum limit."""
        subarrays = 1
        current_sum = 0
        
        for num in nums:
            if current_sum + num > max_sum:
                subarrays += 1
                current_sum = num
                if subarrays > m:
                    return False
            else:
                current_sum += num
        
        return True
    
    left, right = max(nums), sum(nums)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_split(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result


# ----------------------------------------------------------------------
# Example: Koko Eating Bananas
# ----------------------------------------------------------------------
def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Find minimum eating speed to finish all bananas in h hours.

    Args:
        piles (List[int]): Piles of bananas
        h (int): Hours available

    Returns:
        int: Minimum eating speed

    Complexity:
        Time: O(n * log(max_pile))  - Binary search on speed, O(n) validation.
        Space: O(1)                 - Only uses variables.
    """
    def can_finish(speed: int) -> bool:
        """Check if can finish with given speed."""
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
            if hours > h:
                return False
        return True
    
    left, right = 1, max(piles)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_finish(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Binary Search on Answer Demonstration")
    
    # Square root
    x = 16
    sqrt_result = sqrt_binary_search(x)
    print(f"Integer square root of {x}: {sqrt_result}")
    
    # Split array
    print("\n" + "="*50)
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(f"Array: {nums}, Split into {m} subarrays")
    min_sum = split_array_largest_sum(nums, m)
    print(f"Minimum largest sum: {min_sum}")
    
    # Eating bananas
    print("\n" + "="*50)
    piles = [3, 6, 7, 11]
    h = 8
    print(f"Piles: {piles}, Hours: {h}")
    speed = min_eating_speed(piles, h)
    print(f"Minimum eating speed: {speed}")

