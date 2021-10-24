from games import getBoards
from visualize import generateImageMap, generateVideo, generateGameImages

PGN_NAME = "karpov_kasparov_1984.pgn"

game = getBoards(PGN_NAME)

BOARD, MAP = generateImageMap("newspaper", "pixel")
GAME_IMAGES = generateGameImages(game, BOARD, MAP)
generateVideo(GAME_IMAGES, PGN_NAME.split(".")[0])