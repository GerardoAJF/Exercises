n = int(input())

tasks = []
for _ in range(n):
    tasks.append(tuple(map(int, input().split())))
    
tasks = sorted(tasks, key=lambda x: x[0])

award = 0
init_time = 0
for task in tasks:
    init_time += task[0]
    award += (task[1] - init_time)

print(award)
