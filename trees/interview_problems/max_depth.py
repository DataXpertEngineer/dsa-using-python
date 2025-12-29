"""
Maximum Depth of Binary Tree

Find the maximum depth (height) of a binary tree.

Problem Statement:
-------------------
Given the root of a binary tree, return its maximum depth.

Example:
    Tree:    3
            / \
           9   20
              /  \
             15   7
    Output: 3

Why Maximum Depth?
------------------
- Fundamental tree property
- Used in many tree algorithms
- Common interview problem
- Simple recursive solution

Useful in:
- Tree analysis
- Common interview problems
"""

from typing import Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Maximum Depth (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth of binary tree.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Maximum depth (0 for empty tree)

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth (h = height).
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)


# ----------------------------------------------------------------------
# Maximum Depth (Iterative BFS)
# ----------------------------------------------------------------------
def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth using BFS (level-order).

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Maximum depth

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(w)   - Queue storage (w = max width).
    """
    if not root:
        return 0
    
    from collections import deque
    
    queue = deque([(root, 1)])
    max_depth_val = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth_val = max(max_depth_val, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth_val


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Maximum Depth Demonstration")
    
    # Create tree:    3
    #                / \
    #               9   20
    #                  /  \
    #                 15   7
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    depth = max_depth(root)
    print(f"Maximum depth: {depth}")
    print("Expected: 3")
    
    # BFS approach
    depth_bfs = max_depth_bfs(root)
    print(f"Maximum depth (BFS): {depth_bfs}")

