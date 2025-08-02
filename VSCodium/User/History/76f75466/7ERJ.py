def even_numbers(store):
    new = []
    for x in store:
        if x % 2 == 0:
            new.append(x)
    return new