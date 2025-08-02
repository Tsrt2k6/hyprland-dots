from random import randint
import time

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

start = time.time()

store = []
for num in range(10 ** 7):
    store.append(randint(0, 9))

end = time.time()

print(end - start)

start_time = time.time()

count = count_even(store)

end_time = time.time()

print(end_time - start_time)