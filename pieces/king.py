from pieces.piece import Piece

class King(Piece):

    alliance = None
    position = None

    # Creating the King and alliance with it's position
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    # Defining a toString function
    def toString(self):
       return "K" if self.alliance == "Black" else "k"