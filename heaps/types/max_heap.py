"""
Max Heap Implementation

A max heap is a complete binary tree where parent is always greater than or equal to children.
Root contains the maximum element.

Properties:
- Complete binary tree
- Max-heap property: parent >= children
- Stored in array: parent at i, children at 2i+1 and 2i+2

Why Max Heap?
-------------
- O(1) access to maximum element
- O(log n) insert and extract
- Efficient for priority queues
- Foundation for many algorithms

Useful in:
- Priority queues
- Finding maximum elements
- Common interview problems
"""

from typing import Optional, Any, List


class MaxHeap:
    """
    Max heap implementation from scratch.
    """
    
    def __init__(self):
        """
        Initialize an empty max heap.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.heap = []
    
    def _parent(self, index: int):
        """Get parent index."""
        return (index - 1) // 2
    
    def _left_child(self, index: int):
        """Get left child index."""
        return 2 * index + 1
    
    def _right_child(self, index: int):
        """Get right child index."""
        return 2 * index + 2
    
    def _swap(self, i: int, j: int):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, index: int):
        """
        Move element up to maintain heap property.

        Complexity:
            Time: O(log n)  - Moves up at most log n levels.
            Space: O(1)    - Only uses variables.
        """
        while index > 0:
            parent = self._parent(index)
            if self.heap[parent] >= self.heap[index]:
                break
            self._swap(parent, index)
            index = parent
    
    def _heapify_down(self, index: int):
        """
        Move element down to maintain heap property.

        Complexity:
            Time: O(log n)  - Moves down at most log n levels.
            Space: O(1)    - Only uses variables.
        """
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest == index:
                break
            
            self._swap(index, largest)
            index = largest
    
    def insert(self, item):
        """
        Insert element into max heap.

        Args:
            item: Element to insert

        Complexity:
            Time: O(log n)  - Heapify up operation.
            Space: O(1)    - Adds one element.
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self) -> Optional[Any]:
        """
        Remove and return maximum element.

        Returns:
            Optional[Any]: Maximum element, None if heap is empty

        Complexity:
            Time: O(log n)  - Heapify down operation.
            Space: O(1)    - Removes one element.
        """
        if self.is_empty():
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return max_val
    
    def peek(self) -> Optional[Any]:
        """
        Return maximum element without removing.

        Returns:
            Optional[Any]: Maximum element, None if heap is empty

        Complexity:
            Time: O(1)     - Direct access to root.
            Space: O(1)   - Only reads.
        """
        if self.is_empty():
            return None
        return self.heap[0]
    
    def is_empty(self):
        """
        Check if heap is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.heap) == 0
    
    def size(self):
        """
        Get number of elements in heap.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.heap)
    
    def build_heap(self, arr: List[Any]):
        """
        Build max heap from array in-place.

        Args:
            arr (List[Any]): Array to heapify

        Complexity:
            Time: O(n)     - Linear time heap construction.
            Space: O(1)   - In-place operation.
        """
        self.heap = arr
        # Start from last non-leaf node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def __str__(self):
        """
        String representation of heap.

        Returns:
            str: String showing heap elements
        """
        return f"MaxHeap({self.heap})"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Max Heap Demonstration")
    
    heap = MaxHeap()
    print(f"Empty heap: {heap}")
    
    # Insert elements
    print("\nInserting: 5, 2, 8, 1, 9, 3")
    for num in [5, 2, 8, 1, 9, 3]:
        heap.insert(num)
        print(f"  After inserting {num}: {heap}, max: {heap.peek()}")
    
    # Extract maximum
    print("\nExtracting maximum:")
    while not heap.is_empty():
        max_val = heap.extract_max()
        print(f"  Extracted: {max_val}, Heap: {heap}")
    
    # Build heap from array
    print("\n" + "="*50)
    arr = [9, 5, 2, 7, 1, 6]
    print(f"Array: {arr}")
    heap.build_heap(arr)
    print(f"After build_heap: {heap}")

