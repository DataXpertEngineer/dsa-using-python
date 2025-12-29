"""
Shortest Path in Unweighted Graph using BFS

Find shortest path between two vertices in unweighted graph.

Problem Statement:
-------------------
Given an unweighted graph, find shortest path from source to target.
BFS guarantees shortest path in unweighted graphs.

Why BFS for Shortest Path?
--------------------------
- BFS explores level by level
- First time we reach target = shortest path
- Guarantees minimum number of edges
- O(V + E) time complexity

Useful in:
- Path finding
- Minimum steps problems
- Common interview problems
"""

from typing import List, Optional, Dict, Set
from collections import deque
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from graphs import Graph


# ----------------------------------------------------------------------
# Shortest Path - BFS (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def shortest_path_bfs(graph: Graph, start: int, target: int) -> Optional[List[int]]:
    """
    Find shortest path using BFS.

    Algorithm:
    1. Use BFS to explore level by level
    2. Track parent of each vertex
    3. When target found, reconstruct path

    Args:
        graph (Graph): Unweighted graph
        start (int): Source vertex
        target (int): Target vertex

    Returns:
        Optional[List[int]]: Shortest path if exists, None otherwise

    Complexity:
        Time: O(V + E)  - BFS visits vertices until target found.
        Space: O(V)    - Queue + parent map.
    """
    if start == target:
        return [start]
    
    visited: Set[int] = set()
    parent: Dict[int, int] = {}
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        
        if vertex == target:
            # Reconstruct path
            path: List[int] = []
            current = target
            while current is not None:
                path.append(current)
                current = parent.get(current)
            return path[::-1]
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)
    
    return None


# ----------------------------------------------------------------------
# Shortest Distance
# ----------------------------------------------------------------------
def shortest_distance(graph: Graph, start: int, target: int) -> int:
    """
    Find shortest distance (number of edges) between vertices.

    Args:
        graph (Graph): Unweighted graph
        start (int): Source vertex
        target (int): Target vertex

    Returns:
        int: Distance, -1 if not reachable

    Complexity:
        Time: O(V + E)  - BFS traversal.
        Space: O(V)    - Queue + distance map.
    """
    if start == target:
        return 0
    
    distances: Dict[int, int] = {start: 0}
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        if vertex == target:
            return distances[vertex]
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return -1


# ----------------------------------------------------------------------
# All Shortest Paths
# ----------------------------------------------------------------------
def all_shortest_paths(graph: Graph, start: int, target: int) -> List[List[int]]:
    """
    Find all shortest paths between vertices.

    Args:
        graph (Graph): Unweighted graph
        start (int): Source vertex
        target (int): Target vertex

    Returns:
        List[List[int]]: List of all shortest paths

    Complexity:
        Time: O(V + E + P)  - BFS + path reconstruction, P is number of paths.
        Space: O(V + P)    - Queue + paths storage.
    """
    # First, find shortest distance
    dist = shortest_distance(graph, start, target)
    if dist == -1:
        return []
    
    # Find all paths of that length
    paths: List[List[int]] = []
    
    def dfs(vertex: int, path: List[int], visited: Set[int]) -> None:
        if len(path) > dist:
            return
        
        path.append(vertex)
        visited.add(vertex)
        
        if vertex == target and len(path) == dist + 1:
            paths.append(path.copy())
        else:
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs(neighbor, path, visited)
        
        path.pop()
        visited.remove(vertex)
    
    dfs(start, [], set())
    return paths


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Shortest Path using BFS Demonstration")
    
    graph = Graph(directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    
    print("Graph structure:")
    graph.display()
    
    start, target = 0, 5
    print(f"\nShortest path from {start} to {target}:")
    path = shortest_path_bfs(graph, start, target)
    print(f"  Path: {path}")
    
    distance = shortest_distance(graph, start, target)
    print(f"  Distance: {distance} edges")
    
    print(f"\nAll shortest paths from {start} to {target}:")
    all_paths = all_shortest_paths(graph, start, target)
    for i, p in enumerate(all_paths, 1):
        print(f"  Path {i}: {p}")

