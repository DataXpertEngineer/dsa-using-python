# Trees

A tree is a hierarchical data structure consisting of nodes connected by edges. Each tree has a root node, and nodes can have children, forming a parent-child relationship.

## 📁 Folder Structure

```
trees/
├── trees.py                              # Core tree concepts ⭐ MOST IMPORTANT
├── traversals/                            # Tree traversal techniques
│   ├── inorder_traversal.py              # Inorder traversal ⭐ MOST IMPORTANT
│   ├── preorder_traversal.py             # Preorder traversal ⭐ MOST IMPORTANT
│   └── postorder_traversal.py            # Postorder traversal ⭐ MOST IMPORTANT
├── tree_search_algorithms/               # Tree search algorithms
│   ├── depth_first_search.py            # DFS ⭐ MOST IMPORTANT
│   └── breadth_first_search.py           # BFS ⭐ MOST IMPORTANT
├── properties/                            # Key tree properties
│   ├── height.py                         # Height of a tree ⭐ MOST IMPORTANT
│   ├── diameter.py                       # Diameter of a tree ⭐ MOST IMPORTANT
│   └── lca.py                            # Lowest Common Ancestor ⭐ MOST IMPORTANT
└── interview_problems/                    # Typical tree interview questions
    ├── max_depth.py                      # Maximum depth of tree ⭐ MOST IMPORTANT
    ├── min_depth.py                      # Minimum depth of tree 🟡 MEDIUM
    ├── balanced_tree_check.py            # Check if tree is balanced 🟡 MEDIUM
    └── path_sum.py                       # Path sum problems 🟡 MEDIUM
```

## 📚 Definition and Concepts

### What is a Tree?

A **tree** is a hierarchical data structure that consists of nodes connected by edges. It represents relationships in a parent-child hierarchy.

#### Key Characteristics:

1. **Hierarchical Structure**: Data organized in levels
2. **Root Node**: Topmost node with no parent
3. **Parent-Child Relationship**: Each node (except root) has exactly one parent
4. **Acyclic**: No cycles (no path forms a loop)
5. **Connected**: Every node is reachable from root

### Tree Terminology

#### Basic Terms:

- **Root**: Topmost node (no parent)
- **Node**: Element in the tree containing data
- **Edge**: Connection between two nodes
- **Leaf**: Node with no children (terminal node)
- **Internal Node**: Node with at least one child
- **Parent**: Node that has children
- **Child**: Node directly below a parent
- **Sibling**: Nodes with the same parent
- **Ancestor**: Node on path from root to current node
- **Descendant**: Node reachable from current node
- **Subtree**: Tree formed by a node and all its descendants

#### Tree Properties:

- **Depth**: Number of edges from root to a node
- **Height**: Maximum depth of any node (or number of edges in longest path)
- **Level**: Set of nodes at the same depth
- **Degree**: Number of children a node has
- **Path**: Sequence of nodes from one to another
- **Size**: Total number of nodes in the tree

### Binary Tree

A **binary tree** is a tree where each node has at most two children:
- **Left Child**: Left subtree
- **Right Child**: Right subtree

#### Types of Binary Trees:

1. **Full Binary Tree**: Every node has 0 or 2 children
2. **Complete Binary Tree**: All levels filled except possibly last, filled left to right
3. **Perfect Binary Tree**: All internal nodes have 2 children, all leaves at same level
4. **Balanced Binary Tree**: Height difference between left and right subtrees ≤ 1
5. **Binary Search Tree (BST)**: Left < Root < Right (for all nodes)

### Tree Representation

#### Node Structure:
```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val      # Data
        self.left = left    # Left child
        self.right = right  # Right child
```

#### Array Representation (for complete binary trees):
- Root at index 0
- Left child of node at i: 2i + 1
- Right child of node at i: 2i + 2
- Parent of node at i: (i - 1) // 2

## 🔑 Tree Traversals

### 1. Inorder Traversal (`traversals/inorder_traversal.py`) ⭐
- **Order**: Left → Root → Right
- **Use Cases**: BST gives sorted order, expression trees (infix)
- **Time Complexity**: O(n)
- **Space Complexity**: O(h) where h is height

### 2. Preorder Traversal (`traversals/preorder_traversal.py`) ⭐
- **Order**: Root → Left → Right
- **Use Cases**: Tree copying, prefix expressions, serialization
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)

### 3. Postorder Traversal (`traversals/postorder_traversal.py`) ⭐
- **Order**: Left → Right → Root
- **Use Cases**: Tree deletion, postfix expressions, expression evaluation
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)

## 🔍 Tree Search Algorithms

### 1. Depth-First Search (`tree_search_algorithms/depth_first_search.py`) ⭐
- **How it works**: Explores as deep as possible before backtracking
- **Implementation**: Uses stack (recursion or explicit stack)
- **Use Cases**: Path finding, tree traversals
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)

