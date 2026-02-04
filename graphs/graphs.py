"""
Graph Data Structure

A graph is a collection of nodes (vertices) connected by edges.
Graphs are fundamental in computer science for modeling relationships.

Why Graphs?
----------
- Model real-world relationships
- Foundation for many algorithms
- Used in social networks, maps, web pages
- Essential for path finding, network analysis

Useful in:
- Social networks
- Maps and navigation
- Web crawling
- Network analysis
"""

from typing import Dict, List, Set, Optional
from collections import defaultdict


# ----------------------------------------------------------------------
# Graph - Adjacency List Representation (Language-agnostic)
# ----------------------------------------------------------------------
class Graph:
    """
    Graph implementation using adjacency list.
    
    Adjacency list: Each node stores list of its neighbors.
    Efficient for sparse graphs.
    """
    
    def __init__(self, directed: bool = False):
        """
        Initialize graph.

        Args:
            directed (bool): True for directed graph, False for undirected

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty graph.
        """
        self.graph: Dict[int, List[int]] = defaultdict(list)
        self.directed = directed
        self.vertices: Set[int] = set()
    
    def add_edge(self, u: int, v: int):
        """
        Add edge between vertices u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Complexity:
            Time: O(1)     - Constant time addition.
            Space: O(1)   - Adds one edge.
        """
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        
        if not self.directed:
            self.graph[v].append(u)
    
    def remove_edge(self, u: int, v: int):
        """
        Remove edge between vertices u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Complexity:
            Time: O(degree(u))  - Must find edge in adjacency list.
            Space: O(1)       - Only uses variables.
        """
        if v in self.graph[u]:
            self.graph[u].remove(v)
        
        if not self.directed and u in self.graph[v]:
            self.graph[v].remove(u)
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """
        Get neighbors of vertex.

        Args:
            vertex (int): Vertex

        Returns:
            List[int]: List of neighbors

        Complexity:
            Time: O(1)     - Returns list reference.
            Space: O(1)   - Returns existing list.
        """
        return self.graph[vertex]
    
    def has_edge(self, u: int, v: int):
        """
        Check if edge exists between u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Returns:
            bool: True if edge exists

        Complexity:
            Time: O(degree(u))  - Must check neighbors.
            Space: O(1)        - Only uses variables.
        """
        return v in self.graph[u]
    
    def get_vertices(self) -> List[int]:
        """
        Get all vertices.

        Returns:
            List[int]: List of vertices

        Complexity:
            Time: O(V)     - V is number of vertices.
            Space: O(V)   - Returns list of vertices.
        """
        return list(self.vertices)
    
    def get_edges(self) -> List[tuple]:
        """
        Get all edges.

        Returns:
            List[tuple]: List of (u, v) edges

        Complexity:
            Time: O(V + E)  - V vertices, E edges.
            Space: O(E)    - Returns list of edges.
        """
        edges = []
        visited_edges = set()
        
        for u in self.graph:
            for v in self.graph[u]:
                if not self.directed:
                    edge = tuple(sorted((u, v)))
                    if edge not in visited_edges:
                        edges.append((u, v))
                        visited_edges.add(edge)
                else:
                    edges.append((u, v))
        
        return edges
    
    def display(self):
        """Display graph structure."""
        print("Graph (Adjacency List):")
        for vertex in sorted(self.vertices):
            neighbors = self.graph[vertex]
            print(f"  {vertex}: {neighbors}")


# ----------------------------------------------------------------------
# Graph - Adjacency Matrix Representation
# ----------------------------------------------------------------------
class GraphMatrix:
    """
    Graph implementation using adjacency matrix.
    
    Adjacency matrix: 2D array where matrix[i][j] = 1 if edge exists.
    Efficient for dense graphs, fast edge lookup.
    """
    
    def __init__(self, num_vertices: int, directed: bool = False):
        """
        Initialize graph with adjacency matrix.

        Args:
            num_vertices (int): Number of vertices
            directed (bool): True for directed graph

        Complexity:
            Time: O(V²)    - Initialize V×V matrix.
            Space: O(V²)  - Stores V×V matrix.
        """
        self.num_vertices = num_vertices
        self.matrix: List[List[int]] = [[0] * num_vertices for _ in range(num_vertices)]
        self.directed = directed
    
    def add_edge(self, u: int, v: int):
        """
        Add edge between vertices u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Complexity:
            Time: O(1)     - Constant time matrix update.
            Space: O(1)   - Updates one cell.
        """
        self.matrix[u][v] = 1
        if not self.directed:
            self.matrix[v][u] = 1
    
    def remove_edge(self, u: int, v: int):
        """
        Remove edge between vertices u and v.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Complexity:
            Time: O(1)     - Constant time matrix update.
            Space: O(1)   - Updates one cell.
        """
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0
    
    def has_edge(self, u: int, v: int):
        """
        Check if edge exists.

        Args:
            u (int): Source vertex
            v (int): Destination vertex

        Returns:
            bool: True if edge exists

        Complexity:
            Time: O(1)     - Constant time matrix lookup.
            Space: O(1)   - Only uses variables.
        """
        return self.matrix[u][v] == 1
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """
        Get neighbors of vertex.

        Args:
            vertex (int): Vertex

        Returns:
            List[int]: List of neighbors

        Complexity:
            Time: O(V)     - Must scan row.
            Space: O(V)   - Returns list of neighbors.
        """
        neighbors = []
        for v in range(self.num_vertices):
            if self.matrix[vertex][v] == 1:
                neighbors.append(v)
        return neighbors
    
    def display(self):
        """Display adjacency matrix."""
        print("Graph (Adjacency Matrix):")
        print("   ", end="")
        for i in range(self.num_vertices):
            print(f"{i:3}", end="")
        print()
        for i in range(self.num_vertices):
            print(f"{i:3}", end="")
            for j in range(self.num_vertices):
                print(f"{self.matrix[i][j]:3}", end="")
            print()


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Graph Data Structure Demonstration")
    
    # Adjacency list
    graph = Graph(directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    
    graph.display()
    
    print("\n" + "="*60)
    print("GRAPH CONCEPTS SUMMARY")
    print("="*60)
    print("""
Graph Properties:
- Vertex (Node): Element in graph
- Edge: Connection between vertices
- Directed: Edges have direction (u → v)
- Undirected: Edges are bidirectional (u ↔ v)
- Weighted: Edges have weights/costs
- Unweighted: All edges have same weight (1)

Representations:
1. Adjacency List: List of neighbors for each vertex
   - Space: O(V + E)
   - Edge lookup: O(degree(v))
   - Good for sparse graphs

2. Adjacency Matrix: 2D array
   - Space: O(V²)
   - Edge lookup: O(1)
   - Good for dense graphs

Operations:
- Add edge: O(1) list, O(1) matrix
- Remove edge: O(degree(v)) list, O(1) matrix
- Check edge: O(degree(v)) list, O(1) matrix
- Get neighbors: O(degree(v)) list, O(V) matrix
""")

