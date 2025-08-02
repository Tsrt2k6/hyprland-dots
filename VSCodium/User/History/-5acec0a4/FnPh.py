from random import randint

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

for num in range(10 ** 7):
    store.append(randint)