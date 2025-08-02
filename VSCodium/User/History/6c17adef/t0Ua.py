def formatted(store):
    new = []
    for x in range(len(store)):
        new.append(f"{store[x]:.2f}")
    return new

