def largest():
    num = 0
    with open("numbers.txt") as new:
        for line in new:
            print(line[:-1])
            num = max(num, int(line))
    return num


largest()