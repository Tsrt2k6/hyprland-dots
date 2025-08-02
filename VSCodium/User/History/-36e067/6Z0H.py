book = {}

while True:
    option = int(input())
    if option == 2:
        name = input()
        number = input()
        book[name] = number
        print("ok!")
    if option == 1:
        name = input()
        if name in book:
            print(book[name])
        else:
            print("no number")
    else:
        print("quitting...")
        break
