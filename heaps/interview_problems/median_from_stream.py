"""
Find Median from Data Stream

Maintain median of a stream of numbers using two heaps.

Problem Statement:
-------------------
Design a data structure that supports adding numbers and finding median.

Example:
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2

Why Two Heaps?
--------------
- Max heap for smaller half
- Min heap for larger half
- Median is average of two roots or root of larger heap
- O(log n) insert, O(1) find median

Useful in:
- Running statistics
- Common interview problems
"""

from typing import Optional
import heapq


class MedianFinder:
    """
    Find median from data stream using two heaps.
    """
    
    def __init__(self):
        """
        Initialize median finder with two heaps.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty heaps.
        """
        # Max heap for smaller half (negate values for max-heap)
        self.small: list[int] = []
        # Min heap for larger half
        self.large: list[int] = []
    
    def add_num(self, num: int) -> None:
        """
        Add number to data structure.

        Args:
            num (int): Number to add

        Complexity:
            Time: O(log n)  - Heap operations.
            Space: O(1)    - Adds one element.
        """
        # Add to appropriate heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)  # Negate for max-heap
        else:
            heapq.heappush(self.large, num)
        
        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self) -> float:
        """
        Find median of current numbers.

        Returns:
            float: Median value

        Complexity:
            Time: O(1)     - Direct access to heap roots.
            Space: O(1)   - Only reads.
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Find Median from Data Stream Demonstration")
    
    finder = MedianFinder()
    
    nums = [1, 2, 3, 4, 5]
    print("Adding numbers:")
    for num in nums:
        finder.add_num(num)
        median = finder.find_median()
        print(f"  addNum({num}) -> findMedian() = {median}")

