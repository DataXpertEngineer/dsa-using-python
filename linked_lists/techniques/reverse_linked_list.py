"""
Reverse Linked List Technique

Reversing a linked list is a fundamental operation that can be done using
iterative or recursive approaches with pointers.

Approaches:
1. Iterative: Use three pointers (prev, current, next)
2. Recursive: Recursively reverse the rest, then fix current node

Why Reverse?
-----------
- Common interview problem
- Foundation for other problems (reverse k nodes, reverse between positions)
- Understanding pointer manipulation
- Practice with iterative and recursive thinking

Useful in:
- Reversing entire list
- Reversing portion of list
- Palindrome checking
- Common interview problems
"""

from typing import Optional


class ListNode:
    """Simple node class for technique demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Iterative Approach (Language-agnostic)
# ----------------------------------------------------------------------
def reverse_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list using iterative approach with pointers.

    Algorithm:
    1. Initialize prev = None, current = head
    2. For each node:
       - Store next node
       - Reverse current node's pointer
       - Move prev and current forward
    3. Return prev as new head

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: New head of reversed list

    Complexity:
        Time: O(n)     - Traverses the list once, reversing links.
        Space: O(1)   - Only uses three pointer variables.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev forward
        current = next_node  # Move current forward
    
    return prev


# ----------------------------------------------------------------------
# Recursive Approach
# ----------------------------------------------------------------------
def reverse_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list using recursive approach.

    Algorithm:
    1. Base case: If head is None or last node, return head
    2. Recursively reverse the rest of the list
    3. Fix current node's pointer to point to previous
    4. Return new head

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        Optional[ListNode]: New head of reversed list

    Complexity:
        Time: O(n)     - Recursively processes all n nodes.
        Space: O(n)   - Recursion stack depth is n.
    """
    if not head or not head.next:
        return head
    
    # Reverse the rest of the list
    new_head = reverse_recursive(head.next)
    
    # Fix current node
    head.next.next = head
    head.next = None
    
    return new_head


# ----------------------------------------------------------------------
# Reverse Between Positions
# ----------------------------------------------------------------------
def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse linked list nodes from position left to right (1-indexed).

    Args:
        head (Optional[ListNode]): Head of the linked list
        left (int): Start position (1-indexed)
        right (int): End position (1-indexed)

    Returns:
        Optional[ListNode]: Head of modified list

    Complexity:
        Time: O(n)     - Single pass through the list.
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or left == right:
        return head
    
    # Create dummy node to handle edge case of reversing from head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to position before left
    for _ in range(left - 1):
        prev = prev.next
    
    # Reverse nodes from left to right
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next


# ----------------------------------------------------------------------
# Reverse in Groups of K
# ----------------------------------------------------------------------
def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Reverse linked list in groups of k nodes.

    Args:
        head (Optional[ListNode]): Head of the linked list
        k (int): Group size

    Returns:
        Optional[ListNode]: Head of modified list

    Complexity:
        Time: O(n)     - Processes each node once.
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or k == 1:
        return head
    
    # Check if we have k nodes
    count = 0
    temp = head
    while temp and count < k:
        temp = temp.next
        count += 1
    
    if count < k:
        return head  # Not enough nodes to reverse
    
    # Reverse first k nodes
    prev = None
    current = head
    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Recursively reverse remaining groups
    head.next = reverse_k_group(current, k)
    
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
    print("\n📌 Example: Reverse Linked List Technique Demonstration")
    
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = array_to_list([1, 2, 3, 4, 5])
    print(f"Original: {list_to_array(head)}")
    
    # Iterative reverse
    reversed_head = reverse_iterative(array_to_list([1, 2, 3, 4, 5]))
    print(f"Iterative reverse: {list_to_array(reversed_head)}")
    
    # Recursive reverse
    reversed_head_rec = reverse_recursive(array_to_list([1, 2, 3, 4, 5]))
    print(f"Recursive reverse: {list_to_array(reversed_head_rec)}")
    
    # Reverse between positions
    head2 = array_to_list([1, 2, 3, 4, 5])
    reversed_between = reverse_between(head2, 2, 4)
    print(f"Reverse between [2:4]: {list_to_array(reversed_between)}")
    
    # Reverse in groups of k
    head3 = array_to_list([1, 2, 3, 4, 5, 6, 7, 8])
    reversed_k = reverse_k_group(head3, 3)
    print(f"Reverse in groups of 3: {list_to_array(reversed_k)}")

