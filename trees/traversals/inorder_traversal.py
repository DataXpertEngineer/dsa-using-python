"""
Inorder Traversal

Inorder traversal visits nodes in the order: Left → Root → Right.

For Binary Search Tree (BST), inorder traversal gives sorted order.

Why Inorder?
------------
- For BST: Produces sorted sequence
- Natural for expression trees (infix notation)
- Common in tree problems

Useful in:
- BST operations
- Expression evaluation
- Common interview problems
"""

from typing import List, Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Inorder Traversal - Recursive (Language-agnostic)
# ----------------------------------------------------------------------
def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal recursively.

    Order: Left → Root → Right

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: Inorder traversal result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth (h = height).
    """
    result: List[int] = []
    
    def inorder(node: Optional[TreeNode]) -> None:
        if node:
            inorder(node.left)      # Left
            result.append(node.val)  # Root
            inorder(node.right)      # Right
    
    inorder(root)
    return result


# ----------------------------------------------------------------------
# Inorder Traversal - Iterative
# ----------------------------------------------------------------------
def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal iteratively using stack.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: Inorder traversal result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Stack stores at most h nodes.
    """
    result: List[int] = []
    stack: List[TreeNode] = []
    current = root
    
    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Inorder Traversal Demonstration")
    
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
    
    print("Tree structure:")
    print("      1")
    print("     / \\")
    print("    2   3")
    print("   / \\")
    print("  4   5")
    
    result_rec = inorder_traversal(root)
    print(f"\nInorder (recursive): {result_rec}")
    print("Order: Left → Root → Right")
    print("Explanation: 4 → 2 → 5 → 1 → 3")
    
    result_iter = inorder_traversal_iterative(root)
    print(f"Inorder (iterative): {result_iter}")
    print(f"Results match: {result_rec == result_iter}")

