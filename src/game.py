from random import randrange
from abc import abstractmethod

class Game:
    def make_random_move(self):
        moves = self.get_moves()
        move = moves[randrange(len(moves))]
        self.apply_move(move)

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def apply_move(self, move):
        pass
