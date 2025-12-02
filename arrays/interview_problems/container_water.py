"""
Container With Most Water Problem

Find two lines that together with x-axis form a container that holds the most water.

Problem Statement:
------------------
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Example:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
                 In this case, the max area of water the container can contain is 49.

Useful in:
- Two pointers technique
- Greedy algorithms
- Array manipulation
- Common interview problem
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def max_area_naive(height: List[int]) -> int:
    """
    Find maximum water area using brute-force approach (check all pairs).

    This approach works in all programming languages but is inefficient.

    Args:
        height (List[int]): Array of heights

    Returns:
        int: Maximum area of water that can be contained

    Complexity:
        Time: O(n²)    - Nested loops check all pairs of lines.
        Space: O(1)   - Only uses variables for tracking max area.
    """
    max_area = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            min_height = min(height[i], height[j])
            area = width * min_height
            max_area = max(max_area, area)
    
    return max_area


# ----------------------------------------------------------------------
# Two Pointers Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def max_area(height: List[int]) -> int:
    """
    Find maximum water area using two pointers technique (optimal solution).

    Algorithm:
    1. Start with pointers at both ends
    2. Calculate area with current pointers
    3. Move pointer with smaller height (greedy choice)
    4. Repeat until pointers meet

    Why this works: Moving the smaller pointer might find a taller line,
    potentially increasing area. Moving the larger pointer can only decrease area.

    This approach works in all programming languages and is optimal.

    Args:
        height (List[int]): Array of heights

    Returns:
        int: Maximum area of water that can be contained

    Complexity:
        Time: O(n)     - Single pass through array, each pointer moves at most n steps.
        Space: O(1)   - Only uses variables for pointers and max area.
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = width * min_height
        max_area = max(max_area, area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def max_area_with_indices(height: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum water area and return the two line indices.

    Args:
        height (List[int]): Array of heights

    Returns:
        Tuple[int, int, int]: (max_area, left_index, right_index)

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(1)   - Only uses variables for tracking.
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    best_left = 0
    best_right = 0
    
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = width * min_height
        
        if area > max_area:
            max_area = area
            best_left = left
            best_right = right
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return (max_area, best_left, best_right)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Container With Most Water Demonstration")
    
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Heights:", height1)
    
    area = max_area(height1)
    print(f"Maximum area: {area}")
    
    area, left_idx, right_idx = max_area_with_indices(height1)
    print(f"Lines at indices [{left_idx}, {right_idx}]: "
          f"height[{left_idx}]={height1[left_idx]}, height[{right_idx}]={height1[right_idx]}")
    print(f"Area = {right_idx - left_idx} * min({height1[left_idx]}, {height1[right_idx]}) = {area}")
    
    # Test with smaller array
    print("\n" + "="*50)
    height2 = [1, 1]
    print("Heights:", height2)
    area2 = max_area(height2)
    print(f"Maximum area: {area2}")
    
    # Test with increasing heights
    print("\n" + "="*50)
    height3 = [1, 2, 3, 4, 5]
    print("Heights:", height3)
    area3 = max_area(height3)
    print(f"Maximum area: {area3}")

