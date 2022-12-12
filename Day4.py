def pairFullyOverlaps(elf1, elf2) -> bool:
    return (elf1["min"] <= elf2["min"] and
            elf1["max"] >= elf2["max"])


def pairOverlaps(elf1, elf2) -> bool:
    return not (elf1["min"] > elf2["max"] or
                elf1["max"] < elf2["min"])


def Solve1():
    inp = input()
    overlaps = 0

    while inp != "":
        ranges = inp.split(",")
        pair = []

        for i in range(2):
            r = ranges[i].split("-")
            pair.append({"min": int(r[0]), "max": int(r[1])})

        if pairFullyOverlaps(pair[0], pair[1]) or pairFullyOverlaps(pair[1], pair[0]):
            overlaps += 1

        inp = input()

    print(overlaps)


def Solve2():
    inp = input()
    overlaps = 0

    while inp != "":
        ranges = inp.split(",")
        pair = []

        for i in range(2):
            r = ranges[i].split("-")
            pair.append({"min": int(r[0]), "max": int(r[1])})

        if pairOverlaps(pair[0], pair[1]) or pairOverlaps(pair[1], pair[0]):
            overlaps += 1

        inp = input()

    print(overlaps)


# Solve1()
# Solve2()
