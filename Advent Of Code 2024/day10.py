import pprint

with open("day10_input.txt", "r") as f:
    text = f.read()

# text = """
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """

matrix = []
for row in text.strip().splitlines():
    matrix.append(list(map(lambda x: int(x), row)))

rows = len(matrix)
cols = len(matrix[0])

# count = 0
# for row_index, row in enumerate(matrix):
#     for col_index, number in enumerate(row):
#         if number == 0:
#             stack = [(row_index, col_index)]
#             explored_set = set()

#             while stack:
#                 actual_node = stack.pop()
#                 explored_set.add(actual_node)

#                 if matrix[actual_node[0]][actual_node[1]] == 9:
#                     count += 1

#                 for y_movement, x_movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):

#                     new_row = actual_node[0] + y_movement
#                     new_col = actual_node[1] + x_movement

#                     if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
#                         continue

#                     coord = (new_row, new_col)
#                     if coord in explored_set:
#                         continue

#                     if (matrix[new_row][new_col] - matrix[actual_node[0]][actual_node[1]]) == 1:
#                         stack.append(coord)


count = 0
for row_index, row in enumerate(matrix):
    for col_index, number in enumerate(row):
        
        if number == 0:            
            path_id = 0
            stack = [(row_index, col_index, path_id)]
            explored_set = set()

            # Create a new graph
            while stack:
                actual_node = stack.pop()
                
                explored_set.add(actual_node)

                if matrix[actual_node[0]][actual_node[1]] == 9:
                    count += 1

                actual_path_id = actual_node[2]
                for y_movement, x_movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):

                    new_row = actual_node[0] + y_movement
                    new_col = actual_node[1] + x_movement

                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                        continue

                    coord = (new_row, new_col, actual_path_id)
                    if coord in explored_set:
                        continue

                    if (matrix[new_row][new_col] - matrix[actual_node[0]][actual_node[1]]) == 1:
                        stack.append(coord)
                        
                        path_id += 1
                        actual_path_id = path_id


print(count)
