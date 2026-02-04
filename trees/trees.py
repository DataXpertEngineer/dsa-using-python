"""
Tree Data Structure in Python

A tree is a hierarchical data structure consisting of nodes connected by edges.
Each tree has a root node, and nodes can have children, forming a parent-child relationship.

Structure:
    Root
    ├── Child 1
    │   ├── Grandchild 1
    │   └── Grandchild 2
    └── Child 2

Characteristics:
- Hierarchical structure
- One root node
- Each node (except root) has exactly one parent
- Nodes can have zero or more children
- No cycles (acyclic)

Useful in:
- Hierarchical data representation
- File systems
- Database indexing
- Expression parsing
- Common interview problems
"""

from typing import Optional, Any, List


class TreeNode:
    """
    Node class for binary tree.
    
    A binary tree node has:
    - data: Value stored in the node
    - left: Reference to left child
    - right: Reference to right child
    """
    
    def __init__(self, val=0, left: Optional['TreeNode'] = None, 
                 right: Optional['TreeNode'] = None):
        """
        Initialize a tree node.

        Args:
            val: Value to store in the node
            left: Left child node
            right: Right child node

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates one node.
        """
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        """String representation of node."""
        return str(self.val)
    
    def __repr__(self):
        """Official string representation."""
        return f"TreeNode({self.val})"


class Tree:
    """
    Binary tree implementation.
    """
    
    def __init__(self, root: Optional[TreeNode] = None):
        """
        Initialize tree with root node.

        Args:
            root (Optional[TreeNode]): Root node of the tree

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Stores root reference.
        """
        self.root = root
    
    def is_empty(self):
        """
        Check if tree is empty.

        Returns:
            bool: True if tree is empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return self.root is None
    
    def size(self):
        """
        Get number of nodes in tree.

        Returns:
            int: Number of nodes

        Complexity:
            Time: O(n)     - Traverses all nodes.
            Space: O(h)   - Recursion stack depth (h = height).
        """
        def count_nodes(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        return count_nodes(self.root)


# ----------------------------------------------------------------------
# Tree Properties Summary
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Tree Data Structure Demonstration")
    
    # Create a simple tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    tree = Tree(root)
    print(f"Tree size: {tree.size()}")
    print(f"Is empty: {tree.is_empty()}")
    
    print("\n" + "="*60)
    print("TREE CONCEPTS SUMMARY")
    print("="*60)
    print("""
Tree Properties:
- Root: Topmost node (no parent)
- Leaf: Node with no children
- Internal Node: Node with at least one child
- Depth: Distance from root to node
- Height: Maximum depth of any node
- Level: Set of nodes at same depth
- Degree: Number of children a node has
- Path: Sequence of nodes from one to another
- Ancestor: Node on path from root to current node
- Descendant: Node reachable from current node
- Sibling: Nodes with same parent

Binary Tree:
- Each node has at most 2 children
- Left child and right child
- Full: Every node has 0 or 2 children
- Complete: All levels filled except last, filled left to right
- Perfect: All internal nodes have 2 children, all leaves at same level
- Balanced: Height difference between subtrees ≤ 1
""")

