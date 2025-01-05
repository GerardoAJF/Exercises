import itertools

with open("day7_input.txt", "r") as f:
    text = f.read()

# text = """
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """

# answer = 0

# for equation in text.strip().splitlines():
#     result, numbers = equation.split(":")
#     numbers = numbers.strip().split(" ")

#     combinations = itertools.product(("+", "*"), repeat=(len(numbers) - 1))
#     possible_equations = zip(itertools.repeat(numbers, 2 ** (len(numbers) - 1)), combinations)

#     for numbers, operators in possible_equations:
#         total = int(numbers[0])

#         for index, next_number in enumerate(numbers[1:]):

#             if operators[index] == "+":
#                 total += int(next_number)
#             else:
#                 total *= int(next_number)

#         if total == int(result):
#             answer += total
#             break

# print(answer)

answer = 0

for equation in text.strip().splitlines():
    result, numbers = equation.split(":")
    numbers = numbers.strip().split(" ")

    combinations = itertools.product(("+", "*", "||"), repeat=(len(numbers) - 1))
    possible_equations = zip(
        itertools.repeat(numbers, 3 ** (len(numbers) - 1)), combinations
    )

    for numbers, operators in possible_equations:
        total = int(numbers[0])

        for index, next_number in enumerate(numbers[1:]):

            if operators[index] == "+":
                total += int(next_number)
            elif operators[index] == "*":
                total *= int(next_number)
            else:
                total = int(str(total) + next_number)

        if total == int(result):
            answer += total
            break

print(answer)
