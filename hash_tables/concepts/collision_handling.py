"""
Collision Handling in Hash Tables

When two keys hash to the same index, a collision occurs.
Different strategies handle collisions:

1. Chaining: Store multiple items in same bucket (linked list)
2. Open Addressing: Find next available slot
   - Linear Probing: h(k, i) = (h(k) + i) mod m
   - Quadratic Probing: h(k, i) = (h(k) + i²) mod m
   - Double Hashing: h(k, i) = (h1(k) + i * h2(k)) mod m

Why Collision Handling?
-----------------------
- Multiple keys can hash to same index
- Ensures all keys can be stored
- Affects hash table performance

Useful in:
- Hash table implementation
- Understanding hash table internals
- Common interview problems
"""

from typing import Optional, Any, List, Tuple


# ----------------------------------------------------------------------
# Chaining (Separate Chaining)
# ----------------------------------------------------------------------
class ChainingHashTable:
    """
    Hash table using chaining for collision resolution.
    Each bucket contains a list of (key, value) pairs.
    """
    
    def __init__(self, capacity: int = 16):
        """
        Initialize hash table with chaining.

        Args:
            capacity (int): Initial capacity

        Complexity:
            Time: O(n)     - Creates n empty lists.
            Space: O(n)   - Stores n empty lists.
        """
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0
    
    def _hash(self, key):
        """Hash function."""
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        """
        Insert key-value pair using chaining.

        Args:
            key: Key to insert
            value: Value associated with key

        Complexity:
            Time: O(1) average  - Hash + append to list.
            Space: O(1)       - Adds one pair.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new pair
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key) -> Optional[Any]:
        """
        Get value for key using chaining.

        Args:
            key: Key to search

        Returns:
            Optional[Any]: Value if found, None otherwise

        Complexity:
            Time: O(1) average  - Hash + search in bucket.
            Space: O(1)       - Only reads.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        """
        Delete key-value pair using chaining.

        Args:
            key: Key to delete

        Returns:
            bool: True if deleted, False if not found

        Complexity:
            Time: O(1) average  - Hash + remove from list.
            Space: O(1)       - Removes one pair.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False


# ----------------------------------------------------------------------
# Linear Probing (Open Addressing)
# ----------------------------------------------------------------------
class LinearProbingHashTable:
    """
    Hash table using linear probing for collision resolution.
    When collision occurs, check next slot sequentially.
    """
    
    def __init__(self, capacity: int = 16):
        """
        Initialize hash table with linear probing.

        Args:
            capacity (int): Initial capacity

        Complexity:
            Time: O(n)     - Creates array of size n.
            Space: O(n)   - Stores array.
        """
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
    
    def _hash(self, key):
        """Hash function."""
        return hash(key) % self.capacity
    
    def _find_slot(self, key) -> Optional[int]:
        """Find slot for key using linear probing."""
        index = self._hash(key)
        start = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return index
            index = (index + 1) % self.capacity
            if index == start:  # Table is full
                return None
        return index
    
    def insert(self, key, value):
        """
        Insert key-value pair using linear probing.

        Args:
            key: Key to insert
            value: Value associated with key

        Returns:
            bool: True if successful, False if table is full

        Complexity:
            Time: O(1) average  - Finds slot and inserts.
            Space: O(1)       - Adds one pair.
        """
        index = self._find_slot(key)
        if index is None:
            return False
        
        if self.table[index] is None:
            self.size += 1
        
        self.table[index] = (key, value)
        return True
    
    def get(self, key) -> Optional[Any]:
        """
        Get value for key using linear probing.

        Args:
            key: Key to search

        Returns:
            Optional[Any]: Value if found, None otherwise

        Complexity:
            Time: O(1) average  - Finds slot and retrieves.
            Space: O(1)       - Only reads.
        """
        index = self._hash(key)
        start = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
            if index == start:
                break
        
        return None


# ----------------------------------------------------------------------
# Quadratic Probing
# ----------------------------------------------------------------------
class QuadraticProbingHashTable:
    """
    Hash table using quadratic probing for collision resolution.
    When collision occurs, check slots at i² distance.
    """
    
    def __init__(self, capacity: int = 16):
        """
        Initialize hash table with quadratic probing.

        Args:
            capacity (int): Initial capacity

        Complexity:
            Time: O(n)     - Creates array.
            Space: O(n)   - Stores array.
        """
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
    
    def _hash(self, key):
        """Hash function."""
        return hash(key) % self.capacity
    
    def _probe(self, key, i: int):
        """Quadratic probing: h(k, i) = (h(k) + i²) mod m"""
        base = self._hash(key)
        return (base + i * i) % self.capacity
    
    def insert(self, key, value):
        """
        Insert key-value pair using quadratic probing.

        Args:
            key: Key to insert
            value: Value associated with key

        Returns:
            bool: True if successful, False if table is full

        Complexity:
            Time: O(1) average  - Finds slot and inserts.
            Space: O(1)       - Adds one pair.
        """
        for i in range(self.capacity):
            index = self._probe(key, i)
            if self.table[index] is None or self.table[index][0] == key:
                if self.table[index] is None:
                    self.size += 1
                self.table[index] = (key, value)
                return True
        return False  # Table is full
    
    def get(self, key) -> Optional[Any]:
        """
        Get value for key using quadratic probing.

        Args:
            key: Key to search

        Returns:
            Optional[Any]: Value if found, None otherwise

        Complexity:
            Time: O(1) average  - Finds slot and retrieves.
            Space: O(1)       - Only reads.
        """
        for i in range(self.capacity):
            index = self._probe(key, i)
            if self.table[index] is None:
                break
            if self.table[index][0] == key:
                return self.table[index][1]
        return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Collision Handling Demonstration")
    
    # Chaining
    print("Chaining (Separate Chaining):")
    ht_chain = ChainingHashTable(5)
    ht_chain.insert("apple", 1)
    ht_chain.insert("banana", 2)
    ht_chain.insert("cherry", 3)
    print(f"  get('apple'): {ht_chain.get('apple')}")
    print(f"  get('banana'): {ht_chain.get('banana')}")
    
    # Linear Probing
    print("\nLinear Probing:")
    ht_linear = LinearProbingHashTable(5)
    ht_linear.insert("apple", 1)
    ht_linear.insert("banana", 2)
    print(f"  get('apple'): {ht_linear.get('apple')}")
    print(f"  get('banana'): {ht_linear.get('banana')}")
    
    # Quadratic Probing
    print("\nQuadratic Probing:")
    ht_quad = QuadraticProbingHashTable(5)
    ht_quad.insert("apple", 1)
    ht_quad.insert("banana", 2)
    print(f"  get('apple'): {ht_quad.get('apple')}")
    print(f"  get('banana'): {ht_quad.get('banana')}")

