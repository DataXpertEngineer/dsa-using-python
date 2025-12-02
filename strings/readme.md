# Strings in Python (Data Structures & Algorithms)

This folder focuses on **strings** as a fundamental data structure and how they are implemented and manipulated in Python.

You'll learn:

- The **DSA concept** of strings (independent of any language)
- String immutability and its implications
- How strings are **implemented in Python**
- String operations and their complexities
- Common string manipulation techniques and algorithms

---

## A. Strings (DSA Concept)

### 1. What is a String?

A **string** is a sequence of characters:

- Represents text data
- Can be viewed as an array of characters
- Has a fixed length (in many languages)
- Characters are typically stored in contiguous memory

**Structure:**
```
String: ['H', 'e', 'l', 'l', 'o']
Indices:   0    1    2    3    4
```

---

### 2. String Immutability

**Immutability** means strings cannot be changed after creation.

**In Python:**
- Strings are immutable objects
- Operations like `s[0] = 'h'` raise `TypeError`
- Operations that "modify" strings actually create new strings

**Implications:**
- `s1 + s2` creates a new string (O(n + m) time and space)
- String concatenation in loops can be inefficient
- Use `join()` for multiple concatenations (more efficient)

**Example:**
```python
s = "Hello"
s = s + " World"  # Creates new string "Hello World"
# Original "Hello" may be garbage collected
```

---

### 3. Strings vs Character Arrays

| Feature | Strings | Character Arrays |
|---------|---------|------------------|
| **Mutability** | Immutable (Python) | Mutable |
| **Type** | High-level abstraction | Low-level array |
| **Operations** | Rich set of methods | Basic array operations |
| **Memory** | Managed by interpreter | Manual management |

---

### 4. Strengths & Weaknesses of Strings

#### Strengths

- **Rich operations**: Many built-in methods (split, replace, find, etc.)
- **Easy to use**: High-level abstraction
- **Safe**: Immutability prevents accidental modifications
- **Efficient for read operations**: O(1) access by index

#### Weaknesses

- **Immutability**: Can't modify in-place (creates new strings)
- **Concatenation cost**: Creating new strings is expensive
- **Memory overhead**: Each operation may create new objects
- **No direct character modification**: Must create new string

---

### 5. Time & Space Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index `s[i]` | O(1) | O(1) |
| Slice `s[a:b]` | O(k) where k = b - a | O(k) |
| Concatenation `s1 + s2` | O(n + m) | O(n + m) |
| `join([s1, s2, ...])` | O(n) | O(n) |
| `len(s)` | O(1) | O(1) |
| `upper()`, `lower()` | O(n) | O(n) |
| `strip()` | O(n) | O(n) |
| `replace()` | O(n) | O(n) |
| `split()` | O(n) | O(n) |
| `find()`, `index()` | O(n) | O(1) |
| `count()` | O(n) | O(1) |
| `in` operator | O(n) | O(1) |
| `startswith()`, `endswith()` | O(k) | O(1) |
| Comparison `==`, `<`, `>` | O(min(n, m)) | O(1) |
| Iteration | O(n) | O(1) |

Where:
- n, m = lengths of strings
- k = length of substring/slice

---

## B. How Strings Are Implemented in Python

In Python, strings are **immutable sequences of Unicode characters**.

### 1. String Representation

**In Memory:**
- Characters stored as Unicode code points
- Internally uses UTF-8 or UTF-16 encoding
- Objects are stored on the heap
- String objects cache their length and hash

**Example:**
```python
s = "Hello"
# Internally: ['H', 'e', 'l', 'l', 'o'] as Unicode code points
```

### 2. String Interning

Python **interns** (caches) some strings:
- String literals
- Short strings
- Strings used as identifiers

**Benefits:**
- Memory efficiency (shared references)
- Faster comparisons (identity check before value check)

### 3. Common Operations

#### Concatenation

```python
# Inefficient (creates new strings)
result = ""
for s in strings:
    result += s  # O(n²) total time

# Efficient (uses join)
result = "".join(strings)  # O(n) total time
```

#### Slicing

```python
s = "Python"
s[1:4]    # "yth" - creates new string
s[::-1]   # "nohtyP" - reversed copy
```

---

## C. Common Techniques

### 1. Sliding Window

**Use Cases:**
- Longest substring without repeating characters
- Minimum window substring
- Substring with k distinct characters

**How it works:**
- Maintain a window of characters
- Expand and shrink window based on conditions
- Track window state (character frequencies, etc.)

### 2. Two Pointers

**Use Cases:**
- Palindrome checking
- Anagram checking
- Reverse string
- Valid palindrome (with special characters)

**How it works:**
- Two pointers start from both ends
- Move toward center based on conditions
- Process characters as pointers meet

### 3. Prefix Function (KMP)

**Use Cases:**
- Efficient pattern matching
- Finding longest border
- KMP algorithm preprocessing

**How it works:**
- Preprocess pattern to find longest proper prefix that is also a suffix
- Use this information to skip unnecessary comparisons

### 4. Rolling Hash (Rabin-Karp)

**Use Cases:**
- Substring search
- Pattern matching
- Hash-based string comparison

**How it works:**
- Compute hash of sliding window
- Update hash in O(1) when window slides
- Compare hashes (with verification for collisions)

---

## D. When to Use Strings

**Use strings when:**
- Working with text data
- Need rich text manipulation methods
- Immutability is beneficial (thread-safe, hashable)
- Text processing and parsing

**Consider alternatives when:**
- Need frequent modifications (use list of characters)
- Memory is critical (use bytearray for ASCII)
- Need mutable sequences (use list)

---

## E. Folder Structure

```
strings/
├── strings.py                      # Core string operations
│
├── techniques/                     # String manipulation techniques
│   ├── sliding_window.py           # Substring problems, window optimization
│   ├── two_pointers.py             # Palindrome, anagram, reverse
│   ├── prefix_function.py          # KMP preprocessing, pattern matching
│   └── hashing.py                  # Rolling hash, Rabin-Karp
│
├── algorithms/                     # Classic string algorithms
│   ├── searching.py                 # Naive search, KMP, Rabin-Karp
│   ├── sorting.py                  # Sorting strings, custom comparators
│   └── divide_and_conquer.py       # Longest common prefix, string divide & conquer
│
└── interview_problems/             # Common coding problems
    ├── reversal.py                 # Reverse string / words
    ├── longest_palindrome.py       # Longest palindromic substring
    ├── palindrome_check.py         # Check if string is a palindrome
    ├── anagram_check.py            # Check if two strings are anagrams
    ├── frequency_count.py          # Count character frequency
    └── substring_search.py         # Substring search (Naive/KMP)
```

---

## Summary

- Strings are **immutable sequences** of characters
- **Rich operations** but **concatenation can be expensive**
- **Common techniques**: Sliding window, two pointers, prefix function, rolling hash
- **Use when**: Working with text data, need text manipulation methods
- **Consider alternatives**: When frequent modifications are needed

Now you can explore the implementations in this folder to see these concepts in action!

