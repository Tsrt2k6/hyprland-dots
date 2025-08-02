def most_common_character(store):
    most_count = 0
    most_letter = ""
    for x in store:
        if store.count(x) > most_count:
            most_count = store.count(x)
            most_letter = x

    return most_letter