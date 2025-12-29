"""
Diameter of a Tree

Find the diameter (longest path between any two nodes) of a binary tree.

Definition:
- Diameter: Number of edges in longest path between any two nodes
- Path may or may not pass through root

Why Calculate Diameter?
------------------------
- Important tree property
- Measures tree "width"
- Used in tree analysis
- Common interview problem

Useful in:
- Tree analysis
- Network problems
- Common interview problems
"""

from typing import Optional, Tuple
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Diameter of Tree (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def tree_diameter(root: Optional[TreeNode]) -> int:
    """
    Calculate diameter of binary tree.

    Algorithm:
    1. For each node, calculate:
       - Height of left subtree
       - Height of right subtree
       - Diameter passing through this node = left_height + right_height + 2
    2. Return maximum diameter

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Diameter of tree

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth.
    """
    max_diameter = 0
    
    def height_and_diameter(node: Optional[TreeNode]) -> int:
        nonlocal max_diameter
        
        if not node:
            return -1
        
        left_height = height_and_diameter(node.left)
        right_height = height_and_diameter(node.right)
        
        # Diameter passing through this node
        diameter_through_node = left_height + right_height + 2
        max_diameter = max(max_diameter, diameter_through_node)
        
        # Return height of subtree
        return 1 + max(left_height, right_height)
    
    height_and_diameter(root)
    return max_diameter


# ----------------------------------------------------------------------
# Diameter - Alternative Implementation
# ----------------------------------------------------------------------
def tree_diameter_alt(root: Optional[TreeNode]) -> int:
    """
    Calculate diameter using separate height function.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Diameter of tree

    Complexity:
        Time: O(n²)    - Calculates height for each node.
        Space: O(h)   - Recursion stack.
    """
    if not root:
        return 0
    
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        return 1 + max(height(node.left), height(node.right))
    
    # Diameter passing through root
    left_height = height(root.left)
    right_height = height(root.right)
    diameter_through_root = left_height + right_height + 2
    
    # Diameter in subtrees
    left_diameter = tree_diameter_alt(root.left)
    right_diameter = tree_diameter_alt(root.right)
    
    return max(diameter_through_root, left_diameter, right_diameter)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Tree Diameter Demonstration")
    
    # Create tree:    1
    #                / \
    #               2   3
    #              / \
    #             4   5
    #            /
    #           6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    
    diameter = tree_diameter(root)
    print(f"Tree diameter: {diameter}")
    print("Explanation: Longest path is 6→4→2→5 (3 edges)")

