"""
Detect Cycle in Graph

Detect if a cycle exists in directed or undirected graph.

Problem Statement:
-------------------
Given a graph, determine if it contains a cycle.

Why Detect Cycle?
-----------------
- Important graph property
- Prevents infinite loops
- Required for topological sort
- Common interview problem

Useful in:
- Graph validation
- Dependency checking
- Common interview problems
"""

from typing import Set, Dict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from graphs import Graph


# ----------------------------------------------------------------------
# Detect Cycle - Undirected Graph (Language-agnostic)
# ----------------------------------------------------------------------
def has_cycle_undirected(graph: Graph) -> bool:
    """
    Detect cycle in undirected graph using DFS.

    Algorithm:
    - Use DFS to traverse graph
    - If we find an edge to already visited node (not parent), cycle exists

    Args:
        graph (Graph): Undirected graph

    Returns:
        bool: True if cycle exists

    Complexity:
        Time: O(V + E)  - DFS traversal.
        Space: O(V)    - Visited set + recursion stack.
    """
    visited: Set[int] = set()
    
    def has_cycle_dfs(vertex: int, parent: int) -> bool:
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if has_cycle_dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                # Found edge to visited node that's not parent
                return True
        
        return False
    
    # Check each component
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if has_cycle_dfs(vertex, -1):
                return True
    
    return False


# ----------------------------------------------------------------------
# Detect Cycle - Directed Graph
# ----------------------------------------------------------------------
def has_cycle_directed(graph: Graph) -> bool:
    """
    Detect cycle in directed graph using DFS with recursion stack.

    Algorithm:
    - Use DFS with recursion stack
    - If we find edge to node in recursion stack, cycle exists

    Args:
        graph (Graph): Directed graph

    Returns:
        bool: True if cycle exists

    Complexity:
        Time: O(V + E)  - DFS traversal.
        Space: O(V)    - Visited set + recursion stack.
    """
    visited: Set[int] = set()
    rec_stack: Set[int] = set()
    
    def has_cycle_dfs(vertex: int) -> bool:
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if has_cycle_dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                # Found edge to node in recursion stack
                return True
        
        rec_stack.remove(vertex)
        return False
    
    # Check each component
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if has_cycle_dfs(vertex):
                return True
    
    return False


# ----------------------------------------------------------------------
# Detect Cycle - Generic
# ----------------------------------------------------------------------
def has_cycle(graph: Graph) -> bool:
    """
    Detect cycle in graph (handles both directed and undirected).

    Args:
        graph (Graph): Graph to check

    Returns:
        bool: True if cycle exists

    Complexity:
        Time: O(V + E)  - DFS traversal.
        Space: O(V)    - Visited set + recursion stack.
    """
    if graph.directed:
        return has_cycle_directed(graph)
    else:
        return has_cycle_undirected(graph)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Detect Cycle in Graph Demonstration")
    
    # Undirected graph with cycle
    print("Undirected Graph with Cycle:")
    graph1 = Graph(directed=False)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)  # Creates cycle
    print(f"  Has cycle: {has_cycle(graph1)}")
    
    # Undirected graph without cycle (tree)
    print("\nUndirected Graph without Cycle (Tree):")
    graph2 = Graph(directed=False)
    graph2.add_edge(0, 1)
    graph2.add_edge(1, 2)
    graph2.add_edge(1, 3)
    print(f"  Has cycle: {has_cycle(graph2)}")
    
    # Directed graph with cycle
    print("\nDirected Graph with Cycle:")
    graph3 = Graph(directed=True)
    graph3.add_edge(0, 1)
    graph3.add_edge(1, 2)
    graph3.add_edge(2, 0)  # Creates cycle
    print(f"  Has cycle: {has_cycle(graph3)}")
    
    # Directed graph without cycle (DAG)
    print("\nDirected Graph without Cycle (DAG):")
    graph4 = Graph(directed=True)
    graph4.add_edge(0, 1)
    graph4.add_edge(1, 2)
    graph4.add_edge(0, 2)
    print(f"  Has cycle: {has_cycle(graph4)}")

