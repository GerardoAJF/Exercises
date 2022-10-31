"""
The house, is the range between "s" (start point) and "t" (endpoint).

The apple tree is to the left of the house, and the orange tree is to its right.

Assume the trees are located on a single point, where the apple tree is at point "a", and the orange tree is at point "b".

When a fruit falls from its tree, it lands "d" units of distance from its tree of origin along the -axis. *A negative value of means the fruit fell units to the tree's left, and a positive value of means it falls units to the tree's right. *

Given the value of for apples and oranges, determine how many apples and oranges will fall on the house (i.e., in the inclusive range )?

=========SAMPLE========

Input:
s = 7
t = 11 

a = 5 
b = 15 

apples = [-2, 2, 1]
oranges = [5, -6]

Output:
1 1

EXPLANATION:

The first apple falls at position 3.
The second apple falls at position 7.
The third apple falls at position 6.

The first orange falls at position 20.
The second orange falls at position 9.

Only one fruit (the second apple) falls within the region between 7 and 11, so we return 1.
Only one fruit (the second orange) falls within the region between 7 and 11, so we return 1.
"""

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    house_range = range(s, t+1)
    
    #*-------APPLES---------
    
    apple_tree = a
    apples_in_house = 0
    
    for apple in apples:
        apple_position = apple_tree + apple
        
        if apple_position in house_range:
            apples_in_house += 1

    #*------ORANGES---------

    orange_tree = b
    oranges_in_house = 0

    for orange in oranges:
        orange_position = orange_tree + orange

        if orange_position in house_range:
            oranges_in_house += 1

    return apples_in_house, oranges_in_house
