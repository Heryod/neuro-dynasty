from core import Board
from config import get_board_settings, setup_logging
import logging

setup_logging()

LOG = logging.getLogger(__name__)


def GenerateBoard():
    settings = get_board_settings()
    board = Board(
        settings["board_width"],
        settings["board_height"],
        settings["initial_population"],
        settings["initial_food"],
        settings["initial_poison"],
    )
    return board


def main() -> None:
    board = GenerateBoard()
    # print(board.grid)


if __name__ == "__main__":
    main()
