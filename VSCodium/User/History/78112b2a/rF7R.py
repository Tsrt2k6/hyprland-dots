def read_fruits():
    with open("fruits.csv") as new:
        store = {}
        for line in new:
            name, price = line.split(";")
            store[name] = price[:-1]
        