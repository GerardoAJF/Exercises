import math

n = int(input())
numbers = tuple(map(int, input().split()))

prefix_list = [numbers[0]]
sufix_list = [numbers[-1]]

for i in range(1, n):
    prefix_list.append(math.gcd(prefix_list[-1], numbers[i]))
    sufix_list.append(math.gcd(sufix_list[-1], numbers[n -1 -i]))

max_possible = 0
for i in range(n):
    if i == 0:
        if sufix_list[n - 2] > max_possible:
            max_possible = sufix_list[n - 2]
        continue

    if i == n - 1:
        if prefix_list[n - 2] > max_possible:
            max_possible = prefix_list[n - 2]
        continue

    if math.gcd(prefix_list[i - 1], sufix_list[n -2 -i]) > max_possible:
        max_possible = math.gcd(prefix_list[i - 1], sufix_list[n - 2 - i])

print(max_possible)
