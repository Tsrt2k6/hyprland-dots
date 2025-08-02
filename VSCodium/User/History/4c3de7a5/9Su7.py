store = []

while True:
    store.append(input())
    if store[-1] == "0":
        break
    print(f"The list now: {store}")
    print(f"The list in order: {sorted(store)}")
