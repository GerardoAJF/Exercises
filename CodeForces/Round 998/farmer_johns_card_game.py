test_cases = int(input())
out_put = ""

for _ in range(test_cases):
    number_cows, deck_len = input().split(" ")
    number_cows, deck_len = int(number_cows), int(deck_len)

    cows = []
    for _ in (range(number_cows)):
        cows.append(list(map(int, input().split(" "))))

    cows_index = list(range(number_cows))
    cows_order = []
    for position in range(0, number_cows):
        cows_order.append([0, 2000])

        for cow in  cows_index:
            min_card = min(cows[cow])
            if min_card < cows_order[position][1]:
                cows_order[position][0] = cow + 1
                cows_order[position][1] = min_card

        cows_index.remove(cows_order[-1][0] - 1)

    last_card = -1
    while cows[cows_order[-1][0] - 1]:

        stop = False
        for cow, _ in cows_order:
            min_card = min(cows[cow - 1])

            if min_card <= last_card:
                stop = True
                break
            
            cows[cow - 1].remove(min_card)
            last_card = min_card
        
        if stop:
            out_put += "-1\n"
            break
            
    if not stop:
        out_put += " ".join([str(i[0]) for i in cows_order]) + "\n"

print(out_put.strip())
