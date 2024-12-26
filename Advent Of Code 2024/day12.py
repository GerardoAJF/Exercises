# with open("day12_input.txt", "r") as f:
#     text = f.read()

text = """
AAAA
BBCD
BBCC
EEEC
"""

matrix = []
for row in text.strip().splitlines():
    matrix.append(list(row))

rows = len(matrix)
cols = len(matrix[0])

explored_set = set()

groups = dict()
groups_total = dict()

for row_index, row in enumerate(matrix):
    for col_index, plant in enumerate(row):

        if (row_index, col_index) in explored_set:
            continue

        if plant not in groups:
            groups[plant] = []

        stack = [(row_index, col_index)]
        explored_set.add((row_index, col_index))

        area = 1
        border = 0
        while stack:
            cell_row_index, cell_col_index = stack.pop()

            groups[plant].append((cell_row_index, cell_col_index))

            border += 4

            # Get next nodes
            for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_direction = (
                    cell_row_index + direction[0],
                    cell_col_index + direction[1],
                )

                if 0 > new_direction[0] or new_direction[0] >= rows or 0 > new_direction[1] or new_direction[1] >= cols:
                    continue

                if matrix[new_direction[0]][new_direction[1]] != plant:
                    continue

                if new_direction in groups[plant]:
                    border -= 2

                if new_direction in explored_set:
                    continue

                area += 1
                stack.append(new_direction)
                explored_set.add(new_direction)

        if plant not in groups_total:
            groups_total[plant] = 0

        groups_total[plant] += area * border

print(groups_total)
print(sum(groups_total.values()))
