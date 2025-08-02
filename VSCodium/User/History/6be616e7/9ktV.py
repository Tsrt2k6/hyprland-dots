def factorial(number):
    if number == 1:
        return number
    number *= factorial(number - 1)
    return number

def factorials(n):
    store = []
    i = 1
    while i <= n:
        store[i] = factorial(i)
        i += 1
    return i

print(factorials(5)[3])