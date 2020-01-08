#!/usr/bin/env python

import collections
import itertools

"""
This program solves the Drive Ya Nuts puzzle game introduced in 1970
by Milton Bradley. The program searches for all solutions and prints them
out (there is only one solution).

When representing the board state, the pieces are indexed in the following
manner. The printed solution is also in the following order (0 first). The
first side listed on the center faces down. The first side of each edge
piece faces inward.

   4
5     3
   0
6     2
   1
"""

NUM_SIDES = 6

# All of the pieces. The order of the pieces doesn't matter. The
# sides are listed counter-clockwise on each piece, starting with 1
pieces = [
    [1, 5, 3, 2, 6, 4],
    [1, 4, 2, 3, 5, 6],
    [1, 3, 5, 4, 2, 6],
    [1, 3, 5, 2, 4, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 5, 6, 3, 4],
    [1, 6, 5, 4, 3, 2],
]

NUM_PIECES = len(pieces)


def init_state(layout):
    """Inits the state with the specified layout. This state will be
    manipulated to find the solution"""

    state = []

    for piece in layout:
        state.append(collections.deque(piece))

    return state


def necklace_perms(pieces):
    """Generates all position permutations for the board utilizing
    a necklace strategy. Each piece gets one turn at center. Of the
    remaining outer pieces, a single piece is pinned to the first position
    and the remaining pieces are iterated over (the trailer below).
    """

    for i in range(NUM_PIECES):

        # copy the pieces onto the board
        modified_board = pieces[:]
        center = modified_board[i]
        del modified_board[i]

        gen = itertools.permutations(modified_board[1:])

        for trailer in gen:
            yield [center] + [modified_board[0]] + list(trailer)


def get_center_side(piecenum):
    """Given a piece, return the side of the center that should be
    touching. Down is zero and continue counter-clockwise"""
    return piecenum - 1


def check_piece(state, number):
    """Performs a check for matching numbers with the adjacent piece.
    Looking at the board, the right flat of the specified piece
    is compared to the adjacent piece"""

    piece = state[number]
    right = state[number+1 if number < NUM_SIDES else 1]

    return piece[5] == right[1]


def check(state):
    """Checks the entire state, one piece as a time. Returns
       True if solution is found"""

    for i in range(1, NUM_PIECES):
        if not check_piece(state, i):
            return False

    return True


def print_state(state):
    for item in state:
        print(list(item), end='')

    print()


def rotate_center(state):
    """Rotates the center piece"""
    state[0].rotate()


def align_to_center(state):
    """Rotates each outer piece around until the corresponding sides are
    aligned to the center value."""

    center = state[0]

    for pieceidx in range(1, NUM_PIECES):

        stop_value = center[get_center_side(pieceidx)]

        while True:
            piece = state[pieceidx]
            if piece[0] == stop_value:
                break

            piece.rotate()


def main():

    for layout in necklace_perms(pieces):

        state = init_state(layout)

        for _ in range(NUM_SIDES):

            align_to_center(state)

            if check(state):
                print_state(state)

            rotate_center(state)


if __name__ == '__main__':
    main()
