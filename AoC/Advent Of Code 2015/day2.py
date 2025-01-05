with open("day2_input.txt", "r") as f:
    text = f.read()

# text = """
# 2x3x4
# 1x1x10
# """

wrapping_paper = 0
for present in text.strip().splitlines():
    l, w, h = present.split("x")
    l, w, h = int(l), int(w), int(h)
    
    side1, side2, side3 = l * w, l * h, h * w
    
    wrapping_paper += 2 * side1
    wrapping_paper += 2 * side2
    wrapping_paper += 2 * side3
    
    wrapping_paper += min(side1, side2, side3)

print(wrapping_paper)

# ===================================
ribbon = 0
for present in text.strip().splitlines():
    l, w, h = present.split("x")
    l, w, h = int(l), int(w), int(h)

    sort_dimensions = sorted((l, w, h))
    
    ribbon += sort_dimensions[0] * 2 + sort_dimensions[1] * 2
    ribbon += l * w * h

print(ribbon)
