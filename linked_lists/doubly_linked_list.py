"""
Doubly Linked List in Python

A doubly linked list is a linear data structure where each node contains
a data field and two references: one to the next node and one to the previous node.

Structure:
    None <-> Node: [prev | data | next] <-> Node: [prev | data | next] <-> ... <-> None

Characteristics:
- Can traverse in both directions (forward and backward)
- More memory per node (stores two pointers)
- Efficient insertion/deletion at both ends: O(1)
- Can delete a node in O(1) if we have a reference to it
- Better for operations requiring backward traversal

Useful in:
- When bidirectional traversal is needed
- Implementing deque (double-ended queue)
- Browser history (back/forward navigation)
- Undo/redo functionality
"""

from typing import Optional, Any, Iterator


class DoublyNode:
    """
    Node class for doubly linked list.

    Attributes:
        data: The data stored in the node
        prev: Reference to the previous node
        next: Reference to the next node
    """
    def __init__(self, data: Any) -> None:
        """
        Initialize a node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.prev: Optional['DoublyNode'] = None
        self.next: Optional['DoublyNode'] = None


class DoublyLinkedList:
    """
    Doubly Linked List implementation.

    A linked list where each node points to both next and previous nodes.
    Supports bidirectional traversal and efficient operations at both ends.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty doubly linked list.
        """
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None

    def __str__(self) -> str:
        """
        String representation of the doubly linked list.

        Returns:
            str: String representation showing all nodes

        Complexity:
            Time: O(n)    - Traverses all n nodes to build string.
            Space: O(n)   - Stores string representation of all nodes.
        """
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        return " <-> ".join(nodes) if nodes else "Empty"

    def insert_at_start(self, data: Any) -> None:
        """
        Insert a node at the beginning of the list.

        Args:
            data: Data to insert

        Complexity:
            Time: O(1)    - Constant time operation, just update head.
            Space: O(1)   - Only creates one new node.
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data: Any) -> None:
        """
        Insert a node at the end of the list.

        Args:
            data: Data to insert

        Complexity:
            Time: O(1)    - We maintain tail pointer, so constant time.
            Space: O(1)   - Only creates one new node.
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, key: Any) -> bool:
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
        temp = self.head
        
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    # Deleting head
                    self.head = temp.next
                
                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    # Deleting tail
                    self.tail = temp.prev
                
                return True
            temp = temp.next
        
        return False

    def delete_node(self, node: DoublyNode) -> None:
        """
        Delete a node given a reference to it (O(1) operation).

        Args:
            node: Reference to the node to delete

        Complexity:
            Time: O(1)    - Direct deletion using node reference.
            Space: O(1)   - Only updates pointers.
        """
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def search(self, key: Any) -> bool:
        """
        Search for a value in the linked list.

        Args:
            key: Value to search for

        Returns:
            bool: True if found, False otherwise

        Complexity:
            Time: O(n)    - May need to check all n nodes in worst case.
            Space: O(1)   - Only uses a pointer variable.
        """
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def reverse(self) -> None:
        """
        Reverse the doubly linked list in-place.

        Complexity:
            Time: O(n)    - Traverses the list once, swapping prev and next.
            Space: O(1)   - Only uses a pointer variable.
        """
        temp = None
        current = self.head
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev

    def print_forward(self) -> None:
        """
        Print all elements from head to tail.

        Complexity:
            Time: O(n)    - Traverses all n nodes.
            Space: O(1)   - Only uses a pointer variable.
        """
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def print_backward(self) -> None:
        """
        Print all elements from tail to head.

        Complexity:
            Time: O(n)    - Traverses all n nodes.
            Space: O(1)   - Only uses a pointer variable.
        """
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def length(self) -> int:
        """
        Get the length of the linked list.

        Returns:
            int: Number of nodes in the list

        Complexity:
            Time: O(n)    - Must traverse all n nodes to count.
            Space: O(1)   - Only uses a counter variable.
        """
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def clear(self) -> None:
        """
        Clear the linked list (remove all nodes).

        Complexity:
            Time: O(1)    - Just sets head and tail to None.
            Space: O(1)   - No extra space used.
        """
        self.head = self.tail = None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Doubly Linked List Demonstration")
    
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_start(0)

    print("Forward traversal:")
    dll.print_forward()  # 0 <-> 1 <-> 2 <-> 3 <-> None

    print("\nBackward traversal:")
    dll.print_backward()  # 3 <-> 2 <-> 1 <-> 0 <-> None

    print(f"\nSearch 2: {dll.search(2)}")  # True
    
    dll.delete(2)
    print("\nAfter deleting 2:")
    dll.print_forward()

    print(f"\nLength: {dll.length()}")

    dll.reverse()
    print("\nAfter reversing:")
    dll.print_forward()

