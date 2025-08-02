def factorial(number):
    if number == 1:
        return number
    number *= factorial(number - 1)
    return number

print(factorial(6))