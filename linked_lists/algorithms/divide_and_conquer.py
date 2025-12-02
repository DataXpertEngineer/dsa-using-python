"""
Divide and Conquer Algorithms for Linked Lists

Divide and conquer techniques applied to linked lists, including problems
that can be solved by splitting the list and solving subproblems.

Common Problems:
- Merge sort (already covered in sorting.py)
- Finding middle element
- Splitting lists
- Palindrome checking

Useful in:
- Understanding recursive approaches on linked structures
- Solving complex linked list problems
- Common interview problems
"""

from typing import Optional


class ListNode:
    """Simple node class for divide and conquer demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Check Palindrome (Divide and Conquer approach)
# ----------------------------------------------------------------------
def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is a palindrome using divide and conquer.

    Algorithm:
    1. Find middle of list
    2. Reverse second half
    3. Compare first and second halves
    4. Restore list (optional)

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        bool: True if palindrome, False otherwise

    Complexity:
        Time: O(n)     - Find middle O(n), reverse O(n), compare O(n).
        Space: O(1)   - Only uses pointer variables.
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = reverse_list(slow.next)
    slow.next = None
    
    # Compare
    first = head
    second = second_half
    is_pal = True
    
    while second:
        if first.val != second.val:
            is_pal = False
            break
        first = first.next
        second = second.next
    
    # Restore list (optional)
    slow.next = reverse_list(second_half)
    
    return is_pal


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
# Split List
# ----------------------------------------------------------------------
def split_list(head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
    """
    Split linked list into two halves.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        tuple: (First half head, Second half head)

    Complexity:
        Time: O(n)     - Find middle O(n).
        Space: O(1)   - Only uses pointer variables.
    """
    if not head:
        return (None, None)
    
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    second_half = slow.next
    slow.next = None
    
    return (head, second_half)


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
    print("\n📌 Example: Divide and Conquer on Linked Lists Demonstration")
    
    # Palindrome check
    head1 = array_to_list([1, 2, 2, 1])
    print(f"List: {list_to_array(head1)}")
    print(f"Is palindrome: {is_palindrome(head1)}")
    
    head2 = array_to_list([1, 2, 3])
    print(f"\nList: {list_to_array(head2)}")
    print(f"Is palindrome: {is_palindrome(head2)}")
    
    # Split list
    head3 = array_to_list([1, 2, 3, 4, 5])
    first, second = split_list(head3)
    print(f"\nSplit [1,2,3,4,5]:")
    print(f"First half: {list_to_array(first)}")
    print(f"Second half: {list_to_array(second)}")

