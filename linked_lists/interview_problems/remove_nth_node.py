"""
Remove Nth Node From End of List Problem

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Problem Statement:
------------------
Given the head of a linked list, remove the nth node from the end of the list
and return the head of the list.

Example:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    Explanation: Remove the 2nd node from the end (node with value 4)

Useful in:
- Two pointers technique
- Dummy node technique
- Common interview problem
"""

from typing import Optional


class ListNode:
    """Simple node class for problem demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Two Pass Approach (Language-agnostic)
# ----------------------------------------------------------------------
def remove_nth_from_end_two_pass(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end using two passes.

    Algorithm:
    1. First pass: Count total nodes
    2. Calculate position from start
    3. Second pass: Remove node at calculated position

    Args:
        head (Optional[ListNode]): Head of the linked list
        n (int): Position from end (1-indexed)

    Returns:
        Optional[ListNode]: Head of modified list

    Complexity:
        Time: O(n)     - Two passes through the list.
        Space: O(1)   - Only uses pointer variables.
    """
    # Count nodes
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Calculate position from start
    pos_from_start = length - n
    
    if pos_from_start == 0:
        return head.next  # Remove head
    
    # Find node before target
    current = head
    for _ in range(pos_from_start - 1):
        current = current.next
    
    # Remove node
    current.next = current.next.next
    
    return head


# ----------------------------------------------------------------------
# One Pass with Two Pointers (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end using one pass with two pointers.

    Algorithm:
    1. Use dummy node to handle edge cases
    2. Move fast pointer n+1 steps ahead
    3. Move both pointers until fast reaches end
    4. Slow pointer will be at node before target
    5. Remove target node

    Args:
        head (Optional[ListNode]): Head of the linked list
        n (int): Position from end (1-indexed)

    Returns:
        Optional[ListNode]: Head of modified list

    Complexity:
        Time: O(n)     - Single pass through the list.
        Space: O(1)   - Only uses dummy node and pointers.
    """
    dummy = ListNode(0)
    dummy.next = head
    
    fast = dummy
    slow = dummy
    
    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove nth node
    slow.next = slow.next.next
    
    return dummy.next


# ----------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------
def list_to_array(head: Optional[ListNode]) -> list[int]:
    """Convert linked list to array for display."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr: list[int]) -> Optional[ListNode]:
    """Convert array to linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Remove Nth Node From End Problem Demonstration")
    
    # Remove 2nd from end
    head = array_to_list([1, 2, 3, 4, 5])
    print(f"Original: {list_to_array(head)}")
    result = remove_nth_from_end(head, 2)
    print(f"Remove 2nd from end: {list_to_array(result)}")
    print("Expected: [1, 2, 3, 5]")
    
    # Remove head (1st from end)
    head2 = array_to_list([1, 2])
    print(f"\nOriginal: {list_to_array(head2)}")
    result2 = remove_nth_from_end(head2, 2)
    print(f"Remove 2nd from end (head): {list_to_array(result2)}")
    print("Expected: [2]")

