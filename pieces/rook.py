from pieces.piece import Piece


class Rook(Piece):
    alliance = None
    position = None

    # Creating the Rook and alliance with it's position
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    # Defining a to_string function
    def to_string(self):
        return "R" if self.alliance == "Black" else "r"
