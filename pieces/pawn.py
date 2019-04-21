from pieces.piece import Piece

class Pawn(Piece):

    alliance = None
    position = None

    # Creating the Pawn and alliance with it's position
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    # Defining a to_string function
    def to_string(self):
       return "P" if self.alliance == "Black" else "p"