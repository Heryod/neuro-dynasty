import random


class Entity:
    """
    Base class intended to be inherited by various entities located on the board

    Attributes:
        position (tuple[int, int]): The (x, y) coordinates of the entity on the board.
        energy (int): The initial energy of the entity, randomly set between 30 and 100.
    """

    def __init__(self, position: tuple[int, int]):
        self.position = position
        self.energy = random.randint(30, 100)
