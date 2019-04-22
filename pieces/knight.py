from typing import List, Any, Union

from pieces.piece import Piece


class Knight(Piece):
    alliance = None
    position = None
    possibleMoveVectors = [-17, -15, -10, -6, 6, 10, 15, 17]
    value = 300

    # Creating the Knight and alliance with it's position
    def __init__(self, alliance, position):
        super().__init__()
        self.alliance = alliance
        self.position = position

    # Defining a to_string function
    def to_string(self):
        return "N" if self.alliance == "Black" else "n"

    def calculate_legal_moves(self, board):

        legal_moves: List[Union[int, Any]] = []
        for vector in self.possibleMoveVectors:
            dest_coord = self.position + vector
            if 0 <= dest_coord < 64:
                bad_move = self.calculate_edge_cases(self.position, vector)
                if not bad_move:
                    dest_tile = board.game_tiles[dest_coord]
                    if dest_tile.piece_on_tile.to_string() == "-":
                        legal_moves.append(dest_coord)
                    else:
                        if not dest_tile.piece_on_tile.alliance == self.alliance:
                            legal_moves.append(dest_coord)

        return legal_moves

    @staticmethod
    def calculate_edge_cases(position, vector):
        if position in Piece.firstCol:
            if vector == -17 or vector == -10 or vector == 6 or vector == 15:
                return True

        if position in Piece.secondCol:
            if vector == -10 or vector == 6:
                return True

        if position in Piece.seventhCol:
            if vector == -6 or vector == 10:
                return True

        if position in Piece.eighthCol:
            if vector == -15 or vector == -6 or vector == 10 or vector == 17:
                return True

        return False

    # def move(self, destination):
    #   return Knight(self.alliance, destination)
