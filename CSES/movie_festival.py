n = int(input())

movies = []
for _ in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))

movies = sorted(movies, key=lambda x: x[1])

count = 1
prev_end = movies[0][1]

for movie in movies[1:]:

    if movie[0] < prev_end:
        continue
    
    prev_end = movie[1]
    count += 1

print(count)    
