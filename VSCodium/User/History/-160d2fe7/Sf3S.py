def invert(store):
    for key, value in store.items():
        store[value] = key
        store.pop(key)
    
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)