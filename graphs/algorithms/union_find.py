"""
Union-Find (Disjoint Set Union) Data Structure

Efficient data structure for tracking disjoint sets and detecting cycles.

Operations:
1. Find: Find root of element's set
2. Union: Merge two sets

Why Union-Find?
---------------
- O(α(n)) amortized time per operation (almost constant)
- Essential for Kruskal's MST
- Used in cycle detection
- Foundation for many algorithms

Useful in:
- Kruskal's MST algorithm
- Cycle detection
- Connected components
- Common interview problems
"""

from typing import Dict, List, Optional


# ----------------------------------------------------------------------
# Union-Find - Basic Implementation (Language-agnostic)
# ----------------------------------------------------------------------
class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.
    
    Supports:
    - find(x): Find root of x's set
    - union(x, y): Merge sets containing x and y
    - connected(x, y): Check if x and y in same set
    """
    
    def __init__(self, elements: List[int]):
        """
        Initialize union-find with elements.

        Args:
            elements (List[int]): List of elements

        Complexity:
            Time: O(n)     - Initialize n elements.
            Space: O(n)   - Parent and rank arrays.
        """
        self.parent: Dict[int, int] = {x: x for x in elements}
        self.rank: Dict[int, int] = {x: 0 for x in elements}
        self.count = len(elements)
    
    def find(self, x: int):
        """
        Find root of x's set with path compression.

        Args:
            x (int): Element

        Returns:
            int: Root of x's set

        Complexity:
            Time: O(α(n))  - Amortized nearly constant (inverse Ackermann).
            Space: O(1)   - Only uses variables.
        """
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        """
        Union sets containing x and y.

        Args:
            x (int): First element
            y (int): Second element

        Returns:
            bool: True if unioned, False if already in same set

        Complexity:
            Time: O(α(n))  - Amortized nearly constant.
            Space: O(1)   - Only uses variables.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x: int, y: int):
        """
        Check if x and y are in same set.

        Args:
            x (int): First element
            y (int): Second element

        Returns:
            bool: True if in same set

        Complexity:
            Time: O(α(n))  - Two find operations.
            Space: O(1)   - Only uses variables.
        """
        return self.find(x) == self.find(y)
    
    def get_count(self):
        """
        Get number of disjoint sets.

        Returns:
            int: Number of sets

        Complexity:
            Time: O(1)     - Constant time access.
            Space: O(1)   - Only uses variables.
        """
        return self.count


# ----------------------------------------------------------------------
# Union-Find - Without Rank (Simpler)
# ----------------------------------------------------------------------
class UnionFindSimple:
    """
    Simplified union-find without rank optimization.
    """
    
    def __init__(self, elements: List[int]):
        """Initialize union-find."""
        self.parent: Dict[int, int] = {x: x for x in elements}
        self.count = len(elements)
    
    def find(self, x: int):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        """Union sets (always attach x to y)."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        self.parent[root_x] = root_y
        self.count -= 1
        return True
    
    def connected(self, x: int, y: int):
        """Check if connected."""
        return self.find(x) == self.find(y)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Union-Find Data Structure Demonstration")
    
    elements = [0, 1, 2, 3, 4]
    uf = UnionFind(elements)
    
    print("Initial state:")
    print(f"  Number of sets: {uf.get_count()}")
    
    print("\nUnion operations:")
    print(f"  union(0, 1): {uf.union(0, 1)}")
    print(f"  union(2, 3): {uf.union(2, 3)}")
    print(f"  union(1, 2): {uf.union(1, 2)}")
    
    print(f"\nNumber of sets: {uf.get_count()}")
    print(f"connected(0, 3): {uf.connected(0, 3)}")
    print(f"connected(0, 4): {uf.connected(0, 4)}")
    
    print("\n" + "="*50)
    print("UNION-FIND CONCEPTS SUMMARY")
    print("="*50)
    print("""
Union-Find Operations:
- find(x): Find root of x's set
- union(x, y): Merge sets containing x and y
- connected(x, y): Check if x and y in same set

Optimizations:
1. Path Compression: Flatten tree during find
2. Union by Rank: Attach smaller tree to larger

Time Complexity:
- Without optimizations: O(n) worst case
- With optimizations: O(α(n)) amortized (nearly constant)

Applications:
- Kruskal's MST algorithm
- Cycle detection
- Connected components
- Network connectivity
""")

