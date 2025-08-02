def find_segments(data):
    count = 1
    store = []
    for index in range(1, len(data)):
        if data[index] == data[index - 1]:
            count += 1
        else:
            store.append((count, data[index - 1]))
            count = 1
    return store

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]