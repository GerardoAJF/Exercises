list1 = list()
list2 = list()

with open("day1_input.txt", "r") as f:
    for line in f.readlines():
        numbers = line.strip().split("   ")
        
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))


# total_distance = 0
# while list1 and list2:

#     min_number1 = min(enumerate(list1), key=lambda x: x[1])
#     min_number2 = min(enumerate(list2), key=lambda x: x[1])

#     distance = min_number1[1] - min_number2[1]
#     if distance < 0:
#         distance *= -1
    
#     total_distance += distance
    
#     list1.pop(min_number1[0])
#     list2.pop(min_number2[0])


count_numbers = dict()
for number in list2:
    if number not in count_numbers:
        count_numbers[number] = 1
        continue

    count_numbers[number] += 1

similarity_score = 0
for number in list1:
    similarity_score += number * count_numbers.setdefault(number, 0)

print(similarity_score)
