
with open("day8_input.txt", "r") as f:
    text = f.read()

# text = """
# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# """

# Load the matrix
matrix = []
for row in text.strip().splitlines():
    matrix.append(list(row))

rows = len(matrix)
cols = len(matrix[0])

# # Save the frequencies
# frequencies = {}

# for row_index, row in enumerate(matrix):
#     for column_index, char in enumerate(row):

#         if char == ".":
#             continue

#         if char not in frequencies:
#             frequencies[char] = []

#         frequencies[char].append((row_index, column_index))

# count = 0

# for frequency, values in frequencies.items():

#     lines = set()
#     for first_antenna in values:
#         for second_antenna in values:

#             if first_antenna == second_antenna:
#                 continue

#             y_distance = second_antenna[0] - first_antenna[0]
#             x_distance = second_antenna[1] - first_antenna[1]

#             antinode_row = second_antenna[0] + y_distance
#             antinode_column = second_antenna[1] + x_distance

#             if 0 <= antinode_row < rows and 0 <= antinode_column < cols:

#                 if matrix[antinode_row][antinode_column] != "#":
#                     matrix[antinode_row][antinode_column] = "#"
#                     count += 1

# print(count)

# Save the frequencies
frequencies = {}

for row_index, row in enumerate(matrix):
    for column_index, char in enumerate(row):

        if char == ".":
            continue

        if char not in frequencies:
            frequencies[char] = []

        frequencies[char].append((row_index, column_index))


for frequency, values in frequencies.items():

    lines = set()
    for first_antenna in values:
        for second_antenna in values:

            if first_antenna == second_antenna:
                continue
            
            y_distance = second_antenna[0] - first_antenna[0]
            x_distance = second_antenna[1] - first_antenna[1]

            antinode_row = second_antenna[0] + y_distance
            antinode_column = second_antenna[1] + x_distance

            while 0 <= antinode_row < rows and 0 <= antinode_column < cols:

                if matrix[antinode_row][antinode_column] == ".":
                    matrix[antinode_row][antinode_column] = "#"

                antinode_row += y_distance
                antinode_column += x_distance

count = 0
for row in matrix:
    for char in row:
        if char != ".":
            count += 1

for row in matrix:
    print("".join(row))

print(count)
