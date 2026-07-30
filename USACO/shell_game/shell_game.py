with open("shell.in", "r") as file:
    n = int(file.readline())

    swaps = []
    for _ in range(n):
        a, b, q = map(int, file.readline().split(" "))
        swaps.append((a, b, q))

max_score = 0

for i in range(1, 4):
    score = 0
    shells = {i: True}
    for a, b, q in swaps:

        a_value = shells.get(a, False)
        b_value = shells.get(b, False)

        shells[a] = b_value
        shells[b] = a_value

        if shells.get(q, False):
            score += 1

    if score >= max_score:
        max_score = score

with open("shell.out", "w") as f:
    f.write(str(max_score))
