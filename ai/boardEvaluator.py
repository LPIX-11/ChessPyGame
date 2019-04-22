class BoardEvaluator:

    def __init__(self):
        pass

    def evaluate(self, board, depth):
        return self.scorePlayer("White", board) - self.scorePlayer("Black", board)

    def score_player(self, player, board):
        return self.pieceValue(player, board) + self.mobility(player, board)

    def mobility(self, player, board):
        myPieces = board.calculate_active_pieces(player)
        return len(board.calculate_legal_moves(myPieces, board))

    def pieceValue(self, player, board):
        pieceValues = 0
        myPieces = board.calculate_active_pieces(player)

        for piece in myPieces:
            pieceValues += piece.value

        return pieceValues