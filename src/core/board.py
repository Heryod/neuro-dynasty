from enum import IntEnum
import random


class CellType(IntEnum):
    EMPTY = 0
    MALE = 1
    FEMALE = 2
    FOOD = 3
    POISON = 4
    WALL = 5


class Board:
    def __init__(self, width: int, height: int):
        self.widht = width
        self.height = height
        self.grid: list[list[int]] = self._create_empty_board()

    def _create_empty_board(self) -> list[list[int]]:
        return [[CellType.EMPTY for _ in range(self.widht)] for _ in range(self.height)]

    def _create_start_board(self, population, food, poison) -> list[list[int]]:
        empty_board = self._create_empty_board()

        position = random.sample(
            range(self.widht * self.height), population + food + poison
        )

        for i in range(population):
            x = position[i] % self.widht
            y = position[i] // self.widht

            print(x, y)

        return empty_board
