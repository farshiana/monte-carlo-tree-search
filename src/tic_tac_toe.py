import numpy as np
from src.game import Game
from src.utils import get_empty_copy, PLAYER_ONE, PLAYER_TWO

BOARD_SIZE = 3
BOARD_CELLS = BOARD_SIZE * BOARD_SIZE

class Board():
    def __init__(self, board = None):
        self.board = np.array([board if board is None else board.copy() for _ in range(BOARD_CELLS)])
        self.empty_cells_count = BOARD_CELLS
        self.winner = None

    def copy(self):
        board_copy = get_empty_copy(self)
        board_copy.empty_cells_count = self.empty_cells_count
        board_copy.winner = self.winner

        board_copy.board = np.array([None] * len(self.board))
        for i in range(BOARD_CELLS):
            if isinstance(self.board[i], Board):
                board_copy.board[i] = self.board[i].copy()
            else:
                board_copy.board[i] = self.board[i]

        return board_copy

    def apply_move(self, move, player):
        if not self.is_valid_move(move):
            raise Exception('Invalid move')

        self.board[move] = player
        self.empty_cells_count -= 1

        if self.completes_board(move):
            self.winner = player

    def is_valid_move(self, move):
        if move < 0 or move >= BOARD_CELLS:
            return False

        return self.board[move] is None

    def completes_board(self, move):
        x_coord = move % BOARD_SIZE
        y_coord = move // BOARD_SIZE

        return self.completes_horizontal_line(y_coord) or self.completes_vertical_line(x_coord) \
            or self.completes_diagonal(x_coord, y_coord) or self.completes_anti_diagonal(x_coord, y_coord)

    def completes_horizontal_line(self, y_coord):
        return self.board[BOARD_SIZE * y_coord] == self.board[BOARD_SIZE * y_coord + 1] \
            and self.board[BOARD_SIZE * y_coord + 1] == self.board[BOARD_SIZE * y_coord + 2]

    def completes_vertical_line(self, x_coord):
        return self.board[x_coord] == self.board[x_coord + BOARD_SIZE] \
            and self.board[x_coord + BOARD_SIZE] == self.board[x_coord + 2 * BOARD_SIZE]

    def completes_diagonal(self, x_coord, y_coord):
        return x_coord == y_coord and self.board[0] == self.board[4] and self.board[4] == self.board[8]

    def completes_anti_diagonal(self, x_coord, y_coord):
        return x_coord + y_coord == 2 and self.board[2] == self.board[4] and self.board[4] == self.board[6]

    def is_finished(self):
        return self.empty_cells_count == 0 or self.winner

    def pretty_print(self):
        print('\n')
        row = ''

        for i in range(BOARD_CELLS):
            if self.board[i] == PLAYER_ONE:
                row += ' x'
            elif self.board[i] == PLAYER_TWO:
                row += ' o'
            else:
                row += ' _'
            if i % BOARD_SIZE == 2:
                print(row)
                row = ''

class TicTacToe(Game):
    def __init__(self):
        self.board = Board()
        self.player_to_move = PLAYER_ONE

    def copy(self):
        game_copy = TicTacToe()
        game_copy.board = self.board.copy()
        game_copy.player_to_move = self.player_to_move
        return game_copy

    def get_moves(self):
        moves = []
        for i in range(BOARD_CELLS):
            if self.board.board[i] is None:
                moves.append(i)
        return moves

    def get_score(self, player):
        if not self.is_finished():
            raise Exception('Game is not finished yet')

        if not self.board.winner:
            return 0.5

        return 1 if player == self.board.winner else 0

    def apply_move(self, move):
        self.board.apply_move(move, self.player_to_move)

        self.player_to_move = -self.player_to_move

    def is_finished(self):
        return self.board.is_finished()

    def pretty_print(self):
        self.board.pretty_print()
