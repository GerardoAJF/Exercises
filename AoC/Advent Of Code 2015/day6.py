from pprint import pprint

with open("day6_input.txt", "r") as f:
    commands = f.read()

# commands = """
# turn on 0,0 through 0,0
# toggle 0,0 through 999,999
# """

# Create the grid
grid = []
for row in range(1000):
    new_row = []
    for col in range(1000):
        new_row.append(0)
    grid.append(new_row)

# Modify the grid
for command in commands.strip().splitlines():
    *keyword, init_coord, _, end_coord = command.split(" ")
    keyword = " ".join(keyword)

    init_col, init_row = init_coord.split(",")
    end_col, end_row = end_coord.split(",")

    for row in range(int(init_row), int(end_row) + 1):
        for col in range(int(init_col), int(end_col) + 1):

            if keyword == "turn on":
                grid[row][col] = 1
                continue

            if keyword == "turn off":
                grid[row][col] = 0
                continue
               
            grid[row][col] = 0 if grid[row][col] else 1


# Count the lights
count = 0
for row in grid:
    for light in row:
        if light:
            count += 1

print(count)

# ===========================

# Clear the grid
grid = []
for row in range(1000):
    new_row = []
    for col in range(1000):
        new_row.append(0)
    grid.append(new_row)

# Modify the grid
for command in commands.strip().splitlines():
    *keyword, init_coord, _, end_coord = command.split(" ")
    keyword = " ".join(keyword)

    init_col, init_row = init_coord.split(",")
    end_col, end_row = end_coord.split(",")

    for row in range(int(init_row), int(end_row) + 1):
        for col in range(int(init_col), int(end_col) + 1):

            if keyword == "turn on":
                grid[row][col] += 1
                continue

            if keyword == "turn off":
                if grid[row][col]:
                    grid[row][col] -= 1
                continue

            grid[row][col] += 2

# Count the brightness
count = 0
for row in grid:
    for light in row:
        count += light

print(count)
