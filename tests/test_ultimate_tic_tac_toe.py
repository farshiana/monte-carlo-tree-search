import unittest
from src.ultimate_tic_tac_toe import UltimateTicTacToe, BOARD_CELLS
from src.utils import PLAYER_ONE, PLAYER_TWO

class TestUltimateTicTacToe(unittest.TestCase):
    def test_get_moves(self):
        game = UltimateTicTacToe()
        indexes = range(BOARD_CELLS)
        self.assertEqual(game.get_moves(), [(i, j) for i in indexes for j in indexes])

        game.apply_move((0, 7))
        self.assertEqual(game.get_moves(), [(7, j) for j in indexes])

    def test_get_score(self):
        game = UltimateTicTacToe()
        for i in [0, 3, 6]:
            game.apply_move((i, 0))
            game.apply_move((i, 1))
            game.apply_move((i, 3))
            game.apply_move((i, 5))
            game.apply_move((i, 6))
            game.apply_move((i, 7))

        self.assertEqual(game.get_score(PLAYER_ONE), 1)

    def test_apply_move(self):
        game = UltimateTicTacToe()
        game.apply_move((0, 1))

        self.assertEqual(game.player_to_move, PLAYER_TWO)
