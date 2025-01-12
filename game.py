from typing import Optional

from grid import GridSquare
from player import Player

class Game:
    """
    idea: used to play the game, will keep track of the players, the score, and the grid. will
    also be responsible for the game loop
    """

    def __init__(self, grid, connect_n, target_score):
        """
        :param grid: specifies the grid we play on, as created by the Grid class
        :param connect_n: specifies how many pieces must be connected for a player to win
        :param target_score: specifies how many rounds a player must win to win the game
        """
        self._grid = grid
        self._connect_n = connect_n
        self._target_score = target_score

        # create player objects
        self._players = [
            Player("Player 1", GridSquare.RED),
            Player("Player 2", GridSquare.YELLOW)
        ]

        # create dict to keep track of player scores
        self._scores = {player.get_name(): 0 for player in self._players}

    def print_grid(self) -> None:
        """
        idea: print the current game grid to the console
        :return: None
        """
        print("Board:")
        grid = self._grid.get_grid()
        for row in range(len(grid)):
            row_string = ""
            for piece in grid[row]:
                if piece == GridSquare.EMPTY:
                    row_string += "O"
                elif piece == GridSquare.RED:
                    row_string += "Y"
                else:
                    row_string += "R"
            print(row_string)
        print("")

    def play_move(self, player: Player) -> tuple[int, int]:
        """
        :param player: specifies the player who is playing the given move
        :return: tuple of ints specifying the row and column of the move made by the player
        """
        self.print_grid()
        print(f"{player.get_name()}'s turn")
        col_count = self._grid.get_column_count()
        move_col = int(input(f"Enter column between {0} and {col_count-1} to add piece: "))
        move_row = self._grid.place_piece(move_col, player.get_piece_color())
        return move_row, move_col

    def play_round(self) -> Optional[Player]:
        """
        :return: player that won the round, else None
        """
        while True:
            for player in self._players:
                row, col = self.play_move(player)
                piece_color = player.get_piece_color()
                player_won, how = self._grid.check_win(self._connect_n, row, col, piece_color)
                if player_won:
                    print(how)
                    self._scores[player.get_name()] += 1
                    return player

    def play(self) -> None:
        """
        idea: execute the game loop
        :return: None
        """
        max_score = 0
        winner = None

        # play as long as neither player has reached target score
        while max_score < self._target_score:
            winner = self.play_round()
            self.print_grid()
            print(f"{winner.get_name()} won this round")
            print("\n\n\n\n\n\n")
            max_score = max(self._scores[winner.get_name()], max_score)

            # reset grid
            self._grid.init_grid()
        print(f"{winner.get_name()} won the game")