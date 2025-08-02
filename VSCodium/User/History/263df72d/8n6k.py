def shortest(store):
    shortest = store[0]
    for x in store:
        if len(x) < len(shortest):
            shortest = x
    return shortest