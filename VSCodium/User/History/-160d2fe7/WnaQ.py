def invert(store):
    for key, value in store.items():
        store[value] = key
        store.pop(key)
    