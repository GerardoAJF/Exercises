def solution(sequence):
    count = 0
    previous_number = sequence[0] - 1
    for number in sequence:
        if previous_number < number:
            previous_number = number
            continue

        previous_number = number
        count += 1

    if count > 1:
        return False
    return True

solution([1, 3, 2, 1])
