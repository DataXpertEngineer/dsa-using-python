"""
Singly Linked List in Python

A singly linked list is a linear data structure where each element (node) contains
a data field and a reference (link) to the next node in the sequence.

Structure:
    Node: [data | next] -> Node: [data | next] -> ... -> None

Characteristics:
- Dynamic size (grows/shrinks as needed)
- Non-contiguous memory (nodes can be anywhere)
- Sequential access only (no random access)
- Efficient insertion/deletion at head: O(1)
- Inefficient insertion/deletion at tail: O(n)

Useful in:
- When size is unknown or changes frequently
- When frequent insertions/deletions at beginning
- Implementing stacks, queues, and other data structures
- Memory-efficient when exact size is unpredictable
"""

from typing import Optional, Any, Iterator


class Node:
    """
    Node class for singly linked list.

    Attributes:
        data: The data stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self, data: Any) -> None:
        """
        Initialize a node with data.

        Args:
            data: The data to store in the node
        """
        self.data = data
        self.next: Optional['Node'] = None


class SingleLinkedList:
    """
    Singly Linked List implementation.

    A linked list where each node points to the next node.
    Supports insertion, deletion, search, and traversal operations.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty linked list.
        """
        self.head: Optional[Node] = None

    def __iter__(self) -> Iterator[Any]:
        """
        Make the linked list iterable.

        Returns:
            Iterator: Iterator over the linked list elements

        Complexity:
            Time: O(1)    - Returns iterator, actual iteration is O(n).
            Space: O(1)   - Iterator object uses constant space.
        """
        return LinkedListIterator(self.head)
    
    def __str__(self) -> str:
        """
        String representation of the linked list.

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
        return " -> ".join(nodes) + " -> None"

    def insert_at_start(self, data: Any) -> None:
        """
        Insert a node at the beginning of the list.

        Args:
            data: Data to insert

        Complexity:
            Time: O(1)    - Constant time operation, just update head.
            Space: O(1)   - Only creates one new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: Any) -> None:
        """
        Insert a node at the end of the list.

        Args:
            data: Data to insert

        Complexity:
            Time: O(n)    - Must traverse to the end of the list.
            Space: O(1)   - Only creates one new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_after_node(self, prev_node_data: Any, data: Any) -> None:
        """
        Insert a node after a node with specific data.

        Args:
            prev_node_data: Data of the node after which to insert
            data: Data to insert

        Complexity:
            Time: O(n)    - May need to search through the list.
            Space: O(1)   - Only creates one new node.
        """
        temp = self.head
        while temp and temp.data != prev_node_data:
            temp = temp.next
        if not temp:
            print("Previous node not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

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
        prev = None
    
        while temp:
            if temp.data == key:
                if prev is None:
                    # Deleting the head node
                    self.head = temp.next
                else:
                    # Deleting a middle or end node
                    prev.next = temp.next
                return True
            prev = temp
            temp = temp.next
    
        return False

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
        Reverse the linked list in-place (iterative method).

        Complexity:
            Time: O(n)    - Traverses the list once, reversing links.
            Space: O(1)   - Only uses a few pointer variables.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next  # store next node
            current.next = prev  # reverse the link
            prev = current  # move prev forward
            current = next_node  # move current forward
        self.head = prev

    def print_list(self) -> None:
        """
        Print all elements of the linked list.

        Complexity:
            Time: O(n)    - Traverses all n nodes.
            Space: O(1)   - Only uses a pointer variable.
        """
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
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

    def insert_at_position(self, position: int, data: Any) -> None:
        """
        Insert a node at a given position (0-indexed).

        Args:
            position: Position where to insert (0 = head)
            data: Data to insert

        Complexity:
            Time: O(n)    - May need to traverse to position.
            Space: O(1)   - Only creates one new node.
        """
        if position < 0 or position > self.length():
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_start(data)
            return
        temp = self.head
        new_node = Node(data)
        for _ in range(position - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def has_cycle(self) -> bool:
        """
        Detect if the linked list has a cycle using Floyd's algorithm.

        Returns:
            bool: True if cycle exists, False otherwise

        Complexity:
            Time: O(n)    - Slow and fast pointers traverse the list.
            Space: O(1)   - Only uses two pointer variables.
        """
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_middle(self) -> Optional[Any]:
        """
        Find the middle element using slow/fast pointer technique.

        Returns:
            Optional[Any]: Data of middle node, None if list is empty

        Complexity:
            Time: O(n)    - Fast pointer traverses n nodes, slow pointer n/2.
            Space: O(1)   - Only uses two pointer variables.
        """
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    
    def to_list(self) -> list[Any]:
        """
        Convert linked list to Python list.

        Returns:
            list: List containing all elements in order

        Complexity:
            Time: O(n)    - Traverses all n nodes.
            Space: O(n)   - Creates a list of size n.
        """
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
    
    def clear(self) -> None:
        """
        Clear the linked list (remove all nodes).

        Complexity:
            Time: O(1)    - Just sets head to None.
            Space: O(1)   - No extra space used.
        """
        self.head = None


class LinkedListIterator:
    """
    Iterator for linked list to enable iteration with 'for' loops.
    """
    def __init__(self, start_node: Optional[Node]) -> None:
        """
        Initialize iterator with starting node.

        Args:
            start_node: First node to iterate from
        """
        self.current = start_node

    def __iter__(self) -> Iterator[Any]:
        """
        Return iterator object.

        Returns:
            Iterator: Self as iterator
        """
        return self

    def __next__(self) -> Any:
        """
        Get next element in iteration.

        Returns:
            Any: Data of next node

        Raises:
            StopIteration: When end of list is reached
        """
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Singly Linked List Demonstration")
    
    sll = SingleLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_start(0)
    sll.insert_after_node(2, 2.5)

    print("Original List:")
    sll.print_list()  # 0 -> 1 -> 2 -> 2.5 -> 3 -> None

    sll.reverse()
    print("\nReversed List:")
    sll.print_list()  # 3 -> 2.5 -> 2 -> 1 -> 0 -> None

    print(f"\nSearch 2: {sll.search(2)}")  # True
    sll.delete(2.5)
    print("After deleting 2.5:")
    sll.print_list()  # 3 -> 2 -> 1 -> 0 -> None

    print(f"\nLength of the List: {sll.length()}")  # 4

    print(f"Middle of the List: {sll.find_middle()}")  # 2

    print("\nIterating through the list:")
    for item in sll:
        print(item, end=" -> ")  # Outputs: 3 -> 2 -> 1 -> 0 ->
    print()

    print("\nPrinting list using __str__:")
    print(sll)

    print(f"\nList as Python list: {sll.to_list()}")

    print("\nClearing the list.")
    sll.clear()
    sll.print_list()
