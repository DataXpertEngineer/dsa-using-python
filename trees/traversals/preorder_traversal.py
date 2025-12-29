"""
Preorder Traversal

Preorder traversal visits nodes in the order: Root → Left → Right.

Useful for creating a copy of the tree or prefix expression evaluation.

Why Preorder?
-------------
- Natural for tree copying
- Prefix notation in expression trees
- Can be used to serialize tree structure

Useful in:
- Tree copying
- Expression evaluation
- Common interview problems
"""

from typing import List, Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Preorder Traversal - Recursive (Language-agnostic)
# ----------------------------------------------------------------------
def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform preorder traversal recursively.

    Order: Root → Left → Right

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: Preorder traversal result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth (h = height).
    """
    result: List[int] = []
    
    def preorder(node: Optional[TreeNode]) -> None:
        if node:
            result.append(node.val)  # Root
            preorder(node.left)      # Left
            preorder(node.right)     # Right
    
    preorder(root)
    return result


# ----------------------------------------------------------------------
# Preorder Traversal - Iterative
# ----------------------------------------------------------------------
def preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform preorder traversal iteratively using stack.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: Preorder traversal result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Stack stores at most h nodes.
    """
    if not root:
        return []
    
    result: List[int] = []
    stack: List[TreeNode] = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first, then left (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Preorder Traversal Demonstration")
    
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
    
    result_rec = preorder_traversal(root)
    print(f"\nPreorder (recursive): {result_rec}")
    print("Order: Root → Left → Right")
    print("Explanation: 1 → 2 → 4 → 5 → 3")
    
    result_iter = preorder_traversal_iterative(root)
    print(f"Preorder (iterative): {result_iter}")
    print(f"Results match: {result_rec == result_iter}")

