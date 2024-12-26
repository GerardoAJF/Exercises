with open("day5_input.txt", "r") as f:
    text = f.read().strip()

# text = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""


# rules, manuals = text.split("\n\n")

# unblock_dict = {}

# for rule in rules.split("\n"):
#     key, value = rule.strip().split("|")

#     if key not in unblock_dict:
#         unblock_dict[key] = set()

#     unblock_dict[key].add(value)

# total = 0
# for pages in manuals.split("\n"):
#     pages = pages.split(",")
#     explored_pages = []
#     stop = False

#     for page in pages:
#         for explored in explored_pages:
#             if explored in unblock_dict.setdefault(page, ()):
#                 stop = True

#         if stop:
#             break

#         explored_pages.append(page)

#     else:
#         total += int(pages[(len(pages) - 1) // 2])


rules, manuals = text.split("\n\n")

unblock_dict = {}

for rule in rules.split("\n"):
    unblock, blocked = rule.strip().split("|")

    if unblock not in unblock_dict:
        unblock_dict[unblock] = set()

    unblock_dict[unblock].add(blocked)

total = 0
for manual in manuals.split("\n"):
    pages = manual.split(",")

    sort = True
    prev_pages = []
    while pages != prev_pages:

        stop = False

        prev_pages = pages[:]
        explored_pages = []

        for index, page in enumerate(pages):
            for index_explored_page, explored_page in enumerate(explored_pages):

                if explored_page in unblock_dict.get(page, ()):
                    pages[index] = explored_page
                    pages[index_explored_page] = page

                    stop = True
                    break 
            if stop:
                sort = False
                break

            explored_pages.append(page)

        else:
            if not sort:
                total += int(pages[(len(pages) - 1) // 2])

print(total)