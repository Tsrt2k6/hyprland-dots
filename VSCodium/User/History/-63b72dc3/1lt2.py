def check_number(number):
    if len(number) != 9 or int(number[0]) != '0':
        return False
    check = number[:-1]
    multiply = '37137137'
    new = 0
    for index in range(8):
        new += int(check[index]) * int(multiply[index])
    if new % 10 == 0:
        last = 0
    else:
        last = 10 - new % 10
    return last == int(number[-1])

print(check_number('032238170'))