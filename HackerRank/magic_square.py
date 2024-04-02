
"""
We define a magic square to be a n x n matrix of distinct positive
integers from 1 to n^2 where the sum of any row, column, or diagonal of
length n is always equal to the same number: the magic constant.

You will be given a 3 x 3 matrix s of integers in the inclusive range [1, 9].
We can convert any digit a to any other digit b in the range [1, 9] at cost of
[a — b]. Given s, convert it into a magic square at minimal cost. Print this
cost on a new line.

Note: The resulting magic square must contain distinct integers in the
inclusive range [1, 9].

Example

$5=![5, 3, 4), (1. 5, 8], [6, 4, 2)

The matrix looks like this:

534
158
642

We can convert it to the following magic square:

834
159
672

This took three replacements at a cost of [5 — 8] + [8 — 9] + 47]
"""

def magic_square(square):
    used_numbers = list
    left_numbers = list()
    
    for line in square:
        for number in line:
            pass
    
    first_column_sum = 0
    second_column_sum = 0
    third_column_sum = 0
    
    while True:
        if first_column_sum == second_column_sum == third_column_sum:
            break
        
        

    
print(magic_square([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))