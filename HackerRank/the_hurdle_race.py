"""
A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.

========SAMPLE========

Input:
n = 5
k = 4
heights = 1 6 3 5 2

Output:
2

EXPLANATION:
To be able to jump all the hurdles, Dan must drink 6 - 4 = 2 doses.
"""

def hurdle_race (k, height):
    max_height = max(height)

    if (k < max_height):
        return max_height - k
    return 0

print(hurdle_race(7, [2, 5, 4, 5, 2]))
