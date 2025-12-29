"""
Circular Queue Implementation

Circular queue (ring buffer) implementation with fixed capacity.
Uses modulo arithmetic to wrap around when reaching the end.

Why Circular Queue?
-------------------
- Fixed memory usage (no resizing)
- O(1) enqueue and dequeue operations
- Efficient use of memory
- Useful for bounded buffers

Useful in:
- Fixed-size buffers
- Producer-consumer problems
- When memory is constrained
- Real-time systems
"""

from typing import Optional, Any


class CircularQueue:
    """
    Circular queue implementation with fixed capacity.
    """
    
    def __init__(self, capacity: int) -> None:
        """
        Initialize circular queue with given capacity.

        Args:
            capacity (int): Maximum number of elements

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(n)   - Creates array of size capacity.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.items: list[Optional[Any]] = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item: Any) -> bool:
        """
        Add element to rear of queue.

        Args:
            item: Element to add

        Returns:
            bool: True if successful, False if queue is full

        Complexity:
            Time: O(1)     - Constant time operation.
            Space: O(1)   - Adds one element.
        """
        if self.is_full():
            return False
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1
        return True
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return front element.

        Returns:
            Optional[Any]: Front element, None if empty

        Complexity:
            Time: O(1)     - Constant time operation.
            Space: O(1)   - Removes one element.
        """
        if self.is_empty():
            return None
        
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self) -> Optional[Any]:
        """
        Return front element without removing.

        Returns:
            Optional[Any]: Front element, None if empty

        Complexity:
            Time: O(1)     - Direct access.
            Space: O(1)   - Only reads.
        """
        if self.is_empty():
            return None
        return self.items[self.front]
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return self.size == 0
    
    def is_full(self) -> bool:
        """
        Check if queue is full.

        Returns:
            bool: True if full, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return self.size == self.capacity
    
    def get_size(self) -> int:
        """
        Get number of elements in queue.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Returns stored size.
            Space: O(1)   - No extra space used.
        """
        return self.size
    
    def __str__(self) -> str:
        """
        String representation of queue.

        Returns:
            str: String showing queue from front to rear
        """
        if self.is_empty():
            return "CircularQueue([])"
        
        items = []
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            items.append(str(self.items[idx]))
        
        return f"CircularQueue([{', '.join(items)}])"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Circular Queue Demonstration")
    
    # Create circular queue with capacity 5
    queue = CircularQueue(5)
    print(f"Empty queue (capacity=5): {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Is full: {queue.is_full()}")
    
    # Enqueue
    print("\nEnqueuing: 10, 20, 30, 40, 50")
    for i in range(10, 60, 10):
        result = queue.enqueue(i)
        print(f"  Enqueue {i}: {result}, Queue: {queue}")
    
    # Try to enqueue when full
    print(f"\nTry to enqueue 60 (queue is full): {queue.enqueue(60)}")
    
    # Dequeue
    print("\nDequeuing:")
    while not queue.is_empty():
        print(f"  Dequeued: {queue.dequeue()}, Queue: {queue}")
    
    # Wrap around test
    print("\n" + "="*50)
    print("Testing wrap-around:")
    queue2 = CircularQueue(3)
    queue2.enqueue(1)
    queue2.enqueue(2)
    queue2.dequeue()  # Remove 1
    queue2.enqueue(3)
    queue2.enqueue(4)  # Should wrap around
    print(f"Queue after wrap-around: {queue2}")

