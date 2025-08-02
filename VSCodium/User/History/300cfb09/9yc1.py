while True:
    store = [1,2,3,4,5]
    index = int(input())
    if index == -1:
        break
    value = int(input())
    store[index] = value
    print(store)
