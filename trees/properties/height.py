"""
Height of a Tree

Calculate the height (maximum depth) of a binary tree.

Definition:
- Height: Maximum number of edges from root to any leaf
- Depth: Number of edges from root to a node
- Height of empty tree: -1 (or 0 if counting nodes)

Why Calculate Height?
---------------------
- Important tree property
- Used in balancing checks
- Needed for many tree algorithms
- Common interview problem

Useful in:
- Tree balancing
- Tree analysis
- Common interview problems
"""

from typing import Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Height of Tree (Language-agnostic)
# ----------------------------------------------------------------------
def tree_height(root: Optional[TreeNode]) -> int:
    """
    Calculate height of binary tree.

    Height = maximum depth of any node
    Empty tree has height -1

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Height of tree (-1 for empty tree)

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth (h = height).
    """
    if not root:
        return -1
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)


# ----------------------------------------------------------------------
# Height of Tree (Counting Nodes)
# ----------------------------------------------------------------------
def tree_height_nodes(root: Optional[TreeNode]) -> int:
    """
    Calculate height counting nodes (not edges).

    Empty tree has height 0

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Height counting nodes

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth.
    """
    if not root:
        return 0
    
    left_height = tree_height_nodes(root.left)
    right_height = tree_height_nodes(root.right)
    
    return 1 + max(left_height, right_height)


# ----------------------------------------------------------------------
# Depth of Node
# ----------------------------------------------------------------------
def node_depth(root: Optional[TreeNode], target: int) -> int:
    """
    Find depth of a specific node.

    Args:
        root (Optional[TreeNode]): Root of the tree
        target (int): Target node value

    Returns:
        int: Depth of node (-1 if not found)

    Complexity:
        Time: O(n)     - Visits nodes until target found.
        Space: O(h)   - Recursion stack depth.
    """
    def find_depth(node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return -1
        
        if node.val == target:
            return depth
        
        left = find_depth(node.left, depth + 1)
        if left != -1:
            return left
        
        return find_depth(node.right, depth + 1)
    
    return find_depth(root, 0)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Tree Height Demonstration")
    
    # Create tree:    1
    #                / \
    #               2   3
    #              / \
    #             4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    height = tree_height(root)
    print(f"Tree height (edges): {height}")
    print("Explanation: Longest path has 2 edges (1→2→4)")
    
    height_nodes = tree_height_nodes(root)
    print(f"Tree height (nodes): {height_nodes}")
    
    # Depth of node
    print("\n" + "="*50)
    depth = node_depth(root, 5)
    print(f"Depth of node 5: {depth}")

