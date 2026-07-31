with open("mowing.in") as file:

    n = int(file.readline())

    actual_row = 0
    actual_column = 0 

    explored_cells = {}
    maximum_value = -1

    init_time = 1
    for _ in range(n):

        direction, steps = file.readline().strip().split()
        steps = int(steps)

        for i in range(steps):
            if direction == "N":
                actual_row -= 1
            elif direction == "E":
                actual_column -= 1
            elif direction == "S":
                actual_row += 1
            elif direction == "W":
                actual_column += 1

            cell = (actual_row, actual_column)

            if cell in explored_cells:
                if maximum_value == -1:
                    maximum_value = (init_time + i) - explored_cells[cell]

                if (
                    maximum_value
                    == -1 or (
                        (init_time + i) - explored_cells[cell] < maximum_value
                    )
                ):
                    maximum_value = (init_time + i) - explored_cells[cell]

            explored_cells[cell] = init_time + i

        init_time += steps

    with open("mowing.out", "w") as write_file:
        write_file.write(str(maximum_value))
