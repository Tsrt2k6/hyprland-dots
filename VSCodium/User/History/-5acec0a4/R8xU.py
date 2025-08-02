from random import randint
import time

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

store = []
for num in range(10 ** 7):
    store.append(randint(0, 9))

start_time = time.time()

count = count_even(store)

end_time = time.time()

print(end_time - start_time)

start_time = time.time()

count = count_even2(store)

end_time = time.time()

print(end_time - start_time)