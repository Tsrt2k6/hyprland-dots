book = {}

while True:
    option = int(input())
    
    if option == 2:
        name = input()
        number = input()
        if name not in book:
            book[name] = []
        book[name].append(number))
        print("ok!")

    elif option == 1:
        name = input()
        if name in book:
            for number in name:
                print(number)print(book[name])
        else:
            print("no number")

    elif option == 3:
        print("quitting...")
        break
