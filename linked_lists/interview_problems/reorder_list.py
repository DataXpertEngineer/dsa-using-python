"""
Reorder List Problem

You are given the head of a singly linked list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

Problem Statement:
------------------
You are given the head of a singly linked list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Useful in:
- Finding middle element
- Reversing linked list
- Merging lists
- Common interview problem
"""

from typing import Optional


class ListNode:
    """Simple node class for problem demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Optimal Approach (Language-agnostic)
# ----------------------------------------------------------------------
def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorder list: L0 → Ln → L1 → Ln-1 → ...

    Algorithm:
    1. Find middle of list
    2. Reverse second half
    3. Merge first and second halves alternately

    Args:
        head (Optional[ListNode]): Head of the linked list (modified in-place)

    Complexity:
        Time: O(n)     - Find middle O(n), reverse O(n), merge O(n).
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Split and reverse second half
    second = slow.next
    slow.next = None
    second = reverse_list(second)
    
    # Merge two halves
    first = head
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse linked list."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


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
    print("\n📌 Example: Reorder List Problem Demonstration")
    
    # Example 1
    head1 = array_to_list([1, 2, 3, 4])
    print(f"Original: {list_to_array(head1)}")
    reorder_list(head1)
    print(f"Reordered: {list_to_array(head1)}")
    print("Expected: [1, 4, 2, 3]")
    
    # Example 2
    head2 = array_to_list([1, 2, 3, 4, 5])
    print(f"\nOriginal: {list_to_array(head2)}")
    reorder_list(head2)
    print(f"Reordered: {list_to_array(head2)}")
    print("Expected: [1, 5, 2, 4, 3]")

