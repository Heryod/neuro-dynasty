import unittest
from core.board import Board
import random


class TestBoard(unittest.TestCase):
    def __init__(self):
        self.width = self.height = random.randint(10, 500)
        self.population = random.randint(1, 50)
        self.food = random.randint(1, 50)
        self.poison = random.randint(1, 50)

    def setUp(self):
        self.board = Board(
            self.width,
            self.height,
            self.population,
            self.food,
            self.poison,
        )

    def test_generation(self):
        self.assertEqual(self.board.width, self.width)
        self.assertEqual(self.board.height, self.height)

        self.assertEqual(
            sum(len(coords) for coords in self.board.get_population()), self.population
        )
