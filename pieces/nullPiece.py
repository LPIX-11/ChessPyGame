from pieces.piece import Piece


class NullPiece(Piece):

    def __init__(self):
        pass

    @staticmethod
    def to_string():
        return '-'
