import cv2
import os
from games import getSquareColor

def generateImageMap(boardSet, pieceSet):
    dir = os.path.dirname(__file__)
    board_image = cv2.imread(os.path.join(dir, "sprites", "boards", boardSet + ".png"))


    piece2image = {}

    piece2image["white"] = board_image[0:128, 0:128]
    piece2image["black"] = board_image[0:128, 128:256]

    piece_dir = os.path.join(dir, "sprites", "pieces", pieceSet)
    piece2image["b"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "bB.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["k"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "bK.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["n"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "bN.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["p"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "bP.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["q"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "bQ.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["r"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "bR.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["B"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "wB.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["K"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "wK.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["N"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "wN.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["P"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "wP.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["Q"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "wQ.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)
    piece2image["R"] = cv2.resize(cv2.imread(os.path.join(piece_dir, "wR.png"), cv2.IMREAD_UNCHANGED),
                                  (128, 128), cv2.INTER_AREA)

    return board_image, piece2image


def pastePiece(board, piece, index, isPiece):
    rowIndex = index // 8
    colIndex = index % 8

    new_board = board.copy()
    for row in range(128):
        for col in range(128):
            if isPiece:
                if piece[row][col][3] != 0:
                    new_board[rowIndex * 128 + row][colIndex * 128 + col] = piece[row][col][:3]
            else:
                new_board[rowIndex * 128 + row][colIndex * 128 + col] = piece[row][col][:3]
    return new_board

def getNewPositionImage(currentBoard, currentBoardImage, newBoard, imageMAP):
    newBoardImage = currentBoardImage.copy()
    for square in range(64):
        if currentBoard[square] != newBoard[square]:
            if newBoard[square] != ".":
                newBoardImage = pastePiece(newBoardImage, imageMAP[newBoard[square]], square, True)
            else:
                newBoardImage = pastePiece(newBoardImage, imageMAP[getSquareColor(square)], square, False)
    return newBoardImage

def generateVideo(gameImages):


