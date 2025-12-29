"""
Hash Table Data Structure in Python

A hash table (hash map) is a data structure that implements an associative array
or dictionary, mapping keys to values using a hash function.

Structure:
    Key -> Hash Function -> Index -> Bucket -> [Key, Value]

Characteristics:
- Average O(1) time for insert, delete, search
- Uses hash function to compute index
- Handles collisions (multiple keys map to same index)
- Dynamic resizing for efficiency

Useful in:
- Fast lookups
- Counting frequencies
- Caching
- Common interview problems
"""

from typing import Optional, Any, Dict, List


class HashTable:
    """
    Hash table implementation using Python dictionary (built-in hash table).
    
    Python's dict is implemented as a hash table, so this is a wrapper
    demonstrating hash table operations.
    """
    
    def __init__(self, initial_capacity: int = 16) -> None:
        """
        Initialize an empty hash table.

        Args:
            initial_capacity (int): Initial capacity of hash table

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty dictionary.
        """
        self.table: Dict[Any, Any] = {}
        self.capacity = initial_capacity
        self.size = 0
    
    def insert(self, key: Any, value: Any) -> None:
        """
        Insert or update key-value pair in hash table.

        Args:
            key: Key to insert
            value: Value associated with key

        Complexity:
            Time: O(1) average  - Hash function + dictionary insert.
            Space: O(1)        - Adds one key-value pair.
        """
        if key not in self.table:
            self.size += 1
        self.table[key] = value
    
    def get(self, key: Any) -> Optional[Any]:
        """
        Get value associated with key.

        Args:
            key: Key to search for

        Returns:
            Optional[Any]: Value if key exists, None otherwise

        Complexity:
            Time: O(1) average  - Hash function + dictionary lookup.
            Space: O(1)        - Only reads.
        """
        return self.table.get(key)
    
    def delete(self, key: Any) -> bool:
        """
        Delete key-value pair from hash table.

        Args:
            key: Key to delete

        Returns:
            bool: True if key was deleted, False if key not found

        Complexity:
            Time: O(1) average  - Hash function + dictionary delete.
            Space: O(1)        - Removes one key-value pair.
        """
        if key in self.table:
            del self.table[key]
            self.size -= 1
            return True
        return False
    
    def contains(self, key: Any) -> bool:
        """
        Check if key exists in hash table.

        Args:
            key: Key to check

        Returns:
            bool: True if key exists, False otherwise

        Complexity:
            Time: O(1) average  - Hash function + dictionary lookup.
            Space: O(1)        - Only reads.
        """
        return key in self.table
    
    def size(self) -> int:
        """
        Get number of key-value pairs in hash table.

        Returns:
            int: Number of elements

        Complexity:
            Time: O(1)     - Returns stored size.
            Space: O(1)   - No extra space used.
        """
        return self.size
    
    def is_empty(self) -> bool:
        """
        Check if hash table is empty.

        Returns:
            bool: True if empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return self.size == 0
    
    def keys(self) -> List[Any]:
        """
        Get all keys in hash table.

        Returns:
            List[Any]: List of all keys

        Complexity:
            Time: O(n)     - Iterates through all keys.
            Space: O(n)   - Stores all keys.
        """
        return list(self.table.keys())
    
    def values(self) -> List[Any]:
        """
        Get all values in hash table.

        Returns:
            List[Any]: List of all values

        Complexity:
            Time: O(n)     - Iterates through all values.
            Space: O(n)   - Stores all values.
        """
        return list(self.table.values())
    
    def clear(self) -> None:
        """
        Remove all key-value pairs from hash table.

        Complexity:
            Time: O(1)     - Clears dictionary.
            Space: O(1)   - No extra space used.
        """
        self.table.clear()
        self.size = 0
    
    def __str__(self) -> str:
        """
        String representation of hash table.

        Returns:
            str: String showing all key-value pairs
        """
        return f"HashTable({self.table})"
    
    def __repr__(self) -> str:
        """
        Official string representation of hash table.

        Returns:
            str: Official representation
        """
        return self.__str__()


# ----------------------------------------------------------------------
# Hash Table Operations Summary
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Hash Table Operations Demonstration")
    
    # Create hash table
    ht = HashTable()
    print(f"Empty hash table: {ht}")
    print(f"Is empty: {ht.is_empty()}")
    print(f"Size: {ht.size}")
    
    # Insert elements
    print("\nInserting key-value pairs:")
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    print(f"Hash table: {ht}")
    print(f"Size: {ht.size}")
    
    # Get values
    print("\nGetting values:")
    print(f"  get('name'): {ht.get('name')}")
    print(f"  get('age'): {ht.get('age')}")
    print(f"  get('country'): {ht.get('country')}")
    
    # Check contains
    print("\nChecking contains:")
    print(f"  contains('city'): {ht.contains('city')}")
    print(f"  contains('country'): {ht.contains('country')}")
    
    # Delete
    print("\nDeleting 'age':")
    print(f"  delete('age'): {ht.delete('age')}")
    print(f"  Hash table: {ht}")
    print(f"  Size: {ht.size}")
    
    # Keys and values
    print(f"\nKeys: {ht.keys()}")
    print(f"Values: {ht.values()}")
    
    print("\n" + "="*60)
    print("HASH TABLE OPERATIONS COMPLEXITY SUMMARY")
    print("="*60)
    print("""
Operation          Time Complexity    Space Complexity
------------------------------------------------------
insert()           O(1) average       O(1)
get()              O(1) average       O(1)
delete()           O(1) average       O(1)
contains()         O(1) average       O(1)
size()             O(1)               O(1)
is_empty()         O(1)               O(1)
keys()             O(n)               O(n)
values()           O(n)               O(n)
clear()            O(1)               O(1)

Note: Average case assumes good hash function and load factor.
      Worst case can be O(n) if all keys hash to same bucket.
""")

