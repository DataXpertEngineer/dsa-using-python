"""
Trie (Prefix Tree) Data Structure

A trie is a tree-like data structure used to store strings for efficient
prefix matching and retrieval operations.

Why Trie?
---------
- Fast prefix search: O(m) where m is length of prefix
- Space efficient for common prefixes
- Useful for autocomplete, spell checkers, IP routing
- Better than hash table for prefix operations

Useful in:
- Autocomplete systems
- Spell checkers
- IP routing tables
- Dictionary implementations
"""

from typing import Dict, Optional, List


class TrieNode:
    """
    Node in a trie data structure.
    
    Each node contains:
    - children: Dictionary mapping characters to child nodes
    - is_end_of_word: Boolean indicating if this node marks end of a word
    """
    
    def __init__(self) -> None:
        """
        Initialize a trie node.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty node.
        """
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    """
    Trie (Prefix Tree) implementation.
    
    A trie is used to store strings where common prefixes are shared.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty trie.

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates root node.
        """
        self.root = TrieNode()
        self.word_count = 0
    
    def is_empty(self) -> bool:
        """
        Check if trie is empty.

        Returns:
            bool: True if trie is empty, False otherwise

        Complexity:
            Time: O(1)     - Constant time check.
            Space: O(1)   - No extra space used.
        """
        return self.word_count == 0
    
    def size(self) -> int:
        """
        Get number of words in trie.

        Returns:
            int: Number of words

        Complexity:
            Time: O(1)     - Constant time access.
            Space: O(1)   - No extra space used.
        """
        return self.word_count
    
    def get_all_words(self) -> List[str]:
        """
        Get all words stored in trie.

        Returns:
            List[str]: List of all words

        Complexity:
            Time: O(n * m)  - n words, m average length.
            Space: O(n * m) - Storage for all words.
        """
        words: List[str] = []
        
        def dfs(node: TrieNode, prefix: str) -> None:
            if node.is_end_of_word:
                words.append(prefix)
            
            for char, child in node.children.items():
                dfs(child, prefix + char)
        
        dfs(self.root, "")
        return words
    
    def display(self) -> None:
        """
        Display all words in trie.

        Complexity:
            Time: O(n * m)  - Traverses all words.
            Space: O(n * m) - Recursion stack.
        """
        words = self.get_all_words()
        if words:
            print("Words in trie:")
            for word in words:
                print(f"  - {word}")
        else:
            print("Trie is empty")


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Trie Data Structure Demonstration")
    
    trie = Trie()
    print(f"Trie created. Empty: {trie.is_empty()}")
    print(f"Size: {trie.size()}")
    
    print("\n" + "="*60)
    print("TRIE CONCEPTS SUMMARY")
    print("="*60)
    print("""
Trie Properties:
- Root node: Empty node at the top
- Each node: Represents a character
- Path from root: Represents a prefix or word
- is_end_of_word: Marks complete words
- Children: Dictionary of character → TrieNode

Example Structure:
    Root
    ├── 'a' → Node
    │   └── 'p' → Node
    │       └── 'p' → Node (is_end_of_word=True)  # "app"
    │           └── 'l' → Node
    │               └── 'e' → Node (is_end_of_word=True)  # "apple"
    └── 'b' → Node
        └── 'a' → Node
            └── 't' → Node (is_end_of_word=True)  # "bat"

Operations:
- Insert: O(m) where m is word length
- Search: O(m) where m is word length
- Prefix Search: O(m) where m is prefix length
- Space: O(ALPHABET_SIZE * N * M) where N is number of words, M is average length
""")

