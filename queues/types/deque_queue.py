"""
Double-Ended Queue (Deque) Implementation

Deque (pronounced "deck") allows insertion and deletion from both ends.
Implemented using Python's collections.deque for efficiency.

Why Deque?
----------
- O(1) operations on both ends
- More flexible than standard queue
- Efficient implementation using doubly-linked list
- Useful for sliding window problems

Useful in:
- Sliding window problems
- Palindrome checking
- When need to add/remove from both ends
- Common interview problems
"""

from typing import Optional, Any
from collections import deque


class DequeQueue:
    """
    Double-ended queue implementation using collections.deque.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty deque.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty deque.
        """
        self.items = deque()
    
    def enqueue_front(self, item: Any) -> None:
        """
        Add element to front of deque.

        Args:
            item: Element to add

        Complexity:
            Time: O(1)     - Constant time operation.
            Space: O(1)   - Adds one element.
        """
        self.items.appendleft(item)
    
    def enqueue_rear(self, item: Any) -> None:
        """
        Add element to rear of deque.

        Args:
            item: Element to add

        Complexity:
            Time: O(1)     - Constant time operation.
            Space: O(1)   - Adds one element.
        """
        self.items.append(item)
    
    def dequeue_front(self) -> Optional[Any]:
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
        return self.items.popleft()
    
    def dequeue_rear(self) -> Optional[Any]:
        """
        Remove and return rear element.

        Returns:
            Optional[Any]: Rear element, None if empty

        Complexity:
            Time: O(1)     - Constant time operation.
            Space: O(1)   - Removes one element.
        """
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek_front(self) -> Optional[Any]:
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
        return self.items[0]
    
    def peek_rear(self) -> Optional[Any]:
        """
        Return rear element without removing.

        Returns:
            Optional[Any]: Rear element, None if empty

        Complexity:
            Time: O(1)     - Direct access.
            Space: O(1)   - Only reads.
        """
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if deque is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get number of elements in deque.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items)
    
    def __str__(self) -> str:
        """
        String representation of deque.

        Returns:
            str: String showing deque from front to rear
        """
        return f"DequeQueue({list(self.items)})"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Deque (Double-Ended Queue) Demonstration")
    
    dq = DequeQueue()
    print(f"Empty deque: {dq}")
    
    # Enqueue at rear (standard queue behavior)
    print("\nEnqueuing at rear: 10, 20, 30")
    dq.enqueue_rear(10)
    dq.enqueue_rear(20)
    dq.enqueue_rear(30)
    print(f"Deque: {dq}")
    print(f"Front: {dq.peek_front()}, Rear: {dq.peek_rear()}")
    
    # Enqueue at front
    print("\nEnqueuing at front: 5")
    dq.enqueue_front(5)
    print(f"Deque: {dq}")
    print(f"Front: {dq.peek_front()}, Rear: {dq.peek_rear()}")
    
    # Dequeue from front
    print(f"\nDequeue from front: {dq.dequeue_front()}")
    print(f"Deque: {dq}")
    
    # Dequeue from rear
    print(f"Dequeue from rear: {dq.dequeue_rear()}")
    print(f"Deque: {dq}")

