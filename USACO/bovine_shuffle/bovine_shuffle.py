with open("shuffle.in", "r") as file: 
    n = int(file.readline())

    shuffles = {value: i for i, value in enumerate(file.readline().strip().split(" "))}
    cows = file.readline().strip().split(" ")

    output = [""] * n
    for i in range(1, n + 1):
        cow_id = cows[i - 1]
        pos = i

        for _ in range(3):
            pos = shuffles[str(pos)] + 1
        output[pos - 1] = cow_id

    with open("shuffle.out", "w") as write_file:
        write_file.write("\n".join(output))
