from enum import IntEnum
from entities import Person, Food, Poison
from collections import defaultdict
import logging
import random
import math

LOG = logging.getLogger(__name__)


class CellType(IntEnum):
    EMPTY = 0


class Board:
    def __init__(
        self, width: int, height: int, start_population: int, start_food: int, start_poison: int
    ):
        self.width = width
        self.height = height
        self.population = start_population
        self.food = start_food
        self.poison = start_poison
        self.grid: list[list[CellType]] = self._create_start_board()

    def _create_empty_board(self) -> list[list[CellType]]:
        board = [[CellType.EMPTY for _ in range(self.width)] for _ in range(self.height)]
        LOG.debug("empty board generated")
        return board

    def _fill_empty_board(self, board: list[list[CellType]]) -> list[list[CellType]]:
        positions = [(x, y) for x in range(self.width) for y in range(self.height)]
        random.shuffle(positions)

        male_population = female_population = math.floor(self.population / 2)

        factory = {
            "male": lambda pos: Person(pos, "male"),
            "female": lambda pos: Person(pos, "female"),
            "food": lambda pos: Food(pos),
            "poison": lambda pos: Poison(pos),
        }

        values_to_place = [
            ("male", male_population if self.population % 2 == 0 else male_population + 1 ),
            ("female", female_population),
            ("food", self.food),
            ("poison", self.poison),
        ]

        index = 0
        for value, count in values_to_place:
            for _ in range(count):
                x, y = positions[index]
                board[y][x] = factory[value]((x, y))
                index += 1

        LOG.debug("board filling ended")
        return board

    def _create_start_board(self) -> list[list[CellType]]:
        start_board = self._create_empty_board()
        board = self._fill_empty_board(start_board)

        LOG.debug(
            f"grid created, width:{self.width}, height:{self.height}, population:{self.population}, food count:{self.food}, poison count:{self.poison}"
        )
        return board

    def get_population(self) -> defaultdict[str, list[list[int]]]:
        """
        population = {
            'male': [[x, y], [x, y] ...]
            'female': [[x, y], [x, y] ...]
        }
        """

        population = defaultdict(list)

        for row in self.grid:
            for cell in row:
                if isinstance(cell, Person):
                    population[cell.sex].append(cell.position)

        return population
