import doctest

def hours_by_days(minutes, days=20):
    """This function return the hours by days with the minutes and days
    
    >>> hours_by_days(7200)
    6

    >>> hours_by_days(10000)
    8
    """

    hours = minutes // 60
    hours_days = hours // days

    return hours_days 

doctest.testmod()
