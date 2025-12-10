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
    def __init__(
        self, width: int, height: int, population: int, food: int, poison: int
    ):
        self.widht = width
        self.height = height
        self.population = population
        self.food = food
        self.poison = poison
        self.grid: list[list[int]] = self._create_start_board()

    def _create_empty_board(self) -> list[list[int]]:
        return [[CellType.EMPTY for _ in range(self.widht)] for _ in range(self.height)]

    def _fil_empty_board(self, emptyBoard: list[list[int]]) -> list[list[int]]:
        board = emptyBoard

        positions = [(x, y) for x in range(self.widht) for y in range(self.height)]
        random.shuffle(positions)

        man = woman = math.floor(self.population / 2)

        valueToPlace = [
            (CellType.MALE, man),
            (CellType.FEMALE, woman),
            (CellType.FOOD, self.food),
            (CellType.POISON, self.poison),
        ]

        index = 0
        for value, count in valueToPlace:
            for _ in range(count):
                x, y = positions[index]
                board[x][y] = value
                index += 1

        return board

    def _create_start_board(self) -> list[list[int]]:
        startBoard = self._create_empty_board()
        board = self._fil_empty_board(startBoard)

        return board
