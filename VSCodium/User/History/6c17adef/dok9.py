def formatted(store):
    new = store
    for x in range(len(new)):
        new[x] = f"{new[x]:.2f}"
    return new

print(formatted([0.123, 1.23, 0.0234]))