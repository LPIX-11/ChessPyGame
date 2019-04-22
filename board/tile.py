class Tile:
    # Piece placed on tiles
    piece_on_tile = None
    tile_coordinate = None

    def __init__(self, coordinate, piece):
        self.tile_coordinate = coordinate
        self.piece_on_tile = piece
