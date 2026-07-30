with open("speeding.in", "r") as file:
    n, m = map(int, file.readline().split(" "))

    lengths = []
    velocities = []
    for _ in range(n):
        length, velocity = map(int, file.readline().split(" "))

        lengths.append(length)
        velocities.append(velocity)

    max_upp_velocity = 0
    for _ in range(m):
        t_length, t_velocity = map(int, file.readline().split(" "))

        while t_length:
            if t_velocity > velocities[0]:
                upp_velocity = t_velocity - velocities[0]
                
                if upp_velocity > max_upp_velocity:
                    max_upp_velocity = upp_velocity

            if lengths[0] <= t_length:
                t_length -= lengths[0]
                lengths.pop(0)
                velocities.pop(0)
            else:
                lengths[0] -= t_length
                t_length = 0

    with open("speeding.out", "w") as write_file:
        write_file.write(str(max_upp_velocity))