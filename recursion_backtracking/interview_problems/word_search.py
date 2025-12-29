"""
Word Search in Grid

Find if word exists in 2D grid using backtracking.

Problem Statement:
-------------------
Given a 2D board and a word, find if the word exists in the grid.
Word can be constructed from adjacent cells (horizontally or vertically).

Example:
    Board: [['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]
    Word: "ABCCED"
    Output: True

Why Backtracking?
-----------------
- Try each cell as starting point
- For each character, try adjacent cells
- If character matches, recurse to next character
- If word found, return True
- If stuck, backtrack to previous cell
- Mark visited cells to avoid cycles

Useful in:
- Grid search problems
- String matching
- Medium difficulty interview problems
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Word Search (Language-agnostic)
# ----------------------------------------------------------------------
def word_search(board: List[List[str]], word: str) -> bool:
    """
    Check if word exists in board using backtracking.

    Algorithm:
    1. Try each cell as starting point
    2. For each character, check adjacent cells
    3. If character matches, mark visited and recurse
    4. If word found, return True
    5. Backtrack: unmark visited cell

    Args:
        board (List[List[str]]): 2D grid of characters
        word (str): Word to search

    Returns:
        bool: True if word exists, False otherwise

    Complexity:
        Time: O(m * n * 4^L)  - m×n cells, 4 directions, L is word length.
        Space: O(L)          - Recursion depth.
    """
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def is_valid(row: int, col: int) -> bool:
        """Check if cell is valid."""
        return (0 <= row < rows and 0 <= col < cols and
                not visited[row][col])
    
    def backtrack(row: int, col: int, index: int) -> bool:
        """Backtrack to find word."""
        # Base case: word found
        if index == len(word):
            return True
        
        # Check if current cell matches
        if not is_valid(row, col) or board[row][col] != word[index]:
            return False
        
        # Mark as visited
        visited[row][col] = True
        
        # Try all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if backtrack(row + dr, col + dc, index + 1):
                return True
        
        # Backtrack: unmark
        visited[row][col] = False
        return False
    
    # Try each cell as starting point
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    
    return False


# ----------------------------------------------------------------------
# Word Search - Find All Words
# ----------------------------------------------------------------------
def word_search_all(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Find all words from list that exist in board.

    Args:
        board (List[List[str]]): 2D grid
        words (List[str]): List of words to search

    Returns:
        List[str]: Words that exist in board

    Complexity:
        Time: O(m * n * 4^L * W)  - W is number of words.
        Space: O(L)               - Recursion depth.
    """
    found = []
    for word in words:
        if word_search(board, word):
            found.append(word)
    return found


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Word Search Demonstration")
    
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    
    print("Board:")
    for row in board:
        print(row)
    
    words = ["ABCCED", "SEE", "ABCB"]
    print(f"\nSearching words: {words}")
    
    for word in words:
        exists = word_search(board, word)
        print(f"  '{word}': {exists}")

