"""
Stack Data Structure in Python

A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
Elements are added and removed from the same end (top).

Structure:
    Top -> [element] -> [element] -> [element] -> ... -> Bottom

Characteristics:
- LIFO (Last In First Out) order
- Operations: push (add), pop (remove), peek (view top)
- Dynamic size (grows/shrinks as needed)
- Efficient operations: O(1) for push, pop, peek

Useful in:
- Expression evaluation
- Function call management
- Undo/redo operations
- Backtracking algorithms
- Parentheses matching
- Common interview problems
"""

from typing import Optional, Any, List


class Stack:
    """
    Stack implementation using Python list (dynamic array).
    
    A stack is a LIFO (Last In First Out) data structure where elements
    are added and removed from the same end (top).
    """
    
    def __init__(self):
        """
        Initialize an empty stack.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.items = []
    
    def push(self, item):
        """
        Add an element to the top of the stack.

        Args:
            item: Element to add to the stack

        Complexity:
            Time: O(1)     - Appending to end of list is O(1) amortized.
            Space: O(1)   - Adds one element.
        """
        self.items.append(item)
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return the top element from the stack.

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
        Return the top element without removing it.

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
        Check if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of elements in the stack.

        Returns:
            int: Number of elements in the stack

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items)
    
    def __str__(self):
        """
        String representation of the stack.

        Returns:
            str: String showing stack from top to bottom

        Complexity:
            Time: O(n)     - Traverses all elements.
            Space: O(n)   - Creates string representation.
        """
        return f"Stack({self.items[::-1]})"  # Show from top to bottom
    
    def __repr__(self):
        """
        Official string representation of the stack.

        Returns:
            str: Official representation
        """
        return self.__str__()
    
    def clear(self):
        """
        Remove all elements from the stack.

        Complexity:
            Time: O(1)     - Clears the list.
            Space: O(1)   - No extra space used.
        """
        self.items.clear()


# ----------------------------------------------------------------------
# Stack Operations Summary
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Stack Operations Demonstration")
    
    # Create stack
    stack = Stack()
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    print(f"Size: {stack.size()}")
    
    # Push elements
    print("\nPushing elements: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Top element (peek): {stack.peek()}")
    
    # Pop elements
    print("\nPopping elements:")
    print(f"Popped: {stack.pop()}")
    print(f"Stack: {stack}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack: {stack}")
    print(f"Top element: {stack.peek()}")
    
    # Final state
    print(f"\nFinal stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    print(f"Size: {stack.size()}")
    
    print("\n" + "="*60)
    print("STACK OPERATIONS COMPLEXITY SUMMARY")
    print("="*60)
    print("""
Operation          Time Complexity    Space Complexity
------------------------------------------------------
push()             O(1) amortized      O(1)
pop()              O(1)               O(1)
peek()             O(1)               O(1)
is_empty()         O(1)               O(1)
size()             O(1)               O(1)
clear()            O(1)               O(1)

All basic stack operations are O(1) time complexity.
Stack uses O(n) space to store n elements.
""")

