"""
Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

If cat A catches the mouse first, print Cat A.
If cat B catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

EXAMPLE=============================================

x = 2
y = 5
z = 4

The cats are at positions 2 (Cat A) and 5 (Cat B), and the mouse is at position 4. Cat B, at position 5 will arrive first since it is only 1 unit away while the other is 2 units away. Return 'Cat B'.
"""

def cat_mouse(cat1: int, cat2: int, mouse: int) -> str:
    cat1_diference = abs(mouse - cat1)
    cat2_diference = abs(mouse - cat2)
    
    if cat1_diference < cat2_diference:
        return "Cat A"
    
    if cat1_diference > cat2_diference:
        return "Cat B"
    
    return "Mouse C"
    
print(cat_mouse(2, 5, 4))