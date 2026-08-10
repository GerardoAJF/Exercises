n, x = map(int, input().split())
count = 0
sums_ = {0: 1}
sum_ = 0
for num in map(int, input().split()):
    sum_ += num
    a = sum_ - x

    if a in sums_:
        count += sums_[a]
        
    b = sum_ 
    sums_[b] = sums_.get(sum_, 0) + 1

print(count)
