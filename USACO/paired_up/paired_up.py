with open("pairup.in", "r") as file:
    n = int(file.readline())

    cows = []
    for _ in range(n):
        number_cows, milk = map(int, file.readline().split())
        cows.append([number_cows, milk])

    cows.sort(key=lambda x: x[1])

    init = 0
    end = len(cows) - 1
    max_ = 0
    while init <= end:
        milk1 = cows[init]
        milk2 = cows[end]

        if milk2[1] + milk1[1] > max_:
            max_ = milk2[1] + milk1[1]

        if milk2[0] > milk1[0]:
            milk2[0] -= milk1[0]
            init += 1
        elif milk2[0] < milk1[0]:
            milk1[0] -= milk2[0]
            end -= 1
        elif milk2[0] == milk1[0]:
            init += 1
            end -= 1

    with open("pairup.out", "w") as write_file:
        write_file.write(str(max_))
