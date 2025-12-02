"""
Merge Sorted Lists Technique

Merging two sorted linked lists into one sorted list is a fundamental operation
that combines elements from both lists in sorted order.

Approaches:
1. Iterative with dummy node (most common)
2. Recursive approach
3. In-place merging

Why Merge Sorted Lists?
-----------------------
- Foundation for merge sort on linked lists
- Common interview problem
- Understanding two-pointer technique
- Practice with list manipulation

Useful in:
- Merge sort implementation
- Combining sorted data streams
- Common interview problems
"""

from typing import Optional


class ListNode:
    """Simple node class for technique demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Iterative Approach with Dummy Node (Language-agnostic)
# ----------------------------------------------------------------------
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists iteratively using dummy node.

    Args:
        list1 (Optional[ListNode]): Head of first sorted list
        list2 (Optional[ListNode]): Head of second sorted list

    Returns:
        Optional[ListNode]: Head of merged sorted list

    Complexity:
        Time: O(n + m)  - Traverses both lists once, n and m are lengths.
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
# Recursive Approach
# ----------------------------------------------------------------------
def merge_two_lists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists recursively.

    Args:
        list1 (Optional[ListNode]): Head of first sorted list
        list2 (Optional[ListNode]): Head of second sorted list

    Returns:
        Optional[ListNode]: Head of merged sorted list

    Complexity:
        Time: O(n + m)  - Processes each node once.
        Space: O(n + m) - Recursion stack depth is n + m.
    """
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


# ----------------------------------------------------------------------
# Merge K Sorted Lists
# ----------------------------------------------------------------------
def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted list.

    Args:
        lists (list[Optional[ListNode]]): List of k sorted linked lists

    Returns:
        Optional[ListNode]: Head of merged sorted list

    Complexity:
        Time: O(n * k)  - Where n is average length, k is number of lists.
        Space: O(1)    - Only uses pointers (excluding recursion stack).
    """
    if not lists:
        return None
    
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_lists(list1, list2))
        lists = merged_lists
    
    return lists[0]


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
    print("\n📌 Example: Merge Sorted Lists Technique Demonstration")
    
    # Merge two sorted lists
    list1 = array_to_list([1, 2, 4])
    list2 = array_to_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    print(f"Merge [1,2,4] and [1,3,4]: {list_to_array(merged)}")
    print("Expected: [1, 1, 2, 3, 4, 4]")
    
    # Recursive merge
    list3 = array_to_list([1, 3, 5])
    list4 = array_to_list([2, 4, 6])
    merged_rec = merge_two_lists_recursive(list3, list4)
    print(f"\nRecursive merge [1,3,5] and [2,4,6]: {list_to_array(merged_rec)}")
    
    # Merge k lists
    lists = [
        array_to_list([1, 4, 5]),
        array_to_list([1, 3, 4]),
        array_to_list([2, 6])
    ]
    merged_k = merge_k_lists(lists)
    print(f"\nMerge k lists [[1,4,5], [1,3,4], [2,6]]: {list_to_array(merged_k)}")
    print("Expected: [1, 1, 2, 3, 4, 4, 5, 6]")

