from pieces.piece import Piece


class King(Piece):
    alliance = None
    position = None
    possibleMoveVectors = [-9, -7, 7, 9, -8, -1, 1, 8]
    value = 1100

    # Creating the King and alliance with it's position
    def __init__(self, alliance, position):
        super().__init__()
        self.alliance = alliance
        self.position = position

    # Defining a to_string function
    def to_string(self):
        return "K" if self.alliance == "Black" else "k"

    def calculate_legal_moves(self, board):

        legal_moves = []
        for vector in self.possibleMoveVectors:
            dest_coord = self.position + vector

            bad_move = self.calculate_edge_cases(self.position, vector)
            if not bad_move:

                if 0 <= dest_coord < 64:
                    dest_tile = board.game_tiles[dest_coord]
                    if dest_tile.piece_on_tile.to_string() == "-":
                        legal_moves.append(dest_coord)
                    else:
                        if not dest_tile.piece_on_tile.alliance == self.alliance:
                            legal_moves.append(dest_coord)

        enemy_pieces = None
        all_enemy_attacks = []

        if self.alliance == "Black":

            # for tile in range(64):
            #     if not board.game_tiles[tile].piece_on_tile.to_string() == "-":
            #         if not board.game_tiles[tile].piece_on_tile.alliance == self.alliance:
            #             enemy_pieces.append(board.game_tiles[tile].piece_on_tile)
            enemy_pieces = board.calculate_active_pieces("White")

            for enemy in range(len(enemy_pieces)):
                if not enemy_pieces[enemy].to_string() == "k":
                    moves = enemy_pieces[enemy].calculate_legal_moves(board)
                else:
                    moves = enemy_pieces[enemy].helper_cal_legal_moves(board)
                for move in range(len(moves)):
                    all_enemy_attacks.append(moves[move])

        elif self.alliance == "White":

            # for tile in range(64):
            #     if not board.game_tiles[tile].piece_on_tile.to_string() == "-":
            #         if not board.game_tiles[tile].piece_on_tile.alliance == self.alliance:
            #             enemy_pieces.append(board.game_tiles[tile].piece_on_tile)
            enemy_pieces = board.calculate_active_pieces("Black")

            for enemy in range(len(enemy_pieces)):
                if not enemy_pieces[enemy].to_string() == "K":
                    moves = enemy_pieces[enemy].calculate_legal_moves(board)
                else:
                    moves = enemy_pieces[enemy].helper_cal_legal_moves(board)
                for move in range(len(moves)):
                    all_enemy_attacks.append(moves[move])

        if self.firstMove and self.alliance == "Black":

            if board.game_tiles[0].piece_on_tile.to_string() == "R" and board.game_tiles[2].piece_on_tile.firstMove:
                if board.game_tiles[1].piece_on_tile.to_string() == "-":
                    if board.game_tiles[2].piece_on_tile.to_string() == "-":
                        if board.game_tiles[3].piece_on_tile.to_string() == "-":
                            if not 3 in all_enemy_attacks and not 2 in all_enemy_attacks and not 4 in all_enemy_attacks:
                                legal_moves.append(2)

            if board.game_tiles[7].piece_on_tile.to_string() == "R" and board.game_tiles[2].piece_on_tile.firstMove:
                if board.game_tiles[6].piece_on_tile.to_string() == "-":
                    if board.game_tiles[5].piece_on_tile.to_string() == "-":
                        if not 5 in all_enemy_attacks and not 6 in all_enemy_attacks and not 4 in all_enemy_attacks:
                            legal_moves.append(6)

        elif self.firstMove and self.alliance == "White":

            if board.game_tiles[56].piece_on_tile.to_string() == "r" and board.game_tiles[2].piece_on_tile.firstMove:
                if board.game_tiles[57].piece_on_tile.to_string() == "-":
                    if board.game_tiles[58].piece_on_tile.to_string() == "-":
                        if board.game_tiles[59].piece_on_tile.to_string() == "-":
                            if not 58 in all_enemy_attacks and not 59 in all_enemy_attacks and not 60 in all_enemy_attacks:
                                legal_moves.append(58)

            if board.game_tiles[63].piece_on_tile.to_string() == "r" and board.game_tiles[2].piece_on_tile.firstMove:
                if board.game_tiles[62].piece_on_tile.to_string() == "-":
                    if board.game_tiles[61].piece_on_tile.to_string() == "-":
                        if not 62 in all_enemy_attacks and not 61 in all_enemy_attacks and not 60 in all_enemy_attacks:
                            legal_moves.append(62)

        final_legal = []
        for move in legal_moves:
            if move not in all_enemy_attacks:
                final_legal.append(move)

        return final_legal

    @staticmethod
    def calculate_edge_cases(position, vector):

        if position in Piece.firstCol:
            if vector == -9 or vector == 7 or vector == -1:
                return True
        if position in Piece.eighthCol:
            if vector == -7 or vector == 9 or vector == 1:
                return True
        return False

    def helper_cal_legal_moves(self, board):

        legal_moves = []
        for vector in self.possibleMoveVectors:

            dest_coord = self.position + vector

            bad_move = self.calculate_edge_cases(self.position, vector)
            if not bad_move:
                if 0 <= dest_coord < 64:
                    dest_tile = board.game_tiles[dest_coord]
                    if dest_tile.piece_on_tile.to_string() == '-':
                        legal_moves.append(dest_coord)
                    else:
                        if not dest_tile.piece_on_tile.alliance == self.alliance:
                            legal_moves.append(dest_coord)

        return legal_moves
