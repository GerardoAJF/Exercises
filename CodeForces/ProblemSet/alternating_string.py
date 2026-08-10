import copy
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(input())

    if n % 2 == 1:
        if n == 1:
            print(1)
            continue

        prefix_even_list = [{}]
        prefix_odd_list = [{}]
        sufix_even_list = [{}]
        sufix_odd_list = [{}]

        f_counter_even = {}
        f_counter_odd = {}

        b_counter_even = {}
        b_counter_odd = {}
        for i in range(n):
            char = array[i]
            if i % 2 == 0:
                f_counter_even[char] = f_counter_even.get(char, 0) + 1
                prefix_even_list.append(copy.deepcopy(f_counter_even))
            else:
                f_counter_odd[char] = f_counter_odd.get(char, 0) + 1
                prefix_odd_list.append(copy.deepcopy(f_counter_odd))

            char = array[n-1 -i]
            if i % 2 == 0:
                b_counter_even[char] = b_counter_even.get(char, 0) + 1
                sufix_even_list.append(copy.deepcopy(b_counter_even))
            else:
                b_counter_odd[char] = b_counter_odd.get(char, 0) + 1
                sufix_odd_list.append(copy.deepcopy(b_counter_odd))

        min_change = None
        for i in range(n):

            pre_index = (i // 2) + 1
            suf_index = ((n - 1 - i) // 2) + 1
            if i == 0 or i == n-1:
                pre_index -= 1
                suf_index -= 1

            counter_even = Counter(prefix_even_list[pre_index]) + Counter(
                sufix_odd_list[(n - 1 - i) // 2]
            )
            counter_odd = Counter(prefix_odd_list[i//2]) + Counter(
                sufix_even_list[suf_index]
            )

            counter_even.pop(max(counter_even, key=lambda x, y=counter_even: y[x]))
            counter_odd.pop(max(counter_odd, key=lambda x, y=counter_odd: y[x]))

            changes = 1
            changes += sum(counter_even.values())
            changes += sum(counter_odd.values())

            if not min_change:
                min_change = changes

            if changes < min_change:
                min_change = changes

        print(min_change)
    else:
        counter_even = {}
        counter_odd = {}
        for i, char in enumerate(array):
            if i % 2 == 0:
                counter_even[char] = counter_even.get(char, 0) + 1
            else:
                counter_odd[char] = counter_odd.get(char, 0) + 1

        counter_even.pop(max(counter_even, key=lambda x, y=counter_even: y[x]))
        counter_odd.pop(max(counter_odd, key=lambda x, y=counter_odd: y[x]))

        changes = 0
        changes += sum(counter_even.values())
        changes += sum(counter_odd.values())

        print(changes)
