"""
Graph Algorithms Using Heaps

Implement graph algorithms efficiently using heaps (priority queues).

Algorithms:
1. Dijkstra's Shortest Path
2. Prim's Minimum Spanning Tree

Why Heaps for Graph Algorithms?
--------------------------------
- Need to repeatedly extract minimum distance/weight
- Heap provides O(log n) access to minimum
- More efficient than linear search O(n)

Useful in:
- Shortest path problems
- Minimum spanning tree
- Medium difficulty interview problems
"""

from typing import List, Tuple, Dict
import heapq


# ----------------------------------------------------------------------
# Dijkstra's Shortest Path Algorithm
# ----------------------------------------------------------------------
def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int, n: int) -> List[int]:
    """
    Find shortest distances from start to all nodes using Dijkstra's algorithm.

    Algorithm:
    1. Initialize distances to infinity
    2. Use min heap to track (distance, node)
    3. Extract minimum distance node
    4. Relax edges and update distances
    5. Repeat until all nodes processed

    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list {node: [(neighbor, weight), ...]}
        start (int): Starting node
        n (int): Number of nodes

    Returns:
        List[int]: Shortest distances from start to all nodes

    Complexity:
        Time: O((V + E) log V)  - V vertices, E edges, heap operations.
        Space: O(V)            - Distance array and heap.
    """
    INF = float('inf')
    distances = [INF] * n
    distances[start] = 0
    
    heap = [(0, start)]
    visited = set()
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        # Relax edges
        if node in graph:
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
    
    return distances


# ----------------------------------------------------------------------
# Prim's Minimum Spanning Tree
# ----------------------------------------------------------------------
def prim_mst(graph: Dict[int, List[Tuple[int, int]]], n: int) -> int:
    """
    Find minimum spanning tree using Prim's algorithm.

    Algorithm:
    1. Start from any node
    2. Use min heap to track (weight, node)
    3. Add minimum weight edge to MST
    4. Add new edges to heap
    5. Repeat until all nodes in MST

    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list
        n (int): Number of nodes

    Returns:
        int: Total weight of MST

    Complexity:
        Time: O((V + E) log V)  - V vertices, E edges, heap operations.
        Space: O(V)            - Visited set and heap.
    """
    visited = set()
    heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    
    while heap and len(visited) < n:
        weight, node = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        total_weight += weight
        
        # Add edges to heap
        if node in graph:
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (edge_weight, neighbor))
    
    return total_weight if len(visited) == n else -1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Graph Algorithms Using Heaps Demonstration")
    
    # Dijkstra's algorithm
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print("Graph (adjacency list):")
    for node, edges in graph.items():
        print(f"  {node}: {edges}")
    
    distances = dijkstra(graph, 0, 4)
    print(f"\nShortest distances from node 0: {distances}")
    
    # Prim's MST
    print("\n" + "="*50)
    mst_weight = prim_mst(graph, 4)
    print(f"Minimum Spanning Tree weight: {mst_weight}")

