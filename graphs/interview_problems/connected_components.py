"""
Connected Components

Find connected components in undirected graph.

Problem Statement:
-------------------
Given an undirected graph, find all connected components.
A connected component is a maximal set of vertices where each vertex
is reachable from every other vertex.

Why Connected Components?
------------------------
- Important graph property
- Used in network analysis
- Foundation for many algorithms
- Common interview problem

Useful in:
- Network analysis
- Social network clustering
- Medium difficulty interview problems
"""

from typing import List, Set, Dict
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from graphs import Graph


# ----------------------------------------------------------------------
# Connected Components - DFS (Language-agnostic)
# ----------------------------------------------------------------------
def connected_components(graph: Graph) -> List[List[int]]:
    """
    Find all connected components using DFS.

    Algorithm:
    1. For each unvisited vertex, start DFS
    2. All vertices reached form one component
    3. Repeat until all vertices visited

    Args:
        graph (Graph): Undirected graph

    Returns:
        List[List[int]]: List of components

    Complexity:
        Time: O(V + E)  - Visits each vertex and edge once.
        Space: O(V)    - Visited set + recursion stack.
    """
    visited: Set[int] = set()
    components: List[List[int]] = []
    
    def dfs(vertex: int, component: List[int]) -> None:
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            component: List[int] = []
            dfs(vertex, component)
            components.append(component)
    
    return components


# ----------------------------------------------------------------------
# Count Connected Components
# ----------------------------------------------------------------------
def count_components(graph: Graph) -> int:
    """
    Count number of connected components.

    Args:
        graph (Graph): Undirected graph

    Returns:
        int: Number of components

    Complexity:
        Time: O(V + E)  - DFS traversal.
        Space: O(V)    - Visited set.
    """
    return len(connected_components(graph))


# ----------------------------------------------------------------------
# Is Connected
# ----------------------------------------------------------------------
def is_connected(graph: Graph) -> bool:
    """
    Check if graph is connected (single component).

    Args:
        graph (Graph): Undirected graph

    Returns:
        bool: True if connected

    Complexity:
        Time: O(V + E)  - Single DFS.
        Space: O(V)    - Visited set.
    """
    if not graph.get_vertices():
        return True
    
    return count_components(graph) == 1


# ----------------------------------------------------------------------
# Largest Component
# ----------------------------------------------------------------------
def largest_component(graph: Graph) -> List[int]:
    """
    Find largest connected component.

    Args:
        graph (Graph): Undirected graph

    Returns:
        List[int]: Largest component

    Complexity:
        Time: O(V + E)  - Finds all components.
        Space: O(V)    - Component storage.
    """
    components = connected_components(graph)
    if not components:
        return []
    
    return max(components, key=len)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Connected Components Demonstration")
    
    # Graph with multiple components
    graph = Graph(directed=False)
    # Component 1: 0-1-2
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    # Component 2: 3-4
    graph.add_edge(3, 4)
    # Component 3: 5 (isolated)
    graph.add_edge(5, 5)  # Self-loop, but still isolated
    
    print("Graph structure:")
    graph.display()
    
    components = connected_components(graph)
    print(f"\nConnected Components: {components}")
    print(f"Number of components: {count_components(graph)}")
    print(f"Is connected: {is_connected(graph)}")
    print(f"Largest component: {largest_component(graph)}")

