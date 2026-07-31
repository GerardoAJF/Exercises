with open("censor.in", "r") as file:
    s = list(file.readline().strip())
    t = list(file.readline().strip())

    stack = []
    for char in s:
        stack.append(char)

        if len(stack) <= len(t):
            continue

        if stack[-len(t):] == t:
            del stack[-len(t) :]

    with open("censor.out", "w") as write_file:
        write_file.write("".join(stack))