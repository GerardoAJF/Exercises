with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/rucksack_reorganization_input.txt", "r+") as f:

    coincidencies = []

    for line in f:
        line = line.strip()

        first_cluster = line[:len(line)//2]
        second_cluster = line[len(line)//2:]

        letters_of_first_cluster = []
        letters_of_second_cluster = []

        for letter_1 in first_cluster:
            if letter_1 not in letters_of_first_cluster:
                letters_of_first_cluster.append(letter_1)  # Te re daria 7w7
            
        added = []
        for letter_2 in second_cluster:
            if letter_2 not in letters_of_second_cluster:
                letters_of_second_cluster.append(letter_2)

            if (letter_2 in letters_of_first_cluster) and (letter_2 not in added):
                coincidencies.append(letter_2)
                added.append(letter_2)
                print(letter_2)

    result = 0
    for letter in coincidencies:
        if ord(letter) >= 97:  # Minúscula
            result += ord(letter) - 96

        elif ord(letter) >= 65:  # Mayúscula
            result += ord(letter) - 38

    print(result)
    
    # 1 - 26 | 97
    # 27 - 52 | 38

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/rucksack_reorganization_input.txt", "r+") as f:
    
    coincidencies = []

    actual_lines = []
    actual_lines_letters = [[], [],  []]

    for line in f:
        line = line.strip()
        
        if len(actual_lines) < 2:
            actual_lines.append(line)
            continue
            
        else:
            actual_lines.append(line)
            
        for letter_1 in actual_lines[0]:
            if letter_1 not in actual_lines_letters[0]:
                actual_lines_letters[0].append(letter_1)

        for letter_2 in actual_lines[1]:
            if letter_2 not in actual_lines_letters[1]:
                actual_lines_letters[1].append(letter_2)

        added = []
        for letter_3 in actual_lines[2]:
            if letter_3 not in actual_lines_letters[2]:
                actual_lines_letters[2].append(letter_3)

            if (letter_3 in actual_lines_letters[0]) and (letter_3 in actual_lines_letters[1]) and (letter_3 not in added):
                coincidencies.append(letter_3)
                added.append(letter_3)
                    
        actual_lines = []
        actual_lines_letters = [[], [], []]
    
        print(coincidencies)

    result = 0
    for letter in coincidencies:
        if ord(letter) >= 97:  # Minúscula
            result += ord(letter) - 96

        elif ord(letter) >= 65:  # Mayúscula
            result += ord(letter) - 38

    print(result)
