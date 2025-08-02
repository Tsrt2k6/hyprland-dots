while True:
    option = int(input())
    if option == 1:
        with open("diary.txt", "a") as file:
            entry = input()
            file.write(entry)
            
