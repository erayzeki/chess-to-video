from games import getBoards
from visualize import generateImageMap, generateVideo, generateGameImages
import sys
import time

PGN_NAME = sys.argv[1]
BOARD_SET_NAME = sys.argv[2]
PIECE_SET_NAME = sys.argv[3]
TIME_PER_MOVE = int(sys.argv[4])

game = getBoards(PGN_NAME)

BOARD, MAP = generateImageMap(BOARD_SET_NAME, PIECE_SET_NAME)

start = time.time()
GAME_IMAGES = generateGameImages(game, BOARD, MAP)
end = time.time()
print("\nTime: " + str(end - start))

generateVideo(GAME_IMAGES, PGN_NAME.split(".")[0], TIME_PER_MOVE)