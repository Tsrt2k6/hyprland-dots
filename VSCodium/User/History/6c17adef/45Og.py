def formatted(store):
    for x in range(len(store)):
        store[x] = f"{store[x]:.2f}"
    return store

