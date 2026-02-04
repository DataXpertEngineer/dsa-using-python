"""
Weighted vs Unweighted Graphs

Understanding weighted and unweighted graphs.

Unweighted Graph:
- All edges have same weight (typically 1)
- Represents presence/absence of connection
- Simpler algorithms

Weighted Graph:
- Edges have weights/costs
- Represents distance, cost, time, etc.
- Requires more complex algorithms

Why Both?
--------
- Different problem requirements
- Different algorithms (Dijkstra, Bellman-Ford)
- Real-world applications need weights
- Common interview topic

Useful in:
- Shortest path problems
- Network routing
- Resource allocation
- Medium difficulty interview problems
"""

from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from graphs import Graph


# ----------------------------------------------------------------------
# Weighted Graph Implementation
# ----------------------------------------------------------------------
class WeightedGraph:
    """
    Weighted graph using adjacency list.
    """
    
    def __init__(self, directed: bool = False):
        """
        Initialize weighted graph.

        Args:
            directed (bool): True for directed graph

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty graph.
        """
        self.graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.directed = directed
        self.vertices: Set[int] = set()
    
    def add_edge(self, u: int, v: int, weight: int):
        """
        Add weighted edge between u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex
            weight (int): Edge weight

        Complexity:
            Time: O(1)     - Constant time addition.
            Space: O(1)   - Adds one edge.
        """
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
        
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_neighbors(self, vertex: int) -> List[Tuple[int, int]]:
        """
        Get neighbors with weights.

        Args:
            vertex (int): Vertex

        Returns:
            List[Tuple[int, int]]: List of (neighbor, weight) pairs

        Complexity:
            Time: O(1)     - Returns list reference.
            Space: O(1)   - Returns existing list.
        """
        return self.graph[vertex]
    
    def get_weight(self, u: int, v: int) -> Optional[int]:
        """
        Get weight of edge between u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Returns:
            Optional[int]: Weight if edge exists, None otherwise

        Complexity:
            Time: O(degree(u))  - Must search neighbors.
            Space: O(1)        - Only uses variables.
        """
        for neighbor, weight in self.graph[u]:
            if neighbor == v:
                return weight
        return None
    
    def display(self):
        """Display weighted graph."""
        print("Weighted Graph:")
        for vertex in sorted(self.vertices):
            neighbors = self.graph[vertex]
            neighbor_str = ", ".join([f"{v}({w})" for v, w in neighbors])
            print(f"  {vertex}: {neighbor_str}")


# ----------------------------------------------------------------------
# Convert Unweighted to Weighted
# ----------------------------------------------------------------------
def make_weighted(unweighted_graph: Graph, default_weight: int = 1) -> WeightedGraph:
    """
    Convert unweighted graph to weighted (all edges get same weight).

    Args:
        unweighted_graph (Graph): Unweighted graph
        default_weight (int): Default weight for all edges

    Returns:
        WeightedGraph: Weighted graph

    Complexity:
        Time: O(V + E)  - Processes all edges.
        Space: O(V + E) - Creates new graph.
    """
    weighted = WeightedGraph(directed=unweighted_graph.directed)
    
    for u in unweighted_graph.get_vertices():
        for v in unweighted_graph.get_neighbors(u):
            if unweighted_graph.directed or u < v:  # Avoid duplicates in undirected
                weighted.add_edge(u, v, default_weight)
    
    return weighted


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Weighted vs Unweighted Graphs Demonstration")
    
    # Unweighted graph
    print("Unweighted Graph:")
    unweighted = Graph(directed=False)
    unweighted.add_edge(0, 1)
    unweighted.add_edge(1, 2)
    unweighted.add_edge(0, 2)
    unweighted.display()
    print("  Note: All edges have implicit weight = 1")
    
    # Weighted graph
    print("\n" + "="*50)
    print("Weighted Graph:")
    weighted = WeightedGraph(directed=False)
    weighted.add_edge(0, 1, 5)
    weighted.add_edge(1, 2, 3)
    weighted.add_edge(0, 2, 10)
    weighted.display()
    print("  Note: Edges have explicit weights")
    
    # Convert unweighted to weighted
    print("\n" + "="*50)
    print("Converted Weighted Graph:")
    converted = make_weighted(unweighted, default_weight=1)
    converted.display()
    
    print("\n" + "="*50)
    print("WEIGHTED vs UNWEIGHTED SUMMARY")
    print("="*50)
    print("""
Unweighted Graph:
- All edges have same weight (typically 1)
- Represents: Connection exists or not
- Algorithms: BFS (shortest path), DFS
- Examples: Social networks, web links

Weighted Graph:
- Edges have different weights
- Represents: Distance, cost, time, capacity
- Algorithms: Dijkstra, Bellman-Ford, Floyd-Warshall
- Examples: Maps, network routing, resource allocation

Key Differences:
- Shortest path: BFS (unweighted) vs Dijkstra (weighted)
- Complexity: Weighted algorithms are more complex
- Applications: Weighted for real-world distances/costs
""")

