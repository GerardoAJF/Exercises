n, m = map(int, input().split())
cities = tuple(map(int, input().split()))
towers = tuple(map(int, input().split()))

city_pointer = 0
tower_pointer = 0
min_distance = 0
while city_pointer < n:
    distance = abs(cities[city_pointer] - towers[tower_pointer])

    if tower_pointer < m - 1:
        next_distance = abs(cities[city_pointer] - towers[tower_pointer + 1])
        
        if next_distance <= distance:
            tower_pointer += 1
            continue

    if distance > min_distance:
        min_distance = distance
    
    city_pointer += 1

print(min_distance)