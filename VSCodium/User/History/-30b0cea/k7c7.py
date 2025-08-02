def longest(store):
    longest = 0
    for x in store:
        if len(x) > longest:
            longest = len(x)
    return longest

def all_the_longest(store):
    longest = longest(store)
    result = []
    for x in store:
        if len(x) == longest:
            result.append(x)
    return result