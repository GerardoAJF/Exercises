with open("day11_input.txt", "r") as f:
    text = f.read().strip()

# text = "125"

numbers = text.split(" ")

for _ in range(25):

    index = 0
    for number in numbers[:]:

        if number == "0":
            numbers[index] = "1"

        elif len(number) % 2 == 0:
            numbers[index] = number[:len(number) // 2]
            numbers.insert(index + 1, str(int(number[len(number) // 2:])))
            index += 1

        else:
            numbers[index] = str(int(number) * 2024)

        index += 1

print(len(numbers))


# def conditions(number) -> tuple:
#     if number == "0":
#         return ("1", )
        
#     if len(number) % 2 == 0:
#         return (number[:len(number) // 2], str(int(number[len(number) // 2:])))

#     return (str(int(number) * 2024), )


# cache = {}
# def count_rocks(number, blink):
    
#     if (number, blink) in cache:
#         return cache[(number, blink)]

#     if blink == 1:
#         result = conditions(number)
#         cache[(number, blink)] = result
#         return result

#     previous_rocks = count_rocks(number, blink - 1)
#     result = tuple(number for tuple_ in map(conditions, previous_rocks) for number in tuple_)
#     cache[(number, blink)] = result

#     return result


# print(len(count_rocks("125", 75)))
