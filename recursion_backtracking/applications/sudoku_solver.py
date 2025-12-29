"""
Sudoku Solver Using Backtracking

Solve a 9×9 Sudoku puzzle using backtracking algorithm.

Problem Statement:
-------------------
Fill a 9×9 grid with digits so that each column, row, and 3×3 subgrid
contains all digits from 1 to 9.

Why Backtracking?
-----------------
- Try each digit in empty cell
- Check if valid (no conflicts)
- If valid, recurse to next empty cell
- If no valid digit, backtrack to previous cell
- Systematic exploration of all possibilities

Useful in:
- Constraint satisfaction
- Puzzle solving
- Medium difficulty interview problems
"""

from typing import List, Optional, Tuple


# ----------------------------------------------------------------------
# Sudoku Solver (Language-agnostic)
# ----------------------------------------------------------------------
def solve_sudoku(board: List[List[str]]) -> bool:
    """
    Solve Sudoku puzzle using backtracking.

    Algorithm:
    1. Find empty cell
    2. Try digits 1-9
    3. Check if valid (no conflicts)
    4. If valid, place digit and recurse
    5. If solved, return True
    6. If not, backtrack and try next digit

    Args:
        board (List[List[str]]): 9×9 Sudoku board ('.' for empty)

    Returns:
        bool: True if solved, False if unsolvable

    Complexity:
        Time: O(9^m)    - m is number of empty cells, worst case.
        Space: O(1)    - In-place modification.
    """
    def is_valid(row: int, col: int, digit: str) -> bool:
        """Check if placing digit at (row, col) is valid."""
        # Check row
        for c in range(9):
            if board[row][c] == digit:
                return False
        
        # Check column
        for r in range(9):
            if board[r][col] == digit:
                return False
        
        # Check 3×3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == digit:
                    return False
        
        return True
    
    def find_empty() -> Optional[Tuple[int, int]]:
        """Find next empty cell."""
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    return (r, c)
        return None
    
    # Find empty cell
    empty = find_empty()
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    # Try digits 1-9
    for digit in '123456789':
        if is_valid(row, col, digit):
            # Place digit
            board[row][col] = digit
            
            # Recurse
            if solve_sudoku(board):
                return True
            
            # Backtrack
            board[row][col] = '.'
    
    return False


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Sudoku Solver Demonstration")
    
    # Example Sudoku puzzle
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    
    print("Original Sudoku:")
    for row in board:
        print(' '.join(row))
    
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        for row in board:
            print(' '.join(row))
    else:
        print("\nNo solution exists")

