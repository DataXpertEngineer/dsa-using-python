"""
Rat in a Maze Problem

Find path for rat from source to destination in a maze using backtracking.

Problem Statement:
-------------------
Given a maze with obstacles, find all paths from source (0,0) to
destination (n-1, m-1). Rat can move only right or down.

Example:
    Maze: [[1, 0, 0, 0],
           [1, 1, 0, 1],
           [0, 1, 0, 0],
           [1, 1, 1, 1]]
    1 = open path, 0 = obstacle

Why Backtracking?
-----------------
- Try moving in each direction
- If valid, recurse to next position
- If destination reached, save path
- If stuck, backtrack to previous position
- Explore all possible paths

Useful in:
- Path finding
- Maze solving
- Medium difficulty interview problems
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Rat in Maze - Find All Paths (Language-agnostic)
# ----------------------------------------------------------------------
def find_paths(maze: List[List[int]]) -> List[List[Tuple[int, int]]]:
    """
    Find all paths from (0,0) to (n-1, m-1) in maze.

    Algorithm:
    1. Start at (0, 0)
    2. Try moving right and down
    3. If valid (within bounds, not obstacle, not visited), recurse
    4. If destination reached, save path
    5. Backtrack: mark cell as unvisited

    Args:
        maze (List[List[int]]): Maze grid (1 = open, 0 = obstacle)

    Returns:
        List[List[Tuple[int, int]]]: List of all paths

    Complexity:
        Time: O(2^(n*m)) worst case  - Explores all paths.
        Space: O(n*m)               - Recursion depth + path storage.
    """
    if not maze or not maze[0]:
        return []
    
    n, m = len(maze), len(maze[0])
    paths: List[List[Tuple[int, int]]] = []
    visited = [[False] * m for _ in range(n)]
    
    def is_valid(row: int, col: int) -> bool:
        """Check if cell is valid."""
        return (0 <= row < n and 0 <= col < m and
                maze[row][col] == 1 and not visited[row][col])
    
    def backtrack(path: List[Tuple[int, int]], row: int, col: int) -> None:
        """Backtrack to find all paths."""
        # Base case: reached destination
        if row == n - 1 and col == m - 1:
            paths.append(path.copy())
            return
        
        # Try moving right
        if is_valid(row, col + 1):
            visited[row][col + 1] = True
            path.append((row, col + 1))
            backtrack(path, row, col + 1)
            path.pop()
            visited[row][col + 1] = False
        
        # Try moving down
        if is_valid(row + 1, col):
            visited[row + 1][col] = True
            path.append((row + 1, col))
            backtrack(path, row + 1, col)
            path.pop()
            visited[row + 1][col] = False
    
    # Start from (0, 0)
    visited[0][0] = True
    backtrack([(0, 0)], 0, 0)
    return paths


# ----------------------------------------------------------------------
# Rat in Maze - Find One Path
# ----------------------------------------------------------------------
def find_path(maze: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find one path from (0,0) to (n-1, m-1).

    Args:
        maze (List[List[int]]): Maze grid

    Returns:
        Optional[List[Tuple[int, int]]]: Path if exists, None otherwise

    Complexity:
        Time: O(2^(n*m)) worst case.
        Space: O(n*m)   - Recursion depth.
    """
    if not maze or not maze[0]:
        return None
    
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)]
    path: List[Tuple[int, int]] = []
    
    def is_valid(row: int, col: int) -> bool:
        return (0 <= row < n and 0 <= col < m and
                maze[row][col] == 1 and not visited[row][col])
    
    def backtrack(row: int, col: int) -> bool:
        if row == n - 1 and col == m - 1:
            path.append((row, col))
            return True
        
        if is_valid(row, col):
            visited[row][col] = True
            path.append((row, col))
            
            # Try right
            if backtrack(row, col + 1):
                return True
            
            # Try down
            if backtrack(row + 1, col):
                return True
            
            # Backtrack
            path.pop()
            visited[row][col] = False
        
        return False
    
    if backtrack(0, 0):
        return path
    return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Rat in a Maze Demonstration")
    
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    
    print("Maze (1 = open, 0 = obstacle):")
    for row in maze:
        print(row)
    
    paths = find_paths(maze)
    print(f"\nNumber of paths: {len(paths)}")
    for i, path in enumerate(paths):
        print(f"  Path {i + 1}: {path}")
    
    # One path
    print("\n" + "="*50)
    one_path = find_path(maze)
    print(f"One path: {one_path}")

