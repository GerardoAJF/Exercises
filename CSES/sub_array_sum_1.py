import itertools
n, x = map(int, input().split())
array = map(int, input().split())

ans = 0
counter = {}
prefix_list = tuple(itertools.accumulate(array, initial=0))
for i in range(n + 1):
    if prefix_list[i] in counter:
        ans += counter[prefix_list[i]]


    counter[x + prefix_list[i]] = counter.get(x + prefix_list[i], 0) + 1

print(ans)
