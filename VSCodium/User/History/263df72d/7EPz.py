def shortest(store):
    shortest = len(store[0])
    for x in store:
        if len(x) < shortest:
            shortest = len(x)
    return shortest