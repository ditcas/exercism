COLOR_CODES = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def color_code(color: str) -> int:
    """
    Return the numerical value associated with a particular color band

    :param color: str - band's color
    :return: int - numerical value associated with the color
    """

    color = color.lower()

    return COLOR_CODES[color]


def colors():
    """
    Return the list of the different band colors
    """
    return list(COLOR_CODES.keys())
