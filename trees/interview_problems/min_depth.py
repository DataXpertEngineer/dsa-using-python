"""
Minimum Depth of Binary Tree

Find the minimum depth (shortest path from root to leaf) of a binary tree.

Problem Statement:
-------------------
Given the root of a binary tree, return its minimum depth.

Example:
    Tree:    3
            / \
           9   20
              /  \
             15   7
    Output: 2 (path: 3 → 9)

Why Minimum Depth?
------------------
- Different from maximum depth
- Must reach a leaf node
- Common interview problem
- Useful for shortest path problems

Useful in:
- Tree analysis
- Medium difficulty interview problems
"""

from typing import Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Minimum Depth (Language-agnostic)
# ----------------------------------------------------------------------
def min_depth(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth of binary tree.

    Important: Must reach a leaf node (node with no children).

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Minimum depth (0 for empty tree)

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth.
    """
    if not root:
        return 0
    
    # If leaf node
    if not root.left and not root.right:
        return 1
    
    # If only one child
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    
    # Both children exist
    return 1 + min(min_depth(root.left), min_depth(root.right))


# ----------------------------------------------------------------------
# Minimum Depth (BFS - Optimal for this problem)
# ----------------------------------------------------------------------
def min_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth using BFS (stops at first leaf).

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        int: Minimum depth

    Complexity:
        Time: O(n)     - Visits nodes until first leaf.
        Space: O(w)   - Queue storage.
    """
    if not root:
        return 0
    
    from collections import deque
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        # First leaf found
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Minimum Depth Demonstration")
    
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
    
    depth = min_depth(root)
    print(f"Minimum depth: {depth}")
    print("Explanation: Shortest path to leaf is 3 → 9 (depth 2)")
    
    # BFS approach
    depth_bfs = min_depth_bfs(root)
    print(f"Minimum depth (BFS): {depth_bfs}")

