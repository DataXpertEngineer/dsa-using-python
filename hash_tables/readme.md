# Hash Tables

A hash table (hash map) is a data structure that implements an associative array, mapping keys to values using a hash function for efficient lookups.

## 📁 Folder Structure

```
hash_tables/
├── hash_tables.py                        # Core hash table operations ⭐ MOST IMPORTANT
├── concepts/                             # Core concepts
│   ├── hashing.py                        # Hash functions, modular hashing, string hashing ⭐ MOST IMPORTANT
│   └── collision_handling.py             # Chaining, open addressing, linear/quadratic probing ⭐ MOST IMPORTANT
├── applications/                         # Common hash table applications
│   ├── frequency_maps.py                 # Count element frequency in array/string ⭐ MOST IMPORTANT
│   ├── prefix_sum_optimization.py      # Prefix sum + hash for O(n) solutions ⭐ MOST IMPORTANT
│   └── two_three_sum.py                  # Two-sum, three-sum problems ⭐ MOST IMPORTANT
└── interview_problems/                   # Typical interview questions
    ├── subarray_sum_equals_k.py          # Count subarrays with sum = k ⭐ MOST IMPORTANT
    ├── longest_subarray_unique.py        # Longest subarray with unique elements ⭐ MOST IMPORTANT
    ├── group_anagrams.py                 # Group anagrams using hash map 🟡 MEDIUM
    └── first_unique_char.py              # Find first non-repeating character 🟡 MEDIUM
```

## 📚 Core Concepts

### Hash Table Operations

- **insert(key, value)**: Add key-value pair - O(1) average
- **get(key)**: Retrieve value by key - O(1) average
- **delete(key)**: Remove key-value pair - O(1) average
- **contains(key)**: Check if key exists - O(1) average

### Characteristics

- **Fast Lookups**: O(1) average time complexity
- **Hash Function**: Maps keys to indices
- **Collision Handling**: Multiple strategies (chaining, open addressing)
- **Dynamic**: Grows/shrinks as needed

## 🔑 Hash Functions

### 1. Modular Hashing (`concepts/hashing.py`) ⭐
- Formula: `h(k) = k mod m`
- Simple and effective
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

### 2. String Hashing (`concepts/hashing.py`) ⭐
- Polynomial rolling hash
- Formula: `hash(s) = (s[0] * base^0 + s[1] * base^1 + ...) mod m`
- **Time Complexity**: O(n) where n is string length
- **Space Complexity**: O(1)

## 🔄 Collision Handling

### 1. Chaining (`concepts/collision_handling.py`) ⭐
- Store multiple items in same bucket (linked list)
- **Advantages**: Simple, handles any number of collisions
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(n)

### 2. Linear Probing (`concepts/collision_handling.py`) ⭐
- Find next available slot: `h(k, i) = (h(k) + i) mod m`
- **Advantages**: Cache-friendly, no extra memory
- **Disadvantages**: Clustering problem
- **Time Complexity**: O(1) average

### 3. Quadratic Probing (`concepts/collision_handling.py`) ⭐
- Check slots at i² distance: `h(k, i) = (h(k) + i²) mod m`
- **Advantages**: Reduces clustering
- **Time Complexity**: O(1) average

## 🎯 Applications

### 1. Frequency Maps (`applications/frequency_maps.py`) ⭐
- Count element frequencies
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

### 2. Prefix Sum Optimization (`applications/prefix_sum_optimization.py`) ⭐
- Optimize subarray sum problems to O(n)
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

### 3. Two/Three Sum (`applications/two_three_sum.py`) ⭐
- Find pairs/triplets that sum to target
- **Time Complexity**: O(n) for two sum, O(n²) for three sum
- **Space Complexity**: O(n)

## 💼 Interview Problems

### Most Important (⭐)

1. **Subarray Sum Equals K** (`interview_problems/subarray_sum_equals_k.py`)
   - Count subarrays with sum = k
   - Uses prefix sum + hash table
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

2. **Longest Subarray with Unique Elements** (`interview_problems/longest_subarray_unique.py`)
   - Find longest subarray with all unique elements
   - Uses sliding window + hash table
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

3. **Group Anagrams** (`interview_problems/group_anagrams.py`)
   - Group strings that are anagrams
   - Uses sorted string as key
   - **Time Complexity**: O(n * k log k)
   - **Space Complexity**: O(n * k)

4. **First Unique Character** (`interview_problems/first_unique_char.py`)
   - Find first non-repeating character
   - Uses frequency map
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(k)

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| insert() | O(1) average | O(1) |
| get() | O(1) average | O(1) |
| delete() | O(1) average | O(1) |
| contains() | O(1) average | O(1) |
| Frequency Map | O(n) | O(n) |
| Two Sum | O(n) | O(n) |
| Three Sum | O(n²) | O(n) |
| Subarray Sum K | O(n) | O(n) |
| Longest Unique Subarray | O(n) | O(n) |
| Group Anagrams | O(n * k log k) | O(n * k) |
| First Unique Char | O(n) | O(k) |

## 🎓 Learning Path

1. **Start with**: `hash_tables.py` - Understand basic operations
2. **Learn concepts**: 
   - `hashing.py` - Hash functions
   - `collision_handling.py` - Collision resolution strategies
3. **Practice applications**: 
   - `frequency_maps.py` - Counting frequencies
   - `prefix_sum_optimization.py` - Optimizing subarray problems
   - `two_three_sum.py` - Pair/triplet finding
4. **Solve interview problems**: Start with ⭐ marked problems
5. **Advanced topics**: Explore anagram grouping and unique character problems

## 💡 Key Insights

1. **O(1) Average**: Hash tables provide O(1) average time for operations
2. **Hash Function**: Good hash function distributes keys uniformly
3. **Collision Handling**: Essential for hash table performance
4. **Prefix Sum + Hash**: Powerful combination for O(n) solutions
5. **Python dict**: Built-in hash table implementation

## 🔗 Related Topics

- **Arrays**: Array-based hash table implementation
- **Linked Lists**: Used in chaining collision resolution
- **Strings**: String hashing for efficient string operations
- **Stacks/Queues**: Used with hash tables in some problems

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings
- Python's `dict` is implemented as a hash table

