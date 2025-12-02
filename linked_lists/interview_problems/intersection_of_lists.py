"""
Intersection of Two Linked Lists Problem

Given the heads of two singly linked lists headA and headB, return the node
at which the two lists intersect. If the two linked lists have no intersection
at all, return null.

Problem Statement:
------------------
Given the heads of two singly linked lists headA and headB, return the node
at which the two lists intersect. If the two linked lists have no intersection
at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Example:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

Useful in:
- Two pointers technique
- Understanding linked list structure
- Common interview problem
"""

from typing import Optional


class ListNode:
    """Simple node class for problem demonstrations."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ----------------------------------------------------------------------
# Two Pointers Approach (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def get_intersection_node(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find intersection node using two pointers technique.

    Algorithm:
    1. Traverse both lists simultaneously
    2. When one pointer reaches end, switch to other list
    3. They will meet at intersection (or both become None)

    Args:
        headA (Optional[ListNode]): Head of first linked list
        headB (Optional[ListNode]): Head of second linked list

    Returns:
        Optional[ListNode]: Intersection node, None if no intersection

    Complexity:
        Time: O(m + n)  - Traverses both lists, m and n are lengths.
        Space: O(1)    - Only uses two pointer variables.
    """
    if not headA or not headB:
        return None
    
    ptrA = headA
    ptrB = headB
    
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    
    return ptrA


# ----------------------------------------------------------------------
# Hash Set Approach (Alternative)
# ----------------------------------------------------------------------
def get_intersection_node_hashset(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find intersection node using hash set.

    Args:
        headA (Optional[ListNode]): Head of first linked list
        headB (Optional[ListNode]): Head of second linked list

    Returns:
        Optional[ListNode]: Intersection node, None if no intersection

    Complexity:
        Time: O(m + n)  - Traverses both lists once.
        Space: O(m)    - Stores nodes from first list in hash set.
    """
    visited = set()
    current = headA
    
    while current:
        visited.add(current)
        current = current.next
    
    current = headB
    while current:
        if current in visited:
            return current
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


def create_intersection(listA: list[int], listB: list[int], intersect_val: int) -> tuple[Optional[ListNode], Optional[ListNode]]:
    """Create two lists that intersect at a node with given value."""
    # Create nodes
    nodesA = [ListNode(val) for val in listA]
    nodesB = [ListNode(val) for val in listB]
    
    # Link nodes
    for i in range(len(nodesA) - 1):
        nodesA[i].next = nodesA[i + 1]
    
    for i in range(len(nodesB) - 1):
        nodesB[i].next = nodesB[i + 1]
    
    # Find intersection point
    intersect_node = None
    for node in nodesA:
        if node.val == intersect_val:
            intersect_node = node
            break
    
    if intersect_node:
        # Make last node of listB point to intersection
        if nodesB:
            nodesB[-1].next = intersect_node
    
    return (nodesA[0] if nodesA else None, nodesB[0] if nodesB else None)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Intersection of Two Linked Lists Problem Demonstration")
    
    # Create intersecting lists
    # listA: 4 -> 1 -> 8 -> 4 -> 5
    # listB: 5 -> 6 -> 1 -> (intersects at 8)
    headA, headB = create_intersection([4, 1, 8, 4, 5], [5, 6, 1], 8)
    
    print("List A: 4 -> 1 -> 8 -> 4 -> 5")
    print("List B: 5 -> 6 -> 1 -> (intersects at 8)")
    
    intersection = get_intersection_node(headA, headB)
    print(f"Intersection node value: {intersection.val if intersection else None}")
    print("Expected: 8")

