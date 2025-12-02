"""
Add Two Numbers Problem

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Problem Statement:
------------------
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

Useful in:
- Linked list manipulation
- Handling carry
- Common interview problem
"""

from typing import Optional


class ListNode:
    """Simple node class for problem demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Iterative Approach (Language-agnostic)
# ----------------------------------------------------------------------
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Add two numbers represented as linked lists.

    Algorithm:
    1. Traverse both lists simultaneously
    2. Add corresponding digits and carry
    3. Create new node for sum digit
    4. Handle carry for next iteration

    Args:
        l1 (Optional[ListNode]): First number (digits in reverse)
        l2 (Optional[ListNode]): Second number (digits in reverse)

    Returns:
        Optional[ListNode]: Sum as linked list (digits in reverse)

    Complexity:
        Time: O(max(n, m))  - Traverses longer list, n and m are lengths.
        Space: O(max(n, m)) - Creates new list for result.
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
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
    print("\n📌 Example: Add Two Numbers Problem Demonstration")
    
    # Example: 342 + 465 = 807
    # Represented as: [2,4,3] + [5,6,4] = [7,0,8]
    l1 = array_to_list([2, 4, 3])
    l2 = array_to_list([5, 6, 4])
    print(f"Number 1 (reverse): {list_to_array(l1)} = 342")
    print(f"Number 2 (reverse): {list_to_array(l2)} = 465")
    
    result = add_two_numbers(l1, l2)
    print(f"Sum (reverse): {list_to_array(result)} = 807")
    print("Expected: [7, 0, 8]")
    
    # Example with carry
    l3 = array_to_list([9, 9, 9, 9, 9, 9, 9])
    l4 = array_to_list([9, 9, 9, 9])
    print(f"\nNumber 1: {list_to_array(l3)}")
    print(f"Number 2: {list_to_array(l4)}")
    result2 = add_two_numbers(l3, l4)
    print(f"Sum: {list_to_array(result2)}")

