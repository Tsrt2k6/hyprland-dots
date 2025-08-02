while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input())
    if option == 1:
        with open("diary.txt", "a") as file:
            entry = input()
            file.write(f"{entry}\n")
            print("Dairy saved")
    elif option == 2:
        with open("diary.txt") as file:
            print("Entries:")
            for line in file:
                print(line, end="")
    elif option == 0:
        print("Bye now!")
        break
