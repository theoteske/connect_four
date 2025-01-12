from grid import GridSquare

class Player:
    """
    idea: encapsulate the information about the player, especially their piece color
    """

    def __init__(self, name: str, piece_color: GridSquare):
        """
        :param name: specifies the name of the player
        :param piece_color: specifies the color of the pieces used the player
        """
        self._name = name
        self._piece_color = piece_color

    def get_name(self):
        """
        :return: name of player
        """
        return self._name

    def get_piece_color(self):
        """
        :return: piece color used by player
        """
        return self._piece_color