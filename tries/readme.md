# Tries (Prefix Trees)

A **trie** (pronounced "try") is a tree-like data structure used to store strings for efficient prefix matching and retrieval operations. It's also known as a prefix tree or digital tree.

## 📁 Folder Structure

```
tries/
├── trie.py                                 # Trie implementation from scratch ⭐ MOST IMPORTANT
├── insert.py                               # Insert words into trie ⭐ MOST IMPORTANT
├── search.py                               # Search prefix / exact word ⭐ MOST IMPORTANT
└── autocomplete.py                         # Autocomplete system 🟡 MEDIUM
```

## 📚 Definition and Concepts

### What is a Trie?

A **trie** is a tree data structure that stores strings by sharing common prefixes. Each node represents a character, and paths from root to nodes represent strings.

#### Key Characteristics:

1. **Prefix Sharing**: Common prefixes are stored once
2. **Root Node**: Empty node at the top
3. **Character Nodes**: Each node represents a character
4. **End Marker**: `is_end_of_word` marks complete words
5. **Children Dictionary**: Maps characters to child nodes

### Trie Structure

#### Visual Example:

```
        Root
       /    \
      'a'    'b'
       |      |
      'p'    'a'
       |      |
      'p'    't' (end)
       |
      'l'
       |
      'e' (end)
```

This trie stores: "app", "apple", "bat"

### Why Use Tries?

#### Advantages:

1. **Fast Prefix Search**: O(m) where m is prefix length
2. **Space Efficient**: Common prefixes shared
3. **Prefix Matching**: Natural for autocomplete
4. **No Hash Collisions**: Unlike hash tables
5. **Sorted Output**: In-order traversal gives sorted words

#### When to Use:

- ✅ Prefix matching required
- ✅ Autocomplete systems
- ✅ Dictionary implementations
- ✅ Spell checkers
- ✅ IP routing tables

#### When NOT to Use:

- ❌ Exact match only (hash table better)
- ❌ No common prefixes (wasteful)
- ❌ Memory constrained (tries can use more space)

## 🔑 Core Operations

### 1. Trie Implementation (`trie.py`) ⭐

- **TrieNode**: Node with children dictionary and end marker
- **Trie**: Main trie class with root node
- **Time Complexity**: O(1) for initialization
- **Space Complexity**: O(ALPHABET_SIZE × N × M) where N is number of words, M is average length

**Key Methods:**
- `is_empty()`: Check if trie is empty
- `size()`: Get number of words
- `get_all_words()`: Retrieve all words
- `display()`: Display all words

### 2. Insert Operations (`insert.py`) ⭐

- **How it works**: Traverse/create path for each character
- **Time Complexity**: O(m) where m is word length
- **Space Complexity**: O(m) for new nodes
- **Use Cases**: Building dictionary, adding words

**Key Functions:**
- `insert_word()`: Insert single word
- `insert_words()`: Insert multiple words
- `TrieWithCount`: Trie with frequency tracking

### 3. Search Operations (`search.py`) ⭐

- **Exact Search**: Check if word exists
- **Prefix Search**: Check if prefix exists
- **Words with Prefix**: Find all words starting with prefix
- **Time Complexity**: O(m) for search, O(m + k) for prefix words
- **Space Complexity**: O(1) for search, O(k) for prefix words

**Key Functions:**
- `search_word()`: Exact word search
- `search_prefix()`: Prefix existence check
- `words_with_prefix()`: Get all words with prefix
- `longest_common_prefix()`: Find LCP of all words
- `delete_word()`: Remove word from trie

### 4. Autocomplete (`autocomplete.py`) 🟡

- **Basic Autocomplete**: Simple prefix matching
- **With Ranking**: Frequency-based suggestions
- **With Hot Keys**: Learn from user selections
- **Time Complexity**: O(m + k) to O(m + n log k)
- **Space Complexity**: O(k) to O(n)

**Key Classes:**
- `AutocompleteSystem`: Basic autocomplete
- `AutocompleteWithRanking`: Frequency-based ranking
- `AutocompleteWithHotKeys`: Learning from user input

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(m) | O(m) |
| Search (exact) | O(m) | O(1) |
| Search (prefix) | O(m) | O(1) |
| Words with prefix | O(m + k) | O(k) |
| Delete | O(m) | O(m) |
| Autocomplete | O(m + k) | O(k) |

Where:
- m = length of word/prefix
- k = number of words with prefix
- n = number of words in trie

## 🎓 Learning Path

1. **Start with**: `trie.py` - Understand trie structure
2. **Learn insertion**: `insert.py` - How to build trie
3. **Master search**: `search.py` - Core search operations
4. **Build applications**: `autocomplete.py` - Real-world use case

## 💡 Key Insights

### Trie Structure:
1. **Root is Empty**: Root node has no character
2. **Path = Word**: Path from root represents word/prefix
3. **Shared Prefixes**: Common prefixes stored once
4. **End Marker**: `is_end_of_word` distinguishes words from prefixes

### Operations:
1. **Insert**: Create path character by character
2. **Search**: Traverse path, check end marker
3. **Prefix**: Similar to search but no end marker check
4. **Delete**: Remove nodes if no other words use them

### Applications:
1. **Autocomplete**: Natural fit for prefix matching
2. **Spell Checker**: Fast word validation
3. **IP Routing**: Longest prefix matching
4. **Dictionary**: Efficient word storage

## 🔗 Related Topics

- **Trees**: Tries are special trees
- **Hash Tables**: Alternative for exact match
- **String Algorithms**: String matching and search
- **Graphs**: Tries can be viewed as DAGs

## 📝 Notes

- All implementations include detailed docstrings
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles
- Both basic and advanced implementations included

## 🚨 Common Pitfalls

1. **Not Marking End**: Forgetting `is_end_of_word` flag
2. **Empty String**: Handle empty string edge case
3. **Case Sensitivity**: Decide on case handling
4. **Memory Usage**: Tries can use significant memory
5. **Deletion**: Properly handle node cleanup

## 🎯 Real-World Applications

### 1. Autocomplete Systems
- Search engines (Google, Bing)
- Code editors (IntelliSense)
- Mobile keyboards

### 2. Spell Checkers
- Word processors
- Text editors
- Email clients

### 3. IP Routing
- Longest prefix matching
- Network routing tables
- Firewall rules

### 4. Dictionary Implementations
- Word games (Scrabble)
- Crossword solvers
- Text analysis

## 🔍 Comparison with Other Data Structures

| Feature | Trie | Hash Table | Binary Search Tree |
|--------|------|------------|-------------------|
| Prefix Search | O(m) | O(n) | O(n) |
| Exact Search | O(m) | O(1) | O(log n) |
| Space | O(N×M) | O(N) | O(N) |
| Sorted Output | Yes | No | Yes |
| Prefix Sharing | Yes | No | No |

## 💻 Implementation Tips

1. **Use Dictionary**: Python dict for children (flexible)
2. **End Marker**: Always use boolean flag for word end
3. **Recursive DFS**: For collecting words
4. **Iterative Traversal**: For simple operations
5. **Memory Optimization**: Consider compressed tries for large datasets

