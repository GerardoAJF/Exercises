"""
Given: 
    list "s" 
    number "m" 
    number "d"

Find how many sublists of "s" that have length "m" and that the numbers they contain add up to "d" exist.

========SAMPLE========

Input:
s = 1 2 1 3 2
m = 2
d = 3

Output
2

EXPLANATION:

There are only 2 sublists of list "s" that have a length of 2 and a total sum of 3. 
Those sublists are: [1, 2], [2, 1]
"""

def subarray_division(s, m, d):    
    subarrays = 0
    
    for index in range(len(s)): #[0, 1, 2, 3, 4]
        if index+m > len(s): # Is the ultimate element
            continue
        
        first_index = index
        ultimate_index = index+m
            
        subarray = s[first_index : ultimate_index]
        
        if sum(subarray) == d:
            subarrays += 1
    
    return subarrays
