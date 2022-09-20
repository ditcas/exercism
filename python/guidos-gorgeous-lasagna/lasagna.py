# Constants
EXPECTED_BAKE_TIME = 40 # in minutes
PREPARATION_TIME = 2 # minutes to prepare a single layer of the lasagna


def bake_time_remaining(elapsed_bake_time: int):
    '''
    Calculate how many minutes the lasagna still needs to bake, taking into consideration that the expected bake time is 40 minutes.

    :param elapsed_bake_time: actual minutes the lasagna has been in the oven

    :return: the bake time reamining in minutes
    :rtype: int
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int):
    '''
    Calculate how many minutes you would spend making the lasagna, taking into consideration that you need 2 minutes to prepare a single layer.

    :param number_of_layers: the number of layers you want to add to the lasagna

    :return: the total time preparation in minutes
    :rtype: int
    '''
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    '''
    Calculate the total number of minutes you've been cooking.

    :param number_of_layers: the number of layers you want to add to the lasagna.
    :param elapsed_bake_time: actual minutes the lasagna has been in the oven

    :return: the total time in minutes
    :rtype: int
    '''
    total_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_minutes
