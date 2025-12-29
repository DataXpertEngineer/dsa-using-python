"""
Path Sum Problems

Find paths in binary tree that sum to target value.

Problem Statement:
-------------------
1. Path Sum: Check if path from root to leaf sums to target
2. Path Sum II: Find all paths from root to leaf that sum to target
3. Path Sum III: Count paths (any node to any node) that sum to target

Why Path Sum?
-------------
- Common tree problem pattern
- Uses DFS traversal
- Demonstrates backtracking
- Common interview problem

Useful in:
- Tree path problems
- Medium difficulty interview problems
"""

from typing import List, Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from trees import TreeNode


# ----------------------------------------------------------------------
# Path Sum - Check Existence (Language-agnostic)
# ----------------------------------------------------------------------
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    Check if path from root to leaf sums to target.

    Args:
        root (Optional[TreeNode]): Root of the tree
        target_sum (int): Target sum

    Returns:
        bool: True if path exists, False otherwise

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack depth.
    """
    if not root:
        return False
    
    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Check left and right subtrees
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))


# ----------------------------------------------------------------------
# Path Sum II - Find All Paths
# ----------------------------------------------------------------------
def path_sum_all(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Find all paths from root to leaf that sum to target.

    Args:
        root (Optional[TreeNode]): Root of the tree
        target_sum (int): Target sum

    Returns:
        List[List[int]]: List of all paths

    Complexity:
        Time: O(n)     - Visits each node once.
        Space: O(h)   - Recursion stack + path storage.
    """
    paths: List[List[int]] = []
    
    def dfs(node: Optional[TreeNode], remaining: int, path: List[int]) -> None:
        if not node:
            return
        
        path.append(node.val)
        
        # Leaf node
        if not node.left and not node.right and node.val == remaining:
            paths.append(path.copy())
        else:
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)
        
        # Backtrack
        path.pop()
    
    dfs(root, target_sum, [])
    return paths


# ----------------------------------------------------------------------
# Path Sum III - Count All Paths
# ----------------------------------------------------------------------
def path_sum_count(root: Optional[TreeNode], target_sum: int) -> int:
    """
    Count all paths (any node to any node) that sum to target.

    Args:
        root (Optional[TreeNode]): Root of the tree
        target_sum (int): Target sum

    Returns:
        int: Number of paths

    Complexity:
        Time: O(n²)    - For each node, checks all paths.
        Space: O(h)   - Recursion stack.
    """
    def count_paths(node: Optional[TreeNode], target: int) -> int:
        if not node:
            return 0
        
        count = 0
        if node.val == target:
            count += 1
        
        count += count_paths(node.left, target - node.val)
        count += count_paths(node.right, target - node.val)
        
        return count
    
    if not root:
        return 0
    
    # Count paths starting from root
    # Then count paths in subtrees
    return (count_paths(root, target_sum) +
            path_sum_count(root.left, target_sum) +
            path_sum_count(root.right, target_sum))


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Path Sum Problems Demonstration")
    
    # Create tree:    5
    #                / \
    #               4   8
    #              /   / \
    #             11  13  4
    #            /  \    / \
    #           7   2   5   1
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    
    target = 22
    print(f"Target sum: {target}")
    
    has_path = has_path_sum(root, target)
    print(f"Has path sum: {has_path}")
    print("Explanation: Path 5→4→11→2 sums to 22")
    
    # All paths
    print("\n" + "="*50)
    all_paths = path_sum_all(root, target)
    print(f"All paths with sum {target}: {all_paths}")

