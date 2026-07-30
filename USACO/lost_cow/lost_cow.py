import math

with open("lostcow.in", "r") as file:
    x, y = map(int, file.readline().split())
    diff = abs(y - x)

    n = math.ceil(math.log2(diff))
    excess = math.pow(2, n) - diff

    if ((y < x) and (n % 2 == 0)) or ((y > x) and (n % 2 == 1)):
        steps = (2 * (math.pow(2, n + 1) - 1)) + math.pow(2, n) - excess
    else:
        steps = (2 * (math.pow(2, n) - 1)) + math.pow(2, n) - excess

    with open("lostcow.out", "w") as w_file:
        w_file.write(str(int(steps)))
