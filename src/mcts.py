from random import randrange
from src.node import Node

# Monte Carlo Tree Search has 4 steps in its main loop
# 1 - Select the most promissing leaf
# 2 - Expand the tree by adding a child from a random move to the leaf
# 3 - Simulate a random game from the leaf
# 4 - Back propagate to update all parent nodes
def monte_carlo_tree_search(start_state, max_iterations_count = 10000):
    root_node = Node(start_state)

    for _ in range(max_iterations_count):
        game = start_state.copy()
        node = root_node

        while node.has_children() and not node.has_remaining_moves():
            node = node.select_child()
            game.apply_move(node.move)

        if not game.is_finished() and node.has_remaining_moves():
            move = node.remaining_moves[randrange(len(node.remaining_moves))]
            game.apply_move(move)
            node = node.create_child(game, move)

        while not game.is_finished():
            game.make_random_move()

        while node.parent:
            node.update(game.get_score(node.parent.player_to_move))
            node = node.parent
        root_node.visits_count += 1

    child = max(root_node.children, key=lambda child: child.get_expected_success_rate())

    return child.move
