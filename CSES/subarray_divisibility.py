import itertools

n = int(input())
array = map(int, input().split())

prefix_list = tuple(itertools.accumulate(array, initial=0))

count = 0
counter = [0] * n
for i in range(0, n + 1):
    x = (prefix_list[i]) % n

    count += counter[x]
    counter[x] += 1

print(count)