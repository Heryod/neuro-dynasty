from entities import Entity


class Food(Entity):
    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
