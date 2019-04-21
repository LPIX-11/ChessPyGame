# Bishop Class
from pieces.piece import Piece

class Bishop(Piece):

    alliance = None
    position = None

    # Creating the Bishop and alliance with it's position
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    # Defining a to_string function
    def to_string(self):
       return "B" if self.alliance == "Black" else "b"

