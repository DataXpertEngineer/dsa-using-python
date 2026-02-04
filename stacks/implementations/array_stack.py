"""
Stack Implementation Using Array/List

Stack implementation using Python's built-in list (dynamic array).

Why Array-based Stack?
---------------------
Advantages:
- Simple implementation
- Cache-friendly (contiguous memory)
- O(1) amortized push/pop operations
- Easy to understand and implement

Disadvantages:
- Resizing overhead (though amortized O(1))
- Fixed maximum size in some languages (not Python)

Useful in:
- Simple stack implementations
- When size is predictable
- Learning stack fundamentals
"""

from typing import Optional, Any, List


class ArrayStack:
    """
    Stack implementation using Python list (dynamic array).
    """
    
    def __init__(self, capacity: Optional[int] = None):
        """
        Initialize stack with optional capacity.

        Args:
            capacity (Optional[int]): Maximum capacity (None for unlimited)

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.items = []
        self.capacity = capacity
    
    def push(self, item):
        """
        Add element to top of stack.

        Args:
            item: Element to add

        Returns:
            bool: True if successful, False if stack is full

        Complexity:
            Time: O(1)     - Appending to end of list is O(1) amortized.
            Space: O(1)   - Adds one element.
        """
        if self.capacity is not None and len(self.items) >= self.capacity:
            return False  # Stack is full
        self.items.append(item)
        return True
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return top element.

        Returns:
            Optional[Any]: Top element, None if stack is empty

        Complexity:
            Time: O(1)     - Removing from end of list is O(1).
            Space: O(1)   - Removes one element.
        """
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self) -> Optional[Any]:
        """
        Return top element without removing.

        Returns:
            Optional[Any]: Top element, None if stack is empty

        Complexity:
            Time: O(1)     - Direct access to last element.
            Space: O(1)   - Only reads, doesn't modify.
        """
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if stack is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items) == 0
    
    def is_full(self):
        """
        Check if stack is full (only if capacity is set).

        Returns:
            bool: True if full, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity
    
    def size(self):
        """
        Get number of elements in stack.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items)
    
    def __str__(self):
        """
        String representation of stack.

        Returns:
            str: String showing stack from top to bottom
        """
        return f"ArrayStack({self.items[::-1]})"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Array-based Stack Demonstration")
    
    # Create stack
    stack = ArrayStack()
    print(f"Empty stack: {stack}")
    
    # Push elements
    print("\nPushing: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        stack.push(i)
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Top: {stack.peek()}")
    
    # Pop elements
    print("\nPopping:")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}, Stack: {stack}")
    
    # Stack with capacity
    print("\n" + "="*50)
    limited_stack = ArrayStack(capacity=3)
    print(f"Limited stack (capacity=3): {limited_stack}")
    for i in range(1, 5):
        result = limited_stack.push(i)
        print(f"  Push {i}: {result}, Stack: {limited_stack}")

