def most_common_character(store):
    most_letter = store[0]    for x in store:
    if store.count(x) > store.count(most_letter):
        most_letter = x

    return most_letter