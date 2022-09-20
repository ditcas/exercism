COLOR_CODES = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def value(colors: list) -> int:
    """
    Takes a list of color names (we will take into consideration only the first two) and returns a two digit number according to the value of the color-coded band.

    :param colors: list - of color names. Take only first two into consideration.
    :returns: int - two digit number according the color codes.
    """

    color_code_1 = COLOR_CODES[colors[0].lower()]
    color_code_2 = COLOR_CODES[colors[1].lower()]

    if color_code_1 == 0:
        # better to print 8, 9... instead 08, 09...
        return color_code_2

    return int(str(color_code_1) + str(color_code_2))
