from src.game import Game
from src.utils import get_empty_copy, PLAYER_ONE

MAX_MATCHES_PER_MOVE = 3

class Nim(Game):
    def __init__(self, start_matches_count = 21):
        self.matches_count = start_matches_count
        self.player_to_move = PLAYER_ONE

    def copy(self):
        game_copy = get_empty_copy(self)
        game_copy.matches_count = self.matches_count
        game_copy.player_to_move = self.player_to_move
        return game_copy

    def get_moves(self):
        return list(range(1, min(self.matches_count, MAX_MATCHES_PER_MOVE) + 1))

    def get_score(self, player):
        if not self.is_finished():
            raise Exception('Game is not finished yet')

        return 1.0 if player == self.player_to_move else 0.0

    def apply_move(self, move):
        if not self.is_valid_move(move):
            raise Exception('Invalid move')

        self.matches_count -= move
        self.player_to_move = -self.player_to_move

    def is_valid_move(self, move):
        return move <= min(self.matches_count, MAX_MATCHES_PER_MOVE)

    def is_finished(self):
        return self.matches_count == 0

    def pretty_print(self):
        print('\n')
        print('| ' * self.matches_count)
