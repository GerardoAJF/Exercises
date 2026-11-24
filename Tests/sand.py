import os
import sys
import random
import time
from utils import color_print

colors = {
    0: "#FFB3BA",  # Rosa pastel
    1: "#FFDFBA",  # Melocotón pastel
    2: "#FFFFBA",  # Amarillo pastel
    3: "#BAFFC9",  # Verde menta pastel
    4: "#BAE1FF",  # Azul cielo pastel
    5: "#D4BAFF",  # Lavanda pastel
    6: "#FFBAED",  # Rosa chicle pastel
    7: "#C9FFE5",  # Aguamarina pastel
    8: "#FFDAC1",  # Durazno pastel
    9: "#E0BBE4",  # Lila pastel
}

VOID = -1
GROUND = 10

terminal_size = os.get_terminal_size()
matrix = [[VOID for _ in range(terminal_size.columns - 1)] for _ in range(terminal_size.lines - 2)]
matrix.append([GROUND for _ in range(terminal_size.columns - 1)])

def draw(matrix) -> None:
    sys.stdout.write("\033[H")
    for line in matrix:
        for cell in line:
            if cell == VOID:
                char = " "
                sys.stdout.write(char)

            elif cell == GROUND:
                char = "X"
                sys.stdout.write(color_print("#FFFFFF", char))

            else:
                char = "#"
                sys.stdout.write(color_print(colors[cell], char))

        sys.stdout.write("\n")
    sys.stdout.flush()

def spawn_sand(matrix, color) -> None:
    index = random.randint(0, terminal_size.columns - 2)
    matrix[0][index] = color

def update(matrix) -> bool:
    for y, line in enumerate(matrix):
        for x, cell in enumerate(line):
            if cell == VOID or cell == GROUND:
                continue

            if matrix[y + 1][x] == VOID:
                matrix[y + 1][x] = cell
                matrix[y][x] = VOID
                return True

            elif matrix[y + 1][x - 1] == VOID:
                matrix[y + 1][x - 1] = cell
                matrix[y][x] = VOID
                return True

            elif matrix[y + 1][(x + 1) % (terminal_size.columns - 1)] == VOID:
                matrix[y + 1][(x + 1) % (terminal_size.columns - 1)] = cell
                matrix[y][x] = VOID
                return True

    return False

try: 
    color = random.randint(0, GROUND-1)
    spawn_sand(matrix, color)
    count = 1
    while True:
        draw(matrix)

        time.sleep(0.01)

        if not update(matrix):
            count += 1
            spawn_sand(matrix, color)

        if count % 150 == 0:
            color = random.randint(0, GROUND-1)

except KeyboardInterrupt:
    pass
finally:
    os.system("cls")
