class Tile:

    # Piece placed on tiles
    pieceOnTile = None
    tileCoordonate = None

    def __init__(self, coordonate, piece):
        self.tileCoordonate = coordonate
        self.pieceOnTile = piece
