import chess
import chess.pgn

def readPGN(fileName):
    pgn = open(fileName, encoding="utf-8")
    game = chess.pgn.read_game(pgn)
    pgn.close()
    return game

def getBoards(fileName):
    game = readPGN(fileName)
    boards = []
    current_board = chess.Board()

    boards.append(str(current_board.copy()).split())
    for move in game.mainline_moves():
        current_board.push(move)
        boards.append(str(current_board.copy()).split())
    return boards