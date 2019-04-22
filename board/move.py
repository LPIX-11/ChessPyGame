import copy
from board.chessBoard import Board
from board.tile import Tile
from pieces import nullPiece
from pieces import queen
from pieces import rook
# import time


class Move:

    board = None
    movedPiece = None
    destination = None

    def __init__(self, board, movePiece, destination):
        self.board = board
        self.movedPiece = movePiece
        self.destination = destination

    def createNewBoard(self):

        newBoard = Board()
        game_tiles = {}

        # IF THERE WAS AN ENPASSANT PAWN AND WE USED A PAWN TO ATTACK IT'S SQUARE
        # SET A MARKED FOR IT FOR IT TO BE SKIPPED
        enpassLocation = None
        if self.movedPiece.to_string() == 'P':
            if not self.board.en_pass_pawn == None:
                if self.destination == self.board.en_pass_pawnBehind:
                    enpassLocation = self.board.en_pass_pawn.position
        elif self.movedPiece.to_string() == 'p':
            if not self.board.en_pass_pawn == None:
                if self.destination == self.board.en_pass_pawnBehind:
                    enpassLocation = self.board.en_pass_pawn.position

                # FILL NEW BOARD WITH EVERYTHING EXCEPT DESTINATION, CURRENT LOCATION AND ENPASS LOCATION
                # ELSE FILL IT WITH A NULL PIECE FOR NOW
                for tile in range(64):
                    if not tile == self.movedPiece.position and not tile == self.destination and not tile == enpassLocation:
                        game_tiles[tile] = self.board.game_tiles[tile]
                    else:
                        game_tiles[tile] = Tile(tile, nullPiece.NullPiece())

                # IF WE CASTLED, REPLACE THE ROOK WITH A NULL AND MOVE IT TO CORRECT POSITION
                if self.movedPiece.to_string() == 'K' and self.movedPiece.firstMove:
                    if self.destination == 2:
                        if self.board.game_tiles[0].piece_on_tile.to_string() == "R" \
                                and self.board.game_tiles[0].piece_on_tile.firstMove:
                            game_tiles[0] = Tile(0, nullPiece.NullPiece())
                            game_tiles[3] = Tile(3, rook.Rook("Black", 3))
                    elif self.destination == 6:
                        if self.board.game_tiles[7].piece_on_tile.to_string() == "R" \
                                and self.board.game_tiles[7].piece_on_tile.firstMove:
                            game_tiles[7] = Tile(7, nullPiece.NullPiece())
                            game_tiles[5] = Tile(5, rook.Rook("Black", 5))

                # CASTLE FOR WHITE
                elif self.movedPiece.to_string() == 'k':
                    if self.destination == 58:
                        if self.board.game_tiles[56].piece_on_tile.to_string() == "r" \
                                and self.board.game_tiles[56].piece_on_tile.firstMove:
                            game_tiles[56] = Tile(56, nullPiece.NullPiece())
                            game_tiles[59] = Tile(59, rook.Rook("White", 59))
                    elif self.destination == 62:
                        if self.board.game_tiles[63].piece_on_tile.to_string() == "r" \
                                and self.board.game_tiles[56].piece_on_tile.firstMove:
                            game_tiles[63] = Tile(63, nullPiece.NullPiece())
                            game_tiles[61] = Tile(61, rook.Rook("White", 61))

                # FINALLY CREATE A COPY OF MOVED PIECE AND ASSIGN IT TO ITS LOCATION
                updatePiece = copy.copy(self.movedPiece)
                updatePiece.firstMove = False
                updatePiece.position = self.destination
                game_tiles[self.destination] = Tile(self.destination, updatePiece)
                # THEN ASSIGN NEW BOARD'S TILES AS NEW TILES
                newBoard.game_tiles = game_tiles

                # IT WAS A PAWN JUMP MOVE, ASSIGN IT TO BE THE ENPASS PAWN AND SET IT'S LOCATION BEHIND IT
                if self.movedPiece.to_string() == 'P':
                    if self.movedPiece.position + 16 == self.destination:
                        newBoard.en_pass_pawn = updatePiece
                        newBoard.en_pass_pawnBehind = self.movedPiece.position + 8
                elif self.movedPiece.to_string() == 'p':
                    if self.movedPiece.position - 16 == self.destination:
                        newBoard.en_pass_pawn = updatePiece
                        newBoard.en_pass_pawnBehind = self.movedPiece.position - 8

                # IF IT WAS A PAWN MOVE AND IT REACHED THE LAST RANK, REPLACE IT WAS A QUEEN
                if self.movedPiece.to_string() == 'P':
                    if self.destination in self.movedPiece.eighthRow:
                        newBoard.game_tiles[self.destination] = Tile(self.destination,
                                                                    queen.Queen("Black", self.destination))
                elif self.movedPiece.to_string() == 'p':
                    if self.destination in self.movedPiece.firstRow:
                        newBoard.game_tiles[self.destination] = Tile(self.destination,
                                                                    queen.Queen("White", self.destination))

                # SWITCH CURRENT PLAYER OF THE BOARD
                newBoard.current_player = self.board.current_player
                if newBoard.current_player == "White":
                    newBoard.current_player = "Black"
                elif newBoard.current_player == "Black":
                    newBoard.current_player = "White"

                # WITH THE NEW BOARD CREATED, CHECK IF THE OPPONENT DID A VALID MOVE
                good = self.checkChecks(newBoard)

                if not good:
                    return False

                mate = self.checkCheckmateOrStalemate(newBoard, newBoard.current_player)
                if mate:
                    return False

                return newBoard

            def checkMateBoard(self):

                newBoard = Board()
                game_tiles = {}

                # IF THERE WAS AN ENPASSANT PAWN AND WE USED A PAWN TO ATTACK IT'S SQUARE
                # SET A MARKED FOR IT FOR IT TO BE SKIPPED
                enpassLocation = None
                if self.movedPiece.to_string() == 'P':
                    if not self.board.en_pass_pawn == None:
                        if self.destination == self.board.en_pass_pawnBehind:
                            enpassLocation = self.board.en_pass_pawn.position
                elif self.movedPiece.to_string() == 'p':
                    if not self.board.en_pass_pawn == None:
                        if self.destination == self.board.en_pass_pawnBehind:
                            enpassLocation = self.board.en_pass_pawn.position

                # FILL NEW BOARD WITH EVERYTHING EXCEPT DESTINATION, CURRENT LOCATION AND ENPASS LOCATION
                # ELSE FILL IT WITH A NULL PIECE FOR NOW
                for tile in range(64):
                    if not tile == self.movedPiece.position and not tile == self.destination and not tile == enpassLocation:
                        game_tiles[tile] = self.board.game_tiles[tile]
                    else:
                        game_tiles[tile] = Tile(tile, nullPiece.NullPiece())

                # IF WE CASTLED, REPLACE THE ROOK WITH A NULL AND MOVE IT TO CORRECT POSITION
                if self.movedPiece.to_string() == 'K' and self.movedPiece.firstMove:
                    if self.destination == 2:
                        if self.board.game_tiles[0].piece_on_tile.to_string() == "R" \
                                and self.board.game_tiles[0].piece_on_tile.firstMove:
                            game_tiles[0] = Tile(0, nullPiece.NullPiece())
                            game_tiles[3] = Tile(3, rook.Rook("Black", 3))
                    elif self.destination == 6:
                        if self.board.game_tiles[7].piece_on_tile.to_string() == "R" \
                                and self.board.game_tiles[7].piece_on_tile.firstMove:
                            game_tiles[7] = Tile(7, nullPiece.NullPiece())
                            game_tiles[5] = Tile(5, rook.Rook("Black", 5))

                # CASTLE FOR WHITE
                elif self.movedPiece.to_string() == 'k':
                    if self.destination == 58:
                        if self.board.game_tiles[56].piece_on_tile.to_string() == "r" \
                                and self.board.game_tiles[56].piece_on_tile.firstMove:
                            game_tiles[56] = Tile(56, nullPiece.NullPiece())
                            game_tiles[59] = Tile(59, rook.Rook("White", 59))
                    elif self.destination == 62:
                        if self.board.game_tiles[63].piece_on_tile.to_string() == "r" \
                                and self.board.game_tiles[56].piece_on_tile.firstMove:
                            game_tiles[63] = Tile(63, nullPiece.NullPiece())
                            game_tiles[61] = Tile(61, rook.Rook("White", 61))

                # FINALLY CREATE A COPY OF MOVED PIECE AND ASSIGN IT TO ITS LOCATION
                updatePiece = copy.copy(self.movedPiece)
                updatePiece.firstMove = False
                updatePiece.position = self.destination
                game_tiles[self.destination] = Tile(self.destination, updatePiece)
                # THEN ASSIGN NEW BOARD'S TILES AS NEW TILES
                newBoard.game_tiles = game_tiles

                # IT WAS A PAWN JUMP MOVE, ASSIGN IT TO BE THE ENPASS PAWN AND SET IT'S LOCATION BEHIND IT
                if self.movedPiece.to_string() == 'P':
                    if self.movedPiece.position + 16 == self.destination:
                        newBoard.en_pass_pawn = updatePiece
                        newBoard.en_pass_pawnBehind = self.movedPiece.position + 8
                elif self.movedPiece.to_string() == 'p':
                    if self.movedPiece.position - 16 == self.destination:
                        newBoard.en_pass_pawn = updatePiece
                        newBoard.en_pass_pawnBehind = self.movedPiece.position - 8

                # IF IT WAS A PAWN MOVE AND IT REACHED THE LAST RANK, REPLACE IT WAS A QUEEN
                if self.movedPiece.to_string() == 'P':
                    if self.destination in self.movedPiece.eighthRow:
                        newBoard.game_tiles[self.destination] = Tile(self.destination,
                                                                    queen.Queen("Black", self.destination))
                elif self.movedPiece.to_string() == 'p':
                    if self.destination in self.movedPiece.firstRow:
                        newBoard.game_tiles[self.destination] = Tile(self.destination,
                                                                    queen.Queen("White", self.destination))

                # SWITCH CURRENT PLAYER OF THE BOARD
                newBoard.current_player = self.board.current_player
                if newBoard.current_player == "White":
                    newBoard.current_player = "Black"
                elif newBoard.current_player == "Black":
                    newBoard.current_player = "White"

                # WITH THE NEW BOARD CREATED, CHECK IF THE OPPONENT DID A VALID MOVE
                good = self.checkChecks(newBoard)

                if not good:
                    return False

                return newBoard

            def checkChecks(self, newBoard):

                # AFTER MY OPPONENT MOVED AND HE IS STILL IN CHECK, OBVIOUSLY MEANS IT WAS BOT A LEGAL MOVE
                if newBoard.current_player == "White":
                    enemyKing = None
                    for sq in range(len(newBoard.game_tiles)):
                        if newBoard.game_tiles[sq].piece_on_tile.to_string() == "K":
                            enemyKing = newBoard.game_tiles[sq].piece_on_tile.position
                            break

                    myPieces = newBoard.calculate_active_pieces("White")

                    for piece in myPieces:
                        pieceLegals = piece.calculate_legal_moves(newBoard)
                        for legals in pieceLegals:
                            if legals == enemyKing:
                                return False

                else:

                    enemyKing = None
                    for sq in range(len(newBoard.game_tiles)):
                        if newBoard.game_tiles[sq].piece_on_tile.to_string() == "k":
                            enemyKing = newBoard.game_tiles[sq].piece_on_tile.position
                    myPieces = newBoard.calculate_active_pieces("Black")

                    for piece in myPieces:
                        pieceLegals = piece.calculate_legal_moves(newBoard)
                        for legals in pieceLegals:
                            if legals == enemyKing:
                                return False

                return True

            @staticmethod
            def checkCheckmateOrStalemate(board, alliance):
                pieces = board.calculate_active_pieces(alliance)
                moves = board.calculate_legal_moves(pieces, board)

                for myMoves in moves:
                    makeMove = Move(board, myMoves[1], myMoves[0])
                    newboard = makeMove.checkMateBoard()
                    if newboard is not False:
                        return False

                return True