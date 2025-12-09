from core import Board
from config import get_board_settings


def GenerateBoard():
    settings = get_board_settings()
    board = Board(settings["board_width"], settings["board_height"])
    return board


print(GenerateBoard().grid)
