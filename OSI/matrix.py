matrix = [
    ["0", "0", "1"],
    ["0", "0", "1"],
    ["1", "1", "1"]
]


def flood_fill(original, new, matrix, row, col):

    if matrix[row][col] != original:
        return

    matrix[row][col] = new

    for y, x in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_row = row + y
        new_col = col + x

        if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
            continue

        flood_fill(original, new, matrix, new_row, new_col)

flood_fill("1", "2", matrix, 0, 2)
print("\n".join([" ".join(row) for row in matrix]))


# Using a flood fill and BFS
def count_groups_bfs(n, matrix, row, col) -> int:
    count = 0

    queue = [(row, col)]
    explored_set = set()

    while queue:
        
        cell = queue.pop(0)
        
        if cell in explored_set:
            continue
        
        explored_set.add(cell)
        
        if matrix[cell[0]][cell[1]] == n:
            count += 1
            
        for y, x in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            
            new_row = cell[0] + y
            new_col = cell[1] + x
            
            if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
                continue
            
            queue.append((new_row, new_col))
            
    return count

print(count_groups_bfs("2", matrix, 0, 2))


# Using a flood fill and recursion
def count_groups_recursion(n, matrix, row, col, explored_set=None) -> int:
    if not explored_set:
        explored_set = set()

    count = 0

    if (row, col) in explored_set:
        return 0

    if matrix[row][col] != n:
        return 0

    count += 1
    explored_set.add((row, col))
    for y, x in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_row = row + y
        new_col = col + x

        if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
            continue

        count += count_groups_recursion(n, matrix, new_row, new_col, explored_set)

    return count

print(count_groups_recursion("0", matrix, 0, 0))
