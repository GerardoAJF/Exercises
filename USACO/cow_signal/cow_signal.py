with open("cowsignal.in", "r") as file:
    m, n, k = map(int, file.readline().split(" "))
    
    with open("cowsignal.out", "w") as write_file:
        for _ in range(m):
            new_line = ""
            for char in file.readline():
                if char in (".", "X"):
                    new_line += (char * k)
            write_file.write((new_line + "\n") * k)            
