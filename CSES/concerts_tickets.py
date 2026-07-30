n, m = input().split(" ")
n, m = int(n), int(m)

tickets = list(map(int, input().split(" ")))
tickets.sort()

clients = list(map(int, input().split(" ")))

t_l_cursor = 0
t_r_cursor = n - 1
c_cursor = 0

while c_cursor < m:
    if t_l_cursor >= n:
        print(-1)
        c_cursor += 1
        continue

    if t_r_cursor >= 0:
        if clients[c_cursor] > tickets[t_r_cursor]:
            print(tickets[t_r_cursor])
            tickets.pop(t_r_cursor)
            n -= 1
            t_r_cursor -= 1
            c_cursor += 1
            continue

    if clients[c_cursor] > tickets[t_l_cursor]:
        if t_l_cursor < n:
            if clients[c_cursor] >= tickets[t_l_cursor + 1]:
                t_l_cursor += 1
                continue

    print(tickets[t_l_cursor])
    tickets.pop(t_l_cursor)
    n -= 1

    t_l_cursor = 0
    t_r_cursor -= 1

    c_cursor += 1

