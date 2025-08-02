def find_segments(data):
    count = 1
    store = []
    data += " "
    for index in range(1, len(data)):
        prev = data[index - 1]
        if data[index] == prev:
            count += 1
        else:
            store.append((count, prev))
            count = 1
    return store