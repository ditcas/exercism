"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0
    health = 3

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1 # Cada vegada que es crea un alien es crida aquest mètode (és un constructor) i per tant el podem usar per actualitzar el contador d'aliens creats.

    def hit(self):
        # decrements the "health" class variable by 1
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        # returns True if alien's health > 0, if not False
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        # moves the Alien to another coordinates
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        # detects if the Alien has collisioned with another object
        pass



#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(alien_start_positions: list) -> list:
    """
    Creates a `list` of `Alien()` objects given a list of initial positions (coordinates).

    :param alien_start_positions: list - of tuples giving the alien's positions
    :return aliens: list - of "Alien()" objects
    """
    aliens = []

    for start_position in alien_start_positions:
        aliens.append(Alien(start_position[0], start_position[1]))

    return aliens
