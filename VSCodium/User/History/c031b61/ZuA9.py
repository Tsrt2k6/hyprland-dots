def length_of_longest(store):
    longest = 0
    for x in store:
        if len(x) > longest:
            longest = len(x)
    return longest