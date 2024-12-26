
with open("day2_input.txt", "r") as f:
    text = f.read().strip()

# safe_reports = 0

# for line in text.strip().split("\n"):
#     numbers = line.split(" ")

#     decreasing = int(numbers[0]) > int(numbers[1])

#     for number, next_number in zip(numbers, numbers[1:]):
#         if (int(number) > int(next_number)) != decreasing:
#             break

#         distance = int(number) - int(next_number)
#         if distance < 0:
#             distance *= -1

#         if distance == 0 or distance > 3:
#             break

#     else:
#         safe_reports += 1

# print(safe_reports)


safe_reports = 0

for line in text.strip().split("\n"):
    is_safe = False
    real_numbers = line.split(" ")

    for count in range(len(real_numbers)):

        temp_numbers = real_numbers[:count] + real_numbers[count + 1 :]
        decreasing = int(temp_numbers[0]) > int(temp_numbers[1])

        for number, next_number in zip(temp_numbers, temp_numbers[1:]):
            if (int(number) > int(next_number)) != decreasing:
                break

            if not (1 <= abs(int(number) - int(next_number)) <= 3):
                break

        else:
            is_safe = True
            break

    if is_safe:
        safe_reports += 1

print(safe_reports)
