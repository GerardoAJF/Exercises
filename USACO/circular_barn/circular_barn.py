with open("cbarn.in", "r") as file:
    n = int(file.readline())

    rooms = tuple(map(int, file.readlines()))


    min_total_distance = None
    for i in range(n):
        total_distance = 0
        for steps, j in enumerate(range(i, n + i)):
            total_distance += (steps) * rooms[j % n]

        if min_total_distance is None:
            min_total_distance = total_distance
            continue
        
        if min_total_distance > total_distance:
            min_total_distance = total_distance

    with open("cbarn.out", "w") as write_file:
        write_file.write(str(min_total_distance))
