with open("day1_input.txt") as f:
    text = f.read()

# text = "()())"

floor = 0
for char in text:
    if char == "(":
        floor += 1
        continue
    floor -= 1

print(floor)

# ======================
floor = 0
position = 0
for char in text:
    position += 1
    
    if char == "(":
        floor += 1
    else:
        floor -= 1
        
    if floor == -1:
        break

print(position)
