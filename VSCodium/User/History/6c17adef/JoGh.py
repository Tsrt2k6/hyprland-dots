def formatted(store):
    for x in range(len(store)):
        store[x] = f"{store[x]:.2f}"
    return store

print(formatted([1.234, 0.3333, 0.11111, 3.446]))