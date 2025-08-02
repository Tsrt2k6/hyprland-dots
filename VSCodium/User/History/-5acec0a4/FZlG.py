from random import randint
import time

start_time = 

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

store = []
for num in range(10 ** 7):
    store.append(randint(0, 9))

print(count_even(store))