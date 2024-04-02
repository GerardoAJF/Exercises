"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

EXAMPLE=============================================

b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]

The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58.
"""

def electronics_shop(budget: int, keyboards: list, drives: list) -> int:
    max_price = -1
    
    for keyboard in keyboards:
        for drive in drives:
            new_max_price = keyboard + drive
            
            if (new_max_price <= budget) and (new_max_price > max_price):
                max_price = new_max_price
    
    return max_price

print(electronics_shop(60, [40, 50, 60], [5, 8,12]))