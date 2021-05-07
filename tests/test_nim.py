import unittest
from src.nim import Nim
from src.utils import PLAYER_ONE, PLAYER_TWO

class TestNim(unittest.TestCase):
    def test_get_moves(self):
        game = Nim()

        self.assertEqual(game.get_moves(), [1, 2, 3])

    def test_get_score(self):
        game = Nim(6)
        game.apply_move(2)
        game.apply_move(3)
        game.apply_move(1)

        self.assertEqual(game.get_score(PLAYER_ONE), 0)

    def test_apply_move(self):
        game = Nim(6)
        game.apply_move(2)

        self.assertEqual(game.matches_count, 4)
        self.assertEqual(game.player_to_move, PLAYER_TWO)

    def test_is_valid_move(self):
        game = Nim(6)

        self.assertFalse(game.is_valid_move(4))
        self.assertTrue(game.is_valid_move(2))

    def test_is_finished(self):
        game = Nim(6)

        self.assertFalse(game.is_finished())

        game.apply_move(2)
        game.apply_move(3)
        game.apply_move(1)
        self.assertTrue(game.is_finished())
