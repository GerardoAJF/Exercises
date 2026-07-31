import copy

with open("measurement.in", "r") as file:
    n = int(file.readline())

    sorted_cows = sorted([line.strip().split() for line in file.readlines()], key=lambda x: int(x[0]))

    changes = 0
    
    #Mildred, elsie, bessie
    previous_max = [0, 0, 0]
    actual_max = [0, 0, 0]
    cows = [7, 7, 7]
    for day, cow, diff in sorted_cows:

        if cow == "Mildred":
            cows[0] += int(diff)
        elif cow == "Elsie":
            cows[1] += int(diff)
        elif cow == "Bessie":
            cows[2] += int(diff)

        max_score = max(cows)
        for index, score_cow in enumerate(cows):
            if score_cow == max_score:
                actual_max[index] = 1
                continue
            
            actual_max[index] = 0
        
        if actual_max != previous_max:
            changes += 1
            previous_max = copy.deepcopy(actual_max)
           
    with open("measurement.out", "w") as write_file:
        write_file.write(str(changes))