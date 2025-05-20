class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def __str__(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        return " -> ".join(nodes) + " -> None"

    # Insert at the beginning
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert after a specific node (by value)
    def insert_after_node(self, prev_node_data, data):
        temp = self.head
        while temp and temp.data != prev_node_data:
            temp = temp.next
        if not temp:
            print("Previous node not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete(self, key):
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
                print(f"Deleted {key}")
                return
            prev = temp
            temp = temp.next
    
        print("Value not found.")


    # Search for a value (iterative)
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Reverse the linked list (iterative method)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # store next node
            current.next = prev  # reverse the link
            prev = current  # move prev forward
            current = next_node  # move current forward
        self.head = prev

    # Print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

    # Length of the linked list
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Insert at a given position
    def insert_at_position(self, position, data):
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

    # Detect a cycle in the linked list
    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Find the middle element
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    
    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
    
    def clear(self):
        self.head = None


class LinkedListIterator:
    def __init__(self, start_node):
        self.current = start_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration  # End of iteration
        data = self.current.data
        self.current = self.current.next
        return data


# Example usage
if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_start(0)
    sll.insert_after_node(2, 2.5)

    print("Original List:")
    sll.print_list()  # 0 -> 1 -> 2 -> 2.5 -> 3 -> None

    sll.reverse()
    print("Reversed List:")
    sll.print_list()  # 3 -> 2.5 -> 2 -> 1 -> 0 -> None

    print("Search 2:", sll.search(2))  # True
    sll.delete(2.5)
    sll.print_list()  # 3 -> 2 -> 1 -> 0 -> None

    print("Length of the List:", sll.length())  # 4

    print("Middle of the List:", sll.find_middle())  # 2

    print("Iterating through the list:")
    for item in sll:
        print(item, end=" -> ")  # Outputs: 3 -> 2 -> 1 -> 0 ->

    print("Printing list using __str__:")
    print(sll)

    print("List as Python list:", sll.to_list())

    print("Clearing the list.")
    sll.clear()
    sll.print_list()
