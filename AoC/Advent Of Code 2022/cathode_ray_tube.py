with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/no_a_las_lineas_largas_pls_hijueputa.txt", "r+") as f:

    cycle = 1

    new_values = []
    value = 1
    
    results = []
    
    file = f.readlines()
    
    def every_cycle():
        if cycle in [20, 60, 100, 140, 180, 220]:
            print("@@@@@@@@@@@", cycle, value)
            results.append(value * cycle)
            
    
    for index, line in enumerate(file):
        line = line.strip().split(" ")

        if line[0] == "noop":
            cycle += 1
            every_cycle()
            
        
        elif line[0] == "addx":
            print("line",int(line[1]))
            new_values.append(int(line[1]))
            
            if file[index + 1].strip().split()[0] == "noop":
                print(file[index + 1].strip().split()[0])
                value += sum(new_values)
                new_values = []
            
            cycle +=  1
            every_cycle()
            
            cycle += 1
            every_cycle()
            
        print("v: ", value)
        print("c:",cycle)
                    
    print(results)
    
# [420 XD, 1140 XD, 1800 XD, 1820, 2880 XD, 4180]
