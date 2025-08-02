def remove_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    numbers.remove(smallest)