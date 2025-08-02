def shortest(store):
    shortest = ""
    for x in store:
        if len(x) < shortest:
            shortest = x
    return shortest