def read_fruits():
    with open("fruits.csv") as new:
        store = {}
        for line in new:
            name, price = line.split(";")
            store[name] = float(price[:-1])    # Replaces '\n' with ''
    return store