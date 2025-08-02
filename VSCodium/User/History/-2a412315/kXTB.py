def largest():
    num = 0
    with open("numbers.txt") as new:
        for line[:-2] in new:
            num = max(num, int(line))
    return num
