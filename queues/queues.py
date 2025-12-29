"""
Queue Data Structure in Python

A queue is a linear data structure that follows the First In First Out (FIFO) principle.
Elements are added at the rear and removed from the front.

Structure:
    Front -> [element] -> [element] -> [element] -> ... -> Rear

Characteristics:
- FIFO (First In First Out) order
- Operations: enqueue (add at rear), dequeue (remove from front), peek (view front)
- Dynamic size (grows/shrinks as needed)
- Efficient operations: O(1) for enqueue, dequeue, peek

Useful in:
- Task scheduling
- BFS (Breadth-First Search)
- Print queue management
- Request handling
- Common interview problems
"""

from typing import Optional, Any, List
from collections import deque


class Queue:
    """
    Queue implementation using Python list (dynamic array).
    
    A queue is a FIFO (First In First Out) data structure where elements
    are added at the rear and removed from the front.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty queue.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.items: List[Any] = []
    
    def enqueue(self, item: Any) -> None:
        """
        Add an element to the rear of the queue.

        Args:
            item: Element to add to the queue

        Complexity:
            Time: O(1)     - Appending to end of list is O(1) amortized.
            Space: O(1)   - Adds one element.
        """
        self.items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the front element from the queue.

        Returns:
            Optional[Any]: Front element, None if queue is empty

        Complexity:
            Time: O(n)     - Removing from front of list requires shifting elements.
            Space: O(1)   - Removes one element.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self) -> Optional[Any]:
        """
        Return the front element without removing it.

        Returns:
            Optional[Any]: Front element, None if queue is empty

        Complexity:
            Time: O(1)     - Direct access to first element.
            Space: O(1)   - Only reads, doesn't modify.
        """
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
            int: Number of elements in the queue

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items)
    
    def __str__(self) -> str:
        """
        String representation of the queue.

        Returns:
            str: String showing queue from front to rear

        Complexity:
            Time: O(n)     - Traverses all elements.
            Space: O(n)   - Creates string representation.
        """
        return f"Queue({self.items})"
    
    def __repr__(self) -> str:
        """
        Official string representation of the queue.

        Returns:
            str: Official representation
        """
        return self.__str__()
    
    def clear(self) -> None:
        """
        Remove all elements from the queue.

        Complexity:
            Time: O(1)     - Clears the list.
            Space: O(1)   - No extra space used.
        """
        self.items.clear()


# ----------------------------------------------------------------------
# Queue Operations Summary
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Queue Operations Demonstration")
    
    # Create queue
    queue = Queue()
    print(f"Empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Size: {queue.size()}")
    
    # Enqueue elements
    print("\nEnqueuing elements: 10, 20, 30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Queue: {queue}")
    print(f"Size: {queue.size()}")
    print(f"Front element (peek): {queue.peek()}")
    
    # Dequeue elements
    print("\nDequeuing elements:")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue: {queue}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue: {queue}")
    print(f"Front element: {queue.peek()}")
    
    # Final state
    print(f"\nFinal queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Size: {queue.size()}")
    
    print("\n" + "="*60)
    print("QUEUE OPERATIONS COMPLEXITY SUMMARY")
    print("="*60)
    print("""
Operation          Time Complexity    Space Complexity
------------------------------------------------------
enqueue()          O(1) amortized      O(1)
dequeue()          O(n)                O(1)
peek()             O(1)               O(1)
is_empty()         O(1)               O(1)
size()             O(1)               O(1)
clear()            O(1)               O(1)

Note: dequeue() is O(n) because removing from front of list
      requires shifting all elements. Use collections.deque
      for O(1) dequeue operations.
""")

