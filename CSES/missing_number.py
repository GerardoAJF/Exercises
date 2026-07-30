n = int(input())

numbers = map(int, input().split(" "))

total_n = (n * (n + 1)) // 2
print(total_n - sum(numbers))
