def formatteds(store):
    new = store
    for x in range(len(new)):
        new[x] = f"{new[x]:.2f}"
    return new

def formatted(store):
    new = []
    for x in range(len(store)):
        new.append(f"{store[x]:.2f}")
    return new

