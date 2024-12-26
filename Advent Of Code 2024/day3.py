import re

with open("day3_input.txt", "r") as f:
    text = f.read()


# functions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", text)

# total = 0
# for function in functions:
#     number1, number2 = re.findall("[0-9]{1,3},[0-9]{1,3}", function)[0].split(",")
#     total += int(number1) * int(number2)

# print(total)


total = 0
lock = False
while text:
    match = re.findall(r"^mul\([0-9]{1,3},[0-9]{1,3}\)", text)

    if match:
        number1, number2 = re.findall("[0-9]{1,3},[0-9]{1,3}", match[0])[0].split(",")
        if not lock:
            total += int(number1) * int(number2)

        text = text[text.find(match[0]) + len(match[0]) :]
        continue

    match = re.findall(r"^do\(\)", text)
    if match:
        lock = False
        text = text[text.find(match[0]) + len(match[0]) :]
        continue

    match = re.findall(r"^don't\(\)", text)
    if match:
        lock = True
        text = text[text.find(match[0]) + len(match[0]) :]
        continue

    text = text[1:]

print(total)
