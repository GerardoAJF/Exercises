output = ""

test_cases = int(input())
for _ in range(test_cases):
    array_len = int(input())
    array = list(map(int, input().split(" ")))

    sticks = {}
    repeated_sticks = set()
    for stick in array:
        if stick not in sticks:
            sticks[stick] = 1
            continue

        sticks[stick] += 1
        repeated_sticks.add(stick)

    solution = False
    for repeated_stick in repeated_sticks:

        for stick in sticks.keys():

            if stick == repeated_stick:
                if sticks[stick] <= 2:
                    continue

                if sticks[stick] >= 4:
                    output += f"{repeated_stick} {repeated_stick} {repeated_stick} {repeated_stick}\n"
                    solution = True
                    break
            
            elif sticks[stick] >= 2:
                output += f"{repeated_stick} {repeated_stick} {stick} {stick}\n"
                solution = True
                break
            
            for other_stick in sticks.keys():
                if stick == other_stick:
                    continue
                
                if other_stick == repeated_stick and sticks[other_stick] <= 2:
                    continue
                
                rest = stick - other_stick
                if rest < 0:
                    rest *= -1
                    
                if repeated_stick > rest / 2:
                    output += f"{repeated_stick} {repeated_stick} {stick} {other_stick}\n"
                    solution = True
                    break           
            
            if solution:
                break
        if solution:
            break
    
    if not solution:
        output += "-1\n"

print(output.strip())
