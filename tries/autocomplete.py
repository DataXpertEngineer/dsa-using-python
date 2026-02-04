"""
Autocomplete System using Trie

Implement an autocomplete system that suggests words based on prefix input.

Problem Statement:
-------------------
Given a dictionary of words, implement autocomplete that:
1. Suggests words as user types
2. Returns top k suggestions
3. Can rank by frequency or relevance

Why Autocomplete?
------------------
- Common real-world application
- Demonstrates trie power
- Used in search engines, IDEs, mobile keyboards
- Improves user experience

Useful in:
- Search engines
- Code editors
- Mobile keyboards
- Medium difficulty interview problems
"""

from typing import List, Tuple
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from trie import Trie, TrieNode


# ----------------------------------------------------------------------
# Basic Autocomplete (Language-agnostic)
# ----------------------------------------------------------------------
class AutocompleteSystem:
    """
    Autocomplete system using trie.
    """
    
    def __init__(self, words: List[str]):
        """
        Initialize autocomplete with dictionary.

        Args:
            words (List[str]): Dictionary of words

        Complexity:
            Time: O(n * m)  - n words, m average length.
            Space: O(n * m) - Trie storage.
        """
        self.trie = Trie()
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).parent))
        from insert import insert_words
        insert_words(self.trie, words)
    
    def autocomplete(self, prefix: str) -> List[str]:
        """
        Get autocomplete suggestions for prefix.

        Args:
            prefix (str): Input prefix

        Returns:
            List[str]: List of suggestions

        Complexity:
            Time: O(m + k)  - m is prefix length, k is number of suggestions.
            Space: O(k)    - Storage for suggestions.
        """
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).parent))
        from search import words_with_prefix
        return words_with_prefix(self.trie, prefix)


# ----------------------------------------------------------------------
# Autocomplete with Frequency Ranking
# ----------------------------------------------------------------------
class TrieNodeWithFreq(TrieNode):
    """Trie node with frequency for ranking."""
    
    def __init__(self):
        super().__init__()
        self.frequency = 0


class AutocompleteWithRanking:
    """
    Autocomplete system with frequency-based ranking.
    """
    
    def __init__(self, words: List[Tuple[str, int]] = None):
        """
        Initialize with words and their frequencies.

        Args:
            words (List[Tuple[str, int]]): List of (word, frequency) pairs
        """
        self.root = TrieNodeWithFreq()
        if words:
            for word, freq in words:
                self._insert(word, freq)
    
    def _insert(self, word: str, frequency: int):
        """Insert word with frequency."""
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNodeWithFreq()
            current = current.children[char]
        
        current.is_end_of_word = True
        current.frequency = max(current.frequency, frequency)
    
    def autocomplete(self, prefix: str, k: int = 5) -> List[str]:
        """
        Get top k autocomplete suggestions sorted by frequency.

        Args:
            prefix (str): Input prefix
            k (int): Number of suggestions

        Returns:
            List[str]: Top k suggestions

        Complexity:
            Time: O(m + n log k)  - m is prefix length, n is candidates, k is result size.
            Space: O(n)           - Storage for candidates.
        """
        # Navigate to prefix node
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Collect all words with frequencies
        candidates: List[Tuple[int, str]] = []
        
        def dfs(node: TrieNodeWithFreq, suffix: str):
            if node.is_end_of_word:
                candidates.append((node.frequency, prefix + suffix))
            
            for char, child in node.children.items():
                dfs(child, suffix + char)
        
        dfs(current, "")
        
        # Sort by frequency (descending), then alphabetically
        candidates.sort(key=lambda x: (-x[0], x[1]))
        
        # Return top k
        return [word for _, word in candidates[:k]]


# ----------------------------------------------------------------------
# Autocomplete with Hot Keys
# ----------------------------------------------------------------------
class AutocompleteWithHotKeys:
    """
    Autocomplete that learns from user input (hot keys).
    """
    
    def __init__(self, words: List[str]):
        """Initialize with dictionary."""
        self.trie = Trie()
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).parent))
        from insert import insert_words
        insert_words(self.trie, words)
        self.hot_keys = {}  # Track user selections
    
    def select(self, word: str):
        """
        Record user selection (hot key).

        Args:
            word (str): Selected word

        Complexity:
            Time: O(1)     - Dictionary operation.
            Space: O(1)   - Stores one entry.
        """
        self.hot_keys[word] = self.hot_keys.get(word, 0) + 1
    
    def autocomplete(self, prefix: str, k: int = 5) -> List[str]:
        """
        Get suggestions with hot key priority.

        Args:
            prefix (str): Input prefix
            k (int): Number of suggestions

        Returns:
            List[str]: Top k suggestions

        Complexity:
            Time: O(m + n log k)  - Search + sort.
            Space: O(n)           - Storage for candidates.
        """
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).parent))
        from search import words_with_prefix
        candidates = words_with_prefix(self.trie, prefix)
        
        # Sort by hot key count (descending), then alphabetically
        candidates.sort(key=lambda x: (-self.hot_keys.get(x, 0), x))
        
        return candidates[:k]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Autocomplete System Demonstration")
    
    # Basic autocomplete
    words = ["apple", "application", "apply", "app", "bat", "ball", "banana"]
    system = AutocompleteSystem(words)
    
    print("Basic Autocomplete:")
    print(f"  Input: 'app' → {system.autocomplete('app')}")
    print(f"  Input: 'ba' → {system.autocomplete('ba')}")
    
    # With frequency ranking
    print("\n" + "="*50)
    words_with_freq = [
        ("apple", 10),
        ("application", 5),
        ("apply", 8),
        ("app", 15),
    ]
    system2 = AutocompleteWithRanking(words_with_freq)
    
    print("Autocomplete with Ranking:")
    print(f"  Input: 'app' → {system2.autocomplete('app', k=3)}")
    
    # With hot keys
    print("\n" + "="*50)
    system3 = AutocompleteWithHotKeys(words)
    system3.select("application")  # User selects this
    system3.select("application")  # User selects again
    
    print("Autocomplete with Hot Keys:")
    print(f"  Input: 'app' → {system3.autocomplete('app', k=3)}")
    print("  (Note: 'application' appears first due to hot key)")

