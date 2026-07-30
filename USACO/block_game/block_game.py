def get_position(char):
    return ord(char) - ord("a") 

with open("blocks.in", "r") as file:
    n = int(file.readline())

    blocks = [0] * 26
    for _ in range(n):
        word1, word2 = file.readline().strip().split()

        letters1 = [0] * 26
        for char in word1:
            letters1[get_position(char)] += 1

        letters2 = [0] * 26
        for char in word2:
            letters2[get_position(char)] += 1

        for i in range(0, 26):
            blocks[i] += max(letters1[i], letters2[i])

    with open("blocks.out", "w") as write_file:
        write_file.write("\n".join(map(str, blocks)))
