"""
Lowest Common Ancestor (LCA)

Find the lowest common ancestor of two nodes in a binary tree.

Definition:
- LCA: Deepest node that is an ancestor of both nodes
- Node is ancestor of itself

Why LCA?
--------
- Important tree operation
- Used in many tree problems
- Foundation for distance calculations
- Common interview problem

Useful in:
- Tree queries
- Distance calculations
- Common interview problems
"""

from typing import Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# LCA - Binary Tree (Language-agnostic)
# ----------------------------------------------------------------------
def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Find lowest common ancestor of two nodes.

    Algorithm:
    1. If root is None or matches p or q, return root
    2. Recursively search in left and right subtrees
    3. If both found, root is LCA
    4. If one found, return that node
    5. If none found, return None

    Args:
        root (Optional[TreeNode]): Root of the tree
        p (TreeNode): First node
        q (TreeNode): Second node

    Returns:
        Optional[TreeNode]: LCA if found, None otherwise

    Complexity:
        Time: O(n)     - Visits nodes until LCA found.
        Space: O(h)   - Recursion stack depth.
    """
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # If both found, root is LCA
    if left and right:
        return root
    
    # Return non-None result
    return left if left else right


# ----------------------------------------------------------------------
# LCA - With Path Finding
# ----------------------------------------------------------------------
def lca_with_path(root: Optional[TreeNode], p: int, q: int) -> Optional[int]:
    """
    Find LCA by finding paths to both nodes.

    Args:
        root (Optional[TreeNode]): Root of the tree
        p (int): First node value
        q (int): Second node value

    Returns:
        Optional[int]: LCA value if found, None otherwise

    Complexity:
        Time: O(n)     - Finds paths and compares.
        Space: O(h)   - Path storage.
    """
    def find_path(node: Optional[TreeNode], target: int, path: list) -> bool:
        if not node:
            return False
        
        path.append(node.val)
        
        if node.val == target:
            return True
        
        if (find_path(node.left, target, path) or
            find_path(node.right, target, path)):
            return True
        
        path.pop()
        return False
    
    path_p: list[int] = []
    path_q: list[int] = []
    
    if not find_path(root, p, path_p) or not find_path(root, q, path_q):
        return None
    
    # Find last common node in paths
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        i += 1
    
    return path_p[i - 1] if i > 0 else None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Lowest Common Ancestor Demonstration")
    
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
    
    p = root.left.left  # Node 4
    q = root.left.right  # Node 5
    
    lca = lowest_common_ancestor(root, p, q)
    print(f"LCA of 4 and 5: {lca.val if lca else None}")
    print("Expected: 2")
    
    # Using path method
    lca_val = lca_with_path(root, 4, 5)
    print(f"LCA (path method): {lca_val}")

