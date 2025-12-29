# Graphs

A **graph** is a collection of nodes (vertices) connected by edges. Graphs are fundamental in computer science for modeling relationships and are used in many real-world applications.

## 📁 Folder Structure

```
graphs/
├── graphs.py                               # Graph representation (adjacency list/matrix) ⭐ MOST IMPORTANT
├── dfs.py                                  # Depth-First Search ⭐ MOST IMPORTANT
├── bfs.py                                  # Breadth-First Search ⭐ MOST IMPORTANT
├── directed_undirected.py                  # Directed vs Undirected graphs 🟡 MEDIUM
├── weighted_unweighted.py                  # Weighted vs Unweighted graphs 🟡 MEDIUM
├── algorithms/                             # Important graph algorithms
│   ├── dijkstra.py                         # Dijkstra's shortest path ⭐ MOST IMPORTANT
│   ├── prim_mst.py                         # Prim's Minimum Spanning Tree ⭐ MOST IMPORTANT
│   ├── kruskal_mst.py                      # Kruskal's Minimum Spanning Tree ⭐ MOST IMPORTANT
│   └── union_find.py                       # Union-Find / Disjoint Set Union ⭐ MOST IMPORTANT
└── interview_problems/                     # Typical graph interview questions
    ├── detect_cycle.py                     # Detect cycle in graph ⭐ MOST IMPORTANT
    ├── connected_components.py             # Connected components 🟡 MEDIUM
    └── shortest_path_bfs.py                # Shortest path unweighted graph ⭐ MOST IMPORTANT
```

## 📚 Definition and Concepts

### What is a Graph?

A **graph** G = (V, E) consists of:
- **V**: Set of vertices (nodes)
- **E**: Set of edges (connections between vertices)

#### Key Characteristics:

1. **Vertices (Nodes)**: Elements in the graph
2. **Edges**: Connections between vertices
3. **Directed/Undirected**: Edges may have direction
4. **Weighted/Unweighted**: Edges may have weights
5. **Cyclic/Acyclic**: May or may not contain cycles

### Graph Terminology

#### Basic Terms:

- **Vertex (Node)**: Element in graph
- **Edge**: Connection between two vertices
- **Degree**: Number of edges connected to vertex
- **Path**: Sequence of vertices connected by edges
- **Cycle**: Path that starts and ends at same vertex
- **Connected**: All vertices reachable from each other
- **Component**: Maximal connected subgraph

#### Graph Types:

1. **Directed Graph**: Edges have direction (u → v)
2. **Undirected Graph**: Edges are bidirectional (u ↔ v)
3. **Weighted Graph**: Edges have weights/costs
4. **Unweighted Graph**: All edges have same weight
5. **DAG**: Directed Acyclic Graph (no cycles)
6. **Tree**: Connected acyclic graph
7. **Forest**: Collection of trees

### Graph Representations

#### 1. Adjacency List (`graphs.py`)

- **Structure**: Each vertex stores list of neighbors
- **Space**: O(V + E)
- **Edge Lookup**: O(degree(v))
- **Best For**: Sparse graphs

```python
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
```

#### 2. Adjacency Matrix (`graphs.py`)

- **Structure**: 2D array where matrix[i][j] = 1 if edge exists
- **Space**: O(V²)
- **Edge Lookup**: O(1)
- **Best For**: Dense graphs

```python
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
```

## 🔑 Core Algorithms

### 1. Depth-First Search (`dfs.py`) ⭐

- **How it works**: Explores as deep as possible before backtracking
- **Implementation**: Stack (recursion or explicit)
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Use Cases**: Path finding, cycle detection, topological sort

**Key Functions:**
- `dfs_recursive()`: Recursive DFS
- `dfs_iterative()`: Iterative DFS with stack
- `dfs_find_path()`: Find path between vertices
- `dfs_all_paths()`: Find all paths

### 2. Breadth-First Search (`bfs.py`) ⭐

- **How it works**: Explores level by level
- **Implementation**: Queue
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Use Cases**: Shortest path (unweighted), level-order traversal

**Key Functions:**
- `bfs()`: Basic BFS traversal
- `bfs_levels()`: Level-by-level traversal
- `bfs_shortest_path()`: Shortest path using BFS
- `bfs_distances()`: Calculate distances from start

## 🎯 Graph Types

### 1. Directed vs Undirected (`directed_undirected.py`) 🟡

- **Directed**: Edges have direction (u → v)
- **Undirected**: Edges are bidirectional (u ↔ v)
- **In-degree**: Number of incoming edges (directed)
- **Out-degree**: Number of outgoing edges (directed)

### 2. Weighted vs Unweighted (`weighted_unweighted.py`) 🟡

- **Unweighted**: All edges have same weight (typically 1)
- **Weighted**: Edges have different weights
- **Algorithms**: BFS (unweighted) vs Dijkstra (weighted)

## 🔑 Graph Algorithms

### 1. Dijkstra's Algorithm (`algorithms/dijkstra.py`) ⭐

- **Problem**: Shortest path from source to all vertices
- **Requirements**: Non-negative edge weights
- **Time Complexity**: O((V + E) log V) with priority queue, O(V²) with array
- **Space Complexity**: O(V)
- **Use Cases**: Network routing, GPS navigation

**Key Functions:**
- `dijkstra()`: Find shortest distances to all vertices
- `dijkstra_path()`: Find shortest path to target
- `dijkstra_array()`: Array-based implementation

### 2. Prim's MST (`algorithms/prim_mst.py`) ⭐

- **Problem**: Find minimum spanning tree
- **Approach**: Greedy, vertex-based
- **Time Complexity**: O((V + E) log V) with priority queue, O(V²) with array
- **Space Complexity**: O(V)
- **Use Cases**: Network design, cluster analysis

