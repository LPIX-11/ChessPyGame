# Importing pygame library for game environement building
import pygame
# Importing the chess board
from board.chessBoard import Board

# Initializing the environment
pygame.init()

# Setting up the game frame layout
gameDisplay = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Johnson Chess")

# Keeping track of our game
clock = pygame.time.Clock()

# Initializing the chess board
chessBoard = Board()

# Creating the board
chessBoard.create_board()

# Printing the board on console
chessBoard.print_board()

# Keeping track of tiles and pieces
all_tiles = []
all_pieces = []

# Drawing the chess game on screen
############################

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    all_tiles.append([color, [x, y, w, h]])


def draw_chess_pieces():
    x_pos = 0
    y_pos = 0
    color = 0
    width = 100
    height = 100

    black = (99, 99, 89)
    white = (210, 203, 121)

    number_of_tile = 0

    for _ in range(8):
        for _ in range(8):

            if color % 2 == 0:
                squares(x_pos, y_pos, width, height, white)
                if not chessBoard.gameTiles[number_of_tile].piece_on_tile.toString() == '-':
                    img = pygame.image.load('./ChessArt/'
                                            + chessBoard.gameTiles[number_of_tile].piece_on_tile.alliance[0]
                                            + chessBoard.gameTiles[number_of_tile].piece_on_tile.toString().upper()
                                            + '.png')

                    # Reformat the image by 100 x 100
                    img = pygame.transform.scale(img, (100, 100))

                    all_pieces.append([img, [x_pos, y_pos], chessBoard.gameTiles[number_of_tile].piece_on_tile])

                x_pos += 100
            else:
                squares(x_pos, y_pos, width, height, black)
                if not chessBoard.gameTiles[number_of_tile].piece_on_tile.toString() == '-':
                    img = pygame.image.load('./ChessArt/'
                                            + chessBoard.gameTiles[number_of_tile].piece_on_tile.alliance[0]
                                            + chessBoard.gameTiles[number_of_tile].piece_on_tile.toString().upper()
                                            + '.png')

                    # Reformat the image by 100 x 100
                    img = pygame.transform.scale(img, (100, 100))

                    all_pieces.append([img, [x_pos, y_pos], chessBoard.gameTiles[number_of_tile].piece_on_tile])

                x_pos += 100

            color += 1
            number_of_tile += 1
            # Ended the first raw

        color += 1
        x_pos = 0
        y_pos += 100


############################

draw_chess_pieces()

quitGame = False

while not quitGame:

    # Every frame that're going to be displayed
    for event in pygame.event.get():

        # Quiting the game
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    # Setting up the FPS
    pygame.display.update()
    # Every 60 Secs 60 Frame
    clock.tick(60)
