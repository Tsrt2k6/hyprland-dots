store = []
last = 1
while True:
    print(f"The list is now {store}")
    option = input()
    if option == "d":
        store.append(last)
        last += 1
    elif option == "r":
        store.pop()
        last -= 1
    else:
        print("Bye!")
        break