**Key Functions:**
- `prim_mst()`: Find MST using priority queue
- `prim_mst_array()`: Array-based implementation
- `mst_total_weight()`: Calculate total MST weight

### 3. Kruskal's MST (`algorithms/kruskal_mst.py`) ⭐

- **Problem**: Find minimum spanning tree
- **Approach**: Greedy, edge-based
- **Time Complexity**: O(E log E) or O(E log V)
- **Space Complexity**: O(V)
- **Use Cases**: Network design, sparse graphs

**Key Functions:**
- `kruskal_mst()`: Find MST using union-find
- `kruskal_mst_alt()`: Alternative implementation

### 4. Union-Find (`algorithms/union_find.py`) ⭐

- **Problem**: Track disjoint sets efficiently
- **Operations**: Find, Union, Connected
- **Time Complexity**: O(α(n)) amortized (nearly constant)
- **Space Complexity**: O(n)
- **Use Cases**: Kruskal's MST, cycle detection, connected components

**Key Classes:**
- `UnionFind`: Full implementation with path compression and union by rank
- `UnionFindSimple`: Simplified version without rank

## 💼 Interview Problems

### Most Important (⭐)

1. **Detect Cycle** (`interview_problems/detect_cycle.py`)
   - Check if graph contains cycle
   - **Algorithm**: DFS with parent tracking (undirected) or recursion stack (directed)
   - **Time Complexity**: O(V + E)
   - **Space Complexity**: O(V)

2. **Shortest Path BFS** (`interview_problems/shortest_path_bfs.py`)
   - Find shortest path in unweighted graph
   - **Algorithm**: BFS with parent tracking
   - **Time Complexity**: O(V + E)
   - **Space Complexity**: O(V)

### Medium Difficulty (🟡)

3. **Connected Components** (`interview_problems/connected_components.py`)
   - Find all connected components
   - **Algorithm**: DFS for each unvisited vertex
   - **Time Complexity**: O(V + E)
   - **Space Complexity**: O(V)

## 📊 Complexity Analysis

| Operation | Adjacency List | Adjacency Matrix |
|-----------|---------------|------------------|
| Add Edge | O(1) | O(1) |
| Remove Edge | O(degree(v)) | O(1) |
| Check Edge | O(degree(v)) | O(1) |
| Get Neighbors | O(degree(v)) | O(V) |
| Space | O(V + E) | O(V²) |

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |
| Cycle Detection | O(V + E) | O(V) |
| Connected Components | O(V + E) | O(V) |
| Shortest Path (BFS) | O(V + E) | O(V) |
| Dijkstra (PQ) | O((V + E) log V) | O(V) |
| Dijkstra (Array) | O(V²) | O(V) |
| Prim's MST (PQ) | O((V + E) log V) | O(V) |
| Prim's MST (Array) | O(V²) | O(V) |
| Kruskal's MST | O(E log E) | O(V) |
| Union-Find | O(α(n)) amortized | O(n) |

Where:
- V = number of vertices
- E = number of edges

## 🎓 Learning Path

1. **Start with**: `graphs.py` - Understand graph representation
2. **Learn traversals**: 
   - `dfs.py` - Depth-first search
   - `bfs.py` - Breadth-first search
3. **Understand types**: 
   - `directed_undirected.py` - Graph directions
   - `weighted_unweighted.py` - Edge weights
4. **Master algorithms**: 
   - `dijkstra.py` - Shortest path (weighted)
   - `prim_mst.py` - MST (vertex-based)
   - `kruskal_mst.py` - MST (edge-based)
   - `union_find.py` - Disjoint sets
5. **Solve problems**: 
   - `detect_cycle.py` - Cycle detection
   - `connected_components.py` - Components
   - `shortest_path_bfs.py` - Shortest path

## 💡 Key Insights

### Graph Representation:
1. **Adjacency List**: Better for sparse graphs
2. **Adjacency Matrix**: Better for dense graphs, fast edge lookup
3. **Choose based on**: Graph density and operations needed

### Traversals:
1. **DFS**: Explores deep, uses stack, good for paths
2. **BFS**: Explores wide, uses queue, good for shortest path
3. **Choose based on**: Problem requirements

### Graph Properties:
1. **Directed**: One-way relationships (web links, dependencies)
2. **Undirected**: Two-way relationships (friendships, roads)
3. **Weighted**: Real-world distances/costs
4. **Unweighted**: Simple connectivity

## 🔗 Related Topics

- **Trees**: Special case of graphs (connected, acyclic)
- **Tries**: Tree-like structure for strings
- **Dynamic Programming**: Many graph problems use DP
- **Greedy Algorithms**: Used in shortest path algorithms

## 📝 Notes

- All implementations include detailed docstrings
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles
- Both adjacency list and matrix representations included

## 🚨 Common Pitfalls

1. **Visited Set**: Always mark visited to avoid infinite loops
2. **Directed vs Undirected**: Handle edge direction correctly
3. **Self-loops**: Consider self-loops in cycle detection
4. **Multiple Components**: Check all components, not just one
5. **Path Reconstruction**: Track parents for path finding

## 🎯 Real-World Applications

### 1. Social Networks
- Friends relationships (undirected)
- Follow relationships (directed)
- Friend suggestions (BFS)

### 2. Maps and Navigation
- Roads (weighted, undirected)
- Shortest path (Dijkstra, BFS)
- Route planning

### 3. Web Crawling
- Web pages as vertices
- Links as edges (directed)
- BFS for crawling

### 4. Dependency Management
- Package dependencies (directed, acyclic)
- Topological sort
- Cycle detection

