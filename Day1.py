def Solve1() -> None:
    sums = []
    cur_sum = 0

    # work with user input...
    while True:
        inp = input()
        if inp == '':
            if cur_sum == 0:
                # user has not input anything before, this is the end
                break
            sums.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(inp)

    sums = sorted(sums)

    print(max(sums))


def Solve2() -> None:
    sums = []
    cur_sum = 0

    # work with user input...
    while True:
        inp = input()
        if inp == '':
            if cur_sum == 0:
                # user has not input anything before, this is the end
                break
            sums.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(inp)

    sums = sorted(sums)
    l = len(sums)

    print(sum(sums[l-3:l]))


# Solve1()
# Solve2()
