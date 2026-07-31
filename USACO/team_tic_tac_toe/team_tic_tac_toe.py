with open("tttt.in", "r") as file:
    matrix = [tuple(line.strip()) for line in file.readlines()]

    individual_cows = set()
    team_cows = set()

    for k in range(0, 3):
        row_set = set()
        row_set.add(matrix[k][0]) 
        row_set.add(matrix[k][1])
        row_set.add(matrix[k][2])

        if len(row_set) == 1:
            individual_cows.add(tuple(row_set))
        elif len(row_set) == 2:
            team_cows.add(tuple(row_set))

        column_set = set()
        column_set.add(matrix[0][k])
        column_set.add(matrix[1][k])
        column_set.add(matrix[2][k])

        if len(column_set) == 1:
            individual_cows.add(tuple(column_set))
        elif len(column_set) == 2:
            team_cows.add(tuple(column_set))

    first_diagonal_set = set()
    first_diagonal_set.add(matrix[0][0])
    first_diagonal_set.add(matrix[1][1])
    first_diagonal_set.add(matrix[2][2])

    if len(first_diagonal_set) == 1:
        individual_cows.add(tuple(first_diagonal_set))
    elif len(first_diagonal_set) == 2:
        team_cows.add(tuple(first_diagonal_set))

    second_diagonal_set = set()
    second_diagonal_set.add(matrix[0][2])
    second_diagonal_set.add(matrix[1][1]) 
    second_diagonal_set.add(matrix[2][0]) 

    if len(second_diagonal_set) == 1:
        individual_cows.add(tuple(second_diagonal_set))
    elif len(second_diagonal_set) == 2:
        team_cows.add(tuple(second_diagonal_set))

    with open("tttt.out", "w") as write_file:
        write_file.write(str(len(individual_cows)) + "\n" + str(len(team_cows)))
