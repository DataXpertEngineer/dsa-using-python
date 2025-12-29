"""
Moving Average in a Window

Calculate moving average of numbers in a sliding window using queue.

Problem Statement:
-------------------
Given a stream of integers and a window size, calculate the moving average
of all integers in the sliding window.

Example:
    m = MovingAverage(3)
    m.next(1) = 1.0        # (1) / 1
    m.next(10) = 5.5       # (1 + 10) / 2
    m.next(3) = 4.67       # (1 + 10 + 3) / 3
    m.next(5) = 6.0        # (10 + 3 + 5) / 3 (window slides)

Why Queue?
----------
- Need to maintain sliding window
- Remove old elements when window is full
- FIFO order matches time order

Useful in:
- Data streaming
- Time series analysis
- Medium difficulty interview problems
"""

from collections import deque


class MovingAverage:
    """
    Moving average calculator for sliding window.
    """
    
    def __init__(self, size: int):
        """
        Initialize moving average with window size.

        Args:
            size (int): Size of the sliding window

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty deque and variables.
        """
        self.size = size
        self.queue = deque()
        self.sum = 0.0
    
    def next(self, val: int) -> float:
        """
        Add new value and return moving average.

        Args:
            val (int): New value to add

        Returns:
            float: Moving average of current window

        Complexity:
            Time: O(1)     - Constant time operations.
            Space: O(1)   - Adds one element (window size is fixed).
        """
        # Add new value
        self.queue.append(val)
        self.sum += val
        
        # Remove old value if window is full
        if len(self.queue) > self.size:
            old_val = self.queue.popleft()
            self.sum -= old_val
        
        # Calculate average
        return self.sum / len(self.queue)


# ----------------------------------------------------------------------
# Moving Average (Alternative: Using List)
# ----------------------------------------------------------------------
class MovingAverageList:
    """
    Moving average using list (less efficient).
    """
    
    def __init__(self, size: int):
        """
        Initialize moving average with window size.

        Args:
            size (int): Size of the sliding window
        """
        self.size = size
        self.numbers: list[int] = []
    
    def next(self, val: int) -> float:
        """
        Add new value and return moving average.

        Args:
            val (int): New value to add

        Returns:
            float: Moving average of current window

        Complexity:
            Time: O(1)     - Appending and calculating average.
            Space: O(n)   - Stores numbers in window.
        """
        self.numbers.append(val)
        
        # Keep only last 'size' numbers
        if len(self.numbers) > self.size:
            self.numbers.pop(0)
        
        return sum(self.numbers) / len(self.numbers)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Moving Average Demonstration")
    
    m = MovingAverage(3)
    
    values = [1, 10, 3, 5]
    print("Window size: 3")
    print("\nAdding values:")
    for val in values:
        avg = m.next(val)
        print(f"  next({val}) = {avg:.2f}")
    
    print("\nExplanation:")
    print("  After adding 1:   [1]           -> avg = 1.0")
    print("  After adding 10:  [1, 10]       -> avg = 5.5")
    print("  After adding 3:   [1, 10, 3]    -> avg = 4.67")
    print("  After adding 5:   [10, 3, 5]    -> avg = 6.0 (window slides)")

