with open("hps.in") as file:
    n = int(file.readline())

    hoofs = [0]
    papers = [0]
    scissors = [0]

    index = 0
    for _ in range(n):
        gest = file.readline().strip()

        if gest == "H":
            hoofs.append(hoofs[-1])
            scissors.append(scissors[-1])

            papers.append(papers[-1] + 1)
        elif gest == "P":
            hoofs.append(hoofs[-1])
            papers.append(papers[-1])

            scissors.append(scissors[-1] + 1)
        else:
            papers.append(papers[-1])
            scissors.append(scissors[-1])

            hoofs.append(hoofs[-1] + 1)

    max_wins = 0
    for i in range(n + 1):
        first = max(papers[i], hoofs[i], scissors[i])
        second = max(
            papers[-1] - papers[i], hoofs[-1] - hoofs[i], scissors[-1] - scissors[i]
        )

        if first + second > max_wins:
            max_wins = first + second

    with open("hps.out", "w") as write_file:
        write_file.write(str(max_wins))
