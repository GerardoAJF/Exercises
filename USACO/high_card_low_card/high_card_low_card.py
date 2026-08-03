with open("cardgame.in", "r") as file:
    n = int(file.readline())

    elsie_cards = [int(line.strip()) for line in file.readlines()]
    first_elsie = sorted(elsie_cards[:n // 2])
    second_elsie = sorted(elsie_cards[n // 2:], reverse=True)

    bessie_cards = sorted(set(range(1, (2*n) + 1)).difference(elsie_cards))
    first_bessie = sorted(bessie_cards[n // 2:])
    second_bessie = sorted(bessie_cards[: n // 2], reverse=True)

    points = 0

    elsie_index = 0
    bessie_index = 0
    while elsie_index < n / 2 and bessie_index < n / 2:
        if first_bessie[bessie_index] > first_elsie[elsie_index]:
            points += 1
            bessie_index += 1
            elsie_index += 1
            continue
        bessie_index += 1

    elsie_index = 0
    bessie_index = 0
    while elsie_index < n / 2 and bessie_index < n / 2:
        if second_bessie[bessie_index] < second_elsie[elsie_index]:
            points += 1
            bessie_index += 1
            elsie_index += 1
            continue
        bessie_index += 1

    with open("cardgame.out", "w") as write_file:
        write_file.write(str(points))
