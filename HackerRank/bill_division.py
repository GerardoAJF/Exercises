"""
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

The program should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna. 

    - bill: list of numbers, that represents its price ([1, 2, 3, 4]) 
    - k: the index of the item that Ana doesn't eat 
    - b: the amount of money that Anna contributed to the bill

========SAMPLE========

Input:
bill = [3, 10, 2, 9]
k = 1
b = 12

Output:
5

EXPLANATION:

Anna didn't eat the item bill[1] = 10, but she shared the rest of the items with Brian, so what you have to pay is: 
(3 + 2 + 9) / 2 = 7

Anna pay 12, then Brian owes 12 - 7 = 5 to Anna
"""

def fairly_bill_split(bill, k, b):
    bill.pop(k)
    real_price = sum(bill) // 2

    if b == real_price:
        print("Bon Appetit")
    else:
        print(b - real_price)
        