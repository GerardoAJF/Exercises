with open("traffic.in", "r") as file:

    n = int(file.readline())

    lines = file.readlines()

    f_init = False
    final_min_global_v = 0
    final_max_global_v = 0

    for i in range(n):
        word, min_v, max_v = lines[i].strip().split(" ")
        min_v, max_v = int(min_v), int(max_v)

        if word == "none":
            if not f_init:
                final_min_global_v = min_v
                final_max_global_v = max_v
                f_init = True
                continue

            if min_v > final_min_global_v:
                final_min_global_v = min_v
            if max_v < final_max_global_v:
                final_max_global_v = max_v

        elif f_init:
            if word == "on":
                final_min_global_v += min_v
                final_max_global_v += max_v

            elif word == "off":
                final_min_global_v -= max_v
                final_max_global_v -= min_v

    b_init = False

    init_min_global_v = 0
    init_max_global_v = 0

    for i in range(n):
        word, min_v, max_v = lines[n - 1 - i].strip().split(" ")
        min_v, max_v = int(min_v), int(max_v)

        if word == "none":
            if not b_init:
                init_min_global_v = min_v
                init_max_global_v = max_v
                b_init = True
                continue

            if min_v > init_min_global_v:
                init_min_global_v = min_v
            if max_v < init_max_global_v:
                init_max_global_v = max_v

        elif b_init:
            if word == "on":
                init_min_global_v -= max_v
                init_max_global_v -= min_v

            elif word == "off":
                init_min_global_v += min_v
                init_max_global_v += max_v

    init_min_global_v = max(0, init_min_global_v)
    final_min_global_v = max(0, final_min_global_v)

    with open("traffic.out", "w") as write_file:
        print(init_min_global_v, init_max_global_v, file=write_file)
        print(final_min_global_v, final_max_global_v, file=write_file)
