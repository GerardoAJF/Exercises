# def get_permutations(list_: list, cache={}) -> list:
#     if tuple(list_) in cache:
#         return cache[tuple(list_)]

#     if len(list_) == 1:
#         cache[tuple(list_)] = [list_]
#         return [list_]

#     result = []
#     for n in list_:

#         list_copy = list_[:]
#         list_copy.remove(n)
#         for permutation in get_permutations(list_copy, cache):
#             result.append([n] + permutation)

#     cache[tuple(list_)] = result
#     return result


def get_permutation_greedy(list_: list, previous=0):
    if len(list_) == 1:
        return list_

    result = []
    for n in list_:
        if (n % 2 == 0 and not previous) or (n % 2 == 1 and previous):

            list_copy = list_[:]
            list_copy.remove(n)

            result = [n] + get_permutation_greedy(list_copy, n)
            break
    else:
        return list_

    return result


output = ""
test_cases = int(input())
for _ in range(test_cases):

    array_len = int(input())
    array = list(map(int, input().split(" ")))

    points = 0
    s = 0
    for n in get_permutation_greedy(array):
        s += n
        if s % 2 == 0:
            points += 1

        while s % 2 == 0:
            s = s / 2

    output += str(points) + "\n"
print(output.strip())
