"""
Slow-Fast Pointer Technique (Floyd's Algorithm)

The slow-fast pointer technique (also known as Floyd's Tortoise and Hare algorithm)
uses two pointers moving at different speeds to solve various linked list problems.

Common Applications:
1. Detect cycle in linked list
2. Find middle element
3. Find k-th node from end
4. Detect cycle start point
5. Find length of cycle

Why Slow-Fast Pointers?
-----------------------
Without slow-fast pointers:
    Finding middle = O(n) traversal + O(n) to count = O(n) but requires two passes
    Detecting cycle = O(n) with hash set (extra space)
With slow-fast pointers:
    Single pass = O(n) time, O(1) space

Useful in:
- Cycle detection
- Finding middle elements
- Partitioning problems
- Common interview problems
"""

from typing import Optional


class ListNode:
    """Simple node class for technique demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Detect Cycle
# ----------------------------------------------------------------------
def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if linked list has a cycle using Floyd's algorithm.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        bool: True if cycle exists, False otherwise

    Complexity:
        Time: O(n)    - Slow and fast pointers traverse the list, meet in O(n).
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
    Find the starting node of a cycle in linked list.

    Algorithm:
    1. Use slow-fast pointers to detect cycle
    2. If cycle exists, move one pointer to head
    3. Move both pointers one step at a time
    4. They meet at cycle start

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: Starting node of cycle, None if no cycle

    Complexity:
        Time: O(n)    - Two passes through the list.
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
# Find Middle Element
# ----------------------------------------------------------------------
def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node of linked list using slow-fast pointers.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: Middle node, None if list is empty

    Complexity:
        Time: O(n)    - Fast pointer traverses n nodes, slow pointer n/2.
        Space: O(1)   - Only uses two pointer variables.
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# ----------------------------------------------------------------------
# Find k-th Node from End
# ----------------------------------------------------------------------
def find_kth_from_end(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Find k-th node from the end using slow-fast pointers.

    Algorithm:
    1. Move fast pointer k steps ahead
    2. Move both pointers until fast reaches end
    3. Slow pointer will be at k-th from end

    Args:
        head (Optional[ListNode]): Head of the linked list
        k (int): Position from end (1-indexed)

    Returns:
        Optional[ListNode]: k-th node from end, None if not found

    Complexity:
        Time: O(n)    - Single pass through the list.
        Space: O(1)   - Only uses two pointer variables.
    """
    if not head or k <= 0:
        return None
    
    slow = fast = head
    
    # Move fast pointer k steps ahead
    for _ in range(k):
        if not fast:
            return None  # List shorter than k
        fast = fast.next
    
    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# ----------------------------------------------------------------------
# Find Length of Cycle
# ----------------------------------------------------------------------
def cycle_length(head: Optional[ListNode]) -> int:
    """
    Find the length of cycle in linked list.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        int: Length of cycle, 0 if no cycle

    Complexity:
        Time: O(n)    - Detects cycle and measures its length.
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or not head.next:
        return 0
    
    slow = fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0  # No cycle
    
    # Count cycle length
    length = 1
    temp = slow.next
    while temp != slow:
        length += 1
        temp = temp.next
    
    return length


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Slow-Fast Pointer Technique Demonstration")
    
    # Create a list: 1 -> 2 -> 3 -> 4 -> 5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    print("List: 1 -> 2 -> 3 -> 4 -> 5")
    
    # Find middle
    middle = find_middle(node1)
    print(f"Middle element: {middle.val if middle else None}")
    
    # Find k-th from end
    kth = find_kth_from_end(node1, 2)
    print(f"2nd from end: {kth.val if kth else None}")
    
    # Check for cycle
    print(f"Has cycle: {has_cycle(node1)}")
    
    # Create cycle: 5 -> 3
    node5.next = node3
    print(f"\nAfter creating cycle (5 -> 3):")
    print(f"Has cycle: {has_cycle(node1)}")
    cycle_start = detect_cycle_start(node1)
    print(f"Cycle starts at: {cycle_start.val if cycle_start else None}")
    print(f"Cycle length: {cycle_length(node1)}")

