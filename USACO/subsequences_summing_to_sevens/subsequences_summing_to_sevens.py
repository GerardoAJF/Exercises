with open("div7.in", "r") as file:
    n = int(file.readline())

    prefix_list = [0]
    for _ in range(n):
        prefix_list.append(int(file.readline()) + prefix_list[-1])

    groups = [[] for _ in range(n)]
    for i in range(n):
        groups[prefix_list[i] % 7].append(i)

    max_group = 0
    for group in groups:
        if not group:
            continue
        
        if max(group) - min(group) > max_group:
            max_group = max(group) - min(group)

    with open("div7.out", "w") as write_file:
        print(max_group, file=write_file)
