import unittest
from core.board import Board
import random


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.height = self.width = random.randint(20, 500)
        self.population = random.randint(1, 50)
        self.food = random.randint(1, 50)
        self.poison = random.randint(1, 50)

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
            sum(len(coords) for coords in self.board.get_population().values()), self.population
        )
        self.assertEqual(self.board.food, self.food)
        self.assertEqual(self.board.poison, self.poison)

    def test_population_no_duplicate_coords(self):
        all_coords = []

        for coords_list in self.board.get_population().values():
            for coord in coords_list:
                all_coords.append(tuple(coord))

        unique_coords = set(all_coords)
        self.assertEqual(len(all_coords), len(unique_coords))
