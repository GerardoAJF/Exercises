import itertools
n = int(input())

for _ in range(n):
    t = int(input())
    array = map(int, input())

    prefix_sum = tuple(itertools.accumulate(array, initial=0))

    good_subarrays = 0
    counter = {}
    for i in range(0, t + 1):
        x = prefix_sum[i] - i
        
        if x not in counter:
            counter[x] = 1
        else:
            good_subarrays += counter[x]
            counter[x] += 1

    print(good_subarrays)
