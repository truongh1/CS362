# Checking if year is a leap year
def isLeapYear(year) :
    if(int(year) < 0):
        raise ValueError('cannot be a negative year!')
    if (int(year) % 400) == 0:
        return True
    if (int(year) % 100) == 0:
        return False
    if (int(year) % 4) == 0:
        return True
    else:
        return False

