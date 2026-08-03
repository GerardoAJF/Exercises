with open("stuck.in") as file:
    n = int(file.readline())

    movements = [line.strip().split() for line in file.readlines()]

    e_moves = []
    n_moves = []
    for move in movements:
        if move[0] == "E":
            e_moves.append(move)
        else:
            n_moves.append(move)

    e_list = sorted(e_moves, key=lambda x: int(x[1]))
    n_list = sorted(n_moves, key=lambda x: int(x[1]))

    print(e_list)
    print(n_list)