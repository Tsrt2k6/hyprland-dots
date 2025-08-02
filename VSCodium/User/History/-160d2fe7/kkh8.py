def invert(store):
    for key in store:
        temp = store[key]
        store[key] = key
        