"""
Circular Linked List in Python

A circular linked list is a linked list where the last node points back to the first node,
forming a circle. There is no NULL at the end.

Structure:
    Node -> Node -> Node -> ... -> Node -> (back to first Node)

Characteristics:
- Last node points to first node (circular)
- Can start traversal from any node
- Useful for round-robin scheduling
- Can be singly or doubly linked
- No explicit NULL termination

Useful in:
- Round-robin scheduling algorithms
- Implementing circular buffers
- Music playlists (repeat functionality)
- Multiplayer games (turn-based)
"""

from typing import Optional, Any


class CircularNode:
    """
    Node class for circular linked list.

    Attributes:
        data: The data stored in the node
        next: Reference to the next node in the circle
    """
    def __init__(self, data):
        """
        Initialize a node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next: Optional['CircularNode'] = None


class CircularLinkedList:
    """
    Circular Linked List implementation.

    A linked list where the last node points back to the first node.
    Supports circular traversal and operations.
    """
    
    def __init__(self):
        """
        Initialize an empty circular linked list.
        """
        self.head: Optional[CircularNode] = None

    def __str__(self):
        """
        String representation of the circular linked list.

        Returns:
            str: String representation showing all nodes

        Complexity:
            Time: O(n)    - Traverses all n nodes to build string.
            Space: O(n)   - Stores string representation of all nodes.
        """
        if not self.head:
            return "Empty"
        
        nodes = []
        temp = self.head
        nodes.append(str(temp.data))
        temp = temp.next
        
        while temp != self.head:
            nodes.append(str(temp.data))
            temp = temp.next
        
        return " -> ".join(nodes) + " -> (back to head)"

    def insert_at_start(self, data):
        """
        Insert a node at the beginning of the circular list.

        Args:
            data: Data to insert

        Complexity:
            Time: O(n)    - Need to update last node's next pointer.
            Space: O(1)   - Only creates one new node.
        """
        new_node = CircularNode(data)
        
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        
        # Find last node
        last = self.head
        while last.next != self.head:
            last = last.next
        
        new_node.next = self.head
        last.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a node at the end of the circular list.

        Args:
            data: Data to insert

        Complexity:
            Time: O(n)    - Need to find last node to update its next.
            Space: O(1)   - Only creates one new node.
        """
        new_node = CircularNode(data)
        
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        
        # Find last node
        last = self.head
        while last.next != self.head:
            last = last.next
        
        last.next = new_node
        new_node.next = self.head

    def delete(self, key):
        """
        Delete a node with the given key.

        Args:
            key: Data value of the node to delete

        Returns:
            bool: True if node was deleted, False if not found

        Complexity:
            Time: O(n)    - May need to traverse the entire list.
            Space: O(1)   - Only uses variables for pointers.
        """
        if not self.head:
            return False
        
        # If head is the only node
        if self.head.data == key and self.head.next == self.head:
            self.head = None
            return True
        
        # If head needs to be deleted
        if self.head.data == key:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = self.head.next
            return True
        
        # Search for node to delete
        prev = self.head
        current = self.head.next
        
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        
        return False

    def search(self, key):
        """
        Search for a value in the circular linked list.

        Args:
            key: Value to search for

        Returns:
            bool: True if found, False otherwise

        Complexity:
            Time: O(n)    - May need to check all n nodes in worst case.
            Space: O(1)   - Only uses a pointer variable.
        """
        if not self.head:
            return False
        
        temp = self.head
        if temp.data == key:
            return True
        
        temp = temp.next
        while temp != self.head:
            if temp.data == key:
                return True
            temp = temp.next
        
        return False

    def print_list(self):
        """
        Print all elements of the circular linked list.

        Complexity:
            Time: O(n)    - Traverses all n nodes.
            Space: O(1)   - Only uses a pointer variable.
        """
        if not self.head:
            print("Empty")
            return
        
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("(back to head)")

    def length(self):
        """
        Get the length of the circular linked list.

        Returns:
            int: Number of nodes in the list

        Complexity:
            Time: O(n)    - Must traverse all n nodes to count.
            Space: O(1)   - Only uses a counter variable.
        """
        if not self.head:
            return 0
        
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def clear(self):
        """
        Clear the circular linked list (remove all nodes).

        Complexity:
            Time: O(1)    - Just sets head to None.
            Space: O(1)   - No extra space used.
        """
        self.head = None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Circular Linked List Demonstration")
    
    cll = CircularLinkedList()
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)
    cll.insert_at_start(0)

    print("Circular list:")
    cll.print_list()  # 0 -> 1 -> 2 -> 3 -> (back to head)

    print(f"\nSearch 2: {cll.search(2)}")  # True
    
    cll.delete(2)
    print("\nAfter deleting 2:")
    cll.print_list()

    print(f"\nLength: {cll.length()}")

    print(f"\nString representation: {cll}")

