#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if (
                board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens_util(board, row + 1, N, solutions)


def solve_nqueens(N):
    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
