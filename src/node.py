from math import sqrt, log

class Node():
    def __init__(self, game, move = None, parent = None):
        self.player_to_move = game.player_to_move
        self.remaining_moves = game.get_moves()
        self.move = move
        self.parent = parent
        self.cumulative_score = 0.0
        self.visits_count = 0
        self.children = []
        self.uct_score = 0.0

    def has_children(self):
        return len(self.children) > 0

    def has_remaining_moves(self):
        return len(self.remaining_moves) > 0

    def update_uct_score(self):
        self.uct_score = self.cumulative_score / self.visits_count \
            + sqrt(2.0 * log(self.parent.visits_count) / self.visits_count)

    def select_child(self):
        for child in self.children:
            child.update_uct_score()

        return max(self.children, key=lambda child: child.uct_score)

    def create_child(self, game, move):
        child = Node(game, move, self)
        self.children.append(child)
        self.remaining_moves = [m for m in self.remaining_moves if not m == move]
        return child

    def update(self, score):
        self.cumulative_score += score
        self.visits_count += 1

    def get_expected_success_rate(self):
        return (self.cumulative_score + 1) / (self.visits_count + 2)
