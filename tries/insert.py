"""
Insert Words into Trie

Insert operations for adding words to a trie data structure.

Why Insert?
-----------
- Fundamental trie operation
- Builds the trie structure
- Required before any search operations
- Efficient: O(m) time where m is word length

Useful in:
- Building dictionaries
- Creating autocomplete systems
- Setting up prefix trees
"""

from typing import List
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from trie import Trie, TrieNode


# ----------------------------------------------------------------------
# Insert Single Word (Language-agnostic)
# ----------------------------------------------------------------------
def insert_word(trie: Trie, word: str) -> None:
    """
    Insert a single word into trie.

    Algorithm:
    1. Start from root
    2. For each character in word:
       - If character not in children, create new node
       - Move to child node
    3. Mark last node as end of word

    Args:
        trie (Trie): Trie data structure
        word (str): Word to insert

    Complexity:
        Time: O(m)     - m is length of word, one operation per character.
        Space: O(m)    - Creates nodes for new characters.
    """
    if not word:
        return
    
    current = trie.root
    
    for char in word:
        if char not in current.children:
            current.children[char] = TrieNode()
        current = current.children[char]
    
    # Mark end of word (only if not already marked)
    if not current.is_end_of_word:
        current.is_end_of_word = True
        trie.word_count += 1


# ----------------------------------------------------------------------
# Insert Multiple Words
# ----------------------------------------------------------------------
def insert_words(trie: Trie, words: List[str]) -> None:
    """
    Insert multiple words into trie.

    Args:
        trie (Trie): Trie data structure
        words (List[str]): List of words to insert

    Complexity:
        Time: O(n * m)  - n words, m average length.
        Space: O(n * m) - Storage for all words.
    """
    for word in words:
        insert_word(trie, word)


# ----------------------------------------------------------------------
# Insert with Frequency Count
# ----------------------------------------------------------------------
class TrieNodeWithCount(TrieNode):
    """Trie node with frequency count."""
    
    def __init__(self):
        super().__init__()
        self.count = 0


class TrieWithCount:
    """Trie that tracks word frequency."""
    
    def __init__(self):
        self.root = TrieNodeWithCount()
        self.word_count = 0
    
    def insert(self, word: str):
        """
        Insert word and increment count.

        Args:
            word (str): Word to insert

        Complexity:
            Time: O(m)     - m is word length.
            Space: O(m)   - Creates nodes if needed.
        """
        if not word:
            return
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNodeWithCount()
            current = current.children[char]
        
        if not current.is_end_of_word:
            self.word_count += 1
        
        current.is_end_of_word = True
        current.count += 1
    
    def get_frequency(self, word: str):
        """
        Get frequency of word.

        Args:
            word (str): Word to check

        Returns:
            int: Frequency count, 0 if not found

        Complexity:
            Time: O(m)     - m is word length.
            Space: O(1)   - Only uses variables.
        """
        current = self.root
        
        for char in word:
            if char not in current.children:
                return 0
            current = current.children[char]
        
        return current.count if current.is_end_of_word else 0


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Insert Words into Trie Demonstration")
    
    # Basic insert
    trie = Trie()
    words = ["apple", "app", "application", "apply"]
    
    print(f"Inserting words: {words}")
    for word in words:
        insert_word(trie, word)
    
    print(f"\nTrie size: {trie.size()}")
    trie.display()
    
    # Insert multiple at once
    print("\n" + "="*50)
    trie2 = Trie()
    words2 = ["bat", "ball", "bad", "banana"]
    print(f"Inserting words: {words2}")
    insert_words(trie2, words2)
    trie2.display()
    
    # With frequency count
    print("\n" + "="*50)
    trie3 = TrieWithCount()
    words3 = ["hello", "hello", "world", "hello"]
    print(f"Inserting words with counts: {words3}")
    for word in words3:
        trie3.insert(word)
    
    print(f"\nFrequency of 'hello': {trie3.get_frequency('hello')}")
    print(f"Frequency of 'world': {trie3.get_frequency('world')}")

