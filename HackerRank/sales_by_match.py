"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

========SAMPLE========

Input:
[10, 20, 20, 10, 10, 30, 50, 10, 20]

Output:
3

EXPLANATION:

There are 3 pairs of socks:
10 - 10
20 - 20
10 - 10

And 3 loose socks:
30
50
20
"""

def sales_by_match(colors_list):
    pairs = 0
    cache = []
    
    for color in colors_list:     
        if color in cache:
            pairs += 1
            cache.remove(color)
            continue
        
        cache.append(color)
    return pairs

# print(sales_by_match([10, 20, 20, 10, 10, 30, 50, 10, 20]))
