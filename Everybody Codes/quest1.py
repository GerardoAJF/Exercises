with open("quest1.txt", "r") as f:
    text = f.read().strip()

# text = "ABBAC"

potions = 0
for letter in text:
    
    if letter == "A":
        continue
    
    if letter == "B":
        potions += 1
        continue
    
    potions += 3

print(potions)

# =====================================

with open("quest1_p2.txt", "r") as f:
    text = f.read().strip()

# text = "AxBCDDCAxD"

potions = 0
for index in range(0, len(text), 2):
    first_letter = text[index]
    second_letter = text[index + 1]

    if first_letter != "x" and second_letter != "x":
       potions += 2
              
    for letter in (first_letter, second_letter):
        
        if letter in ("A", "x"):
            continue
            
        if letter == "B":
            potions += 1
            continue
        
        if letter == "C":
            potions += 3
            continue
        
        potions += 5

print(potions)

# =====================================

with open("quest1_p3.txt", "r") as f:
    text = f.read().strip()

# text = "xBxAAABCDxCC"

potions = 0
for index in range(0, len(text), 3):
    first_letter = text[index]
    second_letter = text[index + 1]
    third_letter = text[index + 2]

    creatures = 0
    for letter in (first_letter, second_letter, third_letter):
        if letter != "x":
            creatures += 1

        if letter in "A":
            continue

        if letter == "B":
            potions += 1
            continue

        if letter == "C":
            potions += 3
            continue

        if letter == "D":
            potions += 5

    if creatures == 2:
        potions += 2
    elif creatures == 3:
        potions += 6
    
print(potions)
