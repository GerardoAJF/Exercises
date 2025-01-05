with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/rope_bridge_input.txt", "r+") as f:
    
    initial_cell = [0, 0]

    visited_cells = [initial_cell]
    
    T = initial_cell
    H = initial_cell
    
    def matrix(line, column):
        left_up_diagonal = [line + 1, column - 1]
        left_down_diagonal = [line - 1, column - 1]
    
        right_up_diagonal = [line + 1, column + 1]
        right_down_diagonal = [line - 1, column + 1]
    
        center_up = [line + 1, column]
        center_down = [line - 1, column]
        center_left = [line, column - 1]
        center_right = [line, column + 1]
    
        return  left_up_diagonal, left_down_diagonal, right_up_diagonal, right_down_diagonal, center_up, center_down, center_left, center_right
    
    for number, line in enumerate(f):
        line = line.strip().split(" ")

        if line[0] == "L":
            for i in range(int(line[1])):
                H = [H[0], H[1] - 1]
                
                if T not in matrix(*H):
                    T = [H[0], T[1]]
                
                else:
                    continue
                
                if H == T:
                    continue
                
                T = [T[0], H[1] + 1]
                
                if T not in visited_cells:
                    visited_cells.append(T)

        if line[0] == "R":
            for i in range(int(line[1])):
                H = [H[0], H[1]+ 1]
                
                if T not in matrix(*H):
                    T = [H[0], T[1]]
                    
                else:
                    continue
                
                if H == T:
                    continue
                
                T = [T[0], H[1] - 1]

                if T not in visited_cells:
                    visited_cells.append(T)
                
        if line[0] == "U":
            for i in range(int(line[1])):
                H = [H[0] + 1, H[1]]
                
                if T not in matrix(*H):
                    T = [T[0], H[1]]
                    
                else:
                    continue
                
                if H == T:
                    continue
                
                T = [H[0] - 1, T[1]]
                
                if T not in visited_cells:
                    visited_cells.append(T)
                
        if line[0] == "D":
            for i in range(int(line[1])):
                H = [H[0] - 1, H[1]]
                
                if T not in matrix(*H):
                    T = [T[0], H[1]]
                    
                else:
                    continue
                
                if H == T:
                    continue
                
                T = [H[0] + 1, T[1]]

                if T not in visited_cells:
                    visited_cells.append(T)

    print(len(visited_cells))

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/rope_bridge_input.txt", "r+") as f:

    initial_cell = [0, 0]

    visited_cells = [initial_cell]

    H = initial_cell
    one = initial_cell
    two = initial_cell
    tree = initial_cell
    four = initial_cell
    five = initial_cell
    six = initial_cell
    seven = initial_cell
    eight = initial_cell
    T = initial_cell

    all_cells = [H, one, two, tree, four, five, six, seven, eight, T]

    def matrix(line, column):
        center_up = [line + 1, column]
        center_down = [line - 1, column]
        center_left = [line, column - 1]
        center_right = [line, column + 1]
        
        left_up_diagonal = [line + 1, column - 1]
        left_down_diagonal = [line - 1, column - 1]

        right_up_diagonal = [line + 1, column + 1]
        right_down_diagonal = [line - 1, column + 1]

        return left_up_diagonal, left_down_diagonal, right_up_diagonal, right_down_diagonal, center_up, center_down, center_left, center_right

    for line in ["R 5",
                 "U 8",
                 "L 8",]:
        line = line.strip().split(" ")

        if line[0] == "L":
            for i in range(int(line[1])):
                all_cells[0] = [all_cells[0][0], all_cells[0][1] - 1]

                for cell in all_cells[1:]:
                    previous_cell = all_cells[all_cells.index(cell) - 1]

                    print("-", cell)
                    print("-", previous_cell)
                    print("-", all_cells)

                    if cell not in matrix(*previous_cell) and previous_cell != cell:
                        if [previous_cell[0], previous_cell[1] + 1] in matrix(*cell):
                            print("normal")
                            print([previous_cell[0], previous_cell[1] + 1])
                            all_cells[all_cells.index(cell)] = [previous_cell[0], previous_cell[1] + 1]

                        else:
                            print("not normal")
                            for sub_cell in matrix(*cell):
                                if previous_cell in matrix(*sub_cell):
                                    print("loop")
                                    print([sub_cell[0], sub_cell[1]])
                                    all_cells[all_cells.index(cell)] = [sub_cell[0], sub_cell[1]]
                                    break

                        if all_cells[-1] not in visited_cells:
                            visited_cells.append(all_cells[-1])
                print("***", all_cells)
                
        if line[0] == "R":
            for i in range(int(line[1])):
                all_cells[0] = [all_cells[0][0], all_cells[0][1] + 1]

                for cell in all_cells[1:]:
                    previous_cell = all_cells[all_cells.index(cell) - 1]

                    if cell not in matrix(*previous_cell) and previous_cell != cell:
                        if [previous_cell[0], previous_cell[1] - 1] in matrix(*cell):
                            all_cells[all_cells.index(cell)] = [previous_cell[0], previous_cell[1] - 1]

                        else:
                            for sub_cell in matrix(*cell):
                                if previous_cell in matrix(*sub_cell):
                                    all_cells[all_cells.index(cell)] = [sub_cell[0], sub_cell[1]]
                                    break        

                        if all_cells[-1] not in visited_cells:
                            visited_cells.append(all_cells[-1])

        if line[0] == "U":
            for i in range(int(line[1])):                                
                all_cells[0] = [all_cells[0][0] + 1, all_cells[0][1]]

                for cell in all_cells[1:]:
                    previous_cell = all_cells[all_cells.index(cell) - 1]

                    if cell not in matrix(*previous_cell) and previous_cell != cell:
                        
                        if [previous_cell[0] - 1, previous_cell[1]] in matrix(*cell):
                            all_cells[all_cells.index(cell)] = [previous_cell[0] - 1, previous_cell[1]]
     
                        else:
                            for sub_cell in matrix(*cell):
                                if previous_cell in matrix(*sub_cell):
                                    all_cells[all_cells.index(cell)] = [sub_cell[0], sub_cell[1]]
                                    break
                                
                        if all_cells[-1] not in visited_cells:
                            visited_cells.append(all_cells[-1])

        if line[0] == "D":
            for i in range(int(line[1])):
                all_cells[0] = [all_cells[0][0] - 1, all_cells[0][1]]

                for cell in all_cells[1:]:
                    previous_cell = all_cells[all_cells.index(cell) - 1]

                    if cell not in matrix(*previous_cell) and previous_cell != cell:
                        if [previous_cell[0] + 1, previous_cell[1]] in matrix(*cell):
                           all_cells[all_cells.index(cell)] = [previous_cell[0] + 1, previous_cell[1]]

                        else:
                            for sub_cell in matrix(*cell):
                                if previous_cell in matrix(*sub_cell):
                                    all_cells[all_cells.index(cell)] = [sub_cell[0], sub_cell[1]]
                                    break

                        if all_cells[-1] not in visited_cells:
                            visited_cells.append(all_cells[-1])

        print("xd",all_cells)
        print(visited_cells)
        print(len(visited_cells))

"""    
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
#.........................
#.............###.........
#............#...#........
.#..........#.....#.......
..#..........#.....#......
...#........#.......#.....
....#......s.........#....
.....#..............#.....
......#............#......
.......#..........#.......
........#........#........
.........########.........
"""