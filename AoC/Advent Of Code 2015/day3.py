with open("day3_input.txt", "r") as f:
    text = f.read()

# text = "^v^v^v^v^v"

visited_houses = {(0, 0)}
actual_house = (0, 0)

movements = {
    "^": (1, 0),
    ">": (0, 1),
    "v": (-1, 0),
    "<": (0, -1)
}

for movement in text:

    actual_house = (
        actual_house[0] + movements[movement][0],
        actual_house[1] + movements[movement][1],
    )
    
    visited_houses.add(actual_house)

print(len(visited_houses))

# ======================================

visited_houses = {(0, 0)}

santa_actual_house = (0, 0)
robot_santa_actual_house = (0, 0)

movements = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}

for movement_number in range(0, len(text), 2):
    santa_movement = text[movement_number]
    robot_santa_movement = text[movement_number + 1]

    santa_actual_house = (
        santa_actual_house[0] + movements[santa_movement][0],
        santa_actual_house[1] + movements[santa_movement][1],
    )

    robot_santa_actual_house = (
        robot_santa_actual_house[0] + movements[robot_santa_movement][0],
        robot_santa_actual_house[1] + movements[robot_santa_movement][1],
    )

    visited_houses.add(santa_actual_house)
    visited_houses.add(robot_santa_actual_house)
    
print(len(visited_houses))
