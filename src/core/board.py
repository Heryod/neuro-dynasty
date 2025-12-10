from enum import IntEnum
import logging
import random
import math

log = logging.getLogger(__name__)


class CellType(IntEnum):
    EMPTY = 0
    MALE = 1
    FEMALE = 2
    FOOD = 3
    POISON = 4
    WALL = 5


class Board:
    def __init__(self, width: int, height: int, population: int, food: int, poison: int):
        self.widht = width
        self.height = height
        self.population = population
        self.food = food
        self.poison = poison
        self.grid: list[list[CellType]] = self._create_start_board()

    def _create_empty_board(self) -> list[list[CellType]]:
        board = [[CellType.EMPTY for _ in range(self.widht)] for _ in range(self.height)]
        log.debug("empty board created")
        return board

    def _fil_empty_board(self, emptyBoard: list[list[CellType]]) -> list[list[CellType]]:
        board = emptyBoard

        positions = [(x, y) for x in range(self.widht) for y in range(self.height)]
        random.shuffle(positions)

        male = female = math.floor(self.population / 2)

        valueToPlace = [
            (CellType.MALE, male),
            (CellType.FEMALE, female),
            (CellType.FOOD, self.food),
            (CellType.POISON, self.poison),
        ]

        index = 0
        for value, count in valueToPlace:
            for _ in range(count):
                x, y = positions[index]
                board[x][y] = value
                index += 1

        log.debug("board filling ended")
        return board

    def _create_start_board(self) -> list[list[CellType]]:
        startBoard = self._create_empty_board()
        board = self._fil_empty_board(startBoard)

        return board
