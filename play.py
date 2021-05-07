from argparse import ArgumentParser
from random import randrange
from src.utils import PLAYER_ONE, PLAYER_TWO
from src.nim import Nim
from src.tic_tac_toe import TicTacToe
from src.ultimate_tic_tac_toe import UltimateTicTacToe
from src.mcts import monte_carlo_tree_search

def announce_winner(game):
    score = game.get_score(PLAYER_ONE)
    if score == PLAYER_ONE:
        print('Player ONE won!')
    elif score == PLAYER_TWO:
        print('Player TWO won!')
    else:
        print('It\'s a tie!')

def main():
    parser = ArgumentParser()
    parser.add_argument('-g', '--game', dest='game', default='Nim',
        choices=['Nim', 'TicTacToe', 'UltimateTicTacToe'], help='choose game')
    parser.add_argument('-m', '--mode', dest='mode', default='human', choices=['human', 'random'], help='choose mode')

    args = parser.parse_args()

    print(f'Playing {args.game} in {args.mode} mode')

    if args.game == 'Nim':
        game = Nim()
    elif args.game == 'TicTacToe':
        game = TicTacToe()
    elif args.game == 'UltimateTicTacToe':
        game = UltimateTicTacToe()
    game.pretty_print()

    while True:
        move = monte_carlo_tree_search(game)
        game.apply_move(move)
        game.pretty_print()

        if game.is_finished():
            announce_winner(game)
            break

        if args.mode == 'human':
            if args.game == 'Nim':
                move = int(input('Enter number of matches: '))
            elif args.game == 'UltimateTicTacToe':
                move = int(input('Enter number of matches: '))
                i = int(input('Choose board (0 to 8): '))
                j = int(input('Enter position on the board (0 to 8): '))
                move = (i, j)
            else:
                move = int(input('Enter position on the board (0 to 8): '))
        else:
            moves = game.get_moves()
            move = moves[randrange(len(moves))]

        game.apply_move(move)
        game.pretty_print()

        if game.is_finished():
            announce_winner(game)
            break

main()
