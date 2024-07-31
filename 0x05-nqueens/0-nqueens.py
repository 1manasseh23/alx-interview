#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Print number error message and exit with status 1."""
    print("N must be a number")
    sys.exit(1)


def print_minimum_number_error_and_exit():
    """Print minimum number error message and exit with status 1."""
    print("N must be at least 4")
    sys.exit(1)


def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is valid."""
    for i in range(row):
        if (board[i][1] == col or
                board[i][1] - board[i][0] == col - row or
                board[i][1] + board[i][0] == col + row):
            return False
    return True


def solve_nqueens(n):
    """Solve the N-Queens problem and return all solutions."""
    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = [row, col]
                backtrack(row + 1)
                board[row] = [-1, -1]

    solutions = []
    board = [[-1, -1] for _ in range(n)]
    backtrack(0)
    return solutions


def main():
    """Main function to handle command-line arguments and solve the problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if n < 4:
        print_minimum_number_error_and_exit()

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
