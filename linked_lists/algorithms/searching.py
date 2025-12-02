"""
Searching Algorithms for Linked Lists

Searching in linked lists is different from arrays since we can't use binary search
directly. We need sequential search, but can optimize with techniques like
skip lists (advanced) or maintaining sorted order.

Why Sequential Search?
----------------------
- No random access in linked lists
- Must traverse from head to find element
- Binary search requires random access (not available)

Useful in:
- Finding elements in linked lists
- Understanding sequential access limitations
- Common operations on linked data structures
"""

from typing import Optional


class ListNode:
    """Simple node class for searching demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Linear Search (Language-agnostic)
# ----------------------------------------------------------------------
def linear_search(head: Optional[ListNode], target: int) -> Optional[ListNode]:
    """
    Search for target value in linked list using linear search.

    Args:
        head (Optional[ListNode]): Head of the linked list
        target (int): Value to search for

    Returns:
        Optional[ListNode]: Node containing target, None if not found

    Complexity:
        Time: O(n)     - May need to check all n nodes in worst case.
        Space: O(1)   - Only uses a pointer variable.
    """
    current = head
    while current:
        if current.val == target:
            return current
        current = current.next
    return None


def search_with_position(head: Optional[ListNode], target: int) -> tuple[Optional[ListNode], int]:
    """
    Search for target and return node with its position (0-indexed).

    Args:
        head (Optional[ListNode]): Head of the linked list
        target (int): Value to search for

    Returns:
        tuple: (Node containing target, position) or (None, -1) if not found

    Complexity:
        Time: O(n)     - May need to check all n nodes.
        Space: O(1)   - Only uses pointer and counter variables.
    """
    current = head
    position = 0
    
    while current:
        if current.val == target:
            return (current, position)
        current = current.next
        position += 1
    
    return (None, -1)


# ----------------------------------------------------------------------
# Search in Sorted List (Optimized)
# ----------------------------------------------------------------------
def search_sorted(head: Optional[ListNode], target: int) -> Optional[ListNode]:
    """
    Search in sorted linked list (can stop early if value is too large).

    Args:
        head (Optional[ListNode]): Head of sorted linked list
        target (int): Value to search for

    Returns:
        Optional[ListNode]: Node containing target, None if not found

    Complexity:
        Time: O(n) worst case, O(k) best case where k is position
        Space: O(1)   - Only uses a pointer variable.
    """
    current = head
    while current:
        if current.val == target:
            return current
        if current.val > target:
            return None  # Since list is sorted, target not found
        current = current.next
    return None


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
    print("\n📌 Example: Searching Linked Lists Demonstration")
    
    # Linear search
    head = array_to_list([1, 2, 3, 4, 5])
    print(f"List: {list_to_array(head)}")
    
    result = linear_search(head, 3)
    print(f"Search 3: {'Found' if result else 'Not found'}")
    
    result, pos = search_with_position(head, 3)
    print(f"Search 3 with position: {'Found at position ' + str(pos) if result else 'Not found'}")
    
    # Search in sorted list
    sorted_head = array_to_list([1, 2, 3, 4, 5])
    result = search_sorted(sorted_head, 3)
    print(f"Search 3 in sorted list: {'Found' if result else 'Not found'}")

