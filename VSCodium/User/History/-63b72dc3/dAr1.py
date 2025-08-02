def check_number(number):
    check = number[:-1]
    multiply = '37137137'
    new = 0
    for index in range(8):
        new += int(check[index]) * int(multiply[index])
    if new % 10 == 0:
        last = 0
    else:
        last = 10 - new % 10
    return last == int(check[-1])

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False