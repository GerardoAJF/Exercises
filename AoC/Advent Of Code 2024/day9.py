import copy

with open("day9_input.txt", "r") as f:
    text = f.read().strip()

# text = "2333133121414131402"

# Create a new list with the files and the empty space
new_list = []

file_id = 0 
files = True
for number in text:

    if files:
        for _ in range(int(number)):
            new_list.append(file_id)

        file_id += 1
        files = False
        continue

    for _ in range(int(number)):
        new_list.append(".")

    files = True


# # Sort the list of numbers
# for index, number in enumerate(new_list):
#     if number == ".":

#         while True:
#             last_number = new_list.pop()

#             if last_number != ".":
#                 break

#         new_list[index] = last_number


# # Calculate the total
# total = 0
# for position, file_id in enumerate(new_list):
#     total += position * file_id

# print(total)


list_size = len(new_list)

file_id = new_list[-1]
file_size = 0

file_init_index = 0
for file_index, number in enumerate(copy.deepcopy(new_list[::-1])):
    if number != "." and file_id == ".":
        file_size = 1
        file_init_index = file_index
        file_id = number
        continue

    if number == file_id:
        file_size += 1
        continue

    # Search a empty space that can contain the file
    empty_size = 0

    empty_init_index = 0
    for empty_index, char in enumerate(new_list[: list_size - file_index]):
        if char == ".":
            empty_size += 1

            if not empty_init_index:
                empty_init_index = empty_index

            continue

        if empty_init_index:
            # Swap the empty space with the file space

            if empty_size >= file_size:
                file = new_list[::-1][file_init_index: file_index]

                new_list[empty_init_index : empty_index - (empty_size - file_size)] = file
                new_list[list_size - file_index : list_size - file_init_index] = ["."] * file_size
                break

            empty_init_index = 0
            empty_size = 0

    # Start counting the next group
    file_size = 1
    file_init_index = file_index
    file_id = number


# Calculate the total
total = 0
for position, file_id in enumerate(new_list):
    if file_id == ".":
        continue
    
    total += position * file_id

print(total)
