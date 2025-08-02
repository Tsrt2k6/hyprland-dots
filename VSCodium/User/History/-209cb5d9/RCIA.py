def sum_of_positives(store):
    sum = 0
    for x in store:
        if x > 0:
            sum += x
    return sum
    