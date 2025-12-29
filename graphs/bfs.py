"""
Breadth-First Search (BFS) in Graphs

BFS explores all vertices at current level before moving to next level.
Uses queue data structure.

Why BFS?
--------
- Explores level by level
- Finds shortest path (unweighted graphs)
- Guarantees minimum steps
- Useful for level-based problems

Useful in:
- Shortest path (unweighted)
- Level-order traversal
- Minimum steps problems
- Social network analysis
"""

from typing import List, Set, Optional, Dict
from collections import deque
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from graphs import Graph


# ----------------------------------------------------------------------
# BFS - Basic (Language-agnostic)
# ----------------------------------------------------------------------
def bfs(graph: Graph, start: int) -> List[int]:
    """
    Perform BFS starting from vertex.

    Args:
        graph (Graph): Graph to traverse
        start (int): Starting vertex

    Returns:
        List[int]: BFS traversal order

    Complexity:
        Time: O(V + E)  - Visits each vertex and edge once.
        Space: O(V)    - Queue + visited set.
    """
    visited: Set[int] = set()
    result: List[int] = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


# ----------------------------------------------------------------------
# BFS - Level by Level
# ----------------------------------------------------------------------
def bfs_levels(graph: Graph, start: int) -> List[List[int]]:
    """
    Perform BFS returning vertices level by level.

    Args:
        graph (Graph): Graph to traverse
        start (int): Starting vertex

    Returns:
        List[List[int]]: List of levels

    Complexity:
        Time: O(V + E)  - Visits each vertex and edge once.
        Space: O(V)    - Queue storage.
    """
    visited: Set[int] = set()
    levels: List[List[int]] = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        level_size = len(queue)
        level: List[int] = []
        
        for _ in range(level_size):
            vertex = queue.popleft()
            level.append(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        levels.append(level)
    
    return levels


# ----------------------------------------------------------------------
# BFS - Shortest Path (Unweighted)
# ----------------------------------------------------------------------
def bfs_shortest_path(graph: Graph, start: int, target: int) -> Optional[List[int]]:
    """
    Find shortest path using BFS (unweighted graph).

    Args:
        graph (Graph): Graph to search
        start (int): Starting vertex
        target (int): Target vertex

    Returns:
        Optional[List[int]]: Shortest path if found, None otherwise

    Complexity:
        Time: O(V + E)  - Visits vertices until target found.
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
# BFS - Distance from Start
# ----------------------------------------------------------------------
def bfs_distances(graph: Graph, start: int) -> Dict[int, int]:
    """
    Calculate distances from start vertex using BFS.

    Args:
        graph (Graph): Graph to traverse
        start (int): Starting vertex

    Returns:
        Dict[int, int]: Distance from start for each vertex

    Complexity:
        Time: O(V + E)  - Visits all reachable vertices.
        Space: O(V)    - Queue + distance map.
    """
    distances: Dict[int, int] = {start: 0}
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return distances


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Breadth-First Search Demonstration")
    
    graph = Graph(directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    
    print("Graph structure:")
    graph.display()
    
    print("\nBFS from 0:")
    result = bfs(graph, 0)
    print(f"  {result}")
    
    print("\nBFS Level by Level:")
    levels = bfs_levels(graph, 0)
    for i, level in enumerate(levels):
        print(f"  Level {i}: {level}")
    
    print("\nShortest path from 0 to 4:")
    path = bfs_shortest_path(graph, 0, 4)
    print(f"  Path: {path}")
    
    print("\nDistances from 0:")
    distances = bfs_distances(graph, 0)
    for vertex, dist in sorted(distances.items()):
        print(f"  {vertex}: {dist}")

