import copy


with open("day6_input.txt", "r") as f:
    text = f.read()

# text = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

# Create the directions and turns
directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

turns = {"^": ">", ">": "v", "v": "<", "<": "^"}

# # Create the matrix
# matrix = []
# for line in text.splitlines():
#     matrix.append(list(line))

# rows = len(matrix) - 1
# cols = len(matrix[0]) - 1

# # Find the guard
# guard = [0, 0]
# stop = False
# for row_index, row in enumerate(matrix):
#     for column_index, char in enumerate(row):
#         if char == "^":
#             guard = [row_index, column_index]

#             stop = True
#             break
#     if stop:
#         break

# # Mark the explored cells in the matrix
# while guard[0] != 0 and guard[0] != rows and guard[1] != 0 and guard[1] != cols:
#     symbol = matrix[guard[0]][guard[1]]

#     direction = directions[symbol]

#     new_row = guard[0] + direction[0]
#     new_col = guard[1] + direction[1]

#     if matrix[new_row][new_col] == "#":
#         matrix[guard[0]][guard[1]] = turns[symbol]
#         continue

#     matrix[guard[0]][guard[1]] = "X"
#     matrix[new_row][new_col] = symbol

#     guard[0] = new_row
#     guard[1] = new_col

# # Count the explored cells
# count = 0
# for row in matrix:
#     for char in row:
#         if char == "X":
#             count += 1

# count += 1

# print(count)


# Create the matrix
matrix = []
for line in text.splitlines():
    matrix.append(list(line))

rows = len(matrix) - 1
cols = len(matrix[0]) - 1

# Find the guard
init_row = 0
init_column = 0
stop = False
for row_index, row in enumerate(matrix):
    for column_index, char in enumerate(row):
        if char == "^":
            init_row, init_column = row_index, column_index

            stop = True
            break
    if stop:
        break


cycles = 0
for row_index, row in enumerate(matrix):
    for column_index, char in enumerate(row):
        if char == "#" or char == "^":
            continue

        new_matrix = copy.deepcopy(matrix)
        new_matrix[row_index][column_index] = "#"
        guard = [init_row, init_column]
        
        explored = set()

        while guard[0] != 0 and guard[0] != rows and guard[1] != 0 and guard[1] != cols:
            symbol = new_matrix[guard[0]][guard[1]]

            direction = directions[symbol]

            new_row = guard[0] + direction[0]
            new_col = guard[1] + direction[1]

            if new_matrix[new_row][new_col] == "#":
                new_matrix[guard[0]][guard[1]] = turns[symbol]
                continue

            new_matrix[guard[0]][guard[1]] = "X"
            new_matrix[new_row][new_col] = symbol

            guard[0] = new_row
            guard[1] = new_col

            explored_cell = (symbol, guard[0], guard[1])
            if  explored_cell not in explored:
                explored.add(explored_cell)
            else:
                cycles += 1
                break

print(cycles)
