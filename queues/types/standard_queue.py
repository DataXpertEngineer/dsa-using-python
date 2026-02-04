"""
Standard FIFO Queue Implementation

Standard queue implementation using array/list with FIFO (First In First Out) order.

Why Standard Queue?
-------------------
- Simple implementation
- Easy to understand
- Good for learning queue fundamentals
- Suitable for small datasets

Note: Using list.pop(0) makes dequeue O(n).
For better performance, use collections.deque or circular queue.

Useful in:
- Learning queue fundamentals
- Simple queue applications
- When size is small
"""

from typing import Optional, Any, List


class StandardQueue:
    """
    Standard FIFO queue implementation using Python list.
    """
    
    def __init__(self):
        """
        Initialize an empty queue.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.items = []
    
    def enqueue(self, item):
        """
        Add element to rear of queue.

        Args:
            item: Element to add

        Complexity:
            Time: O(1)     - Appending to end of list is O(1) amortized.
            Space: O(1)   - Adds one element.
        """
        self.items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return front element.

        Returns:
            Optional[Any]: Front element, None if empty

        Complexity:
            Time: O(n)     - Removing from front requires shifting elements.
            Space: O(1)   - Removes one element.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self) -> Optional[Any]:
        """
        Return front element without removing.

        Returns:
            Optional[Any]: Front element, None if empty

        Complexity:
            Time: O(1)     - Direct access to first element.
            Space: O(1)   - Only reads.
        """
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """
        Check if queue is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get number of elements in queue.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items)
    
    def __str__(self):
        """
        String representation of queue.

        Returns:
            str: String showing queue from front to rear
        """
        return f"StandardQueue({self.items})"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Standard Queue Demonstration")
    
    queue = StandardQueue()
    print(f"Empty queue: {queue}")
    
    # Enqueue
    print("\nEnqueuing: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        queue.enqueue(i)
    print(f"Queue: {queue}")
    print(f"Size: {queue.size()}")
    print(f"Front: {queue.peek()}")
    
    # Dequeue
    print("\nDequeuing:")
    while not queue.is_empty():
        print(f"  Dequeued: {queue.dequeue()}, Queue: {queue}")

