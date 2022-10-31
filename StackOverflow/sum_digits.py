"""
sum digits is a function to sum every digit of a number with other number

EXAMPLES:

> sum_digits(1111, 8)
9999

> sum_digits(8109, 2)
10331
"""

def sum_digits(number, digit_addition):
    number = str(number)
    digit_addition = str(digit_addition)
    
    number_addition = digit_addition * len(number)
    
    return int(number) + int(number_addition)
