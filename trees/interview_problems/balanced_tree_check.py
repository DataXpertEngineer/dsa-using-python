"""
Balanced Binary Tree Check

Check if a binary tree is height-balanced.

Definition:
- Balanced: Height difference between left and right subtrees ≤ 1
- Applies recursively to all nodes

Why Check Balance?
------------------
- Important for tree performance
- Unbalanced trees degrade to O(n) operations
- Used in AVL trees, Red-Black trees
- Common interview problem

Useful in:
- Tree analysis
- Medium difficulty interview problems
"""

from typing import Optional, Tuple
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Balanced Tree Check (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Check if binary tree is height-balanced.

    Algorithm:
    1. Calculate height of left and right subtrees
    2. Check if difference ≤ 1
    3. Recursively check all nodes

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        bool: True if balanced, False otherwise

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth.
    """
    def check_balance(node: Optional[TreeNode]) -> Tuple[bool, int]:
        """Returns (is_balanced, height)."""
        if not node:
            return (True, -1)
        
        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return (False, 0)
        
        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return (False, 0)
        
        # Check height difference
        if abs(left_height - right_height) > 1:
            return (False, 0)
        
        height = 1 + max(left_height, right_height)
        return (True, height)
    
    balanced, _ = check_balance(root)
    return balanced


# ----------------------------------------------------------------------
# Balanced Tree Check (Alternative)
# ----------------------------------------------------------------------
def is_balanced_alt(root: Optional[TreeNode]) -> bool:
    """
    Check balance using separate height function.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        bool: True if balanced

    Complexity:
        Time: O(n²)    - Calculates height for each node.
        Space: O(h)   - Recursion stack.
    """
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        return 1 + max(height(node.left), height(node.right))
    
    if not root:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return is_balanced_alt(root.left) and is_balanced_alt(root.right)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Balanced Tree Check Demonstration")
    
    # Balanced tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    
    print("Tree 1 (balanced):")
    print("      1")
    print("     / \\")
    print("    2   3")
    print("   /")
    print("  4")
    print(f"Is balanced: {is_balanced(root1)}")
    
    # Unbalanced tree
    print("\n" + "="*50)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    
    print("Tree 2 (unbalanced):")
    print("  1")
    print(" /")
    print("2")
    print("/")
    print("3")
    print("/")
    print("4")
    print(f"Is balanced: {is_balanced(root2)}")

