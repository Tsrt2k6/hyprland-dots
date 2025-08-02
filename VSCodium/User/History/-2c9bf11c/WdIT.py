def distinct_numbers(store):
    new = []
    for x in store:
        if x in new:
            pass
        else:
            new.append(x)
    return sorted(new)