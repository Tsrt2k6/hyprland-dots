def histogram(word):
    store = {}
    for letter in word:
        if letter not in store:
            store[letter] = 0
        store[letter] += 1
    
    for key in store:
        print(key, "*" * store[key])

    histogram("statistically")