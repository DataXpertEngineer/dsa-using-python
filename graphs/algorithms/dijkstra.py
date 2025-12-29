"""
Dijkstra's Shortest Path Algorithm

Find shortest path from source to all vertices in weighted graph
with non-negative edge weights.

Problem Statement:
-------------------
Given a weighted graph and source vertex, find shortest distance
to all vertices.

Why Dijkstra?
-------------
- Efficient for non-negative weights
- O(V²) or O((V + E) log V) depending on implementation
- Guarantees shortest path
- Foundation for many algorithms

Useful in:
- Network routing
- GPS navigation
- Social network analysis
- Common interview problems
"""

from typing import Dict, List, Tuple, Optional
import heapq
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from weighted_unweighted import WeightedGraph


# ----------------------------------------------------------------------
# Dijkstra's Algorithm - Priority Queue (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def dijkstra(graph: WeightedGraph, start: int) -> Dict[int, int]:
    """
    Find shortest distances from start to all vertices using Dijkstra's algorithm.

    Algorithm:
    1. Initialize distances: start = 0, others = infinity
    2. Use priority queue (min-heap) to process vertices
    3. For each vertex, relax all edges
    4. Continue until all vertices processed

    Args:
        graph (WeightedGraph): Weighted graph
        start (int): Source vertex

    Returns:
        Dict[int, int]: Shortest distances to all vertices

    Complexity:
        Time: O((V + E) log V)  - V vertices, E edges, log V for heap operations.
        Space: O(V)            - Distance map + priority queue.
    """
    distances: Dict[int, int] = {v: float('inf') for v in graph.vertices}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq: List[Tuple[int, int]] = [(0, start)]
    visited: set = set()
    
    while pq:
        current_dist, vertex = heapq.heappop(pq)
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        # Relax edges
        for neighbor, weight in graph.get_neighbors(vertex):
            if neighbor in visited:
                continue
            
            new_dist = current_dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances


# ----------------------------------------------------------------------
# Dijkstra's - Shortest Path to Target
# ----------------------------------------------------------------------
def dijkstra_path(graph: WeightedGraph, start: int, target: int) -> Optional[List[int]]:
    """
    Find shortest path from start to target.

    Args:
        graph (WeightedGraph): Weighted graph
        start (int): Source vertex
        target (int): Target vertex

    Returns:
        Optional[List[int]]: Shortest path if exists, None otherwise

    Complexity:
        Time: O((V + E) log V)  - Dijkstra's algorithm.
        Space: O(V)            - Distance map + parent map + queue.
    """
    distances: Dict[int, int] = {v: float('inf') for v in graph.vertices}
    distances[start] = 0
    parent: Dict[int, int] = {}
    
    pq: List[Tuple[int, int]] = [(0, start)]
    visited: set = set()
    
    while pq:
        current_dist, vertex = heapq.heappop(pq)
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        if vertex == target:
            # Reconstruct path
            path: List[int] = []
            current = target
            while current is not None:
                path.append(current)
                current = parent.get(current)
            return path[::-1]
        
        for neighbor, weight in graph.get_neighbors(vertex):
            if neighbor in visited:
                continue
            
            new_dist = current_dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = vertex
                heapq.heappush(pq, (new_dist, neighbor))
    
    return None


# ----------------------------------------------------------------------
# Dijkstra's - Array-based (O(V²))
# ----------------------------------------------------------------------
def dijkstra_array(graph: WeightedGraph, start: int) -> Dict[int, int]:
    """
    Dijkstra's algorithm using array instead of priority queue.

    Args:
        graph (WeightedGraph): Weighted graph
        start (int): Source vertex

    Returns:
        Dict[int, int]: Shortest distances

    Complexity:
        Time: O(V²)     - V iterations, each finds minimum in O(V).
        Space: O(V)    - Distance array + visited set.
    """
    distances: Dict[int, int] = {v: float('inf') for v in graph.vertices}
    distances[start] = 0
    visited: set = set()
    
    for _ in range(len(graph.vertices)):
        # Find unvisited vertex with minimum distance
        min_vertex = None
        min_dist = float('inf')
        
        for v in graph.vertices:
            if v not in visited and distances[v] < min_dist:
                min_dist = distances[v]
                min_vertex = v
        
        if min_vertex is None:
            break
        
        visited.add(min_vertex)
        
        # Relax edges
        for neighbor, weight in graph.get_neighbors(min_vertex):
            if neighbor not in visited:
                new_dist = distances[min_vertex] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
    
    return distances


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Dijkstra's Algorithm Demonstration")
    
    graph = WeightedGraph(directed=False)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 3, 5)
    graph.add_edge(1, 3, 1)
    
    print("Graph structure:")
    graph.display()
    
    start = 0
    print(f"\nShortest distances from vertex {start}:")
    distances = dijkstra(graph, start)
    for vertex, dist in sorted(distances.items()):
        if dist != float('inf'):
            print(f"  {vertex}: {dist}")
        else:
            print(f"  {vertex}: unreachable")
    
    # Shortest path
    print(f"\nShortest path from {start} to 3:")
    path = dijkstra_path(graph, start, 3)
    print(f"  Path: {path}")

