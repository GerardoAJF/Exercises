with open("diamond.in", "r") as file:
    n, k = map(int, file.readline().split())

    diamonds = []
    for _ in range(n):
        diamonds.append(int(file.readline()))
    diamonds.sort()

    can_fit = [0] * n
    j = 0
    for i in range(n):
        while j < n and diamonds[j] - diamonds[i] <= k:
            j += 1
        can_fit[i] = j - i

    max_suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        max_suffix[i] = max(can_fit[i], max_suffix[i + 1])

    first_index = 0
    second_index = 0
    total_max = 0
    while first_index < n - 1 and second_index <= n:
        if second_index < n:
            if diamonds[second_index] - diamonds[first_index] <= k:
                second_index += 1
                continue

        max_ = (second_index - first_index) + max_suffix[second_index]
        if max_ > total_max:
            total_max = max_

        first_index += 1

    with open("diamond.out", "w") as write_file:
        write_file.write(str(total_max))
