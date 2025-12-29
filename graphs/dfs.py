"""
Depth-First Search (DFS) in Graphs

DFS explores as far as possible along each branch before backtracking.
Uses stack (recursion or explicit stack).

Why DFS?
--------
- Explores deep before wide
- Uses less memory than BFS (stack vs queue)
- Natural for recursive problems
- Useful for path finding, cycle detection

Useful in:
- Path finding
- Cycle detection
- Topological sorting
- Connected components
"""

from typing import List, Set, Optional, Dict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from graphs import Graph


# ----------------------------------------------------------------------
# DFS - Recursive (Language-agnostic)
# ----------------------------------------------------------------------
def dfs_recursive(graph: Graph, start: int) -> List[int]:
    """
    Perform DFS starting from vertex using recursion.

    Args:
        graph (Graph): Graph to traverse
        start (int): Starting vertex

    Returns:
        List[int]: DFS traversal order

    Complexity:
        Time: O(V + E)  - Visits each vertex and edge once.
        Space: O(V)    - Recursion stack + visited set.
    """
    visited: Set[int] = set()
    result: List[int] = []
    
    def dfs_visit(vertex: int) -> None:
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_visit(neighbor)
    
    dfs_visit(start)
    return result


# ----------------------------------------------------------------------
# DFS - Iterative
# ----------------------------------------------------------------------
def dfs_iterative(graph: Graph, start: int) -> List[int]:
    """
    Perform DFS using explicit stack.

    Args:
        graph (Graph): Graph to traverse
        start (int): Starting vertex

    Returns:
        List[int]: DFS traversal order

    Complexity:
        Time: O(V + E)  - Visits each vertex and edge once.
        Space: O(V)    - Stack + visited set.
    """
    visited: Set[int] = set()
    result: List[int] = []
    stack: List[int] = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (reverse order for same result as recursive)
            for neighbor in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


# ----------------------------------------------------------------------
# DFS - Find Path
# ----------------------------------------------------------------------
def dfs_find_path(graph: Graph, start: int, target: int) -> Optional[List[int]]:
    """
    Find path from start to target using DFS.

    Args:
        graph (Graph): Graph to search
        start (int): Starting vertex
        target (int): Target vertex

    Returns:
        Optional[List[int]]: Path if found, None otherwise

    Complexity:
        Time: O(V + E)  - Worst case visits all vertices.
        Space: O(V)    - Recursion stack + path.
    """
    visited: Set[int] = set()
    path: List[int] = []
    
    def dfs_visit(vertex: int) -> bool:
        visited.add(vertex)
        path.append(vertex)
        
        if vertex == target:
            return True
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_visit(neighbor):
                    return True
        
        path.pop()
        return False
    
    if dfs_visit(start):
        return path
    return None


# ----------------------------------------------------------------------
# DFS - All Paths
# ----------------------------------------------------------------------
def dfs_all_paths(graph: Graph, start: int, target: int) -> List[List[int]]:
    """
    Find all paths from start to target using DFS.

    Args:
        graph (Graph): Graph to search
        start (int): Starting vertex
        target (int): Target vertex

    Returns:
        List[List[int]]: List of all paths

    Complexity:
        Time: O(2^V) worst case  - Exponential number of paths.
        Space: O(V)              - Recursion stack.
    """
    paths: List[List[int]] = []
    
    def dfs_visit(vertex: int, path: List[int], visited: Set[int]) -> None:
        path.append(vertex)
        visited.add(vertex)
        
        if vertex == target:
            paths.append(path.copy())
        else:
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_visit(neighbor, path, visited)
        
        path.pop()
        visited.remove(vertex)
    
    dfs_visit(start, [], set())
    return paths


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Depth-First Search Demonstration")
    
    graph = Graph(directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    
    print("Graph structure:")
    graph.display()
    
    print("\nDFS Recursive from 0:")
    result_rec = dfs_recursive(graph, 0)
    print(f"  {result_rec}")
    
    print("\nDFS Iterative from 0:")
    result_iter = dfs_iterative(graph, 0)
    print(f"  {result_iter}")
    
    print("\nFind path from 0 to 4:")
    path = dfs_find_path(graph, 0, 4)
    print(f"  Path: {path}")

