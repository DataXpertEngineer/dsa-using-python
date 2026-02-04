"""
Heap Data Structure in Python

A heap is a complete binary tree that satisfies the heap property.
Heaps are used to implement priority queues efficiently.

Structure:
    Complete binary tree stored in array
    Parent at index i, children at 2i+1 and 2i+2

Characteristics:
- Complete binary tree structure
- Heap property (min-heap or max-heap)
- Efficient insert and extract operations
- O(log n) for insert/extract, O(1) for peek

Useful in:
- Priority queues
- Heap sort
- Finding kth largest/smallest
- Graph algorithms (Dijkstra's, Prim's)
- Common interview problems
"""

from typing import Optional, Any, List
import heapq


class Heap:
    """
    Heap implementation using Python's heapq module (min-heap).
    
    Python's heapq provides a min-heap implementation.
    For max-heap, negate values or use custom comparator.
    """
    
    def __init__(self):
        """
        Initialize an empty heap.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.items = []
    
    def insert(self, item):
        """
        Insert element into heap.

        Args:
            item: Element to insert

        Complexity:
            Time: O(log n)  - Heapify up operation.
            Space: O(1)    - Adds one element.
        """
        heapq.heappush(self.items, item)
    
    def extract(self) -> Optional[Any]:
        """
        Remove and return minimum element (min-heap).

        Returns:
            Optional[Any]: Minimum element, None if heap is empty

        Complexity:
            Time: O(log n)  - Heapify down operation.
            Space: O(1)    - Removes one element.
        """
        if self.is_empty():
            return None
        return heapq.heappop(self.items)
    
    def peek(self) -> Optional[Any]:
        """
        Return minimum element without removing.

        Returns:
            Optional[Any]: Minimum element, None if heap is empty

        Complexity:
            Time: O(1)     - Direct access to root.
            Space: O(1)   - Only reads.
        """
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """
        Check if heap is empty.

        Returns:
            bool: True if heap is empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get number of elements in heap.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.items)
    
    def heapify(self, arr: List[Any]):
        """
        Build heap from array in-place.

        Args:
            arr (List[Any]): Array to heapify

        Complexity:
            Time: O(n)     - Linear time heap construction.
            Space: O(1)   - In-place operation.
        """
        self.items = arr
        heapq.heapify(self.items)
    
    def clear(self):
        """
        Remove all elements from heap.

        Complexity:
            Time: O(1)     - Clears the list.
            Space: O(1)   - No extra space used.
        """
        self.items.clear()
    
    def __str__(self):
        """
        String representation of heap.

        Returns:
            str: String showing heap elements
        """
        return f"Heap({self.items})"
    
    def __repr__(self):
        """
        Official string representation of heap.

        Returns:
            str: Official representation
        """
        return self.__str__()


# ----------------------------------------------------------------------
# Heap Operations Summary
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Heap Operations Demonstration")
    
    # Create heap
    heap = Heap()
    print(f"Empty heap: {heap}")
    print(f"Is empty: {heap.is_empty()}")
    print(f"Size: {heap.size()}")
    
    # Insert elements
    print("\nInserting elements: 5, 2, 8, 1, 9, 3")
    for num in [5, 2, 8, 1, 9, 3]:
        heap.insert(num)
    print(f"Heap: {heap}")
    print(f"Size: {heap.size()}")
    print(f"Minimum element (peek): {heap.peek()}")
    
    # Extract elements
    print("\nExtracting elements:")
    while not heap.is_empty():
        print(f"  Extracted: {heap.extract()}, Heap: {heap}")
    
    # Heapify
    print("\n" + "="*50)
    arr = [9, 5, 2, 7, 1, 6]
    print(f"Array: {arr}")
    heap.heapify(arr)
    print(f"After heapify: {heap}")
    
    print("\n" + "="*60)
    print("HEAP OPERATIONS COMPLEXITY SUMMARY")
    print("="*60)
    print("""
Operation          Time Complexity    Space Complexity
------------------------------------------------------
insert()           O(log n)           O(1)
extract()          O(log n)           O(1)
peek()             O(1)              O(1)
is_empty()         O(1)              O(1)
size()             O(1)              O(1)
heapify()          O(n)               O(1)
clear()            O(1)              O(1)

Where n is the number of elements in the heap.
Heap maintains complete binary tree structure.
""")

