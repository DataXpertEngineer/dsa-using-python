"""
Min Heap Implementation

A min heap is a complete binary tree where parent is always less than or equal to children.
Root contains the minimum element.

Properties:
- Complete binary tree
- Min-heap property: parent <= children
- Stored in array: parent at i, children at 2i+1 and 2i+2

Why Min Heap?
-------------
- O(1) access to minimum element
- O(log n) insert and extract
- Efficient for priority queues
- Foundation for many algorithms

Useful in:
- Priority queues
- Finding minimum elements
- Common interview problems
"""

from typing import Optional, Any, List


class MinHeap:
    """
    Min heap implementation from scratch.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty min heap.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty list.
        """
        self.heap: List[Any] = []
    
    def _parent(self, index: int) -> int:
        """Get parent index."""
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        """Get left child index."""
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        """Get right child index."""
        return 2 * index + 2
    
    def _swap(self, i: int, j: int) -> None:
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, index: int) -> None:
        """
        Move element up to maintain heap property.

        Complexity:
            Time: O(log n)  - Moves up at most log n levels.
            Space: O(1)    - Only uses variables.
        """
        while index > 0:
            parent = self._parent(index)
            if self.heap[parent] <= self.heap[index]:
                break
            self._swap(parent, index)
            index = parent
    
    def _heapify_down(self, index: int) -> None:
        """
        Move element down to maintain heap property.

        Complexity:
            Time: O(log n)  - Moves down at most log n levels.
            Space: O(1)    - Only uses variables.
        """
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest
    
    def insert(self, item: Any) -> None:
        """
        Insert element into min heap.

        Args:
            item: Element to insert

        Complexity:
            Time: O(log n)  - Heapify up operation.
            Space: O(1)    - Adds one element.
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self) -> Optional[Any]:
        """
        Remove and return minimum element.

        Returns:
            Optional[Any]: Minimum element, None if heap is empty

        Complexity:
            Time: O(log n)  - Heapify down operation.
            Space: O(1)    - Removes one element.
        """
        if self.is_empty():
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_val
    
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
        return self.heap[0]
    
    def is_empty(self) -> bool:
        """
        Check if heap is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return len(self.heap) == 0
    
    def size(self) -> int:
        """
        Get number of elements in heap.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Constant time length check.
            Space: O(1)   - No extra space used.
        """
        return len(self.heap)
    
    def build_heap(self, arr: List[Any]) -> None:
        """
        Build min heap from array in-place.

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
    
    def __str__(self) -> str:
        """
        String representation of heap.

        Returns:
            str: String showing heap elements
        """
        return f"MinHeap({self.heap})"


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Min Heap Demonstration")
    
    heap = MinHeap()
    print(f"Empty heap: {heap}")
    
    # Insert elements
    print("\nInserting: 5, 2, 8, 1, 9, 3")
    for num in [5, 2, 8, 1, 9, 3]:
        heap.insert(num)
        print(f"  After inserting {num}: {heap}, min: {heap.peek()}")
    
    # Extract minimum
    print("\nExtracting minimum:")
    while not heap.is_empty():
        min_val = heap.extract_min()
        print(f"  Extracted: {min_val}, Heap: {heap}")
    
    # Build heap from array
    print("\n" + "="*50)
    arr = [9, 5, 2, 7, 1, 6]
    print(f"Array: {arr}")
    heap.build_heap(arr)
    print(f"After build_heap: {heap}")

