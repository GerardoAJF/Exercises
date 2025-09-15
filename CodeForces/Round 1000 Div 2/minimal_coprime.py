output = ""
test_cases = int(input())
for _ in range(test_cases):

    init, end = map(int, input().split(" "))

    if init == 1 and end == 1:
        output += "1\n"
        continue

    output += f"{end - init}\n"
print(output.strip())
