with open("mixmilk.in", "r") as file:
    c1, m1 = map(int, file.readline().split(" "))
    c2, m2 = map(int, file.readline().split(" "))    
    c3, m3 = map(int, file.readline().split(" "))
    
    for i in range(0, 100):
        if i % 3 == 0:
            if (c2 - m2) >= m1:
                m2 += m1
                m1 = 0
                continue
            
            m1 -= (c2 - m2)
            m2 = c2
        
        elif i % 3 == 1:
            if (c3 - m3) >= m2:
                m3 += m2
                m2 = 0
                continue
            
            m2 -= (c3 - m3)
            m3 = c3
        
        elif i % 3 == 2:
            if (c1 - m1) >= m3:
                m1 += m3
                m3 = 0
                continue
            
            m3 -= (c1 - m1)
            m1 = c1

with open("mixmilk.out", "w") as file:
    file.write(str(m1) + "\n" + str(m2) + "\n" + str(m3))