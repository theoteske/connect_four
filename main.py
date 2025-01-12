from game import Game
from grid import Grid

"""
idea: play classic game of Connect4 with 6 rows, 7 columns, best of 3
"""
grid = Grid(6, 7)
game = Game(grid, 4, 2)
game.play()