def Solve1():
    sacks = []
    inp = input()

    while inp != "":
        mid = int(len(inp) / 2)
        sacks.append([inp[:mid], inp[mid:]])
        inp = input()

    sum = 0
    for sack in sacks:
        for item in sack[0]:
            if item in sack[1]:
                # item is in both sacks
                sum += ord(item.lower()) - ord("a") + 1
                if item.upper() == item:
                    sum += 26
                break

    print(sum)


def Solve2():
    inp = input()
    groups = []

    while inp != "":
        group = []
        for i in range(3):
            group.append(inp)
            inp = input()
        groups.append(group)

    sum = 0
    for group in groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                # common item found!
                sum += ord(item.lower()) - ord("a") + 1
                if item.upper() == item:
                    sum += 26
                break

    print(sum)


# Solve1()
# Solve2()
