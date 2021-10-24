import cv2
import chess
import chess.pgn
from games import getBoards
from visualize import generateImageMap, getNewPositionImage, generateVideo

PGN_NAME = "karpov_kasparov_1984.pgn"

game = getBoards(PGN_NAME)

BOARD, MAP = generateImageMap("newspaper", "pixel")
EMPTY_BOARD = ["."]*64
GAME_IMAGES = []

currentBoardImage = getNewPositionImage(EMPTY_BOARD, BOARD, game[0], MAP)
GAME_IMAGES.append(currentBoardImage)
for boardNumber in range(len(game)-1):
    currentBoardImage = getNewPositionImage(game[boardNumber], currentBoardImage, game[boardNumber+1], MAP)
    GAME_IMAGES.append(currentBoardImage)
    print("Move: " + str(boardNumber+1))

generateVideo(GAME_IMAGES, "deneme")








