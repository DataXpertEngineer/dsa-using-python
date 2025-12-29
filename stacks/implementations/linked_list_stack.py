"""
Stack Implementation Using Linked List

Stack implementation using a linked list structure.

Why Linked List-based Stack?
----------------------------
Advantages:
- No resizing overhead
- True O(1) push/pop (no amortization)
- Dynamic size (no capacity limit)
- Memory efficient for sparse usage

Disadvantages:
- Extra memory for pointers
- Not cache-friendly (non-contiguous)
- Slightly more complex implementation

Useful in:
- When size is unpredictable
- When avoiding resizing overhead
- Learning different implementations
"""

from typing import Optional, Any


class StackNode:
    """
    Node class for linked list stack.
    """
    def __init__(self, data: Any) -> None:
        """
        Initialize a stack node.

        Args:
            data: Data to store in the node
        """
        self.data = data
        self.next: Optional['StackNode'] = None


class LinkedListStack:
    """
    Stack implementation using linked list.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty stack.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty stack.
        """
        self.top: Optional[StackNode] = None
        self._size = 0
    
    def push(self, item: Any) -> None:
        """
        Add element to top of stack.

        Args:
            item: Element to add

        Complexity:
            Time: O(1)     - Creates node and updates top pointer.
            Space: O(1)   - Creates one new node.
        """
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return top element.

        Returns:
            Optional[Any]: Top element, None if stack is empty

        Complexity:
            Time: O(1)     - Updates top pointer.
            Space: O(1)   - Removes one node.
        """
        if self.is_empty():
            return None
        
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
    
    def peek(self) -> Optional[Any]:
        """
        Return top element without removing.

        Returns:
            Optional[Any]: Top element, None if stack is empty

        Complexity:
            Time: O(1)     - Direct access to top node.
            Space: O(1)   - Only reads, doesn't modify.
        """
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self) -> bool:
        """
        Check if stack is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return self.top is None
    
    def size(self) -> int:
        """
        Get number of elements in stack.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Returns stored size.
            Space: O(1)   - No extra space used.
        """
        return self._size
    
    def __str__(self) -> str:
        """
        String representation of stack.

        Returns:
            str: String showing stack from top to bottom
        """
        if self.is_empty():
            return "LinkedListStack([])"
        
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        
        return f"LinkedListStack([{', '.join(items)}])"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Linked List-based Stack Demonstration")
    
    # Create stack
    stack = LinkedListStack()
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    print(f"Size: {stack.size()}")
    
    # Push elements
    print("\nPushing: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Top: {stack.peek()}")
    
    # Pop elements
    print("\nPopping:")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}, Stack: {stack}, Size: {stack.size()}")

