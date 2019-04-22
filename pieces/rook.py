from pieces.piece import Piece


class Rook(Piece):
    alliance = None
    position = None
    possibleMoveVectors = [-8, -1, 1, 8]
    value = 500

    # Creating the Rook and alliance with it's position
    def __init__(self, alliance, position):
        super().__init__()
        self.alliance = alliance
        self.position = position

    # Defining a to_string function
    def to_string(self):
        return "R" if self.alliance == "Black" else "r"

    def calculate_legal_moves(self, board):
        legal_moves = []
        for vector in self.possibleMoveVectors:
            dest_coord = self.position
            while 0 <= dest_coord < 64:
                bad_move = self.calculate_edge_cases(dest_coord, vector)
                if bad_move:
                    break
                else:
                    dest_coord += vector
                    if 0 <= dest_coord < 64:
                        dest_tile = board.game_tiles[dest_coord]
                        if dest_tile.piece_on_tile.to_string() == "-":
                            legal_moves.append(dest_coord)
                        else:
                            if not dest_tile.piece_on_tile.alliance == self.alliance:
                                legal_moves.append(dest_coord)
                            # break regardless of alliance because blocked
                            break

        return legal_moves

    @staticmethod
    def calculate_edge_cases(position, vector):
        if position in Piece.firstCol:
            if vector == -1:
                return True

        if position in Piece.eighthCol:
            if vector == 1:
                return True

        return False
