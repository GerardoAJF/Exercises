with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/rock_paper_scissors_input.txt", "r+") as f:

    elements = {"rock": {"code": {"1": "A", "2": "X"},
                         "relation": {"killed": "paper", "killer": "scissor"},
                         "value": 1},

                "paper": {"code": {"1": "B", "2": "Y"},
                          "relation": {"killed": "scissor", "killer": "rock"},
                          "value": 2},

                "scissor": {"code": {"1": "C", "2": "Z"},
                            "relation": {"killed": "rock", "killer": "paper"},
                            "value": 3}}

    elements_code = {code: key for key, element in elements.items() for code in element["code"].values()}

    total_score = 0

    for line in f:
        line = line.strip()


        letter_1 = elements[elements_code[line[0]]]
        letter_2 = elements[elements_code[line[2]]]

        if letter_1["relation"]["killer"] == elements_code[line[2]]:
            total_score += letter_2["value"] + 0

        elif letter_1 == letter_2:
            total_score += letter_2["value"] + 3

        elif letter_1["relation"]["killed"] == elements_code[line[2]]:
            total_score += letter_2["value"] + 6

    print(total_score)

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/rock_paper_scissors_input.txt", "r+") as f:

    elements = {"rock": {"code": "A",
                         "relation": {"killed": "paper", "killer": "scissor"},
                         "value": 1},

                "paper": {"code": "B",
                          "relation": {"killed": "scissor", "killer": "rock"},
                          "value": 2},

                "scissor": {"code": "C",
                            "relation": {"killed": "rock", "killer": "paper"},
                            "value": 3}}

    elements_code = {element["code"]: key for key, element in elements.items()}

    total_score = 0

    for line in f:
            line = line.strip()

            finish = line[2]

            letter_1 = elements[elements_code[line[0]]]
            
            if finish == "X":
                letter_2 = elements[letter_1["relation"]["killer"]]
                total_score += letter_2["value"] + 0

            elif finish == "Y":
                letter_2 = letter_1
                total_score += letter_2["value"] + 3

            elif finish == "Z":
                letter_2 = elements[letter_1["relation"]["killed"]]
                total_score += letter_2["value"] + 6

    print(total_score)
