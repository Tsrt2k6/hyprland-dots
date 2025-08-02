def distinct_numbers(store):
    new = []
    for x in store:
        if store[x] in new:
            pass
        else:
            new.append(store[x])
    return sorted(new)