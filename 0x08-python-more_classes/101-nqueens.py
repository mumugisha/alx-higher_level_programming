#!/usr/bin/python3
"""This project will solve the nqueensN puzzle"""

import sys


def init_board(n):
    """Initialize `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return list of lists represented in a solved chessboard."""
    solution = []
    for f in range(len(board)):
        for g in range(len(board)):
            if board[f][g] == "Q":
                solution.append([f, g])
                break
    return (solution)


def xout(board, rows, cols):
    """X out spots on the solved chessboard.
    All spots where non-attacking queens can no
    longer be played are Xed out.
    Args:
        board (list): The current working solved chessboard.
        rows (int): The rows where a queen was last played.
        cols (int): The columns where a queen was last played.
    """
    # X out all forward spots
    for g in range(cols + 1, len(board)):
        board[rows][g] = "x"
    # X out all backwards spots
    for g in range(cols - 1, -1, -1):
        board[rows][g] = "x"
    # X out all spots below
    for f in range(rows + 1, len(board)):
        board[f][cols] = "x"
    # X out all spots above
    for f in range(rows - 1, -1, -1):
        board[f][cols] = "x"
    # X out all spots diagonally down to the right
    g = cols + 1
    for f in range(rows + 1, len(board)):
        if g >= len(board):
            break
        board[f][g] = "x"
        g += 1
    # X out all spots diagonally up to the left
    g = cols - 1
    for f in range(rows - 1, -1, -1):
        if g < 0:
            break
        board[f][g]
        g -= 1
    # X out all spots diagonally up to the right
    g = cols + 1
    for f in range(rows - 1, -1, -1):
        if g >= len(board):
            break
        board[f][g] = "x"
        g += 1
    # X out all spots diagonally down to the left
    g = cols - 1
    for f in range(rows + 1, len(board)):
        if g < 0:
            break
        board[f][g] = "x"
        g -= 1


def recursive_solve(board, rows, queens, solutions):
    """Recursively solved nqueensN puzzle.
    Args:
        board (list): The current working chessboard.
        rows (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for g in range(len(board)):
        if board[rows][g] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[rows][g] = "Q"
            xout(tmp_board, rows, g)
            solutions = recursive_solve(tmp_board, rows + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sols in solutions:
        print(sols)
