_, x = input().split()
algorithms = sorted(map(int, input().split()))

count = 0
cache = 0
for i in algorithms:
    if cache + int(i) > int(x):
        break
    
    cache += int(i)
    count += 1

print(count)
