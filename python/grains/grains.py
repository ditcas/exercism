def square(number):
    try:
        number = int(number)
    except TypeError as err:
        raise print(f"Error: {err}")

    if (number <= 0) or (number > 64):
        raise ValueError("square must be between 1 and 64")
    
    return 2**(number -1)


def total():
    total_grains = 0

    for number in range(1, 65):
        total_grains += square(number)

    return total_grains