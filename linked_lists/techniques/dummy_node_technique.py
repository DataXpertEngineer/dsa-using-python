"""
Dummy Node Technique

The dummy node technique uses a temporary node at the beginning of a list
to simplify edge case handling, especially for insertion/deletion at head.

Why Dummy Node?
--------------
Without dummy node:
    - Need special handling for head operations
    - More conditional checks
    - Complex edge case logic
With dummy node:
    - Uniform handling of all nodes
    - Cleaner code
    - Reduces edge case complexity

Useful in:
- Insertion/deletion at head
- Merging sorted lists
- Removing nodes
- Partitioning lists
- Common interview problems
"""

from typing import Optional


class ListNode:
    """Simple node class for technique demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Merge Two Sorted Lists (with dummy node)
# ----------------------------------------------------------------------
def merge_two_lists_dummy(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists using dummy node technique.

    Args:
        list1 (Optional[ListNode]): Head of first sorted list
        list2 (Optional[ListNode]): Head of second sorted list

    Returns:
        Optional[ListNode]: Head of merged sorted list

    Complexity:
        Time: O(n + m)  - Traverses both lists once.
        Space: O(1)    - Only uses dummy node and pointers.
    """
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes
    current.next = list1 if list1 else list2
    
    return dummy.next


# ----------------------------------------------------------------------
# Remove Elements (with dummy node)
# ----------------------------------------------------------------------
def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Remove all nodes with given value using dummy node.

    Args:
        head (Optional[ListNode]): Head of the linked list
        val (int): Value to remove

    Returns:
        Optional[ListNode]: Head of modified list

    Complexity:
        Time: O(n)     - Single pass through the list.
        Space: O(1)   - Only uses dummy node and pointers.
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next


# ----------------------------------------------------------------------
# Partition List (with dummy node)
# ----------------------------------------------------------------------
def partition_list(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    Partition list such that nodes < x come before nodes >= x.

    Args:
        head (Optional[ListNode]): Head of the linked list
        x (int): Partition value

    Returns:
        Optional[ListNode]: Head of partitioned list

    Complexity:
        Time: O(n)     - Single pass through the list.
        Space: O(1)   - Only uses dummy nodes and pointers.
    """
    # Dummy nodes for two partitions
    before_dummy = ListNode(0)
    after_dummy = ListNode(0)
    
    before = before_dummy
    after = after_dummy
    
    current = head
    
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next
    
    # Connect partitions
    before.next = after_dummy.next
    after.next = None
    
    return before_dummy.next


# ----------------------------------------------------------------------
# Remove Duplicates (with dummy node)
# ----------------------------------------------------------------------
def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from sorted linked list using dummy node.

    Args:
        head (Optional[ListNode]): Head of sorted linked list

    Returns:
        Optional[ListNode]: Head of list with duplicates removed

    Complexity:
        Time: O(n)     - Single pass through the list.
        Space: O(1)   - Only uses dummy node and pointers.
    """
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
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
    print("\n📌 Example: Dummy Node Technique Demonstration")
    
    # Merge two sorted lists
    list1 = array_to_list([1, 2, 4])
    list2 = array_to_list([1, 3, 4])
    merged = merge_two_lists_dummy(list1, list2)
    print(f"Merge [1,2,4] and [1,3,4]: {list_to_array(merged)}")
    
    # Remove elements
    head1 = array_to_list([1, 2, 6, 3, 4, 5, 6])
    removed = remove_elements(head1, 6)
    print(f"Remove 6 from [1,2,6,3,4,5,6]: {list_to_array(removed)}")
    
    # Partition list
    head2 = array_to_list([1, 4, 3, 2, 5, 2])
    partitioned = partition_list(head2, 3)
    print(f"Partition [1,4,3,2,5,2] by 3: {list_to_array(partitioned)}")
    
    # Remove duplicates
    head3 = array_to_list([1, 1, 2, 3, 3])
    no_duplicates = remove_duplicates(head3)
    print(f"Remove duplicates from [1,1,2,3,3]: {list_to_array(no_duplicates)}")

