"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

    1. The elements of the first array are all factors of the integer being considered
    2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.


==========SAMPLE==========

Input:
2 4
16 32 96

Output:
3

EXPLANATION:

2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.
"""

def get_total_x(a, b):
    all_numbers_between_a_b = range(min(a), min(b)+1)

    factors = a
    numbers = b
    factors_numbers = []

    for number_between_a_b in all_numbers_between_a_b:
        error = 0
        
        for factor in factors:
            if number_between_a_b % factor != 0:
                error += 1
        
        for number in numbers:
            if number % number_between_a_b != 0:
                error += 1
        
        if error != 0:
            continue
        
        factors_numbers.append(number_between_a_b)
            
    return len(factors_numbers)


a = [2, 4]
b = [16, 32, 96]

print(get_total_x(a, b))

a = [3, 4]
b = [24, 48]

print(get_total_x(a, b))
