with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/supply_stacks_input.txt", "r+") as f:

    matrix = []

    for line_number, line in enumerate(f):
        if line_number >= 8:
            break

        boxes = []
        cache = []
        for box in line:
            cache.append(box)

            if len(cache) == 4:
                boxes.append("".join(cache).strip())
                cache = []

        for index, column_box in enumerate(boxes):
            if len(matrix) <= index:
                matrix.append([])

            if column_box:
                matrix[index].append(column_box)

    for line in f:
        break

    for line in f:
        line = line.strip().split(" ")

        movements = int(line[1])

        first_column = int(line[3])
        second_column = int(line[5])

        for i in range(movements):
            box = matrix[first_column-1].pop(0)
            matrix[second_column-1].insert(0, box)

    result = ""
    for column in matrix:
        result += column[0][1]

    print(result)

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/supply_stacks_input.txt", "r+") as f:

    matrix = []

    for line_number, line in enumerate(f):
        if line_number >= 8:
            break

        boxes = []
        cache = []
        for box in line:
            cache.append(box)

            if len(cache) == 4:
                boxes.append("".join(cache).strip())
                cache = []

        for index, column_box in enumerate(boxes):
            if len(matrix) <= index:
                matrix.append([])

            if column_box:
                matrix[index].append(column_box)

    for line in f:
        break

    for line in f:
        line = line.strip().split(" ")

        movements = int(line[1])

        first_column = int(line[3])
        second_column = int(line[5])


        boxs = matrix[first_column-1][:movements:]
        del matrix[first_column-1][:movements]

        for box in boxs[::-1]:
            matrix[second_column-1].insert(0, box)

    result = ""
    for column in matrix:
        result += column[0][1]

    print(result)
