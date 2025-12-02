# Linked Lists in Python (Data Structures & Algorithms)

This folder focuses on **linked lists** as a fundamental data structure and how they are implemented in Python.

You'll learn:

- The **DSA concept** of linked lists (independent of any language)
- Types of linked lists (singly, doubly, circular)
- How linked lists are **implemented in Python**
- Linked list operations and their complexities
- Common techniques and algorithms for linked lists

---

## A. Linked Lists (DSA Concept)

### 1. What is a Linked List?

A **linked list** is a linear data structure where elements (nodes) are not stored in contiguous memory locations. Instead, each node contains:

- **Data**: The value stored in the node
- **Pointer/Reference**: Address of the next node (and previous node in doubly linked lists)

Think of a linked list as a chain:

- Each link (node) connects to the next link
- You must follow the chain from the beginning to reach a specific link
- No direct access to middle elements (unlike arrays)

**Structure:**
```
Node: [data | next] -> Node: [data | next] -> ... -> None
```

---

### 2. Types of Linked Lists

#### Singly Linked List

- Each node points only to the next node
- Can traverse only in forward direction
- Last node points to `None`

**Structure:**
```
head -> Node1 -> Node2 -> Node3 -> None
```

#### Doubly Linked List

- Each node points to both next and previous nodes
- Can traverse in both directions
- More memory per node (stores two pointers)
- First node's `prev` and last node's `next` are `None`

**Structure:**
```
None <-> Node1 <-> Node2 <-> Node3 <-> None
```

#### Circular Linked List

- Last node points back to the first node
- No explicit `None` termination
- Can start traversal from any node
- Can be singly or doubly linked

**Structure:**
```
Node1 -> Node2 -> Node3 -> (back to Node1)
```

---

### 3. Linked Lists vs Arrays

| Feature | Arrays | Linked Lists |
|---------|--------|--------------|
| **Memory** | Contiguous | Non-contiguous |
| **Access** | Random access O(1) | Sequential access O(n) |
| **Insertion at start** | O(n) | O(1) |
| **Insertion at end** | O(1) amortized | O(n) |
| **Deletion at start** | O(n) | O(1) |
| **Memory overhead** | Minimal | Extra pointer(s) per node |
| **Size** | Fixed (static) or dynamic | Dynamic |

---

### 4. Strengths & Weaknesses of Linked Lists

#### Strengths

- **Dynamic size**: Grows and shrinks as needed
- **Efficient insertion/deletion**: O(1) at head (singly) or both ends (doubly)
- **No memory waste**: Allocates only what's needed
- **No resizing overhead**: Unlike dynamic arrays
- **Flexible**: Easy to insert/delete in middle (if you have node reference)

#### Weaknesses

- **No random access**: Must traverse from head to reach element → O(n)
- **Extra memory**: Stores pointers (one for singly, two for doubly)
- **Cache unfriendly**: Nodes may be scattered in memory
- **Reverse traversal**: Difficult in singly linked lists (need doubly linked)

---

### 5. Time & Space Complexity Summary

| Operation | Singly Linked List | Doubly Linked List |
|-----------|-------------------|-------------------|
| Access by index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n) | O(1) |
| Insert at position | O(n) | O(n) |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n) | O(1) |
| Delete by value | O(n) | O(n) |
| Delete by node reference | O(n) | O(1) |
| Reverse | O(n) | O(n) |
| Space | O(n) | O(n) |

---

## B. How Linked Lists Are Implemented in Python

In Python, linked lists are implemented using **classes** to represent nodes and the list itself.

### 1. Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to next node
```

**Key Points:**

- `data`: Stores the value
- `next`: Reference to the next node (pointer in other languages)
- In Python, references are similar to pointers but managed by the interpreter

### 2. Linked List Class

```python
class SingleLinkedList:
    def __init__(self):
        self.head = None  # Points to first node
```

**Key Points:**

- `head`: Reference to the first node
- If `head` is `None`, the list is empty
- Operations manipulate `head` and node references

### 3. Memory Representation

**In Memory:**
```
head -> [Node1 at 0x1000] -> [Node2 at 0x2000] -> [Node3 at 0x3000] -> None
         data: 10            data: 20            data: 30
         next: 0x2000        next: 0x3000        next: None
```

**In Python:**
- Objects are stored on the heap
- Variables hold references (like pointers)
- Garbage collector manages memory

---

### 4. Common Operations

#### Insertion at Head

```python
def insert_at_start(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

**Complexity:** O(1) - Just update head reference

#### Insertion at Tail

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new_node
```

**Complexity:** O(n) - Must traverse to end

#### Deletion

```python
def delete(self, key):
    temp = self.head
    prev = None
    while temp:
        if temp.data == key:
            if prev is None:
                self.head = temp.next
            else:
                prev.next = temp.next
            return
        prev = temp
        temp = temp.next
```

**Complexity:** O(n) - May need to traverse entire list

---

## C. Common Techniques

### 1. Slow-Fast Pointer (Floyd's Algorithm)

**Use Cases:**
- Detect cycle
- Find middle element
- Find k-th node from end

**How it works:**
- Two pointers move at different speeds
- Slow pointer: moves 1 step at a time
- Fast pointer: moves 2 steps at a time
- They meet if there's a cycle, or fast reaches end

### 2. Dummy Node Technique

**Use Cases:**
- Simplify head operations
- Merge sorted lists
- Remove elements

**How it works:**
- Create a temporary node before head
- Perform operations uniformly
- Return `dummy.next` as new head

### 3. Reversal Techniques

**Iterative:**
- Use three pointers: prev, current, next
- Reverse links one by one

**Recursive:**
- Recursively reverse rest of list
- Fix current node's pointer

---

## D. When to Use Linked Lists

**Use linked lists when:**
- Size is unknown or changes frequently
- Frequent insertions/deletions at beginning
- Implementing stacks, queues, or other data structures
- Memory is a concern and you want dynamic allocation

**Use arrays when:**
- Random access is needed
- Size is known or relatively fixed
- Cache performance matters
- You need to access elements by index frequently

---

## E. Folder Structure

```
linked_lists/
├── singly_linked_list.py          # Core singly linked list operations
├── doubly_linked_list.py           # Core doubly linked list operations
├── circular_linked_list.py         # Core circular linked list operations
│
├── techniques/                     # Linked list techniques
│   ├── slow_fast_pointer.py        # Floyd's algorithm, middle node, etc.
│   ├── reverse_linked_list.py      # Reversal using pointers
│   ├── dummy_node_technique.py     # Dummy node technique
│   └── merge_sorted_lists.py       # Merge two sorted lists
│
├── algorithms/                     # Linked list algorithms
│   ├── sorting.py                  # Sorting linked lists (merge sort)
│   ├── searching.py                # Search in linked lists
│   └── divide_and_conquer.py       # Divide & conquer problems
│
└── interview_problems/             # Common coding problems
    ├── detect_cycle.py             # Detect loop using Floyd's
    ├── remove_nth_node.py          # Remove nth node from end
    ├── add_two_numbers.py           # Add numbers represented as lists
    ├── reorder_list.py              # Reorder list in specific pattern
    └── intersection_of_lists.py     # Find intersection of two lists
```

---

## Summary

- Linked lists provide **dynamic size** and **efficient insertion/deletion** at head
- **No random access** - must traverse from head
- **Extra memory** for storing pointers
- **Common techniques**: Slow-fast pointers, dummy nodes, reversal
- **Use when**: Size is dynamic, frequent head operations, or implementing other structures

Now you can explore the implementations in this folder to see these concepts in action!

