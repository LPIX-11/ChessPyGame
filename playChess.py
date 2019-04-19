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
chessBoard.createBoard()

# Printing the board on console
chessBoard.printBoard()

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
