import itertools

n, t = map(int, input().split())
books = tuple(map(int, input().split()))

max_books = 0

first_index = 0
second_index = 0

prefix_sum = tuple(itertools.accumulate(books, initial=0))

while first_index < n and second_index < n:
    sum_ = prefix_sum[second_index + 1] - prefix_sum[first_index]
    if sum_ <= t:
        if second_index - first_index + 1 > max_books:
            max_books = second_index - first_index + 1

    if sum_ > t or sum_ == t: 
        first_index += 1
        continue
    
    if sum_ < t:
        second_index += 1

print(max_books)