def invert(store):
    copy = {}
    for key, value in store.items():
        copy[value] = key
    store.clear()
    for key, value in copy.items():
        store[key] = value
