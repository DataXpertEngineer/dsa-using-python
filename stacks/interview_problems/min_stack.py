"""
Min Stack Problem

Design a stack that supports push, pop, top, and getMin() in O(1) time.

Problem Statement:
-------------------
Design a stack that supports all standard operations plus getMin() that
returns the minimum element in O(1) time.

Example:
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.getMin()  # Returns -3
    stack.pop()
    stack.top()     # Returns 0
    stack.getMin()  # Returns -2

Why Two Approaches?
-------------------
- Approach 1: Store (value, min) pairs - simple but uses extra space
- Approach 2: Use auxiliary stack - more space efficient

Useful in:
- Stack design problems
- O(1) minimum queries
- Common interview problems
"""

from typing import Optional, List, Tuple


# ----------------------------------------------------------------------
# Min Stack - Approach 1: Store (value, min) pairs
# ----------------------------------------------------------------------
class MinStack:
    """
    Stack that supports getMin() in O(1) time.
    
    Approach: Store (value, current_min) pairs in stack.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty min stack.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.stack: List[Tuple[int, int]] = []  # (value, min_so_far)
    
    def push(self, val: int) -> None:
        """
        Push element onto stack.

        Args:
            val (int): Value to push

        Complexity:
            Time: O(1)     - Appends to list.
            Space: O(1)   - Adds one tuple.
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))
    
    def pop(self) -> None:
        """
        Remove top element from stack.

        Complexity:
            Time: O(1)     - Removes from end of list.
            Space: O(1)   - Removes one element.
        """
        if self.stack:
            self.stack.pop()
    
    def top(self) -> Optional[int]:
        """
        Get top element without removing.

        Returns:
            Optional[int]: Top element, None if empty

        Complexity:
            Time: O(1)     - Direct access to last element.
            Space: O(1)   - Only reads.
        """
        if not self.stack:
            return None
        return self.stack[-1][0]
    
    def getMin(self) -> Optional[int]:
        """
        Get minimum element in O(1) time.

        Returns:
            Optional[int]: Minimum element, None if empty

        Complexity:
            Time: O(1)     - Direct access to stored minimum.
            Space: O(1)   - Only reads.
        """
        if not self.stack:
            return None
        return self.stack[-1][1]


# ----------------------------------------------------------------------
# Min Stack - Approach 2: Auxiliary Stack
# ----------------------------------------------------------------------
class MinStackAuxiliary:
    """
    Min stack using auxiliary stack for minimum values.
    
    Approach: Use separate stack to track minimums.
    More space efficient when many elements have same minimum.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty min stack.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty lists.
        """
        self.stack: List[int] = []
        self.min_stack: List[int] = []
    
    def push(self, val: int) -> None:
        """
        Push element onto stack.

        Args:
            val (int): Value to push

        Complexity:
            Time: O(1)     - Appends to lists.
            Space: O(1)   - Adds one element.
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        """
        Remove top element from stack.

        Complexity:
            Time: O(1)     - Removes from end of lists.
            Space: O(1)   - Removes one element.
        """
        if self.stack:
            val = self.stack.pop()
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> Optional[int]:
        """
        Get top element without removing.

        Returns:
            Optional[int]: Top element, None if empty

        Complexity:
            Time: O(1)     - Direct access.
            Space: O(1)   - Only reads.
        """
        if not self.stack:
            return None
        return self.stack[-1]
    
    def getMin(self) -> Optional[int]:
        """
        Get minimum element in O(1) time.

        Returns:
            Optional[int]: Minimum element, None if empty

        Complexity:
            Time: O(1)     - Direct access to min stack top.
            Space: O(1)   - Only reads.
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Min Stack Demonstration")
    
    # Approach 1: (value, min) pairs
    print("Approach 1: Store (value, min) pairs")
    stack1 = MinStack()
    stack1.push(-2)
    stack1.push(0)
    stack1.push(-3)
    print(f"  Push: -2, 0, -3")
    print(f"  getMin(): {stack1.getMin()}")
    print(f"  top(): {stack1.top()}")
    stack1.pop()
    print(f"  After pop:")
    print(f"  top(): {stack1.top()}")
    print(f"  getMin(): {stack1.getMin()}")
    
    # Approach 2: Auxiliary stack
    print("\nApproach 2: Auxiliary stack")
    stack2 = MinStackAuxiliary()
    stack2.push(-2)
    stack2.push(0)
    stack2.push(-3)
    print(f"  Push: -2, 0, -3")
    print(f"  getMin(): {stack2.getMin()}")
    print(f"  top(): {stack2.top()}")
    stack2.pop()
    print(f"  After pop:")
    print(f"  top(): {stack2.top()}")
    print(f"  getMin(): {stack2.getMin()}")

