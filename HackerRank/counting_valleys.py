"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 

========SAMPLE========

Input:
steps = 8
path = UDDDUDUU


Output:
1

If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley.
"""

def counting_valleys(steps, path):
    level = 0
    valleys = []
    
    max_level = level
    min_level = level
    
    for step in range(steps):
        if path[step] == "U":
            level += 1
        else:
            level -= 1

        if level > max_level:
            max_level = level
        if level < min_level:
            min_level = level

        if level == 0:
            valleys.append((max_level, min_level))
            
            max_level = level
            min_level = level
    
    return valleys
    

print(counting_valleys(8, "UDDDUDUU"))
