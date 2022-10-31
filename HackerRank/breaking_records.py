"""
A basketball player records his score on a list.

Holds all the highest score records and the lowest score records.

Return first the number of highest score records and later the number of lowest score records.

========SAMPLE========

Input:
10 5 20 20 4 5 2 25 1

Output
2 4

EXPLANATION:

The player broke her best record twice (20, 25) and her worst record four times (5, 4, 2, 1)
"""

def breaking_records(scores):
    best_record = scores[0]
    worst_record = scores[0]
    
    num_best_record = 0
    num_worst_record = 0
    
    for score in scores:
        if score > best_record:
            best_record = score
            num_best_record += 1
            
        elif score < worst_record:
            worst_record = score
            num_worst_record += 1
            
    return num_best_record, num_worst_record
