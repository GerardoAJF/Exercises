import os
import sys
import time
import random

ascii_dict = {
    "0": " ",
    "1": ".",
    "2": "º",
    "3": ";",
    "4": "=",
    "5": "#",
    "6": "%",
    "7": "$",
    "8": "&",
    "9": "@",
}

color_dict = {
    "0": "#000000 ",
    "1": "#A74730",
    "2": "#DB6042",
    "3": "#F87E60",
    "4": "#F7963C",
    "5": "#F8A960",
    "6": "#F7C335",
    "7": "#FFD76A",
    "8": "#FFF1A0",
    "9": "#FFFFFF",
}

terminal_size = os.get_terminal_size()

matrix = [["0" for _ in range(terminal_size.columns - 1)] for _ in range(terminal_size.lines - 2)]
matrix.append(["9" for _ in range(terminal_size.columns - 1)])

def to_hex(color: str) -> str:
    color = color.lstrip("#")
    
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    return f"\033[38;2;{r};{g};{b}m"

def draw() -> None:
    for line in matrix:
        for char in line:

            sys.stdout.write(f"{to_hex(color_dict[char])}{ascii_dict[char]}\033[0m")
        sys.stdout.write("\n")

clear = lambda: os.system("cls")
init = lambda: sys.stdout.write("\033[H")

# def update(matrix, coldness) -> None:
#     for line in range(terminal_size.lines - 4, -1, -1):
#         for col in range(0, terminal_size.columns - 1):

#             value = max(
#                 0, round(int(matrix[line + 1][col]) - random.uniform(0, coldness))
#             )
#             matrix[line][col] = str(value)


def update(matrix, coldness) -> None:
    for line in range(terminal_size.lines - 3, -1, -1):
        for col in range(0, terminal_size.columns - 1):
            
            down = int(matrix[line + 1][col]) if line < (terminal_size.lines - 1) else 0

            left = int(matrix[line][col - 1])
            right = int(matrix[line][(col + 1) % (terminal_size.columns - 1)])

            value = round(down - random.uniform(0, coldness))
            env = (left + right) // 2
            
            if env > value:
                value += int(random.uniform(0, env // 2))
            
            if value > 9: value = 9
            elif value < 0: value = 0

            matrix[line][col] = str(value)

try:
    while True:
        init()
        draw()
        sys.stdout.flush()
        update(matrix, 5)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    clear()
