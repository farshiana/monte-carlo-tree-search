from src.game import Game
from src.tic_tac_toe import Board, BOARD_SIZE, BOARD_CELLS
from src.utils import get_empty_copy, PLAYER_ONE, PLAYER_TWO


class UltimateTicTacToe(Game):
    def __init__(self):
        self.board = Board(Board())
        self.meta_board = Board()
        self.player_to_move = PLAYER_ONE
        self.last_move = None

    def copy(self):
        game_copy = get_empty_copy(self)
        game_copy.board = self.board.copy()
        game_copy.meta_board = self.meta_board.copy()
        game_copy.player_to_move = self.player_to_move
        game_copy.last_move = self.last_move
        return game_copy

    def get_moves(self):
        moves = []

        no_restrictions = not self.last_move or self.board.board[self.last_move[1]].is_finished()

        for i in range(BOARD_CELLS):
            if (no_restrictions or self.last_move[1] == i) and not self.board.board[i].is_finished():
                for j in range(BOARD_CELLS):
                    if self.board.board[i].board[j] is None:
                        moves.append((i, j))

        return moves

    def get_score(self, player):
        if not self.is_finished():
            raise Exception('Game is not finished yet')

        if not self.meta_board.winner:
            return 0.5

        return 1 if player == self.meta_board.winner else 0

    def apply_move(self, move):
        board = self.board.board[move[0]]

        if not board.is_valid_move(move[1]):
            raise Exception('Invalid move')

        board.apply_move(move[1], self.player_to_move)

        if board.winner == self.player_to_move:
            self.meta_board.apply_move(move[0], self.player_to_move)
        elif board.empty_cells_count == 0:
            self.meta_board.empty_cells_count -= 1

        self.last_move = move
        self.player_to_move = -self.player_to_move

    def is_finished(self):
        return self.meta_board.is_finished()

    def pretty_print(self):
        print('\n')

        for i in range(BOARD_CELLS):
            row = ''
            for j in range(BOARD_CELLS):
                x_coord = (i // BOARD_SIZE) * BOARD_SIZE + j // BOARD_SIZE
                y_coord = (i % BOARD_SIZE) * BOARD_SIZE + j % BOARD_SIZE
                cell = self.board.board[x_coord].board[y_coord]

                if cell == PLAYER_ONE:
                    row += ' x'
                elif cell == PLAYER_TWO:
                    row += ' o'
                else:
                    row += ' _'
                if j % BOARD_SIZE == 2 and not j == 8:
                    row += ' |'
            if i % BOARD_SIZE == 0 and not i == 0:
                print('-' * (1 + (2 * BOARD_SIZE + 1) * BOARD_SIZE))
            print(row)
