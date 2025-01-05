with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/tuning_trouble_input.txt", "r+") as f:

    count = {}
    stack = []

    for letter_number, letter in enumerate(f.readline()):
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

        stack.append((letter_number+1, letter))

        if len(stack) == 4:

            if len(count) != 4:  # Repeated
                ultimate = stack.pop(0)[1]

                count[ultimate] -= 1

                if count[ultimate] == 0:
                    del count[ultimate]

            else:
                print(count)
                print(stack)
                print(stack[-1][0])

                break

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/tuning_trouble_input.txt", "r+") as f:

    count = {}
    stack = []

    for letter_number, letter in enumerate(f.readline()):
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

        stack.append((letter_number+1, letter))

        if len(stack) == 14:

            if len(count) != 14:  # Repeated
                ultimate = stack.pop(0)[1]

                count[ultimate] -= 1

                if count[ultimate] == 0:
                    del count[ultimate]

            else:
                print(count)
                print(stack)
                print(stack[-1][0])

                break
