with open("bcount.in", "r") as file:
    n, q = map(int, file.readline().split())

    holsteins = [0]
    guernseys = [0]
    jerseys = [0]
    for _ in range(n):
        cow = int(file.readline())

        if cow == 1:
            holsteins.append(holsteins[-1] + 1)
            guernseys.append(guernseys[-1])
            jerseys.append(jerseys[-1])
        elif cow == 2:
            guernseys.append(guernseys[-1] + 1)
            jerseys.append(jerseys[-1])
            holsteins.append(holsteins[-1])
        else:
            jerseys.append(jerseys[-1] + 1)
            holsteins.append(holsteins[-1])
            guernseys.append(guernseys[-1])

    with open("bcount.out", "w") as write_file:
        for _ in range(q):
            a, b = map(int, file.readline().split())

            num_h = holsteins[b] - holsteins[a - 1] 
            num_g = guernseys[b] - guernseys[a - 1]
            num_j = jerseys[b] - jerseys[a - 1]
            
            print(num_h, num_g, num_j, file=write_file)