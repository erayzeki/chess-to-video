import chess
import chess.pgn

def readPGN(fileName):
    try:
        pgn = open(fileName, encoding="utf-8")
    except:
        print("PGN not found")
        exit()

    games = []
    game = chess.pgn.read_game(pgn)
    while game:
        games.append(game)
        game = chess.pgn.read_game(pgn)
    pgn.close()
    return games

def getBoards(fileName):
    games = readPGN(fileName)
    isMultiple = True
    if len(games) == 1:
        isMultiple = False

    game_boards = []

    for game in games:
        boards = []
        current_board = chess.Board()
        boards.append(str(current_board.copy()).split())
        for move in game.mainline_moves():
            current_board.push(move)
            boards.append(str(current_board.copy()).split())
        game_boards.append(boards)
    return game_boards, isMultiple