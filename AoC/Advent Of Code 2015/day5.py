with open("day5_input.txt", "r") as f:
    text = f.read()

# text = """
# ugknbfddgicrmopn
# aaa
# jchzalrnumimnmhp
# haegwjzuvuyypxyu
# dvszwmarrgswjxmb
# """

nice_strings = 0
for string in text.strip().splitlines():

    vowels = 0
    twice = False
    
    # Check if the final char is a vowel
    if string[-1] in ("a", "e", "i", "o", "u"):
        vowels += 1
    
    for char, next_char in zip(string, string[1:]):
        if char + next_char in ("ab", "cd", "pq", "xy"):
            break
        
        if char in ("a", "e", "i", "o", "u"):
            vowels += 1
            
        if char == next_char:
            twice = True
    
    else:
        if vowels >= 3 and twice:
            nice_strings += 1

print(nice_strings)

# ===========================

# text = """
# qjhvhtzxzqqjkmpb
# xxyxx
# uurcxstgmygtbstg
# ieodomkazucvgmuy
# """

nice_strings = 0
for string in text.strip().splitlines():

    double_pair = False
    for char, next_char in zip(string, string[1:]):
        pair = char + next_char
        
        pair_appear = 0
        index = 0
        for _ in range(len(string)):
            if index + 1 >= len(string):
                break
            
            
            if string[index] + string[index + 1] == pair:
                pair_appear += 1
                index += 1
                
            index += 1

        if pair_appear == 2:
            double_pair = True
            break
    
    repeat_between = False
    for char, end_char in zip(string, string[2:]):
        if char == end_char:
            repeat_between = True   
    
    if double_pair and repeat_between:
        nice_strings += 1     

print(nice_strings)