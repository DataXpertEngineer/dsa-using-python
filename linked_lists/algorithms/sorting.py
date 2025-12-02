"""
Sorting Algorithms for Linked Lists

Sorting linked lists requires different approaches than arrays since we can't
use random access. Merge sort is the most efficient approach for linked lists.

Why Merge Sort for Linked Lists?
---------------------------------
- No random access needed (works with sequential access)
- O(n log n) time complexity
- Stable sort
- Efficient for linked lists

Other approaches like quicksort are less efficient for linked lists due to
the need for random access.

Useful in:
- Sorting linked list data
- Understanding divide-and-conquer on linked structures
- Common interview problems
"""

from typing import Optional


class ListNode:
    """Simple node class for sorting demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Merge Sort (Optimal for Linked Lists)
# ----------------------------------------------------------------------
def merge_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Sort linked list using merge sort algorithm.

    Algorithm:
    1. Find middle of list
    2. Recursively sort left and right halves
    3. Merge sorted halves

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: Head of sorted linked list

    Complexity:
        Time: O(n log n)  - Divide and conquer, log n levels, n work per level.
        Space: O(log n)  - Recursion stack depth is log n.
    """
    if not head or not head.next:
        return head
    
    # Find middle
    mid = get_middle(head)
    right = mid.next
    mid.next = None
    
    # Recursively sort
    left_sorted = merge_sort_linked_list(head)
    right_sorted = merge_sort_linked_list(right)
    
    # Merge
    return merge(left_sorted, right_sorted)


def get_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node using slow-fast pointer technique.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: Middle node
    """
    if not head:
        return head
    
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.

    Args:
        left (Optional[ListNode]): Head of first sorted list
        right (Optional[ListNode]): Head of second sorted list

    Returns:
        Optional[ListNode]: Head of merged sorted list
    """
    dummy = ListNode(0)
    current = dummy
    
    while left and right:
        if left.val <= right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    current.next = left if left else right
    return dummy.next


# ----------------------------------------------------------------------
# Insertion Sort (Alternative, less efficient)
# ----------------------------------------------------------------------
def insertion_sort_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Sort linked list using insertion sort.

    Note: Less efficient than merge sort (O(n²)) but simpler to understand.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: Head of sorted linked list

    Complexity:
        Time: O(n²)     - For each element, may need to traverse sorted portion.
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    current = head.next
    head.next = None
    
    while current:
        next_node = current.next
        prev = dummy
        
        # Find insertion position
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        
        # Insert
        current.next = prev.next
        prev.next = current
        current = next_node
    
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
    print("\n📌 Example: Sorting Linked Lists Demonstration")
    
    # Merge sort
    head1 = array_to_list([4, 2, 1, 3])
    print(f"Original: {list_to_array(head1)}")
    sorted_head = merge_sort_linked_list(head1)
    print(f"Merge sorted: {list_to_array(sorted_head)}")
    
    # Insertion sort
    head2 = array_to_list([4, 2, 1, 3])
    insertion_sorted = insertion_sort_linked_list(head2)
    print(f"Insertion sorted: {list_to_array(insertion_sorted)}")

