"""
Breadth-First Search (BFS) in Trees

BFS explores all nodes at current level before moving to next level.
Uses queue data structure.

Why BFS?
--------
- Explores level by level
- Finds shortest path (unweighted graphs)
- Level-order traversal
- Useful for level-based problems

Useful in:
- Level-order traversal
- Shortest path problems
- Common interview problems
"""

from typing import List, Optional
from collections import deque
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# BFS - Level Order Traversal (Language-agnostic)
# ----------------------------------------------------------------------
def bfs_level_order(root: Optional[TreeNode]) -> List[int]:
    """
    BFS level-order traversal.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[int]: BFS level-order result

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(w)   - Queue stores at most w nodes (w = max width).
    """
    if not root:
        return []
    
    result: List[int] = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


# ----------------------------------------------------------------------
# BFS - Level by Level
# ----------------------------------------------------------------------
def bfs_level_by_level(root: Optional[TreeNode]) -> List[List[int]]:
    """
    BFS returning levels as separate lists.

    Args:
        root (Optional[TreeNode]): Root of the tree

    Returns:
        List[List[int]]: List of levels

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(w)   - Queue storage.
    """
    if not root:
        return []
    
    result: List[List[int]] = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level: List[int] = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


# ----------------------------------------------------------------------
# BFS - Find Level of Node
# ----------------------------------------------------------------------
def bfs_find_level(root: Optional[TreeNode], target: int) -> int:
    """
    Find level of target node using BFS.

    Args:
        root (Optional[TreeNode]): Root of the tree
        target (int): Target value

    Returns:
        int: Level (0-indexed), -1 if not found

    Complexity:
        Time: O(n)     - Visits nodes until target found.
        Space: O(w)   - Queue storage.
    """
    if not root:
        return -1
    
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        
        if node.val == target:
            return level
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return -1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Breadth-First Search Demonstration")
    
    # Create tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print("BFS Level Order:")
    result = bfs_level_order(root)
    print(f"  {result}")
    
    print("\nBFS Level by Level:")
    levels = bfs_level_by_level(root)
    for i, level in enumerate(levels):
        print(f"  Level {i}: {level}")
    
    print("\nFind level of 5:")
    level = bfs_find_level(root, 5)
    print(f"  Level: {level}")

