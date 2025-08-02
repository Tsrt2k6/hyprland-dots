def invert(store):
    for key, value in store.items():
        copy[value] = key
    store.clear()
    for key, value in copy.items():
        store[key] = value
    
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)