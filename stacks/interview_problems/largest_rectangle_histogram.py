"""
Largest Rectangle in Histogram

Find the largest rectangle area in a histogram using stack.

Problem Statement:
-------------------
Given an array of heights representing a histogram, find the area of the
largest rectangle that can be formed.

Example:
    Input: [2, 1, 5, 6, 2, 3]
    Output: 10
    Explanation: Largest rectangle is formed by bars at indices 2 and 3
                 (heights 5 and 6), width = 2, area = 2 * 5 = 10

Why Stack?
----------
- Need to find previous and next smaller elements
- Stack maintains increasing sequence
- Efficient O(n) solution

Useful in:
- Histogram problems
- Monotonic stack applications
- Medium difficulty interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Largest Rectangle in Histogram (Language-agnostic)
# ----------------------------------------------------------------------
def largest_rectangle_area(heights: List[int]) -> int:
    """
    Find largest rectangle area in histogram using stack.

    Algorithm:
    1. Use stack to store indices of increasing heights
    2. When height decreases, calculate area for popped indices
    3. Area = height * (current_index - stack_top - 1)
    4. Process remaining stack at the end

    Args:
        heights (List[int]): Heights of histogram bars

    Returns:
        int: Largest rectangle area

    Complexity:
        Time: O(n)     - Each index pushed and popped at most once.
        Space: O(n)   - Stack storage.
    """
    stack: List[int] = []
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        # Pop indices while current height is less than stack top
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    # Process remaining bars in stack
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area


# ----------------------------------------------------------------------
# Largest Rectangle - Alternative Implementation
# ----------------------------------------------------------------------
def largest_rectangle_area_alt(heights: List[int]) -> int:
    """
    Alternative implementation using sentinel values.

    Args:
        heights (List[int]): Heights of histogram bars

    Returns:
        int: Largest rectangle area

    Complexity:
        Time: O(n)     - Single pass through heights.
        Space: O(n)   - Stack storage.
    """
    # Add sentinel at the end
    heights = heights + [0]
    stack: List[int] = [-1]  # Sentinel at the beginning
    max_area = 0
    
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Largest Rectangle in Histogram Demonstration")
    
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"Histogram heights: {heights1}")
    area1 = largest_rectangle_area(heights1)
    print(f"Largest rectangle area: {area1}")
    print("Explanation: Rectangle formed by bars at indices 2 and 3")
    print("            (heights 5 and 6), width = 2, area = 2 * 5 = 10")
    
    # Another example
    print("\n" + "="*50)
    heights2 = [6, 2, 5, 4, 5, 1, 6]
    print(f"Histogram heights: {heights2}")
    area2 = largest_rectangle_area(heights2)
    print(f"Largest rectangle area: {area2}")
    
    # Single bar
    print("\n" + "="*50)
    heights3 = [1]
    print(f"Histogram heights: {heights3}")
    area3 = largest_rectangle_area(heights3)
    print(f"Largest rectangle area: {area3}")

