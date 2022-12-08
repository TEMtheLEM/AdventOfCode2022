def Solve1():
    associations = {
        "A": { "X": 4, "Y": 8, "Z": 3 },
        "B": { "X": 1, "Y": 5, "Z": 9 },
        "C": { "X": 7, "Y": 2, "Z": 6 },
    }

    score = 0
    inp = input()

    while inp != '':
        score += associations[inp[0]][inp[2]]
        inp = input()

    print(score)


def Solve2():
    associations = {
        "A": { "X": 3, "Y": 4, "Z": 8 },
        "B": { "X": 1, "Y": 5, "Z": 9 },
        "C": { "X": 2, "Y": 6, "Z": 7 },
    }

    score = 0
    inp = input()

    while inp != '':
        score += associations[inp[0]][inp[2]]
        inp = input()

    print(score)


# Solve1()
# Solve2()
