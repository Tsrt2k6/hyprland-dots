def most_common_character(store):
    letters = ""
    for letter in store:
        if letter not in letters:
            letters += letter
    most_count = 0
    most_letter = ""
    for x in letters:
        if store.count(x) > most:
            most = store.count(x)
            most_letter = x

    return most_letter