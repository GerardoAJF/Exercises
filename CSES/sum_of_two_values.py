n, x = map(int, input().split())
array = [(i + 1, int(x)) for i, x in enumerate(input().split())]
array = sorted(array, key=lambda x: x[1])

solution = None

init_pointer = 0
end_pointer = n - 1
while init_pointer != end_pointer:
    sum_ = array[init_pointer][1] + array[end_pointer][1]
    if sum_ == x:
        solution = sorted((array[init_pointer][0], array[end_pointer][0]))
        break

    if sum_ < x:
        init_pointer += 1
        continue

    if sum_ > x:
        end_pointer -= 1

if not solution:
    print("IMPOSSIBLE")
else:
    print(solution[0], solution[1])
