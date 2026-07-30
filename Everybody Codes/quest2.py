with open("quest2.txt", "r") as f:    
    lines = f.readlines()

words, _, helmet = lines
words = words.strip().split(":")[1].split(",")


runic_words = 0
for word in words:
    for i in range(0, len(helmet) - len(word)):
        
        equal = True
        for j in range(0, len(word)):
            
            if word[j] !=  helmet[i + j]:
                equal = False
                break
            
        if equal:
            runic_words += 1

print(runic_words)

# ====================================================

# text = """WORDS:THE,OWE,MES,ROD,HER,QAQ

# AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
# THE FLAME SHIELDED THE HEART OF THE KINGS
# POWE PO WER P OWE R
# THERE IS THE END
# QAQAQ
# """
# lines = text.splitlines()

with open("quest2_p2.txt", "r") as f:
    lines = f.readlines()

words, _, *equipments = lines
words = words.strip().split(":")[1].split(",")

runic_words_index = set()
for word in words:

    for row, equipment in enumerate(equipments):
        for col in range(0, len(equipment) - len(word) + 1):

            if equipment[col: col + len(word)] in (word, word[::-1]) :
                for i in range(len(word)):
                    runic_words_index.add((row, col + i))

print(len(runic_words_index))

# ====================================================

# text = """WORDS:THE,OWE,MES,ROD,RODEO

# HELWORLT
# ENIGWDXL
# TRODEOAL
# """
# lines = text.splitlines()

with open("quest2_p3.txt", "r") as f:
    lines = f.readlines()

words, _, *rows = lines
words = words.strip().split(":")[1].split(",")
matrix = [list(row.strip())  for row in rows]

runic_words_index = set()
for word in words:

    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):

            if letter == word[0]:
                for y_mov, x_mov in ((1, 0), (-1, 0), (0, 1), (0, -1)):

                    correct = True
                    
                    new_row = i
                    new_col = j
                    for pos in range(len(word)):

                        if new_row >= len(matrix) or new_row < 0:
                            correct = False
                            break

                        if new_col >= len(matrix[0]):
                            new_col = 0
                        elif new_col <= -1:
                            new_col = len(matrix[0]) - 1

                        if matrix[new_row][new_col] != word[pos]:
                            correct = False
                            break
                        
                        new_row += y_mov
                        new_col += x_mov

                    if correct:
                        new_row = i
                        new_col = j
                        
                        for pos in range(len(word)):
                            if new_col == len(matrix[0]):
                                new_col = 0
                            elif new_col == -1:
                                new_col = len(matrix[0]) - 1

                            runic_words_index.add((new_row, new_col))
                            
                            new_row += y_mov
                            new_col += x_mov


print(len(runic_words_index))
