cases = int(input())

for _ in range(cases):
    cards = tuple(map(int, input().split(" ")))
    
    cards_sum = sum(cards)
    equal = cards_sum // 3
    
    if cards_sum % 3 != 0:
        print("No")
        continue
    
    if (equal < cards[0] or
        equal < cards[1]):
        print("No")
        continue

    print("Yes")
    
    
   
    
    
    