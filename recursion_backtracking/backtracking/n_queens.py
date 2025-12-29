"""
N-Queens Problem

Place N queens on an N×N chessboard such that no two queens attack each other.

Problem Statement:
-------------------
Place N queens on an N×N chessboard so that no two queens are in the same row,
column, or diagonal.

Example (4-Queens):
    Solution: [1, 3, 0, 2] (queen in row i is in column solution[i])

Why Backtracking?
-----------------
- Try placing queen in each column of current row
- If valid, recurse to next row
- If no valid placement, backtrack to previous row
- Explore all possibilities systematically

Useful in:
- Backtracking fundamentals
- Constraint satisfaction
- Common interview problems
"""

from typing import List, Optional


# ----------------------------------------------------------------------
# N-Queens Solution (Language-agnostic)
# ----------------------------------------------------------------------
def solve_n_queens(n: int) -> List[List[int]]:
    """
    Solve N-Queens problem using backtracking.

    Algorithm:
    1. Try placing queen in each column of current row
    2. Check if placement is valid (no conflicts)
    3. If valid, recurse to next row
    4. If all queens placed, add solution
    5. Backtrack if no valid placement

    Args:
        n (int): Number of queens and board size

    Returns:
        List[List[int]]: List of all solutions (each solution is list of column positions)

    Complexity:
        Time: O(n!)     - In worst case, explores all permutations.
        Space: O(n)    - Recursion depth + solution storage.
    """
    solutions: List[List[int]] = []
    
    def is_safe(board: List[int], row: int, col: int) -> bool:
        """Check if placing queen at (row, col) is safe."""
        for i in range(row):
            # Check column conflict
            if board[i] == col:
                return False
            # Check diagonal conflicts
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board: List[int], row: int) -> None:
        """Backtrack to find all solutions."""
        # Base case: all queens placed
        if row == n:
            solutions.append(board.copy())
            return
        
        # Try each column in current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                # Backtrack: remove queen (implicit, overwritten in next iteration)
    
    board = [-1] * n
    backtrack(board, 0)
    return solutions


# ----------------------------------------------------------------------
# N-Queens (Return First Solution)
# ----------------------------------------------------------------------
def solve_n_queens_first(n: int) -> Optional[List[int]]:
    """
    Find first solution to N-Queens problem.

    Args:
        n (int): Number of queens

    Returns:
        Optional[List[int]]: First solution, None if no solution

    Complexity:
        Time: O(n!) worst case, but often finds solution faster.
        Space: O(n) - Recursion depth.
    """
    def is_safe(board: List[int], row: int, col: int) -> bool:
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board: List[int], row: int) -> bool:
        if row == n:
            return True
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if backtrack(board, row + 1):
                    return True
                # Backtrack
                board[row] = -1
        
        return False
    
    board = [-1] * n
    if backtrack(board, 0):
        return board
    return None


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: N-Queens Problem Demonstration")
    
    n = 4
    print(f"Solving {n}-Queens problem:")
    
    solutions = solve_n_queens(n)
    print(f"Number of solutions: {len(solutions)}")
    for i, sol in enumerate(solutions):
        print(f"  Solution {i + 1}: {sol}")
    
    # First solution
    print("\n" + "="*50)
    first_sol = solve_n_queens_first(n)
    print(f"First solution: {first_sol}")

