def get_board_settings() -> dict[str, int]:
    """
    Initial settings of the simulation

    Attributes:
        board_width (int): width of the simulation grid.
        board_height (int): height of the simulation grid.
        initial_population (int): initial started population count.
        initial_food (int): initial started food count.
        initial_poison (int): initial started poison count.
    """
    return {
        "board_width": 5,
        "board_height": 5,
        "initial_population": 4,
        "initial_food": 5,
        "initial_poison": 5,
    }
