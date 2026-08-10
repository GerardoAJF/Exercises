with open("sleepy.in", "r") as file:
    n = int(file.readline())
    array = list(map(int, file.readline().split()))

    steps = 0
    for i in range(0, n - 1):
        if array[i] > array[i + 1]:
            steps = i + 1

    with open("sleepy.out", "w") as write_file:
        write_file.write(str(steps))
