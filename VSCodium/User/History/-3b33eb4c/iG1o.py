def time_ten(start, end):
    store = {}
    for index in range(start, end + 1):
        store[index] = index * 10
    return store