with open("promote.in", "r") as file:
    _, _ = map(int, file.readline().split())
    a_silver, b_silver = map(int, file.readline().split())
    a_gold, b_gold = map(int, file.readline().split())
    a_platinum, b_platinum = map(int, file.readline().split())

    platinum_proms = b_platinum - a_platinum
    gold_proms = platinum_proms + (b_gold - a_gold)
    silver_proms = gold_proms + (b_silver - a_silver)

    with open("promote.out", "w") as write_file:
        write_file.write(str(silver_proms) + "\n")
        write_file.write(str(gold_proms) + "\n")       
        write_file.write(str(platinum_proms) + "\n")
