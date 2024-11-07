#!/usr/bin/python3
"""N queens solution finder module.

Usage: nqueens N:
    If the user called the program with the wrong number of arguments, print
        Usage: nqueens N, followed by a new line, and exit with the status 1.
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1.
    If N is smaller than 4, print N must be at least 4, followed by a new
    line, and exit with the status 1.
The program should print every possible solution to the problem.
    One solution per line.
You are only allowed to import the sys module.
"""

import sys

def is_safe(board, row, col, n):
    """Check if a queen can be placed at (row, col) without being attacked."""
    # Check column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    """Find all solutions for the N queens problem and return them."""
    def backtrack(row):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

# Main script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution) 
