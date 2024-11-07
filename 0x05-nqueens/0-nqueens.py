#!/usr/bin/python3
"""N queens solution finder module."""

import sys

def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)

def check_arguments():
    """Checks if the argument is valid and returns it as an integer."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n

def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for r in range(row):
        # Check column and diagonals
        if board[r] == col or \
           board[r] - r == col - row or \
           board[r] + r == col + row:
            return False
    return True

def solve_nqueens(n):
    """Finds all solutions to the N queens problem and returns them."""
    def backtrack(row):
        if row == n:
            # Store solution as a list of [row, col] pairs
            solutions.append([[r, board[r]] for r in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

# Main execution
if __name__ == "__main__":
    n = check_arguments()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
