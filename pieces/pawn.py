from pieces.piece import Piece


class Pawn(Piece):
    alliance = None
    position = None

    possibleMoveVectors = [7, 9, 8, 16]
    allianceMultiple = None
    firstMove = True
    value = 100

    # Creating the Pawn and alliance with it's position
    def __init__(self, alliance, position):
        super().__init__()
        self.alliance = alliance
        self.position = position
        if self.alliance == "Black":
            self.allianceMultiple = 1
        else:
            self.allianceMultiple = -1

    # Defining a to_string function
    def to_string(self):
        return "P" if self.alliance == "Black" else "p"

    def calculate_legal_moves(self, board):

        legal_moves = []

        for vector in self.possibleMoveVectors:

            dest_coord = self.position + (vector * self.allianceMultiple)

            if 0 <= dest_coord < 64:

                if vector == 8 and board.game_tiles[dest_coord].piece_on_tile.to_string() == "-":

                    if self.alliance == "Black" and dest_coord in Piece.eighthRow:
                        legal_moves.append(dest_coord)
                    elif self.alliance == "White" and dest_coord in Piece.firstRow:
                        legal_moves.append(dest_coord)
                    else:
                        legal_moves.append(dest_coord)

                elif vector == 16 and self.firstMove and board.game_tiles[dest_coord].piece_on_tile.to_string() == "-":

                    behind_jump = self.position + (8 * self.allianceMultiple)
                    if board.game_tiles[behind_jump].piece_on_tile.to_string() == "-":
                        legal_moves.append(dest_coord)

                elif vector == 7:

                    if self.position in Piece.firstCol and self.alliance == "Black":
                        pass
                    elif self.position in Piece.eighthCol and self.alliance == "White":
                        pass
                    else:

                        if not board.game_tiles[dest_coord].piece_on_tile.to_string() == "-":

                            piece = board.game_tiles[dest_coord].piece_on_tile
                            if not self.alliance == piece.alliance:

                                if self.alliance == "Black" and dest_coord in Piece.eighthRow:
                                    legal_moves.append(dest_coord)
                                elif self.alliance == "White" and dest_coord in Piece.firstRow:
                                    legal_moves.append(dest_coord)
                                else:
                                    legal_moves.append(dest_coord)

                        elif board.en_pass_pawn is None:

                            if board.en_pass_pawnBehind == dest_coord:
                                en_pp = board.en_pass_pawn
                                if not self.alliance == en_pp.alliance:
                                    legal_moves.append(dest_coord)

                elif vector == 9:

                    if self.position in Piece.eighthCol and self.alliance == "Black":
                        pass
                    elif self.position in Piece.firstCol and self.alliance == "White":
                        pass
                    else:

                        if not board.game_tiles[dest_coord].piece_on_tile.to_string() == "-":
                            piece = board.game_tiles[dest_coord].piece_on_tile
                            if not self.alliance == piece.alliance:

                                if self.alliance == "Black" and dest_coord in Piece.eighthRow:
                                    legal_moves.append(dest_coord)
                                elif self.alliance == "White" and dest_coord in Piece.firstRow:
                                    legal_moves.append(dest_coord)
                                else:
                                    legal_moves.append(dest_coord)

                        elif board.en_pass_pawn is not None:

                            if board.en_pass_pawnBehind == dest_coord:
                                en_pp = board.en_pass_pawn
                                if not self.alliance == en_pp.alliance:
                                    legal_moves.append(dest_coord)

        return legal_moves
