# Calculating volume of cube
def volume(a):
    # Raise an error and stop the program if ais negative
    if a <= 0:
        raise Exception("Sorry, a must be greater than 0!")

    result = a*a*a
    return result

