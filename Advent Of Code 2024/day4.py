
with open("day4_input.txt", "r") as f:
    text = f.read()

matrix = []
for line in text.splitlines():
    matrix.append(list(line))

# =================================================

rows = len(matrix)
cols = len(matrix[0])

count = 0

# for row_index, row in enumerate(matrix):
#     for column_index, char in enumerate(row):
#         if char == "X":
#             directions = []

#             for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
#                 new_row, new_col = row_index, column_index

#                 for next_char in ("M", "A", "S"):
#                     new_row += dr
#                     new_col += dc

#                     if 0 > new_row or new_row >= rows or 0 > new_col or new_col >= cols:
#                         break

#                     if matrix[new_row][new_col] != next_char:
#                         break

#                 else:
#                     count += 1

# print(count)

chars = ("M", "S")

for row_index, row in enumerate(matrix):
    for column_index, char in enumerate(row):
        if row_index == 0 or column_index == 0 or row_index == rows - 1 or column_index == cols - 1:
            continue
                
        if char == "A":
            up_left = matrix[row_index - 1][column_index - 1]
            down_right = matrix[row_index + 1][column_index + 1]
            
            up_right = matrix[row_index - 1][column_index + 1]
            down_left = matrix[row_index + 1][column_index - 1]
            
            if up_left not in chars:
                continue
            
            if down_right == up_left or down_right not in chars:
                continue
            
            if up_right not in chars:
                continue
            
            if down_left == up_right or down_left not in chars:
                continue
            
            count += 1

print(count)
