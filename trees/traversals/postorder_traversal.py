"""
Postorder Traversal

Postorder traversal visits nodes in the order: Left → Right → Root.

Useful for deleting a tree or postfix expression evaluation.

Why Postorder?
--------------
- Natural for tree deletion (delete children before parent)
- Postfix notation in expression trees
- Can be used to calculate expressions

Useful in:
- Tree deletion
- Expression evaluation
- Common interview problems
"""

from typing import List, Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Postorder Traversal - Recursive (Language-agnostic)
# ----------------------------------------------------------------------
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal recursively.

    Order: Left → Right → Root

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: Postorder traversal result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth (h = height).
    """
    result: List[int] = []
    
    def postorder(node: Optional[TreeNode]) -> None:
        if node:
            postorder(node.left)     # Left
            postorder(node.right)    # Right
            result.append(node.val)   # Root
    
    postorder(root)
    return result


# ----------------------------------------------------------------------
# Postorder Traversal - Iterative
# ----------------------------------------------------------------------
def postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal iteratively using two stacks.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: Postorder traversal result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Stack storage.
    """
    if not root:
        return []
    
    result: List[int] = []
    stack1: List[TreeNode] = [root]
    stack2: List[TreeNode] = []
    
    # Process nodes and push to stack2 in reverse order
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Pop from stack2 to get postorder
    while stack2:
        result.append(stack2.pop().val)
    
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Postorder Traversal Demonstration")
    
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
    
    result_rec = postorder_traversal(root)
    print(f"\nPostorder (recursive): {result_rec}")
    print("Order: Left → Right → Root")
    print("Explanation: 4 → 5 → 2 → 3 → 1")
    
    result_iter = postorder_traversal_iterative(root)
    print(f"Postorder (iterative): {result_iter}")
    print(f"Results match: {result_rec == result_iter}")

