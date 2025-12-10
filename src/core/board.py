from enum import IntEnum
from entities import Person, Food, Poison
import logging
import random
import math

LOG = logging.getLogger(__name__)


class CellType(IntEnum):
    EMPTY = 0


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
        LOG.debug("empty board generated")
        return board

    def _fil_empty_board(self, emptyBoard: list[list[CellType]]) -> list[list[CellType]]:
        board = emptyBoard

        positions = [(x, y) for x in range(self.widht) for y in range(self.height)]
        LOG.debug(type(positions), positions[0])
        random.shuffle(positions)

        male = female = math.floor(self.population / 2)

        FACTORY = {
            "male": lambda pos: Person(pos, "male"),
            "female": lambda pos: Person(pos, "female"),
            "food": lambda pos: Food(pos),
            "poison": lambda pos: Poison(pos),
        }

        valueToPlace = [
            ("male", male),
            ("female", female),
            ("food", self.food),
            ("poison", self.poison),
        ]

        index = 0
        for value, count in valueToPlace:
            for _ in range(count):
                x, y = positions[index]
                board[y][x] = FACTORY[value]((x, y))
                index += 1

        LOG.debug("board filling ended")
        return board

    def _create_start_board(self) -> list[list[CellType]]:
        startBoard = self._create_empty_board()
        board = self._fil_empty_board(startBoard)

        LOG.debug(
            f"grid created, width:{self.widht}, height:{self.height}, population:{self.population}, food count:{self.food}, poison count:{self.poison}"
        )
        return board
