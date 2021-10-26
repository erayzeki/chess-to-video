from games import getBoards
from visualize import generateImageMap, generateVideo, generateGameImages


PGN_NAME = input("Enter the name of the PGN file: ")
while not PGN_NAME:
    PGN_NAME = input("Enter the name of the PGN file: ")
game = getBoards(PGN_NAME)

BOARD_SET_NAME = input("Enter board style (Default is wood3): ")
if not BOARD_SET_NAME:
    BOARD_SET_NAME = "wood3"
PIECE_SET_NAME = input("Enter piece style (Default cburnett): ")
if not PIECE_SET_NAME:
    PIECE_SET_NAME = "cburnett"
TIME_PER_MOVE = input("Enter moves per second (Default 1): ")
if not TIME_PER_MOVE:
    TIME_PER_MOVE = 1
else:
    TIME_PER_MOVE = int(TIME_PER_MOVE)

print("Processing..")
BOARD, MAP = generateImageMap(BOARD_SET_NAME, PIECE_SET_NAME)
GAME_IMAGES = generateGameImages(game, BOARD, MAP)

generateVideo(GAME_IMAGES, PGN_NAME.split(".")[0], TIME_PER_MOVE)
print(PGN_NAME.split(".")[0] + ".avi created successfully!")