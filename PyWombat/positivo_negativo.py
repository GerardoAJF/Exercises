import doctest

def positive_or_negative(number):
    """Return is the number is negative, neutral or positive

    >>> positive_or_negative(10)
    'positive'

    >>> positive_or_negative(0)
    'neutral'

    >>> positive_or_negative(-100)
    'negative'
    
    """

    if number < 0:
        return "negative"
    elif number == 0:
        return "neutral"
    elif number > 0:
        return "positive"

doctest.testmod()
