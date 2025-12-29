"""
Kruskal's Minimum Spanning Tree (MST)

Find minimum spanning tree using union-find data structure.

Problem Statement:
-------------------
Given a connected weighted graph, find MST by:
1. Sort edges by weight
2. Add edges in order if they don't form cycle
3. Use union-find to detect cycles

Why Kruskal's?
--------------
- Greedy algorithm
- O(E log E) or O(E log V) time
- Works well for sparse graphs
- Simple edge-based approach

Useful in:
- Network design
- Cluster analysis
- Common interview problems
"""

from typing import List, Tuple, Set, Dict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from union_find import UnionFind
from weighted_unweighted import WeightedGraph


# ----------------------------------------------------------------------
# Kruskal's MST (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def kruskal_mst(graph: WeightedGraph) -> List[Tuple[int, int, int]]:
    """
    Find MST using Kruskal's algorithm with union-find.

    Algorithm:
    1. Sort all edges by weight
    2. Initialize union-find structure
    3. For each edge (in sorted order):
       - If endpoints in different sets, add edge to MST
       - Union the sets
    4. Return MST edges

    Args:
        graph (WeightedGraph): Connected weighted undirected graph

    Returns:
        List[Tuple[int, int, int]]: MST edges as (u, v, weight)

    Complexity:
        Time: O(E log E)  - Sort edges O(E log E) + union-find O(E α(V)).
        Space: O(V)      - Union-find structure.
    """
    # Collect all edges
    edges: List[Tuple[int, int, int]] = []
    edge_set: Set[Tuple[int, int]] = set()
    
    for u in graph.vertices:
        for v, weight in graph.get_neighbors(u):
            # Avoid duplicate edges in undirected graph
            edge = tuple(sorted((u, v)))
            if edge not in edge_set:
                edges.append((u, v, weight))
                edge_set.add(edge)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize union-find
    uf = UnionFind(list(graph.vertices))
    
    mst_edges: List[Tuple[int, int, int]] = []
    
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            
            # Early termination if MST complete
            if len(mst_edges) == len(graph.vertices) - 1:
                break
    
    return mst_edges


# ----------------------------------------------------------------------
# Kruskal's - Alternative Implementation
# ----------------------------------------------------------------------
def kruskal_mst_alt(graph: WeightedGraph) -> List[Tuple[int, int, int]]:
    """
    Kruskal's MST with explicit cycle detection.

    Args:
        graph (WeightedGraph): Connected weighted undirected graph

    Returns:
        List[Tuple[int, int, int]]: MST edges

    Complexity:
        Time: O(E log E + E * V)  - Sort + cycle detection.
        Space: O(V)               - Component tracking.
    """
    # Collect and sort edges
    edges: List[Tuple[int, int, int]] = []
    edge_set: Set[Tuple[int, int]] = set()
    
    for u in graph.vertices:
        for v, weight in graph.get_neighbors(u):
            edge = tuple(sorted((u, v)))
            if edge not in edge_set:
                edges.append((u, v, weight))
                edge_set.add(edge)
    
    edges.sort(key=lambda x: x[2])
    
    # Track components
    components: Dict[int, Set[int]] = {v: {v} for v in graph.vertices}
    mst_edges: List[Tuple[int, int, int]] = []
    
    for u, v, weight in edges:
        # Check if u and v in different components
        u_comp = None
        v_comp = None
        
        for comp_id, comp in components.items():
            if u in comp:
                u_comp = comp_id
            if v in comp:
                v_comp = comp_id
        
        if u_comp != v_comp:
            # Merge components
            components[u_comp].update(components[v_comp])
            del components[v_comp]
            mst_edges.append((u, v, weight))
            
            if len(mst_edges) == len(graph.vertices) - 1:
                break
    
    return mst_edges


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Kruskal's MST Algorithm Demonstration")
    
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
    
    mst_edges = kruskal_mst(graph)
    print("\nMST edges (Kruskal's):")
    total_weight = 0
    for u, v, weight in mst_edges:
        print(f"  {u} - {v} (weight: {weight})")
        total_weight += weight
    
    print(f"\nTotal MST weight: {total_weight}")

