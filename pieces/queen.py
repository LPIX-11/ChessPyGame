from pieces.piece import Piece

class Queen(Piece):

    alliance = None
    position = None

    # Creating the Queen and alliance with it's position
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    # Defining a toString function
    def toString(self):
       return "Q" if self.alliance == "Black" else "q"