"""
Depth-First Search (DFS) in Trees

DFS explores as far as possible along each branch before backtracking.

Traversal Orders:
1. Preorder: Root → Left → Right
2. Inorder: Left → Root → Right
3. Postorder: Left → Right → Root

Why DFS?
--------
- Explores deep before wide
- Uses less memory than BFS (stack vs queue)
- Natural for recursive problems
- Useful for path finding

Useful in:
- Tree traversals
- Path finding
- Common interview problems
"""

from typing import List, Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# DFS - Preorder (Language-agnostic)
# ----------------------------------------------------------------------
def dfs_preorder(root: Optional[TreeNode]) -> List[int]:
    """
    DFS using preorder traversal.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: DFS preorder result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth.
    """
    result: List[int] = []
    
    def dfs(node: Optional[TreeNode]) -> None:
        if node:
            result.append(node.val)  # Visit
            dfs(node.left)           # Explore left
            dfs(node.right)          # Explore right
    
    dfs(root)
    return result


# ----------------------------------------------------------------------
# DFS - Iterative
# ----------------------------------------------------------------------
def dfs_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    DFS using iterative approach with stack.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: DFS result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Stack storage.
    """
    if not root:
        return []
    
    result: List[int] = []
    stack: List[TreeNode] = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first, then left (preorder)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# ----------------------------------------------------------------------
# DFS - Find Path
# ----------------------------------------------------------------------
def dfs_find_path(root: Optional[TreeNode], target: int) -> Optional[List[int]]:
    """
    Find path from root to target using DFS.

    Args:
        root (Optional[TreeNode]): Root of the tree
        target (int): Target value

    Returns:
        Optional[List[int]]: Path if found, None otherwise

    Complexity:
        Time: O(n)     - Visits nodes until target found.
        Space: O(h)   - Recursion stack + path storage.
    """
    path: List[int] = []
    
    def dfs(node: Optional[TreeNode]) -> bool:
        if not node:
            return False
        
        path.append(node.val)
        
        if node.val == target:
            return True
        
        if dfs(node.left) or dfs(node.right):
            return True
        
        path.pop()
        return False
    
    if dfs(root):
        return path
    return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Depth-First Search Demonstration")
    
    # Create tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("DFS Preorder:")
    result = dfs_preorder(root)
    print(f"  {result}")
    
    print("\nDFS Iterative:")
    result_iter = dfs_iterative(root)
    print(f"  {result_iter}")
    
    print("\nFind path to 5:")
    path = dfs_find_path(root, 5)
    print(f"  Path: {path}")

