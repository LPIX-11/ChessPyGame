# Importing pygame library for game environement building
import pygame
import os
from pygame.locals import *
# Importing the chess board
from board.chessBoard import Board
from board.move import Move

from ai.minimax import Minimax

# Initializing the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'  # You have to call this before pygame.init()
pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

# Setting up the game frame layout
gameDisplay = pygame.display.set_mode((800, 800), RESIZABLE)
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

## Experiment ##

current_player = chessBoard.current_player


## End ##

# Drawing the chess game on screen
############################
def createSqParams():
    allSqRanges = []
    xMin = 0
    xMax = 100
    yMin = 0
    yMax = 100
    for _ in range(8):
        for _ in range(8):
            allSqRanges.append([xMin, xMax, yMin, yMax])
            xMin += 100
            xMax += 100
        xMin = 0
        xMax = 100
        yMin += 100
        yMax += 100
    return allSqRanges


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
            else:
                squares(x_pos, y_pos, width, height, black)

            if not chessBoard.game_tiles[number_of_tile].piece_on_tile.to_string() == '-':
                img = pygame.image.load('./ChessArt/'
                                        + chessBoard.game_tiles[number_of_tile].piece_on_tile.alliance[0]
                                        + chessBoard.game_tiles[number_of_tile].piece_on_tile.to_string().upper()
                                        + '.png')

                # Reformat the image by 100 x 100
                img = pygame.transform.scale(img, (90, 90))

                all_pieces.append([img, [x_pos, y_pos], chessBoard.game_tiles[number_of_tile].piece_on_tile])

            x_pos += 100

            color += 1
            number_of_tile += 1
            # Ended the first raw

        color += 1
        x_pos = 0
        y_pos += 100


## Experiment ##
def updateChessPieces():
    xpos = 0
    ypos = 0
    number = 0
    newPieces = []

    for _ in range(8):
        for _ in range(8):
            if not chessBoard.game_tiles[number].piece_on_tile.to_string() == "-":
                img = pygame.image.load(
                    "./ChessArt/" + chessBoard.game_tiles[number].piece_on_tile.alliance[0].upper() + chessBoard.game_tiles[
                        number].piece_on_tile.to_string().upper() + ".png")
                img = pygame.transform.scale(img, (100, 100))

                newPieces.append([img, [xpos, ypos], chessBoard.game_tiles[number].piece_on_tile])
            xpos += 100
            number += 1
        xpos = 0
        ypos += 100

    return newPieces


## End ##

############################


#### Experiment ###

selectedImage = None
selectedLegals = None
resetColors = []
## End ##

draw_chess_pieces()

allSqParams = createSqParams()

quitGame = False

while not quitGame:

    # Every frame that're going to be displayed
    for event in pygame.event.get():

        # Quiting the game
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

        ####################
        # Experiment #
        ####################

        if event.type == pygame.MOUSEBUTTONDOWN:

            if selectedImage == None:
                mx, my = pygame.mouse.get_pos()
                for piece in range(len(all_pieces)):

                    if all_pieces[piece][2].alliance == current_player:

                        if all_pieces[piece][1][0] < mx < all_pieces[piece][1][0] + 100:
                            if all_pieces[piece][1][1] < my < all_pieces[piece][1][1] + 100:
                                selectedImage = piece
                                prevx = all_pieces[piece][1][0]
                                prevy = all_pieces[piece][1][1]

                                selectedLegals = all_pieces[selectedImage][2].calculate_legal_moves(chessBoard)
                                for legals in selectedLegals:
                                    resetColors.append([legals, all_tiles[legals][0]])

                                    if all_tiles[legals][0] == (66, 134, 244):
                                        all_tiles[legals][0] = (135, 46, 40)
                                    else:
                                        pass

                                    all_tiles[legals][0] = (183, 65, 56)

        if event.type == pygame.MOUSEMOTION and selectedImage is not None:
            mx, my = pygame.mouse.get_pos()
            all_pieces[selectedImage][1][0] = mx - 50
            all_pieces[selectedImage][1][1] = my - 50

            # #TODO highlight all legal moves
            # selectedLegals = all_pieces[selectedImage][2].calculate_legal_moves(chessBoard)
            # for legals in selectedLegals:
            #     resetColors.append([legals ,allTiles[legals][0]])
            #

        if event.type == pygame.MOUSEBUTTONUP:

            for resets in resetColors:
                all_tiles[resets[0]][0] = resets[1]

            try:

                piece_moves = all_pieces[selectedImage][2].calculate_legal_moves(chessBoard)
                legal = False
                theMove = 0
                for moveDes in piece_moves:
                    if allSqParams[moveDes][0] < all_pieces[selectedImage][1][0] + 50 < allSqParams[moveDes][1]:
                        if allSqParams[moveDes][2] < all_pieces[selectedImage][1][1] + 50 < allSqParams[moveDes][3]:
                            legal = True
                            theMove = moveDes
                if legal == False:
                    all_pieces[selectedImage][1][0] = prevx
                    all_pieces[selectedImage][1][1] = prevy
                else:
                    all_pieces[selectedImage][1][0] = allSqParams[theMove][0]
                    all_pieces[selectedImage][1][1] = allSqParams[theMove][2]

                    # TODO make it so it updates board
                    # TODO update moved piece's legal moves some how
                    # print(all_pieces[selectedImage][2])
                    # print(theMove)
                    # print(chessBoard)
                    thisMove = Move(chessBoard, all_pieces[selectedImage][2], theMove)
                    newBoard = thisMove.createNewBoard()
                    if not newBoard == False:
                        chessBoard = newBoard
                    # else:
                    #     print(newBoard)
                    # chessBoard.printBoard()

                    # TODO update game pieces
                    newP = updateChessPieces()
                    all_pieces = newP
                    # print(len(newP))

                    # print(chessBoard.current_player)
                    current_player = newBoard.current_player

                    # TODO add logic that it is AI player
                    if current_player == "Black":
                        aiBoard = True
                        minimax = Minimax(chessBoard, 1)
                        aiBoard = minimax.getMove()
                        # aiBoard.printBoard()
                        # aiBoard.printBoard()
                        chessBoard = aiBoard

                        # TODO update game pieces
                        newP = updateChessPieces()
                        all_pieces = newP
                        current_player = aiBoard.current_player

                        # pygame.time.delay(1000)

                    # minimax.board.printBoard()

                    # all_pieces[selectedImage][2].position = theMove
                    # all_pieces[selectedImage][2].position = theMove
                    # print(all_pieces[selectedImage][2].position)

            except:
                pass

            prevy = 0
            prevx = 0
            selectedImage = None
    for info in all_tiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

        ### End ####

    # Placing pieces on board
    for img in all_pieces:
        gameDisplay.blit(img[0], img[1])

    # Setting up the FPS
    pygame.display.update()
    # Every 60 Secs 60 Frame
    clock.tick(60)
