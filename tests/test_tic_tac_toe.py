import unittest
from src.tic_tac_toe import Board, TicTacToe, BOARD_CELLS
from src.utils import PLAYER_ONE, PLAYER_TWO

class TestBoard(unittest.TestCase):
    def test_apply_move(self):
        board = Board()
        board.apply_move(2, PLAYER_ONE)

        self.assertEqual(board.empty_cells_count, BOARD_CELLS - 1)

    def test_is_valid_move(self):
        board = Board()
        self.assertFalse(board.is_valid_move(10))
        self.assertTrue(board.is_valid_move(2))

        board.apply_move(2, PLAYER_ONE)
        self.assertFalse(board.is_valid_move(2))

    def test_is_finished(self):
        board = Board()

        self.assertFalse(board.is_finished())

        for move in range(BOARD_CELLS):
            board.apply_move(move, PLAYER_ONE)
        self.assertTrue(board.is_finished())

class TestTicTacToe(unittest.TestCase):
    def test_get_moves(self):
        game = TicTacToe()

        self.assertEqual(game.get_moves(), list(range(BOARD_CELLS)))

    def test_get_score(self):
        game = TicTacToe()
        game.apply_move(0)
        game.apply_move(1)
        game.apply_move(3)
        game.apply_move(5)
        game.apply_move(6)

        self.assertEqual(game.get_score(PLAYER_ONE), 1)

    def test_apply_move(self):
        game = TicTacToe()
        game.apply_move(2)

        self.assertEqual(game.player_to_move, PLAYER_TWO)

    def test_is_finished(self):
        game = TicTacToe()

        self.assertFalse(game.is_finished())

        for move in range(BOARD_CELLS):
            game.apply_move(move)
        self.assertTrue(game.is_finished())
