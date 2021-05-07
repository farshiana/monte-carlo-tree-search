## Monte Carlo Tree Search

Python implementation of the [Monte Carlo Tree Search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) algorithm.
Implemented games are Nim, Tic-Tac-Toe and Ultimate Tic-Tac-Toe
#### Installation
Install pipenv and run `pipenv install` to install dependencies

#### Usage
Play Nim or Tic-Tac-Toe against the AI with `python play.py -g Nim -m human`

Visualize a random bot play Tic-Tac-Toe or Nim against the AI with `python play.py -g TicTacToe -m random`

#### Linter
Run linter with `pylint {file}.py`

#### Tests
Run a module's test with `python -m unittest tests.test_{module}`
