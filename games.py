import chess
import chess.pgn

def read_pgn(fileName):
    pgn = open(fileName, encoding="utf-8")
    game = chess.pgn.read_game(pgn)
    pgn.close()
    return game

def get_boards(fileName):
    game = read_pgn(fileName)
    boards = []
    current_board = chess.Board()

    boards.append(str(current_board.copy()).split())
    for move in game.mainline_moves():
        current_board.push(move)
        boards.append(str(current_board.copy()).split())
    return boards






