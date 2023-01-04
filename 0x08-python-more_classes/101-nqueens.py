#!/usr/bin/python3
"""Solves the N-queens puzzle"""
import sys


def nqueens(n: int) -> None:
    """
    Solves the N queens problem for an N x N chessboard.

    Args:
        n: the size of the chessboard.
            Must be an integer greater than or equal to 4.

    Returns:
    - Every possible solution to the N queens problem,
    one solution per line. Each solution is a list of tuples,
    where each tuple represents the (row, col) indices of a
    queen on the chessboard.
    """
    def is_safe(board, row, col):
        """
        Determines if it's safe to place a queen at board[row][col].

        Args:
            board: the current state of the chessboard
            row: the row index of the position being checked
            col: the column index of the position being checked

        Returns:
            True if it's safe to place a queen at board[row][col],
            False otherwise.
        """
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i][col]:
                return False

        # Check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1

        return True

    def solve(board, row, queens):
        """
        Solves the N queens problem for the given chessboard and
        the remaining rows.

        Args:
            board: the current state of the chessboard
            row: the index of the first row to consider
            queens: a list of tuples representing the (row, col)
            indices of the queens on the chessboard

        Returns:
            The indices of the queens for a valid solution to
            the N queens problem.
        """
        # Base case: all queens have been placed
        if row == n:
            print(queens)
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                queens.append((row, col))
                solve(board, row + 1, queens)
                # Backtrack: unplace the queen
                board[row][col] = 0
                queens.pop()

    # Initialize the board
    board = [[0] * n for _ in range(n)]
    queens = []
    solve(board, 0, queens)


def main():
    """main function"""
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

    nqueens(n)


if __name__ == "__main__":
    main()
