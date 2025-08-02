store = []

while True:
    store.append(int(input()))
    if store[-1] == 0:
        print("Bye!")
        break
    print(f"The list now: {store}")
    print(f"The list in order: {sorted(store)}")
