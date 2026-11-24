n, x = map(int, input().split())
array = [(int(x), i) for i, x in enumerate(input().split())]
array = sorted(array, key=lambda x: x[0])

solution = None

for i in range(n-1):
    if solution:
        break        
    
    first_pointer = i + 1
    second_pointer = n - 1

    while first_pointer != second_pointer:
        sum_ = array[i][0] + array[first_pointer][0] + array[second_pointer][0]
        
        if sum_ == x:
            solution = sorted((array[i][1], array[first_pointer][1], array[second_pointer][1]))
            break
        
        if sum_ < x:
            first_pointer += 1
            continue
        
        second_pointer -= 1

if not solution:
    print("IMPOSSIBLE")
else:
    print(" ".join([str(x + 1) for x in solution]))
