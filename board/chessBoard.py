from board.tile import Tile
# Importing the chess pieces
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.nullPiece import NullPiece
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook


class Board:
    # Game Tiles Dictionary
    game_tiles = {}

    en_pass_pawn = None
    en_pass_pawnBehind = None
    current_player = "White"

    def __init__(self):
        pass

    def calculate_active_pieces(self, alliance):

        active_p = []
        for tile in range(len(self.game_tiles)):
            if not self.game_tiles[tile].piece_on_tile.to_string() == "-":
                if self.game_tiles[tile].piece_on_tile.alliance == alliance:
                    active_p.append(self.game_tiles[tile].piece_on_tile)

        return active_p

    @staticmethod
    def calculate_legal_moves(pieces, board):
        all_legals = []
        for piece in pieces:
            piece_moves = piece.calculate_legal_moves(board)
            for move in piece_moves:
                all_legals.append([move, piece])

        return all_legals

    # Create the board
    def create_board(self):

        # A chess board is constitued of 64 tiles
        for tile in range(64):
            self.game_tiles[tile] = Tile(tile, NullPiece())

        # Placing the pieces on the board

        # Placing black pices

        # First Line
        self.game_tiles[0] = Tile(0, Rook("Black", 0))
        self.game_tiles[1] = Tile(1, Knight("Black", 1))
        self.game_tiles[2] = Tile(2, Bishop("Black", 2))
        self.game_tiles[3] = Tile(3, Queen("Black", 3))
        self.game_tiles[4] = Tile(4, King("Black", 4))
        self.game_tiles[5] = Tile(5, Bishop("Black", 5))
        self.game_tiles[6] = Tile(6, Knight("Black", 6))
        self.game_tiles[7] = Tile(7, Rook("Black", 7))
        self.game_tiles[8] = Tile(8, Pawn("Black", 8))
        self.game_tiles[9] = Tile(9, Pawn("Black", 9))

        # Second Line
        self.game_tiles[10] = Tile(10, Pawn("Black", 10))
        self.game_tiles[11] = Tile(11, Pawn("Black", 11))
        self.game_tiles[12] = Tile(12, Pawn("Black", 12))
        self.game_tiles[13] = Tile(13, Pawn("Black", 13))
        self.game_tiles[14] = Tile(14, Pawn("Black", 14))
        self.game_tiles[15] = Tile(15, Pawn("Black", 15))

        # Placing the white pieces

        # First line
        self.game_tiles[48] = Tile(48, Pawn("White", 48))
        self.game_tiles[49] = Tile(49, Pawn("White", 49))
        self.game_tiles[50] = Tile(50, Pawn("White", 50))
        self.game_tiles[51] = Tile(51, Pawn("White", 51))
        self.game_tiles[52] = Tile(52, Pawn("White", 52))
        self.game_tiles[53] = Tile(53, Pawn("White", 53))
        self.game_tiles[54] = Tile(54, Pawn("White", 54))
        self.game_tiles[55] = Tile(55, Pawn("White", 55))

        # Second line
        self.game_tiles[56] = Tile(56, Rook("White", 56))
        self.game_tiles[57] = Tile(57, Knight("White", 57))
        self.game_tiles[58] = Tile(58, Bishop("White", 58))
        self.game_tiles[59] = Tile(59, Queen("White", 59))
        self.game_tiles[60] = Tile(60, King("White", 60))
        self.game_tiles[61] = Tile(61, Bishop("White", 61))
        self.game_tiles[62] = Tile(62, Knight("White", 62))
        self.game_tiles[63] = Tile(63, Rook("White", 63))

    def print_board(self):

        count = 0

        for tiles in range(64):
            print('|', end=self.game_tiles[tiles].piece_on_tile.to_string())
            count += 1

            if count == 8:
                print('|', end='\n')
                count = 0

    def get_board_arr(self):

        board_arr = []

        for tiles in range(len(self.game_tiles)):
            if self.game_tiles[tiles].piece_on_tile.to_string() == "-":
                board_arr.append(0)
            else:
                if self.current_player == "White":
                    board_arr.append(self.game_tiles[tiles].piece_on_tile.value)
                else:
                    board_arr.append(-self.game_tiles[tiles].piece_on_tile.value)

        return board_arr

    def get_board_arr_side(self):

        board_arr = []

        for tiles in range(len(self.game_tiles)):
            if self.game_tiles[tiles].piece_on_tile.to_string() == "-":
                board_arr.append(0)
            else:
                if self.game_tiles[tiles].piece_on_tile.alliance == "White":
                    board_arr.append(self.game_tiles[tiles].piece_on_tile.value)
                else:
                    board_arr.append(-self.game_tiles[tiles].piece_on_tile.value)

        return board_arr
