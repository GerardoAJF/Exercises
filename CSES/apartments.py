n, m, k = input().split(" ")
n, m, k = int(n), int(m), int(k)

d_apartments = list(map(int, input().split(" ")))
r_apartments = list(map(int, input().split(" ")))

d_apartments.sort()
r_apartments.sort()

d_cursor = 0
r_cursor = 0

count = 0

while d_cursor < n and r_cursor < m:

    if r_apartments[r_cursor] - k > d_apartments[d_cursor]:
        d_cursor += 1
        continue

    if r_apartments[r_cursor] + k < d_apartments[d_cursor]:
        r_cursor += 1
        continue

    count += 1
    d_cursor += 1
    r_cursor += 1


print(count)
