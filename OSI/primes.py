def eratosthenes_sieve(number: int) -> list[int]:
    list_range = list(range(2, number + 1))

    index = 0
    init_index = index
    number = list_range[init_index]

    while init_index < len(list_range) - 1:
        index += 1

        if index >= len(list_range):
            init_index += 1
            index = init_index
            number = list_range[init_index]
            continue

        if not list_range[index] % number:
            list_range.pop(index)
            index -= 1

    return list_range


print(eratosthenes_sieve(20))


