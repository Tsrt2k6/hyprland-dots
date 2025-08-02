def most_common_character(store):
    letters = ""
    for letter in store:
        if letter not in letters:
            letters += letter
    most = 0
    for x in letters:
        if store.count(x) > most:
            most = store.count(x)