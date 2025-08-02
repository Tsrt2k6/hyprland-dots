def count(s):
    count0 = 0
    count1 = 0
    for digit in s:
        if int(digit):
            count1 += 1
        else:
            count0 += 1
    return min(count0, count1)