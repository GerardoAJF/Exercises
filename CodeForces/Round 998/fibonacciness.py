test_cases = int(input())

output = ""
for _ in range(test_cases):

    array = list(map(int, input().split(" ")))
    array.insert(2, 0)

    maximun_fibonacciness = 0
    for i in range(-100, 101):
        array[2] = i

        fibonacciness = 0
        for number1, number2, total in zip(array, array[1:], array[2:]):

            if number1 + number2 == total:
                fibonacciness += 1

        if fibonacciness > maximun_fibonacciness:
            maximun_fibonacciness = fibonacciness

    output += f"{maximun_fibonacciness}\n"

print(output.strip())
