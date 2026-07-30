with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/camp_cleanup_input.txt", "r+") as f:
    
    count = 0
    
    for line in f:
        line = line.strip()
        
        ranges = line.split(",")
        
        first_range = ranges[0]
        second_range = ranges[1]
        
        first_range_parts = first_range.split("-")
        first_range_init = int(first_range_parts[0])
        first_range_end = int(first_range_parts[1])
        
        second_range_parts = second_range.split("-")
        second_range_init = int(second_range_parts[0])
        second_range_end = int(second_range_parts[1])
        
        if (first_range_init <= second_range_init) and (first_range_end >= second_range_end): # 2-8 | 3-7
            count += 1
            continue
        
        if (first_range_init >= second_range_init) and (first_range_end <= second_range_end): # 6-6 | 4-6
            count += 1
            continue
        
    print(count)

# ==========SECOND PART============

with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/camp_cleanup_input.txt", "r+") as f:

    count = 0

    for line in f:
        line = line.strip()

        ranges = line.split(",")

        first_range = ranges[0]
        second_range = ranges[1]

        first_range_parts = first_range.split("-")
        first_range_init = int(first_range_parts[0])
        first_range_end = int(first_range_parts[1])

        second_range_parts = second_range.split("-")
        second_range_init = int(second_range_parts[0])
        second_range_end = int(second_range_parts[1])

        if (first_range_init <= second_range_init) and (first_range_end >= second_range_init):  # 5-7 | 7-9
            count += 1
            continue

        if (first_range_end >= second_range_end) and (first_range_init <= second_range_end):  # 6-6 | 4-6
            count += 1
            continue
        
        if (second_range_init <= first_range_init) and (second_range_end >= first_range_init):  # 3-8 | 2-97
            count += 1
            continue

        print(line)
    print(count)
