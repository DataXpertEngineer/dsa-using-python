"""
Prim's Minimum Spanning Tree (MST)

Find minimum spanning tree of a connected, undirected, weighted graph.

Problem Statement:
-------------------
Given a connected weighted graph, find subset of edges that:
1. Connects all vertices
2. Has minimum total weight
3. Forms a tree (no cycles)

Why Prim's?
-----------
- Greedy algorithm
- O(V²) or O((V + E) log V) depending on implementation
- Works well for dense graphs
- Simple to understand

Useful in:
- Network design
- Cluster analysis
- Common interview problems
"""

from typing import Dict, List, Tuple, Set
import heapq
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from weighted_unweighted import WeightedGraph


# ----------------------------------------------------------------------
# Prim's MST - Priority Queue (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def prim_mst(graph: WeightedGraph) -> List[Tuple[int, int, int]]:
    """
    Find MST using Prim's algorithm with priority queue.

    Algorithm:
    1. Start with arbitrary vertex
    2. Add minimum weight edge connecting tree to new vertex
    3. Repeat until all vertices included

    Args:
        graph (WeightedGraph): Connected weighted undirected graph

    Returns:
        List[Tuple[int, int, int]]: MST edges as (u, v, weight)

    Complexity:
        Time: O((V + E) log V)  - V vertices, E edges, log V for heap operations.
        Space: O(V)            - Visited set + priority queue.
    """
    if not graph.vertices:
        return []
    
    mst_edges: List[Tuple[int, int, int]] = []
    visited: Set[int] = set()
    
    # Start with first vertex
    start = next(iter(graph.vertices))
    visited.add(start)
    
    # Priority queue: (weight, u, v) where u is in MST, v is not
    pq: List[Tuple[int, int, int]] = []
    
    # Initialize with edges from start
    for neighbor, weight in graph.get_neighbors(start):
        heapq.heappush(pq, (weight, start, neighbor))
    
    while pq and len(visited) < len(graph.vertices):
        weight, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst_edges.append((u, v, weight))
        
        # Add edges from new vertex
        for neighbor, edge_weight in graph.get_neighbors(v):
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, v, neighbor))
    
    return mst_edges


# ----------------------------------------------------------------------
# Prim's MST - Array-based (O(V²))
# ----------------------------------------------------------------------
def prim_mst_array(graph: WeightedGraph) -> List[Tuple[int, int, int]]:
    """
    Prim's algorithm using array instead of priority queue.

    Args:
        graph (WeightedGraph): Connected weighted undirected graph

    Returns:
        List[Tuple[int, int, int]]: MST edges

    Complexity:
        Time: O(V²)     - V iterations, each finds minimum in O(V).
        Space: O(V)    - Key array + parent array + visited set.
    """
    if not graph.vertices:
        return []
    
    vertices_list = list(graph.vertices)
    n = len(vertices_list)
    
    # Key: minimum weight to connect to MST
    key: Dict[int, int] = {v: float('inf') for v in vertices_list}
    parent: Dict[int, int] = {v: None for v in vertices_list}
    visited: Set[int] = set()
    
    # Start with first vertex
    start = vertices_list[0]
    key[start] = 0
    
    mst_edges: List[Tuple[int, int, int]] = []
    
    for _ in range(n):
        # Find unvisited vertex with minimum key
        min_vertex = None
        min_key = float('inf')
        
        for v in vertices_list:
            if v not in visited and key[v] < min_key:
                min_key = key[v]
                min_vertex = v
        
        if min_vertex is None:
            break
        
        visited.add(min_vertex)
        
        # Add edge to MST (except for first vertex)
        if parent[min_vertex] is not None:
            weight = graph.get_weight(parent[min_vertex], min_vertex)
            if weight is not None:
                mst_edges.append((parent[min_vertex], min_vertex, weight))
        
        # Update keys of neighbors
        for neighbor, weight in graph.get_neighbors(min_vertex):
            if neighbor not in visited and weight < key[neighbor]:
                key[neighbor] = weight
                parent[neighbor] = min_vertex
    
    return mst_edges


# ----------------------------------------------------------------------
# MST Total Weight
# ----------------------------------------------------------------------
def mst_total_weight(graph: WeightedGraph) -> int:
    """
    Calculate total weight of MST.

    Args:
        graph (WeightedGraph): Connected weighted undirected graph

    Returns:
        int: Total weight of MST

    Complexity:
        Time: O((V + E) log V)  - Prim's algorithm.
        Space: O(V)             - Algorithm storage.
    """
    mst_edges = prim_mst(graph)
    return sum(weight for _, _, weight in mst_edges)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Prim's MST Algorithm Demonstration")
    
    graph = WeightedGraph(directed=False)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)
    
    print("Graph structure:")
    graph.display()
    
    mst_edges = prim_mst(graph)
    print("\nMST edges:")
    total_weight = 0
    for u, v, weight in mst_edges:
        print(f"  {u} - {v} (weight: {weight})")
        total_weight += weight
    
    print(f"\nTotal MST weight: {total_weight}")

