"""
Given an array of integers "s" with len "n" and a positive integer "k".
Determine the number of ("i", "j") pairs where "i" < "j" and s["i"] + s["j"] is divisible by "k"

========SAMPLE========

Input:
s = [1, 3, 2, 6, 1, 2]
n = 6
k = 3

Output:
5

EXPLANATION:

Here are the 5 valid pairs when the number is divisible by k (3):

(0, 2) -> s[0] + s[2] = 1 + 2 = 3
(0, 5) -> s[0] + s[5] = 1 + 2 = 3
(1, 3) -> s[1] + s[3] = 3 + 6 = 9
(2, 4) -> s[2] + s[4] = 2 + 1 = 3
(4, 5) -> s[4] + s[5] = 1 + 2 = 3
"""

def subarray_division(s, n , k):
    arrays_counter = 0
        
    for first_number, first_number_index in zip(s, range(n)):
        for second_number, second_number_index in zip(s, range(n)):
            
            if (first_number_index < second_number_index) and ((first_number + second_number) % k == 0):
                arrays_counter += 1
                print(first_number, "---", second_number)
                
    return arrays_counter
