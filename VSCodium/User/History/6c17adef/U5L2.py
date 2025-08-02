def formatted(store):
    new = store
    for x in range(len(new)):
        new[x] = f"{new[x]:.2f}"
    return new
