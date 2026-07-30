n, x = input().split(" ")
n, x = int(n), int(x)

weights = list(map(int, input().split(" ")))
weights.sort()

num_gondolas = 0

l_cursor = 0
r_cursor = n - 1

while l_cursor < r_cursor:

    if weights[l_cursor] + weights[r_cursor] <= x:
        num_gondolas += 1
        l_cursor += 1
        r_cursor -= 1

        if l_cursor == r_cursor:
            num_gondolas += 1
        continue

    elif l_cursor + 1 == r_cursor:
        num_gondolas += 1

    num_gondolas += 1
    r_cursor -= 1

print(num_gondolas)
