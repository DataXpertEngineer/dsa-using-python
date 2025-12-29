"""
Directed vs Undirected Graphs

Understanding the difference between directed and undirected graphs.

Directed Graph:
- Edges have direction (u → v)
- Edge (u, v) is different from (v, u)
- Represents one-way relationships

Undirected Graph:
- Edges are bidirectional (u ↔ v)
- Edge (u, v) is same as (v, u)
- Represents two-way relationships

Why Both?
---------
- Different real-world scenarios
- Different algorithms apply
- Different complexity analysis
- Common interview topic

Useful in:
- Modeling relationships
- Understanding graph properties
- Algorithm selection
"""

from typing import List, Set, Dict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from graphs import Graph


# ----------------------------------------------------------------------
# Directed Graph Operations
# ----------------------------------------------------------------------
def in_degree(graph: Graph, vertex: int) -> int:
    """
    Calculate in-degree of vertex in directed graph.

    In-degree: Number of incoming edges.

    Args:
        graph (Graph): Directed graph
        vertex (int): Vertex

    Returns:
        int: In-degree

    Complexity:
        Time: O(V + E)  - Must check all edges.
        Space: O(1)    - Only uses counter.
    """
    if not graph.directed:
        return len(graph.get_neighbors(vertex))
    
    count = 0
    for u in graph.get_vertices():
        if vertex in graph.get_neighbors(u):
            count += 1
    return count


def out_degree(graph: Graph, vertex: int) -> int:
    """
    Calculate out-degree of vertex in directed graph.

    Out-degree: Number of outgoing edges.

    Args:
        graph (Graph): Directed graph
        vertex (int): Vertex

    Returns:
        int: Out-degree

    Complexity:
        Time: O(1)     - Returns length of adjacency list.
        Space: O(1)   - Only uses variables.
    """
    return len(graph.get_neighbors(vertex))


# ----------------------------------------------------------------------
# Convert Undirected to Directed
# ----------------------------------------------------------------------
def make_directed(undirected_graph: Graph) -> Graph:
    """
    Convert undirected graph to directed (each edge becomes two directed edges).

    Args:
        undirected_graph (Graph): Undirected graph

    Returns:
        Graph: Directed graph

    Complexity:
        Time: O(V + E)  - Processes all edges.
        Space: O(V + E) - Creates new graph.
    """
    directed = Graph(directed=True)
    
    for u in undirected_graph.get_vertices():
        for v in undirected_graph.get_neighbors(u):
            directed.add_edge(u, v)
    
    return directed


# ----------------------------------------------------------------------
# Check Graph Type
# ----------------------------------------------------------------------
def is_directed(graph: Graph) -> bool:
    """
    Check if graph is directed.

    Args:
        graph (Graph): Graph to check

    Returns:
        bool: True if directed

    Complexity:
        Time: O(1)     - Constant time check.
        Space: O(1)   - Only uses variables.
    """
    return graph.directed


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Directed vs Undirected Graphs Demonstration")
    
    # Undirected graph
    print("Undirected Graph:")
    undirected = Graph(directed=False)
    undirected.add_edge(0, 1)
    undirected.add_edge(1, 2)
    undirected.display()
    print(f"  Edge (0,1) exists: {undirected.has_edge(0, 1)}")
    print(f"  Edge (1,0) exists: {undirected.has_edge(1, 0)}")
    print("  Note: Both edges exist (bidirectional)")
    
    # Directed graph
    print("\n" + "="*50)
    print("Directed Graph:")
    directed = Graph(directed=True)
    directed.add_edge(0, 1)
    directed.add_edge(1, 2)
    directed.display()
    print(f"  Edge (0,1) exists: {directed.has_edge(0, 1)}")
    print(f"  Edge (1,0) exists: {directed.has_edge(1, 0)}")
    print("  Note: Only (0,1) exists (one-way)")
    
    # In-degree and out-degree
    print("\n" + "="*50)
    print("In-degree and Out-degree:")
    print(f"  Vertex 1 in-degree: {in_degree(directed, 1)}")
    print(f"  Vertex 1 out-degree: {out_degree(directed, 1)}")
    
    print("\n" + "="*50)
    print("DIRECTED vs UNDIRECTED SUMMARY")
    print("="*50)
    print("""
Directed Graph:
- Edges have direction: u → v
- (u, v) ≠ (v, u)
- In-degree: incoming edges
- Out-degree: outgoing edges
- Examples: Web links, dependencies, social media follows

Undirected Graph:
- Edges are bidirectional: u ↔ v
- (u, v) = (v, u)
- Degree: total connected edges
- Examples: Friendships, roads, connections

Algorithms:
- DFS/BFS: Work on both
- Topological sort: Only directed
- Cycle detection: Different for each
- Shortest path: Same algorithm, different interpretation
""")

