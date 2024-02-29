"""
Given an array of birds where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

========SAMPLE========

Input:
[1, 4, 4, 4, 5, 3]

Output:
4

EXPLANATION:

The different types of birds occur in the following frequencies:

Type 1 : 1 bird
Type 2 : 0 birds
Type 3 : 1 bird
Type 4 : 3 birds
Type 5 : 1 bird

The type number that occurs at the highest frequency is type 4.
"""

def migratory_birds(birds_list):
    birds_list = [int(bird) for bird in birds_list]
    birds_dict = {}
    
    for bird in range(max(birds_list)+1):
        birds_dict[bird] = 0
    
    for bird in birds_list:
        if bird not in birds_dict:
            birds_dict[bird] = 1

        birds_dict[bird] += 1
    
    best_bird = [0, 0]  # [bird, number of birds]
    for bird_id, bird_count in birds_dict.items():
        if bird_count > best_bird[1]:
            best_bird[0]=bird_id
            best_bird[1]=bird_count

    return best_bird[0]
