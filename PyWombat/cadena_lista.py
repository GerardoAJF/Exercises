import doctest

def string_to_list(string):
    """Convert strings to lists

    >>> string_to_list("Hello World")
    ['Hello', 'World']

    >>> string_to_list("The Rubick Cube Is Not Dificult")
    ['The', 'Rubick', 'Cube', 'Is', 'Not', 'Dificult']
    """
        
    return string.split(" ")

doctest.testmod()
