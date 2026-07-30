cases = int(input())

integers = input()
integers_set = set()
integers_numbers = 0

for integer in integers.split(" "):
    if integer not in integers_set:
        integers_numbers += 1
        integers_set.add(integer)

print(integers_numbers)
