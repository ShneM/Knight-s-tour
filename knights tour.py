"""
Knight's tour for a 8 * 8 chess board for all possible board positions

"""
# import libraries

import numpy as np

# Constants

N = '\u2658'  # Unicode character for a knight
BOARD_COUNT = 0

COLUMNS = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']  # Files of a chessboard
ROWS = [1, 2, 3, 4, 5, 6, 7, 8]  # Rows of a chessboard

PERMUTATIONS = ([-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1])  # Possible moves generation

"""
Pretty print to replace normal print function
Credit to user FOAD link: https://stackoverflow.com/questions/53126305/pretty-printing-numpy-ndarrays-using-unicode-characters
"""


def npprint(ar):
    assert isinstance(ar, np.ndarray), "input of npprint must be array like"

    if ar.ndim == 1:
        print(ar)

    else:

        for i in range(ar.shape[1]):
            npprint(ar[:, i])

    return


# function for generationof possible moves from a given position

def move_knight(x, y, board):
    valid_moves = []

    for i in range(8):

        if 0 <= x + PERMUTATIONS[i][0] <= 7 and 0 <= y + PERMUTATIONS[i][1] <= 7 and board[x + PERMUTATIONS[i][0]][
            y + PERMUTATIONS[i][1]] != N:
            valid_moves.append((x + PERMUTATIONS[i][0], y + PERMUTATIONS[i][1]))

    return valid_moves


# Warnsdorff Algorithm for minimum accessibility position

def possible_moves(p_moves, board):
    move_count = []

    next_move = []

    new_move = ()

    for j in range(len(p_moves)):
        px, py = p_moves[j]

        move_count.append(len(move_knight(px, py, board)))

        next_move.append((px, py))

    if len(next_move) == 0:

        m = False

    else:

        new_move = next_move[move_count.index(min(move_count))]

        m = True

    return new_move, m


# Knights tour

def knights_tour(qx, qy):
    chess_board = np.array([['*' for _ in range(8)] for _ in range(8)])

    chess_board[qx][qy] = N

    npprint(chess_board)

    sq_count = 1

    move = True

    while move:

        n_move = move_knight(qx, qy, chess_board)

        if len(n_move) != 0:

            k_move, move = possible_moves(n_move, chess_board)

            qx, qy = k_move[0], k_move[1]

            chess_board[qx][qy] = N

            sq_count += 1

        else:

            move = False

    return chess_board, sq_count


# main function

for column in range(8):

    for row in range(8):
        print("Board_count: ", f'{BOARD_COUNT}')

        print("Starting Position: ", f'{COLUMNS[column], ROWS[row]}')

        solution, squares = knights_tour(row, column)

        npprint(solution)

        BOARD_COUNT += 1

        print("No. of squares visited: ", f'{squares}')
