with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/counting_calories_input.txt", "r+") as f:

    calories = [[0, 0]]
    for line in f:
        line = line.strip()

        if line == "":
            calories.append([calories[-1][0] + 1, 0])
            continue

        calories[-1][1] += int(line)
    
    max_calorie = 0 # TOP TREE
    for calorie in calories:
        if calorie[1] >= max_calorie:
            max_calorie = calorie[1]

    print(max_calorie)

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/counting_calories_input.txt", "r+") as f:

    calories = [[0, 0]]
    for line in f:
        line = line.strip()

        if line == "":
            calories.append([calories[-1][0] + 1, 0])
            continue

        calories[-1][1] += int(line)

    max_calories = [[0, 0], [0, 0], [0, 0]]  # TOP TREE
    for calorie in calories:
        if calorie[1] >= max_calories[0][1]:
            max_calories[0] = calorie

        elif calorie[1] >= max_calories[1][1]:
            max_calories[1] = calorie

        elif calorie[1] >= max_calories[2][1]:
            max_calories[2] = calorie

    print(max_calories)
    print(max_calories[0][1] + max_calories[1][1] + max_calories[2][1])
