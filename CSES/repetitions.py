sequence = input()

max_sequence = 1
curr_sequence = 1
actual_char = sequence[0]

for char in sequence[1:]:

    if char != actual_char:
        actual_char = char
        curr_sequence = 1
        continue
    
    curr_sequence += 1    
    
    if curr_sequence > max_sequence:
        max_sequence = curr_sequence

print(max_sequence)