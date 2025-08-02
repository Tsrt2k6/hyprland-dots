def formatted(store):
    for x in range(len(store)):
        print(f"{store[x]:.2f}")
        store[x] = f"{store[x]:.2f}"
    return store
print(formatted([0.123, 1.23, 0.0234]))