import unittest
from src.node import Node
from src.utils import PLAYER_ONE

class TestGame():
    # pylint: disable=too-few-public-methods, no-method-argument, no-self-use
    def __init__(self):
        self.player_to_move = PLAYER_ONE

    def get_moves():
        return [None]

class TestNode(unittest.TestCase):
    def test_has_children(self):
        game = TestGame()
        node = Node(game)

        self.assertFalse(node.has_children())

        node.children = [None]
        self.assertTrue(node.has_children())

    def test_has_remaining_moves(self):
        game = TestGame()
        node = Node(game)

        node.remaining_moves = []
        self.assertFalse(node.has_remaining_moves())

        node.remaining_moves = [None]
        self.assertTrue(node.has_remaining_moves())

    def test_update_uct_score(self):
        game = TestGame()
        parent = Node(game)
        parent.visits_count = 1
        node = Node(game, parent=parent)

        node.cumulative_score = 1
        node.visits_count = 1
        node.update_uct_score()
        self.assertEqual(node.uct_score, 1)

    def test_select_child(self):
        game = TestGame()
        node = Node(game)
        node.visits_count = 1
        child1 = Node(game, parent=node)
        child1.visits_count = 1
        child2 = Node(game, parent=node)
        child2.visits_count = 1
        child2.cumulative_score = 2
        child3 = Node(game, parent=node)
        child3.visits_count = 1
        node.children = [child1, child2, child3]

        self.assertEqual(node.select_child(), child2)

    def test_create_child(self):
        game = TestGame()
        node = Node(game)
        node.remaining_moves = [None]
        child = node.create_child(game, None)

        self.assertEqual(node.children, [child])
        self.assertEqual(len(node.remaining_moves), 0)

    def test_update(self):
        game = TestGame()
        node = Node(game)
        node.update(10)

        self.assertEqual(node.visits_count, 1)
        self.assertEqual(node.cumulative_score, 10)

    def test_get_expected_success_rate(self):
        game = TestGame()
        node = Node(game)
        node.cumulative_score = 7
        node.visits_count = 2

        self.assertEqual(node.get_expected_success_rate(), 2)
