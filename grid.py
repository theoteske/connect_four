from enum import Enum
from typing import List

class GridSquare(Enum):
    """
    idea: represent the state of a given square in the connect four grid with an Enum
    """
    EMPTY = 0
    RED = 1
    YELLOW = 2

class Grid:
    """
    idea: represent the game board as a List[List[GridSquare]] object
    """

    def __init__(self, num_rows: int, num_cols: int):
        """
        :param num_rows: specifies number of rows in the grid
        :param num_cols: specifies number of columns in the grid
        """
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._grid = None
        self.init_grid()

    def init_grid(self) -> None:
        """
        :idea: initialize grid with List[List[GridSquare]] object where each GridSquare is EMPTY
        :return: None
        """
        self._grid = [[GridSquare(0)] * self._num_cols for _ in range(self._num_rows)]

    def get_grid(self) -> List[List[GridSquare]]:
        """
        :return: List[List[GridSquare]] _grid
        """
        return self._grid

    def get_column_count(self) -> int:
        """
        :return: int _num_cols
        """
        return self._num_cols

    def place_piece(self, col: int, piece: GridSquare) -> int:
        """
        :param col: specifies column in which to place a piece
        :param piece: specifies color of piece to place (RED or YELLOW)
        :return: row at which piece is placed
        """
        # validate input
        if col >= self._num_cols or col < 0:
            raise ValueError("Invalid column")
        if piece == GridSquare(0):
            raise ValueError("Invalid piece")

        # place piece in grid
        for row in range(self._num_rows-1, -1, -1):
            if self._grid[row][col] == GridSquare(0):
                self._grid[row][col] = piece
                return row

    def check_win(self, connect_n: int, row: int, col: int, piece: GridSquare) -> tuple[bool, str]:
        """
        :param connect_n: specifies number of pieces that must be connected to win
        :param row: specifies row of piece which was just placed
        :param col: specifies column of piece which was just placed
        :param piece: specifies piece that was just placed (esp piece color)
        :return: bool representing whether the player who just placed a piece has won or not
        """
        # check horizontal
        count = 0
        for c in range(self._num_cols):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0

            if count == connect_n:
                return True, "horizontal"

        # check vertical
        count = 0
        for r in range(self._num_rows):
            if self._grid[r][col] == piece:
                count += 1
            else:
                count = 0

            if count == connect_n:
                return True, "vertical"

        # check diagonal
        count = 0
        for idx in range(-min(row, col), min(self._num_rows - row, self._num_cols - col)):
            if self._grid[row + idx][col + idx] == piece:
                count += 1
            else:
                count = 0

            if count == connect_n:
                return True, "diagonal"

        # check anti-diagonal
        count = 0
        for r in range(self._num_rows):
            c = col - row + r
            if c in range(self._num_cols) and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0

            if count == connect_n:
                return True, "anti-diagonal"

        # else, connect_n is not reached
        return False, "no win"