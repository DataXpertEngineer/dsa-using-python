"""
Detect Cycle in Linked List Problem

Given head, the head of a linked list, determine if the linked list has a cycle.

Problem Statement:
------------------
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example:
    Input: head = [3,2,0,-4], pos = 1 (cycle from -4 to 2)
    Output: true

This is solved using Floyd's Cycle Detection Algorithm (Tortoise and Hare).

Useful in:
- Cycle detection
- Floyd's algorithm
- Common interview problem
"""

from typing import Optional


class ListNode:
    """Simple node class for problem demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Floyd's Algorithm (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using Floyd's Tortoise and Hare algorithm.

    Algorithm:
    1. Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
    2. If there's a cycle, fast will eventually catch up to slow
    3. If fast reaches None, there's no cycle

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        bool: True if cycle exists, False otherwise

    Complexity:
        Time: O(n)     - Slow and fast pointers traverse the list, meet in O(n).
        Space: O(1)   - Only uses two pointer variables.
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the starting node of the cycle.

    Algorithm:
    1. Use Floyd's algorithm to detect cycle and find meeting point
    2. Move one pointer to head, keep other at meeting point
    3. Move both one step at a time - they meet at cycle start

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: Starting node of cycle, None if no cycle

    Complexity:
        Time: O(n)     - Two passes through the list.
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# ----------------------------------------------------------------------
# Hash Set Approach (Alternative)
# ----------------------------------------------------------------------
def has_cycle_hashset(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using hash set to track visited nodes.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        bool: True if cycle exists, False otherwise

    Complexity:
        Time: O(n)     - Traverses list once, hash operations are O(1).
        Space: O(n)   - Stores up to n nodes in hash set.
    """
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False


# ----------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------
def create_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    """Create a cycle in linked list at given position (for testing)."""
    if pos == -1:
        return head
    
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    if pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return head


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Detect Cycle Problem Demonstration")
    
    # Create list with cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create cycle
    
    print("List: 3 -> 2 -> 0 -> -4 -> (back to 2)")
    print(f"Has cycle (Floyd's): {has_cycle(node1)}")
    print(f"Has cycle (HashSet): {has_cycle_hashset(node1)}")
    
    cycle_start = detect_cycle_start(node1)
    print(f"Cycle starts at node with value: {cycle_start.val if cycle_start else None}")

