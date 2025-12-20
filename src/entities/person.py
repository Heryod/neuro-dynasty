from entities import Entity


class Person(Entity):
    def __init__(self, sex: str, position: tuple[int, int]):
        self.sex = sex
        super().__init__(position)
