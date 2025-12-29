"""
Search in Trie

Search operations for finding words and prefixes in a trie.

Operations:
1. Exact word search: Check if word exists
2. Prefix search: Check if prefix exists
3. Words with prefix: Find all words starting with prefix

Why Search?
-----------
- Core trie functionality
- Fast prefix matching: O(m) time
- Foundation for autocomplete
- Efficient dictionary lookup

Useful in:
- Word validation
- Prefix matching
- Autocomplete systems
- Spell checkers
"""

from typing import List, Optional
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from trie import Trie, TrieNode


# ----------------------------------------------------------------------
# Exact Word Search (Language-agnostic)
# ----------------------------------------------------------------------
def search_word(trie: Trie, word: str) -> bool:
    """
    Search for exact word in trie.

    Args:
        trie (Trie): Trie data structure
        word (str): Word to search

    Returns:
        bool: True if word exists, False otherwise

    Complexity:
        Time: O(m)     - m is length of word.
        Space: O(1)   - Only uses variables.
    """
    if not word:
        return False
    
    current = trie.root
    
    for char in word:
        if char not in current.children:
            return False
        current = current.children[char]
    
    return current.is_end_of_word


# ----------------------------------------------------------------------
# Prefix Search
# ----------------------------------------------------------------------
def search_prefix(trie: Trie, prefix: str) -> bool:
    """
    Check if prefix exists in trie.

    Args:
        trie (Trie): Trie data structure
        prefix (str): Prefix to search

    Returns:
        bool: True if prefix exists, False otherwise

    Complexity:
        Time: O(m)     - m is length of prefix.
        Space: O(1)   - Only uses variables.
    """
    if not prefix:
        return True  # Empty prefix exists
    
    current = trie.root
    
    for char in prefix:
        if char not in current.children:
            return False
        current = current.children[char]
    
    return True


# ----------------------------------------------------------------------
# Find All Words with Prefix
# ----------------------------------------------------------------------
def words_with_prefix(trie: Trie, prefix: str) -> List[str]:
    """
    Find all words that start with given prefix.

    Args:
        trie (Trie): Trie data structure
        prefix (str): Prefix to search

    Returns:
        List[str]: List of words with prefix

    Complexity:
        Time: O(m + k)  - m is prefix length, k is number of words with prefix.
        Space: O(k)    - Storage for result words.
    """
    if not prefix:
        return trie.get_all_words()
    
    # Navigate to prefix node
    current = trie.root
    for char in prefix:
        if char not in current.children:
            return []
        current = current.children[char]
    
    # Collect all words from this node
    words: List[str] = []
    
    def dfs(node: TrieNode, suffix: str) -> None:
        if node.is_end_of_word:
            words.append(prefix + suffix)
        
        for char, child in node.children.items():
            dfs(child, suffix + char)
    
    dfs(current, "")
    return words


# ----------------------------------------------------------------------
# Longest Common Prefix
# ----------------------------------------------------------------------
def longest_common_prefix(trie: Trie) -> str:
    """
    Find longest common prefix of all words in trie.

    Args:
        trie (Trie): Trie data structure

    Returns:
        str: Longest common prefix

    Complexity:
        Time: O(m)     - m is length of shortest word.
        Space: O(1)   - Only uses variables.
    """
    if trie.is_empty():
        return ""
    
    prefix = ""
    current = trie.root
    
    # Traverse while node has exactly one child
    while len(current.children) == 1 and not current.is_end_of_word:
        char = next(iter(current.children))
        prefix += char
        current = current.children[char]
    
    return prefix


# ----------------------------------------------------------------------
# Delete Word
# ----------------------------------------------------------------------
def delete_word(trie: Trie, word: str) -> bool:
    """
    Delete word from trie.

    Args:
        trie (Trie): Trie data structure
        word (str): Word to delete

    Returns:
        bool: True if word was deleted, False if not found

    Complexity:
        Time: O(m)     - m is word length.
        Space: O(m)   - Recursion stack.
    """
    def delete_helper(node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        
        char = word[index]
        if char not in node.children:
            return False
        
        child = node.children[char]
        should_delete_child = delete_helper(child, word, index + 1)
        
        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        
        return False
    
    if not word:
        return False
    
    deleted = delete_helper(trie.root, word, 0)
    if deleted:
        trie.word_count -= 1
    return deleted


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Search in Trie Demonstration")
    
    trie = Trie()
    words = ["apple", "app", "application", "apply", "bat", "ball"]
    
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent))
    from insert import insert_words
    insert_words(trie, words)
    
    # Exact word search
    print("Exact word search:")
    print(f"  'app' exists: {search_word(trie, 'app')}")
    print(f"  'apps' exists: {search_word(trie, 'apps')}")
    
    # Prefix search
    print("\nPrefix search:")
    print(f"  Prefix 'app' exists: {search_prefix(trie, 'app')}")
    print(f"  Prefix 'xyz' exists: {search_prefix(trie, 'xyz')}")
    
    # Words with prefix
    print("\nWords with prefix 'app':")
    words_with_app = words_with_prefix(trie, "app")
    print(f"  {words_with_app}")
    
    # Longest common prefix
    print("\nLongest common prefix:")
    lcp = longest_common_prefix(trie)
    print(f"  {lcp}")
    
    # Delete word
    print("\nDelete word 'app':")
    deleted = delete_word(trie, "app")
    print(f"  Deleted: {deleted}")
    print(f"  'app' exists now: {search_word(trie, 'app')}")

