book = {}

while True:
    option = int(input())
    
    if option == 2:
        name = input()
        number = input()
        book[name] = number
        print("ok!")

    elif option == 1:
        name = input()
        if name in book:
            print(book[name])
        else:
            print("no number")

    elif option == 3:
        print("quitting...")
        break