### 2. Breadth-First Search (`tree_search_algorithms/breadth_first_search.py`) ⭐
- **How it works**: Explores level by level
- **Implementation**: Uses queue
- **Use Cases**: Level-order traversal, shortest path, level-based problems
- **Time Complexity**: O(n)
- **Space Complexity**: O(w) where w is maximum width

## 📏 Tree Properties

### 1. Height (`properties/height.py`) ⭐
- **Definition**: Maximum depth of any node
- **Empty tree**: Height = -1 (counting edges) or 0 (counting nodes)
- **Algorithm**: Recursively calculate max height of subtrees
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)

### 2. Diameter (`properties/diameter.py`) ⭐
- **Definition**: Longest path between any two nodes (number of edges)
- **May or may not pass through root**
- **Algorithm**: For each node, calculate diameter through it
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)

### 3. Lowest Common Ancestor (`properties/lca.py`) ⭐
- **Definition**: Deepest node that is ancestor of both nodes
- **Algorithm**: Recursively search, return node if both found in subtrees
- **Time Complexity**: O(n)
- **Space Complexity**: O(h)

## 💼 Interview Problems

### Most Important (⭐)

1. **Maximum Depth** (`interview_problems/max_depth.py`)
   - Find height of tree
   - **Algorithm**: Recursive or BFS
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(h)

### Medium Difficulty (🟡)

2. **Minimum Depth** (`interview_problems/min_depth.py`)
   - Find shortest path to leaf
   - **Algorithm**: Recursive or BFS (optimal)
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(h) or O(w)

3. **Balanced Tree Check** (`interview_problems/balanced_tree_check.py`)
   - Check if tree is height-balanced
   - **Algorithm**: Calculate height and check difference
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(h)

4. **Path Sum** (`interview_problems/path_sum.py`)
   - Find paths that sum to target
   - **Variations**: Existence, all paths, count paths
   - **Time Complexity**: O(n) to O(n²)
   - **Space Complexity**: O(h)

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Inorder Traversal | O(n) | O(h) |
| Preorder Traversal | O(n) | O(h) |
| Postorder Traversal | O(n) | O(h) |
| DFS | O(n) | O(h) |
| BFS | O(n) | O(w) |
| Height | O(n) | O(h) |
| Diameter | O(n) | O(h) |
| LCA | O(n) | O(h) |
| Max Depth | O(n) | O(h) |
| Min Depth | O(n) | O(h) or O(w) |
| Balanced Check | O(n) | O(h) |
| Path Sum | O(n) to O(n²) | O(h) |

Where:
- n = number of nodes
- h = height of tree
- w = maximum width of tree

## 🎓 Learning Path

1. **Start with**: `trees.py` - Understand tree structure and terminology
2. **Learn traversals**: 
   - `inorder_traversal.py` - Left → Root → Right
   - `preorder_traversal.py` - Root → Left → Right
   - `postorder_traversal.py` - Left → Right → Root
3. **Master search algorithms**: 
   - `depth_first_search.py` - DFS with stack
   - `breadth_first_search.py` - BFS with queue
4. **Understand properties**: 
   - `height.py` - Tree height calculation
   - `diameter.py` - Longest path
   - `lca.py` - Common ancestor
5. **Solve interview problems**: Start with ⭐ marked problems

## 💡 Key Insights

### Tree Structure:
1. **Hierarchical**: Natural for representing hierarchies
2. **Recursive**: Trees are recursive structures
3. **No Cycles**: Acyclic structure
4. **One Root**: Single entry point

### Traversals:
1. **Inorder for BST**: Produces sorted sequence
2. **Preorder for Copying**: Natural order for tree construction
3. **Postorder for Deletion**: Delete children before parent
4. **Level-order (BFS)**: Natural for level-based problems

### Search Algorithms:
1. **DFS**: Uses less memory, good for deep trees
2. **BFS**: Finds shortest path, good for level problems
3. **Choose based on problem**: DFS for paths, BFS for levels

### Properties:
1. **Height**: Important for balancing
2. **Diameter**: Measures tree "width"
3. **LCA**: Foundation for many tree problems

## 🔗 Related Topics

- **Recursion**: Natural for tree operations
- **Stacks**: Used in DFS and iterative traversals
- **Queues**: Used in BFS
- **Graphs**: Trees are special case of graphs
- **Binary Search Trees**: Sorted binary trees

## 📝 Notes

- All implementations include both recursive and iterative approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings
- Trees are fundamental to many algorithms and data structures

## 🚨 Common Pitfalls

1. **Null Checks**: Always check if node is None before accessing
2. **Base Cases**: Proper base cases in recursion
3. **Height vs Depth**: Height is max depth, depth is distance from root
4. **Leaf Nodes**: Nodes with no children, not just nodes with one child
5. **Path Problems**: Must reach leaf nodes in path sum problems

