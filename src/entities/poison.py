from entities import Entity


class Poison(Entity):
    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
