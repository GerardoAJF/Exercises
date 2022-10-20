def roman_to_int(letters):
    letters = list(letters)
    values = []

    ran = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for number in letters:
        values.append(ran[number])

    # Get the negatives values
    for actual_number_index, actual_number in enumerate(values):
        if actual_number_index + 1 >= len(values):  # Final letter
            break

        next_number = values[actual_number_index + 1]

        if actual_number < next_number:
            values.pop(actual_number_index + 1)
            values.pop(actual_number_index)

            values.insert(actual_number_index, next_number - actual_number)

    return sum(values)


print(roman_to_int("VII"))
print(roman_to_int("LXXX"))
print(roman_to_int("MCCC"))
print(roman_to_int("CM"))
print(roman_to_int("IX"))
print(roman_to_int("XC"))
