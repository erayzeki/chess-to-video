import cv2
import chess
import chess.pgn
from games import get_boards

PGN_NAME = "karpov_kasparov_1984.pgn"

game = get_boards(PGN_NAME)

print(game)


