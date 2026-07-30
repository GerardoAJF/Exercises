with open("blist.in", "r") as file:
    times = [0] * 1000

    n = int(file.readline())
    
    for _ in range(n):
        s, t, b = map(int, file.readline().strip().split(" "))
        
        for i in range(s - 1, t):
            times[i] += b
    
    with open("blist.out", "w") as write_file:
        write_file.write(str(max(times)))