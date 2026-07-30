with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/treetop_tree_house_input.txt", "r+") as f:

    matrix = []

    for line in f:
        line = line.strip()
        new_line = []
        
        for element in line:
            new_line.append(element)
        
        matrix.append(new_line)

    visible_trees = []
    
    visible_trees += matrix[0][1:-1] # up margin
    visible_trees += matrix[-1][1:-1] # down margin
        
    for line in matrix:
        visible_trees += line[0] # right margin
        visible_trees += line[-1] # left margin
        
    center_trees = []
    
    for line_index, line in enumerate(matrix):
        if line_index == 0 or line_index == len(matrix) - 1:
            continue
        
        for column_index, element in enumerate(line):
            if column_index == 0 or column_index == len(line) - 1:
                continue
    
            center_trees.append(((line_index, column_index), element))
    
    for index, tree in center_trees:
        
        for up_line_index in range(index[0]):
            if int(matrix[up_line_index][index[1]]) >= int(tree): # The upper tree is bigger
                break
        
        else:
            visible_trees.append(tree)
            continue
        
        for down_line_index in range(index[0]+1,len(matrix)):
            if int(matrix[down_line_index][index[1]]) >= int(tree):
                break
            
        else:
            visible_trees.append(tree)
            continue
            
        for righ_column_index in range(index[1]):
            if int(matrix[index[0]][righ_column_index]) >= int(tree):
                break
            
        else:
            visible_trees.append(tree)
            continue
            
        for left_column_index in range(index[1]+1, len(matrix[index[0]])):
            if int(matrix[index[0]][left_column_index]) >= int(tree):
                break
            
        else:
            visible_trees.append(tree)
            continue
            
            
    print(len(visible_trees))
    
# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/treetop_tree_house_input.txt", "r+") as f:

    matrix = []

    for line in f:
        line = line.strip()
        new_line = []

        for element in line:
            new_line.append(element)

        matrix.append(new_line)

    visible_trees = []

    visible_trees += matrix[0][1:-1]  # up margin
    visible_trees += matrix[-1][1:-1]  # down margin

    for line in matrix:
        visible_trees += line[0]  # right margin
        visible_trees += line[-1]  # left margin

    center_trees = []

    for line_index, line in enumerate(matrix):
        if line_index == 0 or line_index == len(matrix) - 1:
            continue

        for column_index, element in enumerate(line):
            if column_index == 0 or column_index == len(line) - 1:
                continue

            center_trees.append(((line_index, column_index), element))

    best_scenic = 0
    for index, tree in center_trees:
        
        up_scenic = 0
        for up_line_index in reversed(range(0, index[0])):
            up_scenic += 1
            
            if int(matrix[up_line_index][index[1]]) >= int(tree):  # The upper tree is bigger
                break
        
        down_scenic = 0
        for down_line_index in range(index[0]+1, len(matrix)):
            down_scenic += 1
            
            if int(matrix[down_line_index][index[1]]) >= int(tree):
                break

        right_scenic = 0
        for righ_column_index in reversed(range(0, index[1])):
            right_scenic += 1
            
            if int(matrix[index[0]][righ_column_index]) >= int(tree):
                break

        left_scenic = 0
        for left_column_index in range(index[1]+1, len(matrix[index[0]])):
            left_scenic += 1
            
            if int(matrix[index[0]][left_column_index]) >= int(tree):
                break

        scenic = up_scenic * down_scenic * right_scenic * left_scenic

        if scenic >= best_scenic:
            best_scenic = scenic

    print(best_scenic)
