def everything_reversed(store):
    new = []
    for i in range(len(store), -1):
        new.append(store[i])
    return new